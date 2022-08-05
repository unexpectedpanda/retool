import html
import os
import sys

from urllib.parse import quote

from modules.utils import Font, natural_keys, old_windows, printwrap
from modules.xml import header


def generate_config(
    languages,
    regions,
    list_prefix=False,
    list_suffix=False,
    gui=False,
    filters=False,
    gui_settings=False,
    overwrite=False):
    new_user_config = False
    new_global_filter = False

    if not os.path.exists('user-config.yaml') or overwrite == True:
        try:
            with open('user-config.yaml', 'w', encoding='utf-8') as output_file:
                output_file.writelines('---\n# If the -l option is used, only include titles with the following languages.')
                output_file.writelines('\n# Comment out languages you don\'t want.')
                output_file.writelines('\nlanguage filter:')

                def write_entry(string, comment=False):
                    if comment == True:
                        output_file.writelines(f'\n# - {string}')
                    else:
                        output_file.writelines(f'\n- {string}')

                if overwrite == False:
                    for language in languages:
                        write_entry(language, True)
                else:
                    for language in languages:
                        if 'True|' in language:
                            write_entry(language[5:], True)
                        else:
                            write_entry(language)

                output_file.writelines('\n\n# The region order Retool follows. Comment out the regions you don\'t want.')
                output_file.writelines('\nregion order:')

                for region in regions:
                    if overwrite == False:
                        write_entry(region)
                    else:
                        if 'True|' in region:
                            write_entry(region[5:], True)
                        else:
                            write_entry(region)

                output_file.writelines('\n\n# If the --list option is used, you can optionally add a prefix and suffix')
                output_file.writelines('\n# to each title.')
                output_file.writelines('\n#')
                output_file.writelines('\n# If you start a prefix with http://, https://, or ftp://, each line in the')
                output_file.writelines('\n# list will be URL encoded.')
                output_file.writelines('\n#')
                output_file.writelines('\n# The text must be inside double quotes. You must escape other double quotes')
                output_file.writelines('\n# and backslashes inside the quotes like so: \\", \\\\')
                output_file.writelines('\nlist prefix:')

                if list_prefix != False:
                    write_entry(f'"{list_prefix}"')
                else:
                    output_file.writelines('\n# - "This text will be at the start of each line"')

                output_file.writelines(f'\n\nlist suffix:')

                if list_suffix != False:
                    write_entry(f'"{list_suffix}"')
                else:
                    output_file.writelines('\n# - "This text will be at the end of each line"')


                output_file.writelines('\n\n# GUI settings only, not used by the CLI.')
                output_file.writelines('\ngui settings:')

                if gui_settings != False:
                    for setting in gui_settings:
                        write_entry(setting)

                new_user_config = True

        except OSError as e:
            print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

    if (
        filters != False and type(filters) is not list):
        if filters.system_file != '':
            if not os.path.isfile(f'user-filters/{filters.system_file}.yaml') or overwrite == True:
                try:
                    with open(f'user-filters/{filters.system_file}.yaml', 'w', encoding='utf-8') as output_file:
                        output_file.writelines('---\n# Contains user defined strings that can be used to include or exclude')
                        output_file.writelines('\n# titles that Retool ordinarily wouldn\'t.')
                        output_file.writelines('\n#')
                        output_file.writelines(f'\n# This is the include/exclude file for the {filters.system_file} DAT.')
                        output_file.writelines('\n#')
                        output_file.writelines('\n# Refer to the readme-cli.md file in this folder for how to set up this file,')
                        output_file.writelines('\n# along with system include/exclude files.')
                        output_file.writelines('\n#')
                        output_file.writelines('\n# The text must be inside double quotes. You must escape double quotes and')
                        output_file.writelines('\n# backslashes like so: \\", \\\\')
                        output_file.writelines('\n#')
                        output_file.writelines('\n# Comment out lines you don\'t want.')
                        output_file.writelines('\n\nexclude:')
                        for filter_text in filters.system_exclude:
                            output_file.writelines(f'\n- "{filter_text}"')
                        output_file.writelines('\ninclude:')
                        for filter_text in filters.system_include:
                            output_file.writelines(f'\n- "{filter_text}"')
                except OSError as e:
                    print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
                    raise

    if not os.path.exists('user-filters'):
        try:
            os.mkdir('user-filters')
        except:
            pass

    if not os.path.exists('user-filters/global.yaml') or overwrite == True:
        try:
            with open('user-filters/global.yaml', 'w', encoding='utf-8') as output_file:
                output_file.writelines('---\n# Contains user defined strings that can be used to include or exclude')
                output_file.writelines('\n# titles that Retool ordinarily wouldn\'t.')
                output_file.writelines('\n#')
                output_file.writelines('\n# This is the global include/exclude file, and will affect all dats.')
                output_file.writelines('\n#')
                output_file.writelines('\n# Refer to the readme-cli.md file in this folder for how to set up this file,')
                output_file.writelines('\n# along with system include/exclude files.')
                output_file.writelines('\n#')
                output_file.writelines('\n# The text must be inside double quotes. You must escape double quotes and')
                output_file.writelines('\n# backslashes like so: \\", \\\\')
                output_file.writelines('\n#')
                output_file.writelines('\n# Comment out lines you don\'t want.')
                output_file.writelines('\n\nexclude:')
                if filters == False:
                    output_file.writelines('\n# - \'[b]\'')
                    output_file.writelines('\n# - \'/.*?\(Virtual*\'\n')
                elif type(filters) is not list:
                    for filter_text in filters.global_exclude:
                        output_file.writelines(f'\n- "{filter_text}"')
                output_file.writelines('\ninclude:')
                if filters == False:
                    output_file.writelines('\n# - \'|My favorite title (Japan)\'')
                elif type(filters) is not list:
                    for filter_text in filters.global_include:
                        output_file.writelines(f'\n- "{filter_text}"')

                new_global_filter = True

        except OSError as e:
            print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

    if (
        overwrite == False
        and gui == False):
        if (
            not os.path.exists('clonelists')
            or not os.path.exists('metadata')):
                if new_user_config or new_global_filter:
                    printwrap(f'{Font.warning}Retool needs to download clone lists and '
                            'metadata files, and generate some configuration files '
                            'before continuing. It can\'t be used without them.', 'no_indent')
                else:
                    printwrap(f'{Font.warning}Retool needs to download clone lists and '
                            'metadata files before continuing. It can\'t be used without '
                            'them.', 'no_indent')

                download = input(f'\nContinue? (y/n) {Font.end}')

                if download == 'n':
                    sys.exit()
                else:
                    import updateclonelists
                    updateclonelists.main()
                    print()
                    if not (new_user_config or new_global_filter):
                        printwrap(f'{Font.warning}You can now run Retool normally.{Font.end}', 'no_indent')

        if new_user_config == True or new_global_filter == True:
            file_list = []
            if new_user_config == True:
                file_list.append(f'* {Font.warning_bold}user-config.yaml{Font.warning}')
            if new_global_filter == True:
                file_list.append(f'* {Font.warning_bold}user-filters/global.yaml{Font.warning}')

            file_list = '\n'.join(file_list)

            printwrap(f'\n{Font.warning}The following system files were '
                      f'missing and have been created:', 'no_indent')

            print(f'\n{file_list}\n')

            if new_user_config == True:
                printwrap(f'You might want to edit {Font.warning_bold}'
                          f'user-config.yaml{Font.warning} to define a custom '
                          f'region order, or to filter specific languages.',
                          'no_indent')
                print('')

            printwrap(f'You can now run Retool normally.{Font.end}', 'no_indent')

            sys.exit()


def write_dat_file(input_dat, user_input, output_file_name, stats, titles, dat_numbered, version):
    """ Output the final DAT file """

    dat_header = header(input_dat, stats.final_title_count, user_input, version)

    # Write the file
    try:
        audit_list = {}

        if user_input.keep_remove == True:
            keep_remove_list = output_file_name[:-4] + ' auto keep-remove list.txt'
            user_remove_list = output_file_name[:-4] + ' user remove list.txt'

            with open(keep_remove_list, 'a', encoding='utf-8') as list_output:
                list_output.writelines(f'This file shows which titles have been kept in the output DAT with a `+`,\n')
                list_output.writelines(f'and which have been automatically removed by Retool with a `-`. If the\n')
                list_output.writelines(f'`-` is indented, then the title was removed because it was a clone of the\n')
                list_output.writelines(f'title above it with a `+`.\n\n')

            list_output.close()

            if user_input.removed_titles != {}:
                with open(user_remove_list, 'a', encoding='utf-8') as list_output:
                    list_output.writelines(f'This file shows which titles have been removed from the output dat\n')
                    list_output.writelines(f'due to the user setting an option.\n')

                list_output.close()

        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            output_file.writelines(dat_header)
            progress = 0
            progress_old = 0

            if user_input.legacy == False:
                progress_total = stats.final_title_count + stats.clone_count
            else:
                progress_total = stats.final_title_count

            final_xml = {}

            for group in sorted(titles.all):
                for title in sorted(titles.all[group], key=lambda x: natural_keys(x.full_name)):

                    if dat_numbered == False:
                        final_name = title.full_name
                    else:
                        final_name = title.numbered_name

                    progress += 1
                    progress_percent = int(progress/progress_total*100)

                    if progress_old != progress_percent:
                        if old_windows() != True:
                            sys.stdout.write("\033[K")
                        print(f'* Writing DAT file... [{str(progress_percent)}%]', sep='', end='\r', flush=True)

                    game_xml = ''

                    if title.cloneof == '':
                        game_xml = f'\t<game name="{html.escape(final_name, quote=False)}">'
                        if (
                            user_input.keep_remove == True
                            or user_input.list == True):
                                if final_name not in audit_list:
                                    audit_list[final_name] = []
                    else:
                        if (
                            user_input.keep_remove == True
                            or user_input.list == True):
                                if title.cloneof not in audit_list:
                                    audit_list[title.cloneof] = []
                                audit_list[title.cloneof].append(final_name)

                        if user_input.legacy == True:
                            game_xml = f'\t<game name="{html.escape(final_name, quote=False)}" cloneof="{html.escape(title.cloneof, quote=False)}">'

                    rom_xml = []

                    for rom in title.roms:
                        if rom.crc:
                            crc_string = f'crc="{rom.crc}"'
                        else:
                            crc_string = ''

                        if rom.md5:
                            md5_string = f'md5="{rom.md5}"'
                        else:
                            md5_string = ''

                        if rom.sha1:
                            sha1_string = f'sha1="{rom.sha1}"'
                        else:
                            sha1_string = ''

                        if rom.sha256:
                            sha256_string = f'sha256="{rom.sha256}"'
                        else:
                            sha256_string = ''

                        if rom.header:
                            header_string = f'header="{rom.header}"'
                        else:
                            header_string = ''

                        if rom.mia:
                            mia_string = f'mia="{rom.mia}"'
                        else:
                            mia_string = ''

                        name_string = f'name="{html.escape(rom.name, quote=False)}"'
                        size_string = f'size="{rom.size}"'

                        rom_xml_elements = [
                            name_string,
                            size_string,
                            mia_string,
                            header_string,
                            crc_string,
                            md5_string,
                            sha1_string,
                            sha256_string,
                            ]

                        rom_xml_elements = [x for x in rom_xml_elements if x != '']

                        rom_xml.append(
                            f'\n\t\t<rom {" ".join(rom_xml_elements)}/>')

                    rom_xml = ''.join(rom_xml)

                    if game_xml != '':
                        release = ''
                        if user_input.legacy == True:
                            region_list = title.regions.split(', ')
                            language_list = title.languages.split(', ')

                            release = []

                            for region in sorted(region_list):
                                for language in sorted(language_list):
                                    release.append(f'\n\t\t<release name="{html.escape(final_name, quote=False)}" region="{region}" language="{language}"/>')

                            release = ''.join(release)

                        categories = []
                        for category in title.categories:
                            categories.append(f'<category>{html.escape(category, quote=False)}</category>\n\t\t')

                        final_xml[final_name] = (
                            f'{game_xml}\n\t\t'
                            f'{"".join(categories)}'
                            f'<description>{html.escape(title.description, quote=False)}'
                            f'</description>'
                            f'{release}'
                            f'{rom_xml}\n\t</game>\n'
                        )

                    progress_old = progress_percent

            final_xml_sort = []

            for xml in sorted(final_xml):
                final_xml_sort.append(xml)

            for key in final_xml_sort:
                    output_file.writelines(final_xml[key])

            # 1G1R list output, if --list is set
            if user_input.list == True:
                keep_list = output_file_name[:-4] + ' 1G1R list.txt'

                with open(keep_list, 'w', encoding='utf-8') as list_output:
                    final_keep_sort = sorted(audit_list)
                    final_keep_list = []

                    for key in final_keep_sort:
                        if audit_list[key] == []:
                            final_keep_list.append(key)

                    parents_clones = {}

                    for key, values in audit_list.items():
                        if values != []:
                            parents_clones[key] = []

                    if parents_clones != {}:
                        final_parents_clones_sort = sorted(parents_clones)

                        for title in final_parents_clones_sort:
                            final_keep_list.append(title)

                    final_keep_list = sorted(final_keep_list)

                    for keep in final_keep_list:
                        if user_input.user_config.data["list prefix"] == '':
                            list_prefix = ''
                        else:
                            list_prefix = user_input.user_config.data["list prefix"][0]

                        if user_input.user_config.data["list suffix"] == '':
                            list_suffix = ''
                        else:
                            list_suffix = user_input.user_config.data["list suffix"][0]

                        line = f'{list_prefix}{keep}{list_suffix}'
                        if (
                            list_prefix.startswith('http://')
                            or list_prefix.startswith('https://')
                            or list_prefix.startswith('ftp://')
                        ):
                            list_output.writelines(f'{quote(line, safe="/").replace("http%3A//", "http://").replace("https%3A//", "https://").replace("ftp%3A//", "ftp://")}\n')
                        else:
                            list_output.writelines(f'{line}\n')

            # Keep/remove lists output, if --log is set
            if user_input.keep_remove == True:
                with open(user_remove_list, 'a', encoding='utf-8') as list_output:
                    if user_input.removed_titles != {}:
                        temp_sort = sorted(user_input.removed_titles)
                        temp_removed_titles = {}

                        for key in temp_sort:
                            temp_removed_titles[key] = user_input.removed_titles[key]

                        user_input.removed_titles = temp_removed_titles

                        list_output.writelines(f'\nTITLE TYPES REMOVED\n')
                        list_output.writelines(f'===================\n')
                        for key, values in user_input.removed_titles.items():
                            if values != []:
                                output_key = key
                                if key == 'Console': output_key = 'BIOS and other chips'
                                list_output.writelines(f'* {output_key.upper().replace("_"," ")}\n')

                        list_output.writelines(f'\n')
                        for key, values in user_input.removed_titles.items():
                            if values != []:
                                output_key = key
                                if key == 'Console': output_key = 'BIOS and other chips'
                                list_output.writelines(f'\n# {output_key.upper().replace("_"," ")}\n')
                                underline = []
                                for i in range(0,len(output_key) + 2):
                                    underline.append('=')
                                list_output.writelines(f'{"".join(underline)}\n')
                                for value in sorted(values, key=lambda x: natural_keys(x)):
                                    list_output.writelines(f'- {value}\n')
                                list_output.writelines(f'\n')

                    list_output.close()


                with open(keep_remove_list, 'a', encoding='utf-8') as list_output:
                    list_output.writelines(f'\n# STANDALONES\n')
                    list_output.writelines(f'==============\n')

                    final_keep_remove_sort = sorted(audit_list)

                    for key in final_keep_remove_sort:
                        if audit_list[key] == []:
                            list_output.writelines(f'+ {key}\n')

                    parents_clones = {}

                    for key, values in audit_list.items():
                        if values != []:
                            parents_clones[key] = []
                            for value in values:
                                parents_clones[key].append(f'\t- {value}\n')

                    if parents_clones != {}:
                        final_parents_clones_sort = sorted(parents_clones)

                        list_output.writelines(f'\n\n# PARENTS & CLONES\n')
                        list_output.writelines(f'===================\n')

                        for title in final_parents_clones_sort:
                            list_output.writelines(f'+ {title}\n')
                            for clone in parents_clones[title]:
                                list_output.writelines(clone)

                    list_output.close()

            output_file.writelines('</datafile>')
            output_file.close()

        if old_windows() != True:
            sys.stdout.write("\033[K")
        print('* Writing DAT file... done. ') # Intentional trailing space for Win 7
    except OSError as e:
        print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
        raise