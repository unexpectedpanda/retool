from __future__ import annotations

import os
import pathlib
import re
from collections.abc import Iterator
from copy import deepcopy
from typing import TYPE_CHECKING, Any

from lxml import etree
from lxml import html as html_

from modules.titletools import TitleTools
from modules.utils import eprint, pattern2string

if TYPE_CHECKING:
    import pathlib

    from modules.config.config import Config
    from modules.dat.process_dat import Dat
    from modules.input import UserInput


class TitleData:
    def __init__(
        self,
        name: str = '',
        categories: set[str] | None = None,
        description: str = '',
        tag_name: str = 'game',
        tag_attribs: dict[str, str] | None = None,
        files: list[dict[str, str]] | None = None,
        unrecognized_children: list[str] | None = None,
    ) -> None:
        """
        Creates an object that contains an input DAT's titles.

        Args:
            name (str, optional): The name of the title. Defaults to `''`.

            categories (set[str], optional): The categories of the title. Defaults to
                `None`.

            description (str, optional): The description of the title. Defaults to `''`.

            tag_name (str, optional): Whether the tag around the title is set to `game`
                or `machine`. Defaults to `''`.

            tag_attribs (dict[str, str]): Additional unrecognized attributes set on the
                `game` or `machine` tag. Defaults to `None`.

            files (list[dict[str, str]], optional): The files in the title. Defaults to
                `None`.

            unrecognized_children (list[str]): Child elements not recognized by Retool.
                Defaults to `None`.
        """
        self.name: str = name
        self.categories: set[str] = categories if categories is not None else set()
        self.description: str = description
        self.tag_name: str = tag_name
        self.tag_attribs: dict[str, str] = tag_attribs if tag_attribs is not None else {}
        self.files: list[dict[str, str]] = files if files is not None else []
        self.unrecognized_children: list[str] = (
            unrecognized_children if unrecognized_children is not None else []
        )


def clean_namespaces(element: etree._Element) -> etree._Element:
    """
    Removes unneeded namespaces from XML elements.

    Args:
        element (etree._Element): An element from an XML file.

    Returns:
        etree._Element: The cleaned element with no namespaces.
    """
    for attr in element.attrib:
        if etree.QName(attr).namespace:
            del element.attrib[attr]

    etree.cleanup_namespaces(element)

    return element


def define_lxml_parser() -> etree.XMLParser:
    """Defines the LXML parser."""
    parser = etree.XMLParser(
        encoding='utf-8',
        no_network=True,
        ns_clean=True,
        recover=True,
        remove_comments=True,
        remove_pis=True,
        resolve_entities=False,
        strip_cdata=True,
    )

    return parser


def fast_lxml_iter(context: etree.iterparse, func: Any, *args: Any, **kwargs: Any) -> None:
    """
    Reads through XML without chewing up huge amounts of memory.

    http://lxml.de/parsing.html#modifying-the-tree
    Based on Liza Daly's fast_iter
    https://public.dhe.ibm.com/software/dw/xml/x-hiperfparse/x-hiperfparse-pdf.pdf
    See also http://effbot.org/zone/element-iterparse.htm

    Args:
        context (etree.iterparse): The iterparse context.

        func (Any): The `process_element` function.

        args (Any): Additional arguments.

        kwargs (Any): Additional keyword arguments.
    """
    for _, element in context:
        func(element, *args, **kwargs)
        # It's safe to call clear() here because no descendants will be accessed
        element.clear()
        # Also eliminate now-empty references from the root node to element
        for ancestor in element.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]
    del context


def format_system_name(
    original_name: str,
    config: Config,
    url: str = '',
    homepage: str = '',
    comment: str = '',
    author: str = '',
) -> str:
    """
    Sanitizes a DAT file's system name to match it with clone lists, metadata files, and
    system configs.

    Args:
        original_name (str): The original system name to process.

        config (Config): The Retool config object.

        url (str, optional): The URL in the header of the input DAT. Defaults to `''`.

        homepage (str, optional): The homepage in the header of the input DAT. Defaults
            to `''`.

        comment (str, optional): The comment in the header of the input DAT. Defaults to
            `''`.

        author (str, optional): The author in the header of the input DAT. Defaults to
            `''`.

    Returns:
        str: The formatted system name.
    """
    remove_string: str = f' \\(({"|".join(config.dat_file_tags)})\\)'

    search_name: str = ''

    if re.search(remove_string, original_name) is not None:
        search_name = re.sub(remove_string, '', original_name)
    else:
        search_name = original_name

    # Add group names to differentiate DATs that cover the same system
    if 'no-intro' in url:
        search_name = f'{search_name} (No-Intro)'
    elif 'MAMERedump' in url or 'MAME Redump' in author:
        search_name = f'{search_name} (MAME Redump)'
    elif (
        'redump' in url
        or 'Redump.org ISOs converted' in comment
        or 'Redump' in author
        or 'redump' in author
    ):
        search_name = f'{search_name} (Redump)'
    elif 'TOSEC' in homepage or 'tosecdev.org' in url:
        search_name = f'{search_name} (TOSEC)'
    else:
        search_name = f'{search_name}'

    # Deal with https://dats.site DATs
    if 'GameCube' in search_name:
        if (
            'NKit GCZ' in search_name
            or 'NKit ISO' in search_name
            or 'NKit RVZ' in search_name
            or 'NASOS' in search_name
        ):
            search_name = 'Nintendo - GameCube (Redump)'

    if 'Wii' in search_name:
        if (
            'NKit GCZ' in search_name
            or 'NKit ISO' in search_name
            or 'NKit RVZ' in search_name
            or 'NASOS' in search_name
        ):
            search_name = 'Nintendo - Wii (Redump)'

    if 'Wii U' in search_name and 'WUX' in search_name:
        search_name = 'Nintendo - Wii U (Redump)'

    return search_name


def get_dat_header(
    dat_file: pathlib.Path, input_dat: Dat, config: Config, gui_input: UserInput | None = None
) -> Dat:
    """
    Extract the header from a CLRMAMEPro or LogiqX DAT file.

    Args:
        dat_file (pathlib.Path): A pathlib object pointing to the DAT file.

        input_dat (Dat): The Retool input_dat object.

        config (Config): The Retool config object.

        gui_input (UserInput, optional): Indicates that the main function has been called
            from Retool GUI. Defaults to `None`.

    Returns:
        Dat: The updated input DAT object.
    """
    # Attempt to read in CLRMAMEPro format
    with open(dat_file, encoding='utf-8') as input_file:
        header_complete: bool = False
        clrmamepro_header: list[str] = []

        for i, line in enumerate(input_file):
            if i == 0 and line.strip() == 'clrmamepro (':
                # Likely a valid CLRMAMEPro file, continue reading the file
                clrmamepro_header = ['clrmamepro (']
                input_dat.is_clrmamepro = True
                if not gui_input:
                    eprint(
                        '• Checking DAT file format... file is a CLRMAMEPro DAT file.',
                        overwrite=True,
                    )
            elif i == 0 and line.strip() != 'clrmamepro (':
                # Not a valid CLRMAMEPro DAT file, exit the loop
                break
            elif input_dat.is_clrmamepro and not header_complete:
                # Get the CLRMAMEPro DAT file header and details
                clrmamepro_header.append(line.strip())
                if re.match(
                    '^clrmamepro \\((?:.|\n)*?^\\)$',
                    '\n'.join(clrmamepro_header).strip(),
                    re.MULTILINE,
                ):
                    header_complete = True

                    for header_detail in clrmamepro_header[1:-1]:
                        if header_detail.startswith('author '):
                            input_dat.author = replace_quotes(re.sub('^author ', '', header_detail))

                        if header_detail.startswith('category '):
                            input_dat.clrmamepro_category = replace_quotes(
                                re.sub('^category ', '', header_detail)
                            )

                        if header_detail.startswith('description '):
                            input_dat.description = replace_quotes(
                                re.sub('^description ', '', header_detail)
                            )

                        if header_detail.startswith('name '):
                            input_dat.name = replace_quotes(re.sub('^name ', '', header_detail))

                        if header_detail.startswith('version '):
                            input_dat.version = replace_quotes(
                                re.sub('^version ', '', header_detail)
                            )

                    clrmamepro_header.clear()

    # Attempt to read in LogiqX format
    if not input_dat.is_clrmamepro:

        # Get the LogiqX DAT file header
        input_dat.original_header = []
        input_dat.original_header = get_logiqx_header(dat_file)

        if not input_dat.original_header:
            # Exit if the file isn't in a recognized format
            input_dat.end = True
        else:
            # Parse out the header details
            parser = define_lxml_parser()

            for header_detail in input_dat.original_header:
                element = etree.XML(
                    html_.tostring(html_.fromstring(header_detail.strip())), parser=parser
                )

                # Get ROM manager directives
                if pattern2string(re.compile('(?:clrmamepro|romcenter|romvault)'), element.tag):
                    element = clean_namespaces(element)
                    input_dat.dat_manager_directives.append(html_.tostring(element).decode('utf-8'))

                # Get other header details
                keys = {
                    'name',
                    'description',
                    'version',
                    'author',
                    'homepage',
                    'url',
                    'comment',
                    'retool',
                }

                for key in keys:
                    if element.tag == key:
                        if not element.text:
                            setattr(input_dat, key, 'Unknown')
                        else:
                            setattr(input_dat, key, element.text)

            # Get the <datafile> element in case it has extra attributes like XSD definitions
            with open(dat_file, encoding='utf-8') as input_file:
                for line in input_file:
                    if '<datafile' in line:
                        input_dat.datafile_tag = line.strip()
                        break

    if not input_dat.end:
        # Fix some formatting
        input_dat.name = re.sub(' \\(Retool.*?\\)', '', input_dat.name).replace('&amp;', '&')

        # Sanitize some header details which are used in the output filename
        input_dat.name = TitleTools.replace_invalid_characters(
            input_dat.name, config, is_header_detail=True
        )
        input_dat.version = TitleTools.replace_invalid_characters(
            input_dat.version, config, is_header_detail=True
        )

        for filename in config.reserved_filenames:
            search_string: str = f'^{filename}$'
            if re.search(search_string, input_dat.name) is not None:
                input_dat.name = 'Unknown'
            if re.search(search_string, input_dat.version) is not None:
                input_dat.version = 'Unknown'

        # Sanitize the system name to make referencing support files like clone lists and
        # system configurations easier
        input_dat.search_name = format_system_name(
            input_dat.name,
            config,
            input_dat.url,
            input_dat.homepage,
            input_dat.comment,
            input_dat.author,
        )

        # Set the <datafile> tag
        if not input_dat.datafile_tag:
            input_dat.datafile_tag = '<datafile>'

    return input_dat


def get_clrmamepro_titles(dat_file: pathlib.Path, input_dat: Dat) -> set[TitleData]:
    """
    Gets titles from a CLRMAMEPro DAT file.

    Args:
        dat_file (pathlib.Path): A pathlib object pointing to the DAT file.

        input_dat (Dat): The Retool input_dat object.

    Returns:
        list[TitleData]: A list of titles.
    """
    # Attempt to read in CLRMAMEPro format
    header_complete: bool = False
    clrmamepro_header: list[str] = []
    title_section: list[str] = []
    titles: set[TitleData] = set()

    with open(dat_file, encoding='utf-8') as input_file:
        for line in input_file:
            title: TitleData = TitleData()

            if not header_complete:
                # Skip the CLRMAMEPro DAT file header
                clrmamepro_header.append(line.strip())
                if re.match(
                    '^clrmamepro \\((?:.|\n)*?^\\)$',
                    '\n'.join(clrmamepro_header).strip(),
                    re.MULTILINE,
                ):
                    header_complete = True
            elif line.strip():
                title_section.append(line.strip())
                if re.match(
                    '^(game|set) \\((?:.|\n)*?^\\)$',
                    '\n'.join(title_section).strip(),
                    re.MULTILINE,
                ):
                    # Reset the variables
                    title.name = ''
                    title.description = ''
                    title.categories = set()
                    title.files.clear()

                    # Collect the details
                    if input_dat.clrmamepro_category:
                        title.categories = {input_dat.clrmamepro_category}

                    for title_detail in title_section[1:-1]:
                        if title_detail.startswith('name '):
                            title.name = replace_quotes(re.sub('^name ', '', title_detail))
                        elif title_detail.startswith('description '):
                            title.description = replace_quotes(
                                re.sub('^description ', '', title_detail)
                            )
                        elif title_detail.startswith(('rom ', 'disk ')):
                            file_type: str = 'rom'

                            if title_detail.startswith('disk '):
                                file_type = 'disk'

                            # Check if the name has quotes around it, and then format
                            # accordingly
                            title_name: str

                            if pattern2string(re.compile('name\\s\".*?\"\\s'), title_detail):
                                title_name = pattern2string(
                                    re.compile('name\\s\".*?\"\\s'), title_detail
                                )

                                title_name = replace_quotes(title_name.strip().replace('name ', ''))
                            else:
                                title_name = (
                                    pattern2string(re.compile('name\\s.*?\\s'), title_detail)
                                    .strip()
                                    .replace('name ', '')
                                )

                            title.files.append(
                                {
                                    'name': title_name,
                                    'size': replace_quotes(
                                        pattern2string(
                                            re.compile('size\\s\"?.*?\"?\\s'), title_detail
                                        )
                                    )
                                    .strip()
                                    .replace('size ', ''),
                                    'crc': replace_quotes(
                                        pattern2string(
                                            re.compile('crc\\s\"?.*?\"?\\s'), title_detail
                                        )
                                    )
                                    .strip()
                                    .replace('crc ', ''),
                                    'md5': replace_quotes(
                                        pattern2string(
                                            re.compile('md5\\s\"?.*?\"?\\s'), title_detail
                                        )
                                    )
                                    .strip()
                                    .replace('md5 ', ''),
                                    'sha1': replace_quotes(
                                        pattern2string(
                                            re.compile('sha1\\s\"?.*?\"?\\s'), title_detail
                                        )
                                    )
                                    .strip()
                                    .replace('sha1 ', ''),
                                    'sha256': replace_quotes(
                                        pattern2string(
                                            re.compile('sha256\\s\"?.*?\"?\\s'), title_detail
                                        )
                                    )
                                    .strip()
                                    .replace('sha256 ', ''),
                                    'type': file_type,
                                }
                            )

                    if title.files and title.name:
                        titles.add(deepcopy(title))
                    title_section.clear()
    return titles


def get_logiqx_file_details(
    child: etree._Element, file_type: str, digest_only: bool
) -> dict[str, str]:
    """
    Gets the following file details from a LogiqX rom or disk element.

    * name
    * size
    * mia
    * header
    * crc
    * md5
    * sha1
    * sha256

    Args:
        child (etree._Element): The rom or disk element.

        file_type (str): Whether the element has a rom or disk tag.

        digest_only (bool): Whether to only return digests.

    Returns:
        dict[str, str]: The file details.
    """
    if not digest_only:
        file_name = child.attrib.get('name', '')
        file_size = child.attrib.get('size', '')
        file_mia = child.attrib.get('mia', '')
        file_header = child.attrib.get('header', '')

    file_crc: str = child.attrib.get('crc', '')
    file_md5: str = child.attrib.get('md5', '')
    file_sha1: str = child.attrib.get('sha1', '')
    file_sha256: str = child.attrib.get('sha256', '')

    if digest_only:
        file_details = {'crc': file_crc, 'md5': file_md5, 'sha1': file_sha1, 'sha256': file_sha256}
    else:
        file_details = {
            'name': file_name,
            'size': file_size,
            'crc': file_crc,
            'md5': file_md5,
            'sha1': file_sha1,
            'sha256': file_sha256,
            'type': file_type,
            'mia': file_mia,
            'header': file_header,
        }

    return file_details


def get_logiqx_header(dat_file: pathlib.Path) -> list[str]:
    """
    Reads in the first bytes of a LogiqX DAT file until the header is retrieved. Much
    lighter on memory than parsing with lxml.

    Args:
        dat_file (pathlib.Path): A pathlib object pointing to the DAT file.

    Returns:
        list[str]: The contents of the node for processing later.
    """
    header: list[str] = []

    with open(pathlib.Path(dat_file), 'rb') as file:
        pos: int = 0

        first_line: bytes = file.readline()
        header_bytes: bytes = b''

        file.seek(0)

        # Basic check to make sure it's a LogiqX file
        if (
            b'<?xml version' in first_line
            or b'<!DOCTYPE datafile' in first_line
            or b'<datafile>"' in first_line
        ):
            while file.read(9) != b'</header>':
                pos += 1
                file.seek(pos, os.SEEK_SET)

            file.seek(0)
            header_bytes = file.read(pos + 9)

            header_str = header_bytes.decode('utf-8')

            regex_search_index_start = re.search('\\s*?<header', header_str)
            regex_search_index_end = re.search('\n*\\s*?</header', header_str)

            if regex_search_index_start and regex_search_index_end:
                header_str = header_str[
                    regex_search_index_start.start() : regex_search_index_end.start()
                ]

            # Convert header lines to a list, and handle line endings
            header = [line.replace('\r', '\n') for line in header_str.split('\n') if line != '\r']
            header = [f'{x}\n' if '\n' not in x else x for x in header]
            header[-1] = header[-1].replace('\n', '')

            # Remove the opening header tag
            header_tag_position: int = [index for index, s in enumerate(header) if '<header>' in s][
                0
            ] + 1
            header = header[header_tag_position:]

    return header


def get_logiqx_titles(
    dat_file: pathlib.Path, tag_names: tuple[str, ...], ra_digest_only: bool = False
) -> set[TitleData]:
    """
    Gets the titles from a LogiqX DAT file.

    Args:
        dat_file (pathlib.Path): The path to the DAT file.

        tag_names (tuple[str, ...]): Which tag names to search for in the DAT file (
            usually `game` and `machine`).

        ra_digest_only (bool, optional): Only return the title name and hashes for
            RetroAchievements

    Returns:
        set[TitleData]: A set of titles.
    """
    titles: set[TitleData] = set()

    def process_element(element: etree._Element) -> None:
        if element is not None:
            title: TitleData = TitleData()

            if not ra_digest_only:
                # Collect the details for each title
                title.tag_name = element.tag
                title.name = element.attrib.get('name', '')

                # Only add the title if there's a name
                if title.name:
                    known_attribs: set[str] = {
                        'name',
                        'cloneof',
                        'cloneofid',
                        'retroachievements',
                        'romof',
                    }
                    collected_attribs: dict[str, str] = {}

                    for attrib in element.attrib:
                        if attrib not in known_attribs:
                            collected_attribs[str(attrib)] = str(element.attrib[attrib])

                    title.tag_attribs = collected_attribs

                    if description_element := [
                        x.text for x in element.iterchildren(tag='description')
                    ]:
                        title.description = str(description_element[0])

                    title.categories = {str(x.text) for x in element.iterchildren(tag='category')}

                    files: Iterator[etree._Element] = element.iterchildren(tag=('rom', 'disk'))
                    file_type: str

                    if files:
                        for child in files:
                            file_type = 'rom'

                            if child.tag == 'disk':
                                file_type = 'disk'

                            file_details = get_logiqx_file_details(child, file_type, ra_digest_only)

                            # Check for at least one digest in the file
                            if file_details['name'] and (
                                file_details['crc']
                                or file_details['md5']
                                or file_details['sha1']
                                or file_details['sha256']
                            ):
                                title.files.append(file_details)

                    # Add unrecognized children found in the element
                    unrecognized_children: list[etree._Element] = list(
                        element.xpath(  # type: ignore
                            '*[not(self::category) '
                            'and not(self::description) '
                            'and not(self::disk) '
                            'and not(self::name) '
                            'and not(self::release) '
                            'and not(self::rom)]'
                        )
                    )

                    if unrecognized_children:
                        parser = define_lxml_parser()

                        for child in unrecognized_children:
                            child = etree.XML(html_.tostring(child), parser=parser)
                            title.unrecognized_children.append(
                                etree.tostring(clean_namespaces(child)).decode('utf-8')
                            )
            else:
                title.name = ''

                title.name = element.attrib.get('name', '')

                files = element.iterchildren(tag=('rom', 'disk'))
                file_details = {}

                for child in files:
                    if 'name' in child.attrib:
                        # Exclude CUE or GDI files, which can change digests if the
                        # file name changes
                        if not any(x in child.attrib['name'] for x in ('.cue', '.gdi')):
                            file_details = get_logiqx_file_details(child, '', ra_digest_only)

                    # Check for at least one digest in the file
                    if file_details:
                        if (
                            'crc' in file_details
                            or 'md5' in file_details
                            or 'sha1' in file_details
                            or 'sha256' in file_details
                        ):
                            # RetroAchievements only takes track 0 for multi-track games, so we
                            # only want to return one file anyway
                            if not title.files and file_details:
                                title.files.append(file_details)

            # Add the title if it has files listed
            if title.files:
                titles.add(title)

    context = etree.iterparse(
        source=dat_file,
        events=('end',),
        tag=tag_names,
        attribute_defaults=False,
        encoding='utf-8',
        no_network=True,
        recover=True,
        remove_blank_text=True,
        remove_comments=True,
        remove_pis=True,
        resolve_entities=False,
        strip_cdata=True,
    )

    fast_lxml_iter(context, process_element)

    return titles


def replace_quotes(string: str) -> str:
    """
    Removes quotes around a CLRMAMEPro DAT file entry.

    Args:
        string (str): The string to remove quotes from.

    Returns:
        str: The string with removed quotes.
    """
    return re.sub('^"(.*)"$', '\\1', string)
