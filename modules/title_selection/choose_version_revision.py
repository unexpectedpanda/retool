from __future__ import annotations

import itertools
import re
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.titletools import TraceTools


def choose_version_revision(
    title_set: set[DatNode], version_string: str, config: Config, report_on_match: bool
) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes to see which one has the highest
    version/revision tag.

    Args:
        title_set (set[DatNode]): A set of titles as DatNode instances.

        version_string (str): The key in the titles' `normalized_version` property to use
            as the basis for comparison.

        config (Config): The Retool config object.

        report_on_match (bool): Whether Retool needs to report any titles being traced.

    Returns:
        set[DatNode]: A set of DatNodes filtered by highest version.
    """
    remove_titles: set[DatNode] = set()

    for title_1, title_2 in itertools.combinations(title_set, 2):
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
            if (
                version_string in title_1.normalized_version
                and version_string not in title_2.normalized_version
            ):
                if 'preproduction' in title_1.normalized_version:
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
                        [keep_title_name, remove_title_name],
                        keep_remove=True,
                    )
            elif (
                version_string in title_2.normalized_version
                and version_string not in title_1.normalized_version
            ):
                if 'preproduction' in title_2.normalized_version:
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
                        [keep_title_name, remove_title_name],
                        keep_remove=True,
                    )
            # Perform version comparison between two titles that both have version strings
            elif (
                version_string in title_1.normalized_version
                and version_string in title_2.normalized_version
            ):

                def process_versions(ver_1: str, ver_2: str) -> list[str]:
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
                                version (list[Any]): A version of a title that's already
                                    been parsed.

                            Returns:
                                list[Any]: A normalized version of the input.
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

                # Normalize the versions
                if (
                    version_string in title_1.normalized_version
                    and version_string in title_2.normalized_version
                ):
                    version_compare_normalize: list[str] = process_versions(title_1.normalized_version[version_string], title_2.normalized_version[version_string])  # type: ignore

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
                                            [keep_title_name, remove_title_name],
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
                                            [keep_title_name, remove_title_name],
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
                                            [keep_title_name, remove_title_name],
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
                                            [keep_title_name, remove_title_name],
                                            keep_remove=True,
                                        )
                                break

    for title in remove_titles:
        if title in title_set:
            title_set.remove(title)

    return title_set
