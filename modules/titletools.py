from __future__ import annotations

import re
from copy import deepcopy
from re import Pattern
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modules.dats import DatNode
    from modules.config import Config

from modules.utils import Font, eprint, pattern2string


class Removes:
    def __init__(self) -> None:
        """Creates an object that contains titles that have been removed."""
        self.add_ons_removes: set[DatNode] = set()
        self.aftermarket_removes: set[DatNode] = set()
        self.applications_removes: set[DatNode] = set()
        self.audio_removes: set[DatNode] = set()
        self.bad_dumps_removes: set[DatNode] = set()
        self.bios_removes: set[DatNode] = set()
        self.bonus_discs_removes: set[DatNode] = set()
        self.coverdiscs_removes: set[DatNode] = set()
        self.demos_removes: set[DatNode] = set()
        self.educational_removes: set[DatNode] = set()
        self.games_removes: set[DatNode] = set()
        self.manuals_removes: set[DatNode] = set()
        self.mia_removes: set[DatNode] = set()
        self.multimedia_removes: set[DatNode] = set()
        self.pirate_removes: set[DatNode] = set()
        self.preproduction_removes: set[DatNode] = set()
        self.promotional_removes: set[DatNode] = set()
        self.unlicensed_removes: set[DatNode] = set()
        self.video_removes: set[DatNode] = set()
        self.clone_list_removes: set[DatNode] = set()
        self.language_removes: set[DatNode] = set()
        self.region_removes: set[DatNode] = set()
        self.system_excludes: set[DatNode] = set()
        self.global_excludes: set[DatNode] = set()
        self.global_filter_removes: set[DatNode] = set()
        self.system_filter_removes: set[DatNode] = set()


class Regex:
    def __init__(self, LANGUAGES: str) -> None:
        """
        Regular expressions used in Retool.

        Args:
            LANGUAGES (str): All available languages to look for.
        """
        # This is set in the Config class
        self.region_order_default: Pattern[str]

        # Preproduction
        self.alpha: Pattern[str] = re.compile('\\((?:\\w*?\\s)*Alpha(?:\\s\\d+)?\\)', flags=re.I)
        self.beta: Pattern[str] = re.compile('\\((?:\\w*?\\s)*Beta(?:\\s\\d+)?\\)', flags=re.I)
        self.proto: Pattern[str] = re.compile(
            '\\((?:\\w*?\\s)*Proto(?:type)?(?:\\s\\d+)?\\)', flags=re.I
        )
        self.preprod: Pattern[str] = re.compile('\\((?:Pre-production|Prerelease)\\)', flags=re.I)
        self.dev: Pattern[str] = re.compile('\\(DEV|DEBUG\\)', flags=re.I)

        # Possibly production
        self.not_for_resale: Pattern[str] = re.compile(
            '\\((?:Hibaihin|Not for Resale)\\)', flags=re.I
        )
        self.review: Pattern[str] = re.compile('\\(Review (Code|Kit [0-9]+)\\)', re.IGNORECASE)

        # Versions
        self.version: Pattern[str] = re.compile('\\(v[\\.0-9].*?\\)', flags=re.I)
        self.version_non_parens: Pattern[str] = re.compile('(?<!^)(?<=\\(|\\s)v(?:\\d\\.?)+')
        self.long_version: Pattern[str] = re.compile(
            '\\s?(?!Version Vol\\.|Version \\(|Version$|Version -|Version \\d-)(?: - )?\\(?(?:\\((?:\\w[\\.\\-]?\\s*)*|)[Vv]ers(?:ion|ao)\\s?(?:[\\d\\.\\-]+)+[A-Za-z]?(?: (?:\\d-?)+)?.*?(?:(?:\\w[\\.\\-]?\\s*)*\\))?'
        )
        self.revision: Pattern[str] = re.compile('\\(R[eE][vV](?:[ -][0-9A-Z].*?)?\\)', flags=re.I)
        self.build: Pattern[str] = re.compile('\\(Build [0-9].*?\\)', flags=re.I)
        self.dreamcast_version: Pattern[str] = re.compile('V[0-9]{2,2} L[0-9]{2,2}')
        self.fds_version: Pattern[str] = re.compile('\\(DV [0-9].*?\\)', flags=re.I)
        self.fmtowns_pippin_version: Pattern[str] = re.compile(
            '(?<!^)\\s(?:V|Ver\\. |- Version |Version )\\d(?:\\.\\d+)?(?: L(?:evel )?\\d+[A-Z]?)?'
        )
        self.hyperscan_version: Pattern[str] = re.compile('\\(USE[0-9]\\)')
        self.nec_mastering_code: Pattern[str] = re.compile('\\((?:(?:FA|S)[A-F][ABT]S?(?:, )?)+\\)')
        self.nintendo_mastering_code: Pattern[str] = re.compile(
            '\\((?:A[BDEFNPS]|B[58DFJNPT]|CX|FT|JE|K[AFIKMRZ]|PN|QA|RC|S[KN]|T[ABCJQ]|V[BEJKLMW]|Y[XW])[ABCDEFGHIKJMLNPQSTUVWYZ0-9][DEJPVXYZ]\\)'
        )
        self.ps_firmware: Pattern[str] = re.compile('\\(FW[0-9].*?\\)', flags=re.I)
        self.ps1_2_id: Pattern[str] = re.compile('\\([SP][BCL][EKPU][ADHMNSX]-\\d{5}\\)')
        self.ps3_id: Pattern[str] = re.compile('\\([BM][CLR][AEJKTU][BCDMST]-\\d{5}\\)')
        self.ps4_id: Pattern[str] = re.compile('\\([CP][CLU][ACJKS][AMS]-\\d{5}\\)')
        self.psp_id: Pattern[str] = re.compile('\\(U[CLT][EJUS][BST]-\\d{5}\\)')
        self.psv_id: Pattern[str] = re.compile('\\(P[CS]{2}[ABEFGH]\\d{5}\\)')
        self.sega_panasonic_ring_code: Pattern[str] = re.compile(
            '\\((?:(?:[0-9]{1,2}[ABCMRS],? ?)*|R[E]?[-]?[0-9]*)\\)'
        )

        # Video standards
        self.mpal_1: Pattern[str] = re.compile('(?:-)?[( ]MPAL\\)?')
        self.ntsc_1: Pattern[str] = re.compile('(?:-)?[( ]NTSC\\)?')
        self.ntsc_2: Pattern[str] = re.compile('\\[(.*)?NTSC(.*)?\\]')
        self.ntsc_pal: Pattern[str] = re.compile('[( ]NTSC-PAL(\\))?')
        self.pal_1: Pattern[str] = re.compile(
            '( -)?[( ]PAL(?: [a-zA-Z]+| 50[Hh]z)?(?:\\)?| (?=\\())'
        )
        self.pal_2: Pattern[str] = re.compile('\\[(.*)?PAL(?!P)(.*)?\\]')
        self.pal_60: Pattern[str] = re.compile('\\(PAL 60[Hh]z\\)')
        self.secam_1: Pattern[str] = re.compile('(?:-)?[( ]SECAM\\)?')
        self.secam_2: Pattern[str] = re.compile('\\[(.*)?SECAM(.*)?\\]')

        # Other tags
        self.aftermarket: Pattern[str] = re.compile('\\(Aftermarket\\)', flags=re.I)
        self.alt: Pattern[str] = re.compile('\\(Alt.*?\\)', flags=re.I)
        self.bad: Pattern[str] = re.compile('\\[b\\]', flags=re.I)
        self.bios: Pattern[str] = re.compile('\\[BIOS\\]|\\(Enhancement Chip\\)', flags=re.I)
        self.covermount: Pattern[str] = re.compile('\\(Covermount\\)', flags=re.I)
        self.edc: Pattern[str] = re.compile('\\(EDC\\)', flags=re.I)
        self.fmtowns_marty: Pattern[str] = re.compile('\\(FM Towns Marty.*?\\)', flags=re.I)
        self.languages: Pattern[str] = re.compile('\\(((' + LANGUAGES + ')(,\\s?)?)*\\)')
        self.madein: Pattern[str] = re.compile('\\(Made in.*?\\)', flags=re.I)
        self.manuals: Pattern[str] = re.compile('\\(Manual\\)', flags=re.I)
        self.multimedia: Pattern[str] = re.compile('\\(Magazine\\)', flags=re.I)
        self.oem: Pattern[str] = re.compile('\\((?:\\w-?\\s*)*?OEM\\)', flags=re.I)
        self.pirate: Pattern[str] = re.compile('\\(Pirate\\)', flags=re.I)
        self.programs: Pattern[str] = re.compile(
            '\\((?:Test )?Program\\)|(Check|Sample) Program', flags=re.I
        )
        self.promotional: Pattern[str] = re.compile('EPK|Press Kit|\\(Promo\\)', flags=re.I)
        self.rerelease: Pattern[str] = re.compile('\\(Rerelease\\)', flags=re.I)
        self.sega32x: Pattern[str] = re.compile('\\((?:Sega |Mega-)CD 32X\\)', flags=re.I)
        self.unlicensed: Pattern[str] = re.compile('\\(Unl\\)', flags=re.I)

        # Groups for easier application
        self.dates: tuple[Pattern[str], ...] = (
            re.compile('\\(\\d{8}\\)'),
            re.compile('\\(\\d{4}-\\d{2}-\\d{2}\\)'),
            re.compile('\\(\\d{2}-\\d{2}-\\d{4}\\)'),
            re.compile('\\(\\d{2}-\\d{2}-\\d{2}\\)'),
            re.compile('\\(\\d{4}-\\d{2}-\\d{2}T\\d{6}\\)'),
            re.compile('\\((\\d{4}-\\d{2})-xx\\)'),
            re.compile('\\(~?(\\d{4})-xx-xx\\)'),
            re.compile(
                '\\((January|February|March|April|May|June|July|August|September|October|November|December),\\s?\\d{4}\\)',
                flags=re.I,
            ),
        )

        self.demos: tuple[Pattern[str], ...] = (
            re.compile('\\((?:\\w[-.]?\\s*)*Demo(?:(?:,?\\s|-)[\\w0-9\\.]*)*\\)', flags=re.I),
            re.compile('Taikenban', flags=re.I),
            re.compile('\\(@barai\\)', flags=re.I),
            re.compile('\\(GameCube Preview\\)', flags=re.I),
            re.compile('\\(Preview\\)', flags=re.I),
            re.compile('\\(Sample(?:\\s[0-9]*|\\s\\d{4}-\\d{2}-\\d{2})?\\)', flags=re.I),
            re.compile('Trial (Disc|Edition|Version|ver\\.)', flags=re.I),
            re.compile('\\((?:Full )?Trial\\)', flags=re.I),
            re.compile(
                '\\((?:\\w-?\\s*)*?Kiosk,?(?:\\s\\w*?)*\\)|Kiosk Demo Disc|(PSP System|PS2) Kiosk',
                flags=re.I,
            ),
        )

        self.mpal: tuple[Pattern[str], ...] = (self.mpal_1,)

        self.ntsc: tuple[Pattern[str], ...] = (self.ntsc_1, self.ntsc_2, self.ntsc_pal)

        self.pal: tuple[Pattern[str], ...] = (self.pal_1, self.pal_2, self.ntsc_pal)

        self.pal_60hz: tuple[Pattern[str], ...] = (self.pal_60,)

        self.secam: tuple[Pattern[str], ...] = (self.secam_1, self.secam_2)

        self.preproduction: tuple[Pattern[str], ...] = (
            self.alpha,
            self.beta,
            self.proto,
            self.preprod,
            self.dev,
        )

        self.unl_group: tuple[Pattern[str], ...] = (
            self.aftermarket,
            self.pirate,
            self.unlicensed,
        )

        self.video: tuple[Pattern[str], ...] = (
            re.compile('Game Boy Advance Video', flags=re.I),
            re.compile('- (Preview|Movie) Trailer', flags=re.I),
            re.compile('\\((?:\\w*\\s)*Trailer(?:s|\\sDisc)?(?:\\s\\w*)*\\)', flags=re.I),
        )

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)


class TitleTools:
    """Manipulates and validates titles found in DATs for use in Retool."""

    @staticmethod
    def convert_to_virtual_titles(
        title_set: set[DatNode],
        compare_groups: dict[str, set[DatNode]],
        title_group: str,
        config: Config,
    ) -> dict[str, set[DatNode]]:
        """
        Breaks compilations into into separate, virtual titles.

        Args:
            title_set (set[DatNode]): Compilation titles to be considered.

            compare_groups (dict[str, set[DatNode]]): A dictionary to store the
            virtual titles in for comparison later.

            title_group (str): The group the title should be assigned to.

            config (Config): The Retool config object.
        """
        for title in title_set:
            if title_group in ','.join([x.lower() for x in title.contains_titles]):
                # Split compilations into virtual titles
                virtual_languages: str = ''

                # Get preproduction strings out of the title
                for pattern in config.regex.preproduction:
                    preproduction_string = pattern2string(pattern, title.full_name, 0)
                    if preproduction_string:
                        preproduction_string = f' {preproduction_string}'
                        break

                # Assign properties like full names, short names, languages and priority to the virtual title
                for individual_title in title.contains_titles:
                    if '+' in title.languages_title_orig_str:
                        compilation_languages: list[str] = title.languages_title_orig_str.split('+')

                        virtual_languages = f' ({compilation_languages[title.contains_titles[individual_title]["position"] - 1]})'
                    elif title.languages:
                        virtual_languages = f' ({",".join(title.languages)})'

                    virtual_title: DatNode = deepcopy(title)

                    virtual_title.full_name = f':V: {individual_title} ({", ".join(title.regions)}){virtual_languages}{preproduction_string} • {title.full_name}'
                    virtual_title.short_name = individual_title.lower()
                    virtual_title.languages = tuple(
                        virtual_languages.strip().replace('(', '').replace(')', '').split(',')
                    )
                    virtual_title.clonelist_priority = title.contains_titles[individual_title][
                        "priority"
                    ]

                    if individual_title.lower() == title_group:
                        if virtual_title.full_name not in [
                            x.full_name for x in compare_groups[title_group]
                        ]:
                            compare_groups[title_group].add(virtual_title)

        return compare_groups

    @staticmethod
    def find_title(
        name: str,
        name_type: str,
        titles: dict[str, set[DatNode]],
        missing_titles: set[str],
        config: Config,
        deep_search: bool = False,
    ) -> set[DatNode]:
        """
        Finds titles in a dict of DatNodes, whether by short, tag free, or full name,
        or regex.

        Args:
            name (str): The name to search for.

            name_type (str): Whether to search for the `short` name,
            `regionFree` name, `full` name, or by `regex` on the full name.

            titles (dict[str, set[DatNode]]): A dictionary of DatNodes to search.

            missing_titles (set[str]): Somewhere to store searched for names that aren't
            found in the DAT file when going through `titles`. These are reported as not
            found if the user has clone list warnings turned on.

            config (Config): The Retool config object.

            deep_search (bool, optional): Usually for speed a title is searched for by
            deriving the group name from the full name. If Retool has done a certain
            amount of processing already, titles might have changed groups. A deep search
            traverses the entire dictionary for the title instead. Mandatory for a
            `match_type` of `regex`, defaults to `False`.

        Returns:
            set[DatNode]: A list of titles that match the search terms.
        """
        found_titles: set[DatNode] = set()

        if deep_search:
            # Find the title not knowing the group name
            for group in titles:
                for title in list(titles[group]):
                    if name_type == 'short' and title.short_name.lower() == name.lower():
                        found_titles.add(title)
                    elif name_type == 'full' and title.full_name.lower() == name.lower():
                        found_titles.add(title)
                    elif name_type == 'regex' and re.search(name, title.full_name.lower(), re.I):
                        found_titles.add(title)
                    elif (
                        name_type == 'regionFree' and title.region_free_name.lower() == name.lower()
                    ):
                        found_titles.add(title)
            if not found_titles:
                missing_titles.add(name)
        else:
            # Find the title by deriving the group name
            group_name: str = TitleTools.get_group_name(name, config)

            if group_name in titles:
                for title in titles[group_name]:
                    if name_type == 'short' and title.short_name.lower() == name.lower():
                        found_titles.add(title)
                    elif name_type == 'full' and title.full_name.lower() == name.lower():
                        found_titles.add(title)
                    elif name_type == 'regex' and re.search(name, title.full_name.lower(), re.I):
                        found_titles.add(title)
                    elif (
                        name_type == 'regionFree' and title.region_free_name.lower() == name.lower()
                    ):
                        found_titles.add(title)
            else:
                missing_titles.add(name)

        return found_titles

    @staticmethod
    def get_date(name: str, config: Config) -> int:
        """
        Looks for a date tag in a title's name, then returns the date in a consistent
        format.

        Args:
            name (str): A title's full name.

            config (Config): The Retool config object.

        Returns:
            int: The date in a consistent, comparable format.
        """
        months: list[str] = [
            'january',
            'february',
            'march',
            'april',
            'may',
            'june',
            'july',
            'august',
            'september',
            'october',
            'november',
            'december',
        ]

        formatted_date: int = 0

        # Normalize YYYY-MM-xx and YYYY-xx-xx dates
        if re.search(config.regex.dates[5], name):
            name = re.sub(config.regex.dates[5], '(\\1-01)', name)

        if re.search(config.regex.dates[6], name):
            name = re.sub(config.regex.dates[6], '(\\1-01-01)', name)

        us_date: bool = False
        short_date: bool = False
        utc_date: bool = False
        time: str = '000000'

        if re.search('|'.join(months), name, flags=re.I):
            for i, month in enumerate(months):
                if i < 9:
                    name = re.sub(f'{month}, ', f'0{i + 1}-01-', name, flags=re.I)
                else:
                    name = re.sub(f'{month}, ', f'{i + 1}-01-', name, flags=re.I)

        if re.search(config.regex.dates[2], name):
            us_date = True
        if re.search(config.regex.dates[3], name):
            short_date = True
        if re.search(config.regex.dates[4], name):
            utc_date = True

        for regex in config.regex.dates:
            year: str = ''
            month = ''
            day: str = ''

            if re.search(regex, name):
                regex_search_str = pattern2string(regex, name)

                name = name.replace(regex_search_str, regex_search_str.replace('-', ''))

                regex = config.regex.dates[0]
                regex_search_str = pattern2string(regex, name)

                if short_date:
                    regex = re.compile('\\(\\d{6}\\)')
                    regex_search_str = pattern2string(regex, name)
                    if int(regex_search_str[1:-5]) < 70:
                        year = str(2000 + int(regex_search_str[1:-5]))
                    else:
                        year = str(1900 + int(regex_search_str[1:-5]))
                    month = regex_search_str[3:-3]
                    day = regex_search_str[5:-1]
                elif us_date:
                    year = regex_search_str[5:-1]
                    month = regex_search_str[1:-7]
                    day = regex_search_str[3:-5]
                elif utc_date:
                    regex = re.compile('\\(\\d{8}T\\d{6}\\)')
                    regex_search_str = pattern2string(regex, name)
                    year = regex_search_str[1:5]
                    month = regex_search_str[5:7]
                    day = regex_search_str[7:9]
                    time = regex_search_str[10:16]
                else:
                    year = regex_search_str[1:-5]
                    month = regex_search_str[5:-3]
                    day = regex_search_str[7:-1]

                if (
                    int(year) >= 1970
                    and int(month) >= 1
                    and int(month) <= 12
                    and int(day) >= 1
                    and int(day) <= 31
                ):
                    formatted_date = int(f'{year}{month}{day}{time}')
                    break

        return formatted_date

    @staticmethod
    def languages(name: str, tags: set[str], config: Config, method: str) -> str:
        """
        Identifies the languages in a title's name, and either returns just
        the languages, or returns the title's name without the languages tag.

        Args:
            name (str): A title's full name.

            config (Config): The Retool config object.

            tags: (set[str]): The title tags.

            method (str): Whether to `get` the languages from the title's
            name, or `remove` them.

        Returns:
            str: Either the name of the title with the languages tag stripped,
            or just the languages.
        """
        regex_search_str: str = ''
        result: str = ''

        if tags:
            for tag in tags:
                if pattern2string(config.regex.languages, tag):
                    regex_search_str = pattern2string(config.regex.languages, tag)
                    break
        else:
            regex_search_str = pattern2string(config.regex.languages, name)

        if regex_search_str:
            if method == 'remove':
                result = name.replace(f'{regex_search_str}', '').replace('  ', ' ').strip()

            if method == 'get':
                result = regex_search_str.strip()[1:-1]

        return result

    @staticmethod
    def regions(name: str, config: Config, method: str) -> str:
        """
        Identifies the regions in a title's name, and either returns just
        the regions, or returns the title's name without the regions tag.

        Args:
            name (str): A title's full name.

            config (Config): The Retool config object.

            method (str): Whether to `get` the languages from the title's
            name, or `remove` them.

        Returns:
            str: Either the name of the title with the region tag stripped, or
            just the regions.
        """
        regex_search_str: str = pattern2string(config.regex.region_order_default, name)

        result: str = ''

        if regex_search_str:
            regex_search_str = f' {regex_search_str}'
            if method == 'remove':
                result = name.replace(regex_search_str, '').strip()

            if method == 'get':
                result = regex_search_str.strip()[1:-1].replace('Export', 'World')

        return result

    @staticmethod
    def remove_tags(name: str, config: Config) -> str:
        """
        Removes tags found in internal-config.json that are set as "ignore tags" from
        the input title's full name. This includes the explicit `ignore_tags` array, but
        also the `promote_editions`, `demote_editions`, and `modern_editions` arrays.

        Args:
            name (str): A title's full name.

            config (Config): The Retool config object.

        Returns:
            str: The full name of the title without any ignored tags.
        """
        for tag in config.tags_ignore:
            if tag[1] == 'regex':
                name = re.sub(tag[0], '', name).strip()
            elif tag[1] == 'string':
                if tag[0] in name:
                    name = name.replace(f'{tag[0]}', '').replace('  ', ' ').strip()

        return name

    @staticmethod
    def normalize_discs(name: str, config: Config) -> str:
        """
        Renames multiple variants of "Disk", "Disc", "Disque" and more found in title
        names to the same standard to make title matching easier. The strings are defined
        in the `disc_rename` array in internal-config.json.

        Args:
            name (str): A title's full name.

            config (Config): The Retool config object.

        Returns:
            str: The full name of the title with any disc tags normalized.
        """
        for key, value in config.tags_disc_rename.items():
            if key in name:
                name = name.replace(key, value)

        return name

    @staticmethod
    def get_group_name(name: str, config: Config) -> str:
        """
        Finds the group name of a given title from one of its other names.
        A group name is generally determined by taking a name string up to the first
        instance of ' (', although some exceptions have to be made for custom versioning
        where parentheses aren't used.

        Args:
            name (str): A title's full name.

            config (Config): The Retool config object.

        Returns:
            str: The group name of the title, derived from one of its other names.
        """
        name = name.rstrip()

        if name.find('(') != -1:
            name = name[: (name.find('(') - 1)].rstrip()

        # Dreamcast version compensation
        if re.search(config.regex.dreamcast_version, name):
            name = re.sub(config.regex.dreamcast_version, '', name)

        # FM-Towns/Pippin version compensation
        if re.search(config.regex.fmtowns_pippin_version, name):
            name = re.sub(config.regex.fmtowns_pippin_version, '', name)

        # Long version compensation
        if re.search(config.regex.long_version, name):
            name = re.sub(config.regex.long_version, '', name)

        # Short version compensation
        if re.search(config.regex.version_non_parens, name):
            name = re.sub(config.regex.version_non_parens, '', name)

        # Video standard compensation
        for pattern in config.regex.ntsc:
            if re.search(pattern, name):
                name = re.sub(pattern, '', name)

        for pattern in config.regex.pal:
            if re.search(pattern, name):
                name = re.sub(pattern, '', name)

        for pattern in config.regex.pal_60hz:
            if re.search(pattern, name):
                name = re.sub(pattern, '', name)

        for pattern in config.regex.secam:
            if re.search(pattern, name):
                name = re.sub(pattern, '', name)

        return name.lower().replace('  ', ' ').strip()

    @staticmethod
    def get_region_free_name(name: str, tags: set[str], config: Config) -> str:
        """
        Finds the region-free name of a title, given its full name. This means both
        the name's regions and languages are removed.

        Args:
            name (str): A title's full name.

            tags: (set[str]): The title tags.

            config (Config): The Retool config object.

        Returns:
            str: The region-free name of the title.
        """
        original_name: str = name

        remove_regions: str = TitleTools.regions(name, config, 'remove')

        if remove_regions:
            name = remove_regions

        remove_languages = TitleTools.languages(name, tags, config, 'remove')

        if remove_languages:
            name = remove_languages

        if not name:
            name = original_name

        return name

    @staticmethod
    def get_short_name(name: str, tags: set[str], config: Config) -> str:
        """
        Finds the short name of a given title. A short name is a full name that has
        had its ignored, region, and language tags removed, and its disc names normalized.

        Among other things, the short name helps to differentiate titles that are assigned
        to the same group. For example, `Title 1 (USA) (Disc 1)` and
        `Title 1 (USA) (Disc 2)` end up in the same group, `title 1`. However the short
        names of `title 1 (disc 1)` and `title 1 (disc 2)` mean that the titles aren't
        confused with one another.

        Args:
            name (str): A title's full name.

            tags: (set[str]): The title tags.

            config (Config): The Retool config object.

        Returns:
            str: The short name of the title.
        """
        name = TitleTools.normalize_discs(name, config)
        name = TitleTools.remove_tags(name, config)
        name = TitleTools.get_region_free_name(name, tags, config).strip()

        return name.lower()

    @staticmethod
    def replace_invalid_characters(name: str, config: Config, is_header_detail: bool) -> str:
        r"""
        Removes invalid file / folder name characters from a string.

        Args:
            name (str): A title's full name, or a DAT header detail.

            config (Config): The Retool config object.

            is_header_detail (bool): Set to `True` if checking a DAT's header strings
            for invalid characters. Unlike filepaths, `/` and `\` are replaced for
            header details.

        Returns:
            str: A string with invalid characters removed.
        """
        for character in config.sanitized_characters:
            if character in name:
                if character == ':':
                    if re.search('(\\S):\\s', name):
                        name = re.sub('(\\S):\\s', '\\1 - ', name)
                    else:
                        name = name.replace(character, '-')
                elif character == '"':
                    name = name.replace(character, '\'')
                elif character == '\\':
                    if is_header_detail:
                        name = name.replace(character, '-')
                elif character == '/':
                    if is_header_detail:
                        name = name.replace(character, '-')
                else:
                    name = name.replace(character, '-')

        # For strings that start with ., use the fixed width ．instead
        if not is_header_detail:
            name = re.sub('^\\.', '．', name)  # noqa: RUF001

        return name


class TraceTools:
    """Tools to trace a title's progress throughout Retool."""

    @staticmethod
    def trace_enable(title_set: set[DatNode], trace_str: str) -> bool:
        """
        Works through a set of DatNodes to see if it contains a title the user is
        searching for. If so, enable a trace.

        Args:
            title_set (set[DatNode]): A set of DatNodes currently being processed.

            trace_str (str): The string being traced.

        Returns:
            bool: If a match for the trace string is foundm returns `True`. Otherwise,
            returns `False`.
        """
        report_on_match: bool = False

        if any(
            re.search(trace_str.lower(), d.full_name.lower(), flags=re.I) for d in list(title_set)
        ):
            report_on_match = True

        return report_on_match

    @staticmethod
    def trace_title(
        trace_reference: str,
        variable: list[str] = [],
        title_set: set[DatNode] = set(),
        keep_remove: bool = False,
    ) -> None:
        """
        Messages for when a title being traced through Retool's process is acted upon.
        Where possible, the trace calls a reference message listed here to keep the code
        in other places neater.

        Args:
            trace_reference (str): In the format `REF####`. Causes the relevant message
            print, based on its reference number.

            variable (list[str], optional): Variables that can be included in the
            reference message, or alternatively, to specify which title is being kept and
            which is being removed when comparing two titles. Defaults to `[]`.

            title_set (set[DatNode], optional): The set of DatNodes that are being
            acted upon. Defaults to `set()`.

            keep_remove (bool, optional): Whether or not to show text which indicates
            which title has been kept, and which has been removed when comparing two
            titles. Defaults to `False`.
        """
        message: str = ''
        if trace_reference == 'REF0001':
            message = 'Original unmodified group:'
        if trace_reference == 'REF0002':
            message = 'Group after taking clone list priorities into account:'
        if trace_reference == 'REF0003':
            message = (
                'Group after cleaning up preproduction/bad/pirate/mixed version-revision titles:'
            )
        if trace_reference == 'REF0004':
            message = 'Group after handling modern title rips:'
        if trace_reference == 'REF0005':
            message = '[First pass] Group after filtering by user language order:'
        if trace_reference == 'REF0006':
            message = 'Group after handling special editions:'
        if trace_reference == 'REF0007':
            message = 'Group after handling versions and revisions:'
        if trace_reference == 'REF0008':
            message = 'Group after handling modern title rips:'
        if trace_reference == 'REF0009':
            message = 'Group after choosing dates:'
        if trace_reference == 'REF0010':
            message = 'Group after choosing good, original versions over alternatives:'
        if trace_reference == 'REF0011':
            message = 'Group after handling promotions and demotions:'
        if trace_reference == 'REF0012':
            message = 'Group after handling "Made in" titles:'
        if trace_reference == 'REF0013':
            message = 'Cross region parents:'
        if trace_reference == 'REF0014':
            message = 'Group after lower priority region, non-superset clones removed:'
        if trace_reference == 'REF0015':
            message = 'Highest language priority titles:'
        if trace_reference == 'REF0016':
            message = f'{Font.warning_bold}Top superset title for tag free name {variable[1]}: {variable[0]}'
        if trace_reference == 'REF0017':
            message = 'Top superset title/s for group:'
        if trace_reference == 'REF0018':
            message = 'Group after production title check:'
        if trace_reference == 'REF0019':
            message = f'{Font.success_bold}ACTION: Clone assignments (might be reassigned later):'
        if trace_reference == 'REF0020':
            message = 'ACTION: Compare clone list priority:'
        if trace_reference == 'REF0021':
            message = 'ACTION: Compare clone list priority:'
        if trace_reference == 'REF0022':
            message = 'ACTION: Compare clone list priority (both titles are supersets):'
        if trace_reference == 'REF0023':
            message = 'ACTION: Compare clone list priority (both titles are supersets):'
        if trace_reference == 'REF0024':
            message = 'ACTION: Compare dates:'
        if trace_reference == 'REF0028':
            message = f'Compare languages\nUser language order: {variable[0]}'
        if trace_reference == 'REF0029':
            message = f'Compare languages\nUser language order: {variable[0]}'
        if trace_reference == 'REF0030':
            message = 'ACTION: Favor multiple regions higher up user region order:'
        if trace_reference == 'REF0031':
            message = 'ACTION: Favor multiple regions higher up user region order:'
        if trace_reference == 'REF0032':
            message = 'ACTION: Choose title with string:'
        if trace_reference == 'REF0033':
            message = 'ACTION: Choose title without string:'
        if trace_reference == 'REF0034':
            message = 'ACTION: Choose title with string:'
        if trace_reference == 'REF0035':
            message = 'ACTION: Choose title without string:'
        if trace_reference == 'REF0036':
            message = 'ACTION: Choose "Made in" title:'
        if trace_reference == 'REF0037':
            message = 'ACTION: Choose "Made in" title:'
        if trace_reference == 'REF0038':
            message = 'ACTION: Choose higher versions:'
        if trace_reference == 'REF0039':
            message = 'ACTION: Choose higher versions:'
        if trace_reference == 'REF0040':
            message = 'ACTION: Choose higher versions:'
        if trace_reference == 'REF0041':
            message = 'ACTION: Choose higher versions:'
        if trace_reference == 'REF0042':
            message = f'ACTION: Excluded due to categories: {variable[0]}'
        if trace_reference == 'REF0043':
            message = '[Second pass] Group after filtering by user language order:'
        if trace_reference == 'REF0044':
            message = f'ACTION: Excluded due to a categories regex: {variable[0]}'
        if trace_reference == 'REF0045':
            message = 'ACTION: Excluded due to a system override:'
        if trace_reference == 'REF0046':
            message = 'ACTION: Excluded due to a global override:'
        if trace_reference == 'REF0047':
            message = 'ACTION: Included due to a system override:'
        if trace_reference == 'REF0048':
            message = 'ACTION: Included due to a global override:'
        if trace_reference == 'REF0049':
            message = f'ACTION: Removed due to user language filters: {variable[0]}'
        if trace_reference == 'REF0050':
            message = 'Would have been a system override exclude, but was cancelled out by a system include:'
        if trace_reference == 'REF0051':
            message = 'Would have been a global override exclude, but was cancelled out by a global include:'
        if trace_reference == 'REF0052':
            message = 'Would have been a global override exclude, but was cancelled out by a system include:'
        if trace_reference == 'REF0053':
            message = f'ACTION: Changing categories for title found in clone list {Font.b}Categories{Font.be} object:'
        if trace_reference == 'REF0054':
            message = f'ACTION: Removing title found in clone list {Font.b}Removes{Font.be} object:'
        if trace_reference == 'REF0055':
            message = f'ACTION: Moving title found in clone list {Font.b}Variants{Font.be} object to other group:'
        if trace_reference == 'REF0056':
            message = f'ACTION: Overriding default group for title found in clone list {Font.b}overrides{Font.be} object:'
        if trace_reference == 'REF0057':
            message = 'ACTION: Fail safe removal of title with lower string value:'
        if trace_reference == 'REF0058':
            message = 'ACTION: Fail safe removal of title with lower string value:'
        if trace_reference == 'REF0059':
            message = 'Group after filtering by string comparison:'
        if trace_reference == 'REF0060':
            message = 'Group after handling unlicensed/aftermarket/pirate versions:'
        if trace_reference == 'REF0061':
            message = 'Group after handling Alt versions:'
        if trace_reference == 'REF0062':
            message = 'ACTION: Excluded due to known MIA:'
        if trace_reference == 'REF0063':
            message = 'ACTION: Title tagged as MIA:'
        if trace_reference == 'REF0066':
            message = 'ACTION: Included due to being related to a system or global override:'
        if trace_reference == 'REF0067':
            message = 'Original unmodified group: \n\nVirtual titles are marked with a :V:, the original compilation title is after the •'
        if trace_reference == 'REF0068':
            message = 'Group after filtering by user language order:\n\nVirtual titles are marked with a :V:, the original compilation title is after the •'
        if trace_reference == 'REF0069':
            message = 'Group after filtering by region order:\n\nVirtual titles are marked with a :V:, the original compilation title is after the •'
        if trace_reference == 'REF0070':
            message = 'Group with original compilation names:'
        if trace_reference == 'REF0071':
            message = f'Contenders for crossover groups: {Font.b}{variable[0]}{Font.be}'
        if trace_reference == 'REF0072':
            message = f'Looking for this ideal combination: {Font.b}{variable}{Font.be}\n\nFound:'
        if trace_reference == 'REF0073':
            message = 'ACTION: Compilation clone assignments'
        if trace_reference == 'REF0074':
            message = 'Only one title in this region, skipping filtering:'
        if trace_reference == 'REF0075':
            message = 'ACTION: Tie breaker, remove the compilation title:'
        if trace_reference == 'REF0076':
            message = 'Group after choosing superset titles:'
        if trace_reference == 'REF0077':
            message = 'ACTION: Choose supersets:'
        if trace_reference == 'REF0078':
            message = 'ACTION: Choose supersets:'
        if trace_reference == 'REF0079':
            message = 'Group after favoring multiple regions higher up user region order:'
        if trace_reference == 'REF0080':
            message = 'Group after filtering by clone list priority:'
        if trace_reference == 'REF0081':
            message = 'ACTION: Choose more languages:'
        if trace_reference == 'REF0082':
            message = 'ACTION: Choose more languages:'
        if trace_reference == 'REF0083':
            message = f'Fallback language comparison. Compare languages based on default region order.\nDefault region language order: {variable[0]}'
        if trace_reference == 'REF0084':
            message = f'Fallback language comparison. Compare languages based on default region order.\nDefault region language order: {variable[0]}'
        if trace_reference == 'REF0085':
            message = f'ACTION: ROM tagged as MIA in {Font.b}{variable[0]}{Font.be}:'
        if trace_reference == 'REF0086':
            message = 'ACTION: User has region bias enabled, selecting a higher region title than the superset:'
        if trace_reference == 'REF0087':
            message = 'ACTION: Keeping superset title:'
        if trace_reference == 'REF0088':
            message = 'ACTION: Keeping superset title:'
        if trace_reference == 'REF0089':
            message = 'Group after filtering by user language order:\n\nVirtual titles are marked with a :V:, the original title is after the •'
        if trace_reference == 'REF0090':
            message = 'ACTION: Keeping compilation that contains another:'
        if trace_reference == 'REF0091':
            message = 'ACTION: Keeping compilation that contains another:'
        if trace_reference == 'REF0092':
            message = 'Group after removing preproduction:'
        if trace_reference == 'REF0093':
            message = 'ACTION: Tie breaker, remove the compilation title:'
        if trace_reference == 'REF0094':
            message = 'ACTION: Favor primary region higher up user region order (individual title vs compilation):'
        if trace_reference == 'REF0095':
            message = 'ACTION: Favor primary region higher up user region order (individual title vs compilation):'
        if trace_reference == 'REF0096':
            message = 'Group after choosing video standard:'
        if trace_reference == 'REF0097':
            message = f'Fallback language comparison. Compare languages based on region order.\nRegion language order: {variable[0]}'
        if trace_reference == 'REF0098':
            message = f'Fallback language comparison. Compare languages based on region order.\nRegion language order: {variable[0]}'
        if trace_reference == 'REF0099':
            message = 'ACTION: Kept due to system post filter:'
        if trace_reference == 'REF0100':
            message = 'ACTION: Kept due to global post filter:'
        if trace_reference == 'REF0101':
            message = 'Group after fallback user language priority check:'
        if trace_reference == 'REF0102':
            message = 'Group after fallback higher priority region check:'
        if trace_reference == 'REF0103':
            message = 'Group after non-superset clones removed:'
        if trace_reference == 'REF0104':
            message = 'Group after fallback user language priority check:'
        if trace_reference == 'REF0105':
            message = 'ACTION: Tie breaker, keep the first compilation title:'
        if trace_reference == 'REF0106':
            message = 'ACTION: Compare clone list priority (both titles are supersets):'
        if trace_reference == 'REF0107':
            message = 'ACTION: Compare clone list priority (both titles are supersets):'
        if trace_reference == 'REF0108':
            message = f'ACTION: Changing categories for title found in clone list {Font.b}Variants{Font.be} object:'
        if trace_reference == 'REF0109':
            message = f'ACTION: Moving title found in clone list {Font.b}Variants{Font.be} object to other group due to a condition being true:'
        if trace_reference == 'REF0110':
            message = f'ACTION: Changing a title\'s priority due to a condition in the {Font.b}Variants{Font.be} object being true:'
        if trace_reference == 'REF0111':
            message = f'ACTION: Setting a title\'s local name due to a condition in the {Font.b}Variants{Font.be} object being true:'
        if trace_reference == 'REF0112':
            message = f'ACTION: Marking a title as English-friendly due to an entry in the {Font.b}Variants{Font.be} object:'
        if trace_reference == 'REF0113':
            message = f'ACTION: Marking a title as English-friendly due to a condition in the {Font.b}Variants{Font.be} object being true:'
        if trace_reference == 'REF0114':
            message = 'ACTION: Found a superset assigned as a both a parent and clone. Setting title with the superset as a parent to the superset\'s parent to resolve the conflict:'
        if trace_reference == 'REF0115':
            message = f'ACTION: Setting a title\'s local name as defined in the {Font.b}Variants{Font.be} object:'
        if trace_reference == 'REF0116':
            message = f'ACTION: Setting a title as a superset due to a condition in the {Font.b}Variants{Font.be} object being true:'
        if trace_reference == 'REF0117':
            message = 'ACTION: Choose title without string:'
        if trace_reference == 'REF0118':
            message = 'ACTION: Choose title without string:'
        if trace_reference == 'REF0119':
            message = 'Group after good dump/production/retail check:'
        if trace_reference == 'REF0120':
            message = 'INFO: Here are the title groups in contention:'
        if trace_reference == 'REF0121':
            message = 'INFO: Here are the regions required for each group in contention:'
        if trace_reference == 'REF0122':
            message = f'INFO: Here are the combinations in groups of {variable[0]}:'
        if trace_reference == 'REF0123':
            message = 'INFO: Here are the results of the candidate selection stages:'
        if trace_reference == 'REF0124':
            message = 'INFO: Testing these candidates for consideration:'
        if trace_reference == 'REF0125':
            message = 'INFO: Test details for candidate:'
        if trace_reference == 'REF0126':
            message = 'Group after choosing individual title due to user preference:'
        if trace_reference == 'REF0127':
            message = 'Group after choosing superset:'
        if trace_reference == 'REF0128':
            message = 'Group after comparing compilations:'
        if trace_reference == 'REF0129':
            message = f'ACTION: Marking a title as the oldest due to an entry in the {Font.b}Variants{Font.be} object:'
        if trace_reference == 'REF0130':
            message = 'ACTION: Compare clone list priority, oldest title:'
        if trace_reference == 'REF0131':
            message = 'ACTION: Compare clone list priority, oldest title:'
        if trace_reference == 'REF0132':
            message = f'ACTION: Marking a title as the oldest due to a condition in the {Font.b}Variants{Font.be} object being true:'
        if trace_reference == 'REF0133':
            message = 'Group after handling budget editions:'

        if trace_reference:
            eprint(
                f'\n{Font.b}{Font.u}{trace_reference}{Font.end}: {message}{Font.end}\n', indent=0
            )

        if title_set:
            # Superset titles can be in multiple groups, so deduping needs to be done
            reported_title_set: dict[str, DatNode] = {}

            for title in title_set:
                reported_title_set[title.full_name] = title

            title_set = set(reported_title_set.values())

            for title in sorted(title_set, key=lambda x: x.full_name):
                eprint(f'• {title.full_name}', wrap=False)
            eprint(pause=True)

        if keep_remove:
            eprint(f'+ Keeping:  {variable[0]}', wrap=False)
            eprint(f'- Removing: {variable[1]}', level='disabled', wrap=False, pause=True)
