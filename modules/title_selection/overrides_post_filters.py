from __future__ import annotations

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config import Config
    from modules.dats import DatNode
    from modules.titletools import Removes

from modules.titletools import TraceTools
from modules.utils import eprint


def user_override_post_filter_match(
    title: DatNode,
    filter_list: list[str],
    is_post_filter: bool = False,
    cloneof_check: bool = False,
) -> bool:
    """
    Establishes what kind of match a user is trying to make with their
    overrides or post filters, whether it be relational (`<>`), regex (`/`),
    full match (`|`) or partial. Matches are case insensitive.

    Args:
        title (DatNode): The title to look for a match in.

        filter_list (list[str]): A list of overrides or post filters that define search
            criteria for a match.

        is_post_filter (bool): `False` for overrides, `True` for post filters. Defaults to
            `False`.

        cloneof_check(bool): Set to `True` when dealing with titles that have a
            `cloneof` property. Defaults to `False`.

    Returns:
        bool: Whether or not a match has been made.
    """
    match: bool = False

    for string in filter_list:
        match_string: str = string

        if cloneof_check:
            if title.cloneof:
                if match_string.startswith('/'):
                    match = bool(re.search(match_string[1:], title.cloneof, flags=re.I))
                elif match_string.startswith('|'):
                    match = match_string[1:].lower() == title.cloneof.lower()
                else:
                    match = match_string.lower() in title.cloneof.lower()

            if match:
                break
        else:
            if not is_post_filter:
                if match_string.startswith('<') and match_string.endswith('>'):
                    match_string = match_string[1:-1]

                    title.exclude_include_related = True

            if match_string.startswith('/'):
                match = bool(re.search(match_string[1:], title.full_name, flags=re.I))
            elif match_string.startswith('|'):
                match = match_string[1:].lower() == title.full_name.lower()
            else:
                match = match_string.lower() in title.full_name.lower()

            if match:
                break

    return match


def post_filters(
    processed_titles: dict[str, set[DatNode]], config: Config, removes: Removes
) -> dict[str, set[DatNode]]:
    """
    Works through a dict of DatNodes and removes nodes that match user criteria.

    Args:
        processed_titles (dict[str, set[DatNode]]): A work in progress dictionary
        of DatNodes, originally populated from the input DAT and actively being worked
        on by Retool.

        config (Config): The Retool config object.

        removes (Removes): The Retool removes object, which contains and categorizes
        all the titles that have been removed from consideration. Is used for stats
        and other output files generated by Retool.

    Returns:
        dict[str, set[DatNode]]: A dictionary of DatNodes with titles excluded
        based on user criteria.
    """
    if config.system_filter:
        if {'override': 'true'} in config.system_filter:
            eprint('• Applying post filters... ')
    if config.global_filter:
        if {'override': 'false'} in config.system_filter:
            eprint('• Applying post filters... ')

    # Set up title tracking
    report_on_match: bool = False

    for titles in processed_titles.values():
        report_on_match = TraceTools.trace_enable(set(titles), config.user_input.trace)

        if report_on_match:
            break

    if report_on_match and config.user_input.trace:
        eprint('Stage: Post filters', level='heading')

    dupe_check: set[DatNode] = set()
    filter_titles: set[tuple[str, DatNode]] = set()
    global_count: int = 0
    system_count: int = 0

    for group_name, titles in processed_titles.items():
        if config.user_input.trace:
            report_on_match = TraceTools.trace_enable(set(titles), config.user_input.trace)

        for title in titles:
            if title not in dupe_check:
                if config.system_filter:
                    if [x for x in config.system_filter if x != {'override': 'true'}]:
                        if {'override': 'true'} in config.system_filter:
                            if title.cloneof:
                                if not user_override_post_filter_match(
                                    title,
                                    [
                                        str(x)
                                        for x in config.system_filter
                                        if x != {'override': 'true'} and x != {'override': 'false'}
                                    ],
                                    is_post_filter=True,
                                    cloneof_check=True,
                                ):
                                    filter_titles.add((group_name, title))

                                    # Compensate for supersets being in multiple groups for the stats and log
                                    if not any(d.full_name == title.full_name for d in dupe_check):
                                        system_count = config.stats.system_filter_count
                                        system_count += 1
                                        setattr(config.stats, 'system_filter_count', system_count)

                                        title.exclude_reason = 'System post filter exclude'

                                        dupe_check.add(title)
                                        removes.system_filter_removes.add(title)
                            elif not user_override_post_filter_match(
                                title,
                                [
                                    str(x)
                                    for x in config.system_filter
                                    if x != {'override': 'true'} and x != {'override': 'false'}
                                ],
                                is_post_filter=True,
                            ):
                                filter_titles.add((group_name, title))

                                # Compensate for supersets being in multiple groups for the stats and log
                                if not any(d.full_name == title.full_name for d in dupe_check):
                                    system_count = config.stats.system_filter_count
                                    system_count += 1
                                    setattr(config.stats, 'system_filter_count', system_count)

                                    title.exclude_reason = 'System post filter exclude'

                                    dupe_check.add(title)
                                    removes.system_filter_removes.add(title)
                            else:
                                if report_on_match and config.user_input.trace:
                                    TraceTools.trace_title(
                                        'REF0099', [], {title}, keep_remove=False
                                    )

                if config.global_filter:
                    if not config.system_filter or {'override': 'false'} in config.system_filter:
                        if title.cloneof:
                            if not user_override_post_filter_match(
                                title,
                                config.global_filter,
                                is_post_filter=True,
                                cloneof_check=True,
                            ):
                                filter_titles.add((group_name, title))

                                # Compensate for supersets being in multiple groups for the stats and log
                                if not any(d.full_name == title.full_name for d in dupe_check):
                                    global_count = config.stats.global_filter_count
                                    global_count += 1
                                    setattr(config.stats, 'global_filter_count', global_count)

                                    title.exclude_reason = 'Global post filter exclude'

                                    dupe_check.add(title)
                                    removes.global_filter_removes.add(title)
                        elif not user_override_post_filter_match(
                            title, config.global_filter, is_post_filter=True
                        ):
                            filter_titles.add((group_name, title))

                            # Compensate for supersets being in multiple groups for the stats and log
                            if not any(d.full_name == title.full_name for d in dupe_check):
                                global_count = config.stats.global_filter_count
                                global_count += 1
                                setattr(config.stats, 'global_filter_count', global_count)

                                title.exclude_reason = 'Global post filter exclude'

                                dupe_check.add(title)
                                removes.global_filter_removes.add(title)
                        else:
                            if report_on_match and config.user_input.trace:
                                TraceTools.trace_title('REF0100', [], {title}, keep_remove=False)

    # Remove the titles
    for filter_title in filter_titles:
        processed_titles[filter_title[0]].remove(filter_title[1])

    # Catch compilations
    compilation_removes: set[DatNode] = set()

    if (
        'retool_compilations_winners' in processed_titles
        and 'retool_compilations_discards' in processed_titles
    ):
        for compilation_title in processed_titles['retool_compilations_winners']:
            for filter_title in filter_titles:
                if filter_title[1].full_name == compilation_title.full_name:
                    compilation_removes.add(compilation_title)

        for compilation_title in processed_titles['retool_compilations_discards']:
            for filter_title in filter_titles:
                if filter_title[1].full_name == compilation_title.full_name:
                    compilation_removes.add(compilation_title)

        for compilation_remove in compilation_removes:
            if compilation_remove in processed_titles['retool_compilations_winners']:
                processed_titles['retool_compilations_winners'].remove(compilation_remove)
            if compilation_remove in processed_titles['retool_compilations_discards']:
                processed_titles['retool_compilations_discards'].remove(compilation_remove)

    if config.system_filter:
        if {'override': 'true'} in config.system_filter:
            eprint('• Applying post filters... done.', overwrite=True)
    if config.global_filter:
        if {'override': 'false'} in config.system_filter:
            eprint('• Applying post filters... done.', overwrite=True)

    return processed_titles