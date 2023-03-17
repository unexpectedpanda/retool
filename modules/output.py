
from __future__ import annotations

import datetime
import html
import pathlib
import re

from typing import TYPE_CHECKING
from urllib.parse import quote

if TYPE_CHECKING:
    from modules.config import Config
    from modules.dats import Dat, DatNode

from modules.titletools import Removes
from modules.utils import eprint, Font


class WriteFiles(object):
    """ Methods for writing files to disk """


    @staticmethod
    def output(processed_titles: dict[str, list[DatNode]], log: tuple[dict[str, set[str]], set[DatNode]], config: Config, input_dat: Dat, removes: Removes) -> None:
        """ The main function for managing output. The actual writing of files is done by
        other functions.

        Args:
            `processed_titles (dict[str, list[DatNode]])`: A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.
            `log (tuple[dict[str, set[str]], set[DatNode]])`: Contains all the
            titles included and removed from the output DAT, and their relationships.
            Used if the user specifies `--log`.
            `config (Config)`: The Retool config object.
            `input_dat (Dat)`: The Retool input_dat object.
            `removes (Removes)`: The Retool removes object, which contains every title
            that's been removed, organized by why they were removed.
        """

        timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        # Check if a system config is in play
        region_order: list[str] = config.region_order_user

        if config.system_region_order_user:
            if {'override': 'true'} in config.system_region_order_user:
                region_order = [str(x) for x in config.system_region_order_user if 'override' not in x]

        if config.user_input.output_region_split:
            for region in region_order:
                region_processed_titles: dict[str, list[DatNode]] = {}

                for group in processed_titles:
                    for title in processed_titles[group]:
                        if (
                            title.primary_region == region
                            and not title.cloneof):
                                if group not in region_processed_titles:
                                    region_processed_titles[group] = []
                                region_processed_titles[group].append(title)

                if region_processed_titles:
                    WriteFiles.write_dat(region_processed_titles, config, input_dat, timestamp, '', f' ({region})')
        else:
            WriteFiles.write_dat(processed_titles, config, input_dat, timestamp)

        # Add removed titles to a separate DAT if requested
        if config.user_input.output_remove_dat:
            removed_titles: dict[str, list[DatNode]] = {}

            # Get the titles from various remove categories
            for removes_group in removes.__dict__.values():
                for title in removes_group:
                    if title.group_name not in removed_titles:
                        removed_titles[title.group_name] = []

                    removed_titles[title.group_name].append(title)

            # Add clones
            for titles in processed_titles.values():
                for title in titles:
                    if title.cloneof:
                        title.exclude_reason = f'Clone of {title.cloneof}'
                        title.cloneof = ''
                        if title.group_name not in removed_titles:
                            removed_titles[title.group_name] = []

                        removed_titles[title.group_name].append(title)

            # Write the DAT/s
            if removed_titles:
                if config.user_input.output_region_split:
                    for region in region_order:
                        region_removed_titles: dict[str, list[DatNode]] = {}

                        for group in removed_titles:
                            for title in removed_titles[group]:
                                if (
                                    title.primary_region == region
                                    and not title.cloneof):
                                        if group not in region_removed_titles:
                                            region_removed_titles[group] = []
                                        region_removed_titles[group].append(title)

                        if region_removed_titles:
                            WriteFiles.write_dat(region_removed_titles, config, input_dat, timestamp, ' (Removed titles)', f' ({region})')
                else:
                    WriteFiles.write_dat(removed_titles, config, input_dat, timestamp, ' (Removed titles)')

        # Write the log if requested
        if config.user_input.log:
            WriteFiles.write_log(log, removes, config, input_dat, timestamp)


    @staticmethod
    def write_dat(processed_titles: dict[str, list[DatNode]], config: Config, input_dat: Dat, timestamp: str, output_file_removes: str = '', output_file_region: str = '') -> None:
        """ Writes DAT files. Additionally writes the output for `--listnames` if the user
        has requested it, which contains the names of the titles which have been kept,
        and optionally a user-defined prefix and suffix.

        Args:
            `processed_titles (dict[str, list[DatNode]])`: A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.
            `config (Config)`: The Retool config object.
            `input_dat (Dat)`: The Retool input_dat object.
            `timestamp (str)`: Timestamp used in the date header of the output DAT and
            its filename.
            `output_file_removes (str, optional)`: The string to append to a DAT file if
            it contains the titles Retool has removed. Defaults to `''`.
            `output_file_region (str, optional)`: An additional region tag to append to
            the removes DAT filename if the user has opted to split by region. Defaults
            to `''`.
        """

        eprint(f'* Creating{output_file_region.replace("(", "").replace(")", "")}{output_file_removes.replace("(", "").replace(")", "").lower()} DAT... ', sep=' ', end='', flush=True)

        # Create a list titles, deduped of superset titles
        final_titles: set[DatNode] = set()
        dupe_check: set[str] = set()

        for titles in processed_titles.values():
            for title in titles:
                if title.full_name not in dupe_check:
                    dupe_check.add(title.full_name)
                    final_titles.add(title)

        dupe_check.clear()

        # Generate the XML content
        final_xml: list[str] = []
        dat_xml: list[str] = []
        list_names: list[str] = []

        config.stats.file_count = 0

        # Create the title data first
        for title in sorted(final_titles, key=lambda x: x.full_name):
            if input_dat.numbered:
                final_name = title.numbered_name
            else:
                final_name = title.full_name

            if title.cloneof:
                if config.user_input.legacy:
                    dat_xml.append(f'\t<game name="{html.escape(final_name, quote=False)}" cloneof="{html.escape(title.cloneof, quote=False)}">\n')

                    if config.user_input.list_names:
                        list_names.append(final_name)

                    config.stats.file_count += 1
                else:
                    continue
            elif not title.cloneof:
                dat_xml.append(f'\t<game name="{html.escape(final_name, quote=False)}">\n')

                if config.user_input.list_names:
                    list_names.append(final_name)

                config.stats.file_count += 1

            for category in title.categories:
                dat_xml.append(f'\t\t<category>{html.escape(category, quote=False)}</category>\n')

            if title.exclude_reason:
                dat_xml.append(f'\t\t<comment>Remove reason: {html.escape(title.exclude_reason, quote=False)}</comment>\n')

            dat_xml.append(f'\t\t<description>{html.escape(title.description, quote=False)}</description>\n')

            if config.user_input.legacy:
                for region in sorted(title.regions):
                    if not title.languages:
                        dat_xml.append(f'\t\t<release name="{html.escape(final_name, quote=False)}" region="{region}"/>\n')
                    else:
                        for language in sorted(title.languages):
                            dat_xml.append(f'\t\t<release name="{html.escape(final_name, quote=False)}" region="{region}" language="{language}"/>\n')

            for rom in title.roms:
                crc: str = ''
                md5: str = ''
                sha1: str =''
                sha256: str = ''
                header: str = ''
                mia: str = ''

                if rom['crc']:
                    crc = f'crc="{rom["crc"]}"'
                if rom['md5']:
                    md5 = f'md5="{rom["md5"]}"'
                if rom['sha1']:
                    sha1 = f'sha1="{rom["sha1"]}"'
                if rom['sha256']:
                    sha256 = f'sha256="{rom["sha256"]}"'
                if rom['header']:
                    header = f'header="{rom["header"]}"'
                if rom['mia']:
                    mia = f'mia="{rom["mia"]}"'

                rom_status: str = ''

                if not (
                    rom['crc']
                    or rom['md5']
                    or rom['sha1']
                    or rom['sha256']):
                    if not rom['size']:
                        rom['size'] = '0'
                        rom_status = 'status="nodump"'

                rom_xml: list[str] = [
                    f'name="{html.escape(rom["name"], quote=False)}"',
                    f'size="{rom["size"]}"',
                    mia,
                    rom_status,
                    header,
                    crc,
                    md5,
                    sha1,
                    sha256
                ]

                rom_xml = [x for x in rom_xml if x != '']

                if not (
                    config.user_input.no_mia
                    and mia == 'mia="yes"'):
                        dat_xml.append(
                            f'\t\t<rom {" ".join(rom_xml)}/>\n')

            dat_xml.append('\t</game>\n')

        dat_xml.append('</datafile>')

        # Now create the header data
        if input_dat.author:
            input_dat.author = re.sub(' &amp; Retool', '', input_dat.author)
            input_dat.author = f'{html.escape(input_dat.author, quote=False)} &amp; Retool'
        else:
            input_dat.author = 'Unknown &amp; Retool'

        # Show user exclude options in the output filename
        excludes: str = ''

        if config.user_input.excludes:
            excludes = f' [-{config.user_input.excludes}]'

        # Add DAT manager directives that were in the original DAT
        rom_header: list[str] = []

        for directive in input_dat.dat_manager_directives:
            rom_header.append(f'\t\t{directive.strip()}\n')

        dtd_line: str = ''

        if input_dat.is_dtd:
            dtd_line = '<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "https://raw.githubusercontent.com/unexpectedpanda/retool-clonelists-metadata/main/datafile.dtd">'

        final_xml.append('<?xml version="1.0"?>\n')

        if dtd_line:
            final_xml.append(f'{dtd_line}\n')

        if input_dat.datafile_tag:
            final_xml.append(f'{input_dat.datafile_tag}\n')

        final_xml.extend(
            [
            '\t<header>\n',
            f'\t\t<name>{html.escape(input_dat.name, quote=False)} (Retool){output_file_region}{output_file_removes}</name>\n',
            f'\t\t<description>{html.escape(input_dat.name, quote=False)} ({str("{:,}".format(config.stats.file_count))}){config.user_input.user_options}{excludes} ({input_dat.version}) (Retool {config.version_major}.{config.version_minor}){output_file_region}{output_file_removes}</description>\n',
            f'\t\t<version>{html.escape(input_dat.version, quote=False)}</version>\n',
            f'\t\t<date>{timestamp}</date>\n',
            f'\t\t<author>{input_dat.author}</author>\n',
            '\t\t<homepage>http://www.github.com/unexpectedpanda/retool</homepage>\n',
            f'\t\t<url>{html.escape(input_dat.url, quote=False)}</url>\n'])

        if rom_header:
            final_xml.extend(rom_header)

        final_xml.append('\t</header>\n')

        final_xml.extend(dat_xml)

        # Check if the user has set a system output folder
        input_dat.output_filename = f'{config.user_input.output_folder_name}/{input_dat.name} ({input_dat.version}) (Retool {timestamp}){output_file_region}{output_file_removes} ({str("{:,}".format(config.stats.file_count))}){config.user_input.user_options}{excludes}.dat'

        if {'override': 'true'} in config.system_user_path_settings:
            if config.system_output:
                input_dat.output_filename = f'{str(pathlib.Path(config.system_output))}/{input_dat.name} ({input_dat.version}) (Retool {timestamp}){output_file_region}{output_file_removes} ({str("{:,}".format(config.stats.file_count))}){config.user_input.user_options}{excludes}.dat'

        # Create the output folder if it doesn't exist
        if not pathlib.Path(input_dat.output_filename[:-4]).parent.exists():
            pathlib.Path(pathlib.Path(input_dat.output_filename[:-4]).parent).mkdir(parents=True, exist_ok=True)

        # Write a list of title names if requested
        if config.user_input.list_names:
            try:
                with open(pathlib.Path(f'{input_dat.output_filename[:-4]} names.txt'), 'w', encoding='utf-8') as output_file:
                    def output_list_names(prefix: str, suffix: str, name: str) -> None:
                        """ Writes the lines in the list of title names, appends prefixes
                        and suffixes if present. Converts to a URL encoded string if the
                        prefix starts with `http://`, `https://`, or `ftp://`.

                        Args:
                            `prefix (str)`: The prefix to add to the line.
                            `suffix (str)`: The suffix to add to the line.
                            `name (str)`: The title to add to the line.
                        """
                        if (
                            prefix.startswith('http://')
                            or prefix.startswith('https://')
                            or prefix.startswith('ftp://')
                            ):
                                output_file.writelines(f'{prefix}{quote(name)}{suffix}\n')
                        else:
                            output_file.writelines(f'{prefix}{name}{suffix}\n')

                    for name in list_names:
                        if {'override options': 'true'} in config.system_exclusions_options:
                            output_list_names(config.system_user_prefix, config.system_user_suffix, name)
                        else:
                            output_list_names(config.user_prefix, config.user_suffix, name)

            except OSError as e:
                eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
                raise

        # Write the output DAT
        try:
            if config.stdout:
                for line in final_xml:
                    print(line.replace('\n', ''))
            else:
                with open(pathlib.Path(input_dat.output_filename), 'w', encoding='utf-8') as output_file:
                    output_file.writelines(final_xml)
        except OSError as e:
            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

        eprint('done.')


    @staticmethod
    def write_log(log: tuple[dict[str, set[str]], set[DatNode]], removes: Removes, config: Config, input_dat: Dat, timestamp: str) -> None:
        """ Write the output file for `--log`, which contains a list of what titles have
        been kept and removed.

        Args:
            `log (tuple[dict[str, set[str]], set[DatNode]])`: Contains all the
            titles included and removed from the output DAT, and their relationships.
            `removes (Removes)`: The Retool removes object, which contains every title
            that's been removed, organized by why they were removed.
            `config (Config)`: The Retool config object.
            `input_dat (Dat)`: The Retool input_dat object.
            `timestamp (str)`: Timestamp used in the output filename.
        """

        eprint(f'* Creating log file... ', sep=' ', end='', flush=True)

        # Figure out 1G1R titles with clones
        title_names_with_clones: dict[str, set[str]] = log[0]

        # Figure out titles without clones
        titles_without_clones: set[DatNode] = log[1]

        log_file_contents: list[str] = []

        log_file_contents.append('This file shows which titles have been kept in the output dat with a `+`,'
                    '\nand which have been removed with a `-`. If the `-` is indented, then the'
                    '\ntitle was removed because it was a clone of the previous title with a `+`.\n')

        if (
            title_names_with_clones
            or titles_without_clones
            or removes.category_removes
            or removes.clonelist_removes
            or removes.mia_removes
            or removes.language_removes
            or removes.region_removes
            or removes.global_excludes
            or removes.system_excludes):

                log_file_contents.append('\nSECTIONS\n========\n')
                log_file_contents.append('Search for these section names to jump to that part of the file.\n\n')
                if title_names_with_clones: log_file_contents.append('* TITLES WITH CLONES\n')
                if titles_without_clones: log_file_contents.append('* TITLES WITHOUT CLONES\n')
                if removes.category_removes: log_file_contents.append('* CATEGORY REMOVES\n')
                if removes.clonelist_removes: log_file_contents.append('* CLONE LIST REMOVES\n')
                if removes.language_removes: log_file_contents.append('* LANGUAGE REMOVES\n')
                if removes.mia_removes: log_file_contents.append('* MIA REMOVES\n')
                if removes.region_removes: log_file_contents.append('* REGION REMOVES\n')
                if removes.global_excludes: log_file_contents.append('* SYSTEM EXCLUDES\n')
                if removes.system_excludes: log_file_contents.append('* SYSTEM EXCLUDES\n')

                log_file_contents.append('\n')

                if title_names_with_clones:
                    log_file_contents.append('\nTITLES WITH CLONES\n==================\n\n')
                    # Assign clones to their 1G1R titles
                    for title_name, title_group in sorted(title_names_with_clones.items()):
                        log_file_contents.append(f'+ {title_name}')

                        for clone in sorted(title_group):
                            log_file_contents.append(f'\n  - {clone}')

                            if clone == sorted(title_group)[-1]:
                                log_file_contents.append('\n')

                if titles_without_clones:
                    log_file_contents.append('\nTITLES WITHOUT CLONES\n==================\n\n')

                    for title in sorted(titles_without_clones, key=lambda x: x.full_name):
                        log_file_contents.append(f'+ {title.full_name}\n')

                if removes.category_removes:
                    log_file_contents.append('\nCATEGORY REMOVES\n==================\n')
                    log_file_contents.append('These titles were removed because the user excluded one or more categories.\n\n')

                    for title in sorted(removes.category_removes, key=lambda x: x.full_name):
                        log_file_contents.append(f'- {title.full_name}\n')

                if removes.clonelist_removes:
                    log_file_contents.append('\nCLONE LIST REMOVES\n==================\n')
                    log_file_contents.append('These titles were force removed by the clone list because they are duplicates.\n\n')

                    for title in sorted(removes.clonelist_removes, key=lambda x: x.full_name):
                        log_file_contents.append(f'- {title.full_name}\n')

                if removes.language_removes:
                    log_file_contents.append('\nLANGUAGE REMOVES\n==================\n')
                    log_file_contents.append('These titles were removed because the user excluded one or more languages.\n\n')

                    for title in sorted(removes.language_removes, key=lambda x: x.full_name):
                        log_file_contents.append(f'- {title.full_name}\n')

                if removes.mia_removes:
                    log_file_contents.append('\nMIA REMOVES\n==================\n')
                    log_file_contents.append('These titles were removed because the user excluded MIA titles.\n\n')

                    for title in sorted(removes.mia_removes, key=lambda x: x.full_name):
                        log_file_contents.append(f'- {title.full_name}\n')

                if removes.region_removes:
                    log_file_contents.append('\nREGION REMOVES\n==================\n')
                    log_file_contents.append('These titles were removed because the user excluded one or more regions.\n\n')

                    for title in sorted(removes.region_removes, key=lambda x: x.full_name):
                        log_file_contents.append(f'- {title.full_name}\n')

                if removes.global_excludes:
                    log_file_contents.append('\nGLOBAL EXCLUDES\n==================\n')
                    log_file_contents.append('These titles were removed because they matched the user\'s global excludes.\n\n')

                    for title in sorted(removes.global_excludes, key=lambda x: x.full_name):
                        log_file_contents.append(f'- {title.full_name}\n')

                if removes.system_excludes:
                    log_file_contents.append('\nSYSTEM EXCLUDES\n==================\n')
                    log_file_contents.append('These titles were removed because they matched the user\'s system excludes.\n\n')

                    for title in sorted(removes.system_excludes, key=lambda x: x.full_name):
                        log_file_contents.append(f'- {title.full_name}\n')

        # Show user exclude options in the output filename
        excludes: str = ''

        if config.user_input.excludes:
            excludes = f' [-{config.user_input.excludes}]'

        output_filename: str = f'{config.user_input.output_folder_name}/{input_dat.name} ({input_dat.version}) (Retool {timestamp}){config.user_input.user_options}{excludes}'

        if {'override': 'true'} in config.system_user_path_settings:
            if config.system_output:
                output_filename = f'{str(pathlib.Path(config.system_output))}/{input_dat.name} ({input_dat.version}) (Retool {timestamp}){config.user_input.user_options}{excludes}'

        try:
            with open(pathlib.Path(f'{output_filename} log.txt'), 'w', encoding='utf-8') as output_file:
                output_file.writelines(log_file_contents)
        except OSError as e:
            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

        eprint(f'done.')

