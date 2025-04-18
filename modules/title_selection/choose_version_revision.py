from __future__ import annotations

import itertools
import re
from re import Pattern
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modules.config import Config
    from modules.dats import DatNode

from modules.titletools import TraceTools
from modules.utils import Font, pattern2string


def choose_version_revision(
    pattern: Pattern[str], title_set: set[DatNode], config: Config, report_on_match: bool
) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes to see which one has the
    highest version/revision tag.

    Args:
        pattern (Pattern[str]): The version pattern to search for in the title name.

        title_set (set[DatNode]): A set of titles as DatNode instances.

        config (Config): The Retool config object.

        report_on_match (bool): Whether Retool needs to report any titles being
        traced.

    Returns:
        set[DatNode]: A set of DatNodes filtered by highest version.
    """
    remove_titles: set[DatNode] = set()

    for title_1, title_2 in itertools.combinations(title_set, 2):
        # Normalize titles that contain "Version #", "(v#)" and "v#" formatting
        title_1_name_normalized: str = re.sub(' Version ((\\d\\.?)+)', ' (v\\1)', title_1.full_name)
        title_2_name_normalized: str = re.sub(' Version ((\\d\\.?)+)', ' (v\\1)', title_2.full_name)
        title_1_name_normalized = re.sub(' (v(\\d\\.?)+)', ' (\\1)', title_1_name_normalized)
        title_2_name_normalized = re.sub(' (v(\\d\\.?)+)', ' (\\1)', title_2_name_normalized)

        # Fix bad beta tags
        title_1_name_normalized = re.sub(
            ' \\((v(\\d\\.?)+)beta\\)', ' (\\1) (Beta)', title_1_name_normalized
        )
        title_2_name_normalized = re.sub(
            ' \\((v(\\d\\.?)+)beta\\)', ' (\\1) (Beta)', title_2_name_normalized
        )

        if (
            title_1.short_name == title_2.short_name
            and title_1 in title_set
            and title_2 in title_set
            and 'BIOS' not in title_1.categories
            and 'BIOS' not in title_2.categories
        ):

            keep_title_name: str = ''
            remove_title_name: str = ''

            # Perform version comparison between a title that has a version string and a title that doesn't
            if re.search(pattern, title_1_name_normalized) and not re.search(
                pattern, title_2_name_normalized
            ):
                if pattern in config.regex.preproduction:
                    if title_1 in title_set:
                        keep_title_name = title_2.full_name
                        remove_title_name = title_1.full_name

                        remove_titles.add(title_1)
                else:
                    if config.user_input.oldest:
                        if title_1 in title_set:
                            keep_title_name = title_2.full_name
                            remove_title_name = title_1.full_name

                            remove_titles.add(title_1)
                    else:
                        if title_2 in title_set:
                            keep_title_name = title_1.full_name
                            remove_title_name = title_2.full_name

                            remove_titles.add(title_2)

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0038',
                        [
                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {keep_title_name}',
                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {remove_title_name}{Font.end}',
                        ],
                        keep_remove=True,
                    )
            elif re.search(pattern, title_2_name_normalized) and not re.search(
                pattern, title_1_name_normalized
            ):
                if pattern in config.regex.preproduction:
                    if title_2 in title_set:
                        keep_title_name = title_1.full_name
                        remove_title_name = title_2.full_name

                        remove_titles.add(title_2)
                else:
                    if config.user_input.oldest:
                        if title_2 in title_set:
                            keep_title_name = title_1.full_name
                            remove_title_name = title_2.full_name

                            remove_titles.add(title_2)
                    else:
                        if title_1 in title_set:
                            keep_title_name = title_2.full_name
                            remove_title_name = title_1.full_name

                            remove_titles.add(title_1)

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0039',
                        [
                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {keep_title_name}',
                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {remove_title_name}{Font.end}',
                        ],
                        keep_remove=True,
                    )

            # Perform version comparison between two titles that both have version strings
            elif re.search(pattern, title_1_name_normalized) and re.search(
                pattern, title_2_name_normalized
            ):

                def process_versions(ver_1: str, ver_2: str) -> list[Any]:
                    """
                    Attempts to convert versions into a comparable format.

                    Args:
                        ver_1 (str): The first title's version.

                        ver_2 (str): The second title's version.

                    Returns:
                        list[Any]: A list of normalized versions.
                    """
                    version_compare_normalize: list[Any] = []

                    if '.' in ver_1 or '.' in ver_2:
                        ver_1_parsed: list[Any] = [[ver_1]]
                        ver_2_parsed: list[Any] = [[ver_2]]

                        # Compensate for bad version strings that start with '.'
                        if re.search('^\\.', ver_1):
                            ver_1 = re.sub('^\\.', '0.', ver_1)

                        if re.search('^.', ver_2):
                            ver_2 = re.sub('^\\.', '0.', ver_2)

                        if '.' in ver_1:
                            ver_1_parsed = [
                                re.findall('(\\d+|[A-za-z]+)', x) for x in ver_1.split('.')
                            ]

                        if '.' in ver_2:
                            ver_2_parsed = [
                                re.findall('(\\d+|[A-za-z]+)', x) for x in ver_2.split('.')
                            ]

                        # Leading zeroes handling: compensate for leading zeroes in subversions
                        ver_compare = (ver_1_parsed, ver_2_parsed)
                        min_ver_length = len(min(ver_compare, key=len))

                        # Leading zeroes handling: chop the versions to the shortest length to accurately compare
                        ver_1_parsed_min = ver_1_parsed[0:min_ver_length]
                        ver_2_parsed_min = ver_2_parsed[0:min_ver_length]

                        # Replace empty lists with zeroes
                        for i, ver in enumerate(ver_1_parsed_min):
                            if not ver:
                                ver_1_parsed_min[i] = ['0']

                        for i, ver in enumerate(ver_2_parsed_min):
                            if not ver:
                                ver_2_parsed_min[i] = ['0']

                        # Leading zeroes handling: add extra zeroes to versions without trailing zeroes
                        for i in range(min_ver_length):
                            if len(ver_1_parsed_min[i][0]) > len(ver_2_parsed_min[i][0]):
                                if ver_1_parsed_min[i][0].startswith('0'):
                                    ver_2_parsed[i][
                                        0
                                    ] = f'{ver_2_parsed_min[i][0]}{"0"*(len(ver_1_parsed_min[i][0]) - len(ver_2_parsed_min[i][0]))}'

                            elif len(ver_2_parsed_min[i][0]) > len(ver_1_parsed_min[i][0]):
                                if ver_2_parsed_min[i][0].startswith('0'):
                                    ver_1_parsed[i][
                                        0
                                    ] = f'{ver_1_parsed_min[i][0]}{"0"*(len(ver_2_parsed_min[i][0]) - len(ver_1_parsed_min[i][0]))}'

                        def normalize_version(version: list[Any]) -> list[Any]:
                            """
                            Formats versions so they can be compared.

                            Args:
                                version (list[Any]): A version of a
                                title that's already been parsed.

                            Returns:
                                list[Any]: A normalized version of the
                                input.
                            """
                            ver_normalized: list[Any] = []

                            for split_version in version:
                                sub_version_group: list[Any] = []

                                for subversion in split_version:
                                    try:
                                        sub_version_group.append(int(subversion))
                                    except Exception:
                                        sub_version_group.append(subversion)

                                ver_normalized.append(sub_version_group)

                            return ver_normalized

                        ver_1_normalized: list[Any] = normalize_version(ver_1_parsed)
                        ver_2_normalized: list[Any] = normalize_version(ver_2_parsed)

                        version_compare_zip: list[Any] = list(
                            itertools.zip_longest(ver_1_normalized, ver_2_normalized, fillvalue=[0])
                        )

                        # Convert tuples to list
                        for version_pairs in version_compare_zip:
                            version_compare_normalize.append(list(version_pairs))

                        # Equalize the list lengths
                        for version_pairs_normalized in version_compare_normalize:
                            shorter: int
                            longer: int

                            if len(version_pairs_normalized[0]) != len(version_pairs_normalized[1]):
                                if len(version_pairs_normalized[0]) < len(
                                    version_pairs_normalized[1]
                                ):
                                    shorter = 0
                                    longer = 1

                                elif len(version_pairs_normalized[1]) < len(
                                    version_pairs_normalized[0]
                                ):
                                    shorter = 1
                                    longer = 0

                                for i, version_pairs_item in enumerate(
                                    version_pairs_normalized[longer]
                                ):
                                    if i != 0:
                                        if isinstance(version_pairs_item, str):
                                            version_pairs_normalized[shorter].append('0')
                                        else:
                                            version_pairs_normalized[shorter].append(0)
                    else:
                        # Process versions that don't contain '.'
                        try:
                            versions: list[Any] = []
                            versions.append(int(ver_1))
                            versions.append(int(ver_2))
                        except Exception:
                            versions = []
                            versions.append(ver_1)
                            versions.append(ver_2)

                        version_compare_normalize.append(versions)

                    return version_compare_normalize

                # Get the version from the title
                regex_search_str_1 = pattern2string(pattern, title_1_name_normalized)
                regex_search_str_2 = pattern2string(pattern, title_2_name_normalized)

                title_1_ver: str = regex_search_str_1.replace('(', '').replace(')', '')
                title_2_ver: str = regex_search_str_2.replace('(', '').replace(')', '')

                # Preprocess special version types
                if pattern == config.regex.fds_version:
                    title_1_ver = max(re.findall('\\d+', title_1_ver))
                    title_2_ver = max(re.findall('\\d+', title_2_ver))
                elif pattern == config.regex.nec_mastering_code:
                    title_1_ver = max(title_1_ver.split(', '))
                    title_2_ver = max(title_2_ver.split(', '))
                elif pattern == config.regex.sega_panasonic_ring_code:
                    if re.search('\\d+', title_1_ver) and re.search('\\d+', title_2_ver):
                        title_1_ver = str(max([int(i) for i in re.findall('\\d+', title_1_ver)]))
                        title_2_ver = str(max([int(i) for i in re.findall('\\d+', title_2_ver)]))
                    elif re.search('\\d+', title_1_ver) and not re.search('\\d+', title_2_ver):
                        title_1_ver = '1'
                        title_2_ver = '0'
                    elif re.search('\\d+', title_2_ver) and not re.search('\\d+', title_1_ver):
                        title_1_ver = '0'
                        title_2_ver = '1'

                # Preprocess double versions that turn up in 3DS (Digital), Commodore Amiga, PS3 (Digital) (Content),
                # IBM - PC and Compatibles (Flux), and IBM - PC and Compatibles (Digital) (GOG)
                title_1_ver = (
                    title_1_ver.replace('PS3 ', '').replace('-to-', ', ').replace(' - AGI', ',').replace('rev', '')
                )
                title_2_ver = (
                    title_2_ver.replace('PS3 ', '').replace('-to-', ', ').replace('- AGI', ',').replace('rev', '')
                )

                match_1_length: int = len(re.findall('v[\\d+\\.\\-]+', title_1_ver))
                match_2_length: int = len(re.findall('v[\\d+\\.\\-]+', title_2_ver))

                if re.search('v[\\d+\\.]+(?:, )\\d{4}-\\d{2}-\\d{2}', title_1_ver):
                    match_1_length = len(
                        re.findall('(v[\\d+\\.]+|\\d{4}-\\d{2}-\\d{2})', title_1_ver)
                    )

                if re.search('v[\\d+\\.]+(?:, )\\d{4}-\\d{2}-\\d{2}', title_2_ver):
                    match_2_length = len(
                        re.findall('(v[\\d+\\.]+|\\d{4}-\\d{2}-\\d{2})', title_2_ver)
                    )

                if match_1_length == 2 and match_2_length == 2:
                    # Split the versions
                    title_1_ver_a = re.findall('[\\d+\\.\\-]+', title_1_ver)[0]
                    title_1_ver_b = str(re.findall('[\\d+\\.\\-]+', title_1_ver)[1]).replace(
                        '-', '.'
                    )
                    title_2_ver_a = re.findall('[\\d+\\.\\-]+', title_2_ver)[0]
                    title_2_ver_b = str(re.findall('[\\d+\\.\\-]+', title_2_ver)[1]).replace(
                        '-', '.'
                    )

                    # Normalize the primary version lengths
                    title_1_ver_a_parsed = [
                        re.findall('[\\d+\\.\\-]+', x) for x in title_1_ver_a.split('.')
                    ]
                    title_2_ver_a_parsed = [
                        re.findall('[\\d+\\.\\-]+', x) for x in title_2_ver_a.split('.')
                    ]

                    primary_version_zip: list[Any] = list(
                        itertools.zip_longest(
                            title_1_ver_a_parsed, title_2_ver_a_parsed, fillvalue=['0']
                        )
                    )

                    try:
                        title_1_ver = '.'.join([i[0][0] for i in primary_version_zip])
                        title_2_ver = '.'.join([i[1][0] for i in primary_version_zip])
                    except Exception:
                        # If an unexpected versioning system turns up that causes a tuple
                        # item in primary_version_zip to be empty, fail silently
                        pass

                    # Add the secondary version to the primary
                    title_1_ver = f'{title_1_ver}.{title_1_ver_b}'
                    title_2_ver = f'{title_2_ver}.{title_2_ver_b}'

                # Remove known prefixes and strip whitespace
                title_1_ver = re.sub(
                    'version|^(v|Rev|Version|Beta|Alpha|Proto|Build)|\\s',
                    '',
                    title_1_ver,
                    flags=re.I,
                )
                title_2_ver = re.sub(
                    'version|^(v|Rev|Version|Beta|Alpha|Proto|Build)|\\s',
                    '',
                    title_2_ver,
                    flags=re.I,
                )

                # Compensate for Doom version wackiness
                if '666' in title_1_ver and 'Doom' in title_1.full_name:
                    title_1_ver.replace('666', '6.6.6')

                if '666' in title_2_ver and 'Doom' in title_2.full_name:
                    title_1_ver.replace('666', '6.6.6')

                # Normalize the versions
                version_compare_normalize: list[Any] = process_versions(title_1_ver, title_2_ver)

                # Compare the normalized versions
                for subversion in version_compare_normalize:
                    try:
                        if subversion[0] < subversion[1]:
                            if title_1 in title_set:
                                if config.user_input.oldest:
                                    keep_title_name = title_1.full_name
                                    remove_title_name = title_2.full_name

                                    remove_titles.add(title_2)
                                else:
                                    keep_title_name = title_2.full_name
                                    remove_title_name = title_1.full_name

                                    remove_titles.add(title_1)

                                if report_on_match:
                                    TraceTools.trace_title(
                                        'REF0041',
                                        [
                                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {keep_title_name}',
                                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {remove_title_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )
                            break

                        if subversion[1] < subversion[0]:
                            if title_2 in title_set:
                                if config.user_input.oldest:
                                    keep_title_name = title_2.full_name
                                    remove_title_name = title_1.full_name

                                    remove_titles.add(title_1)
                                else:
                                    keep_title_name = title_1.full_name
                                    remove_title_name = title_2.full_name

                                    remove_titles.add(title_2)

                                if report_on_match:
                                    TraceTools.trace_title(
                                        'REF0040',
                                        [
                                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {keep_title_name}',
                                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {remove_title_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )
                            break
                    except Exception:
                        # If there's a combination string and int, convert the int as a fallback.
                        # This might result in the wrong version being chosen.
                        if str(subversion[0]) < str(subversion[1]):
                            if title_1 in title_set:
                                if config.user_input.oldest:
                                    keep_title_name = title_1.full_name
                                    remove_title_name = title_2.full_name

                                    remove_titles.add(title_2)
                                else:
                                    keep_title_name = title_2.full_name
                                    remove_title_name = title_1.full_name

                                    remove_titles.add(title_1)

                                if report_on_match:
                                    TraceTools.trace_title(
                                        'REF0041',
                                        [
                                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {keep_title_name}',
                                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {remove_title_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )
                            break

                        if str(subversion[1]) < str(subversion[0]):
                            if title_2 in title_set:
                                if config.user_input.oldest:
                                    keep_title_name = title_2.full_name
                                    remove_title_name = title_1.full_name

                                    remove_titles.add(title_1)
                                else:
                                    keep_title_name = title_1.full_name
                                    remove_title_name = title_2.full_name

                                    remove_titles.add(title_2)

                                if report_on_match:
                                    TraceTools.trace_title(
                                        'REF0040',
                                        [
                                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {keep_title_name}',
                                            f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {remove_title_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )
                            break

    for title in remove_titles:
        if title in title_set:
            title_set.remove(title)

    return title_set
