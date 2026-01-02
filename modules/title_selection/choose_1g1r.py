from __future__ import annotations

import itertools
import re
from re import Pattern
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.title_selection.choose_date import choose_date
from modules.title_selection.choose_good import choose_good
from modules.title_selection.choose_highest_string import choose_highest_string
from modules.title_selection.choose_language import choose_language, choose_language_top
from modules.title_selection.choose_made_in import choose_made_in
from modules.title_selection.choose_priority import choose_priority
from modules.title_selection.choose_region import choose_region
from modules.title_selection.choose_retroachievements import choose_retroachievements
from modules.title_selection.choose_string import choose_string
from modules.title_selection.choose_superset import choose_superset
from modules.title_selection.choose_version_revision import choose_version_revision
from modules.title_selection.choose_video_standard import choose_video_standard
from modules.titletools import TitleTools, TraceTools
from modules.utils import Font, eprint, pattern2string


def choose_1g1r(
    config: Config,
    is_numbered: bool,
    potential_parents: dict[str, set[DatNode]],
    is_superset_titles: bool,
    is_compilations: bool,
    title_set: set[DatNode],
) -> dict[str, set[DatNode]]:
    """
    Determines a 1G1R title, given a dictionary of DatNode objects.

    Args:
        config (Config): The Retool config object.

        is_numbered (bool): Whether the DAT file prefixes its title names with numbers.

        potential_parents (dict[str, set[DatNode]]): A dictionary of DatNodes that
            contains non-finalized parents. Only needed when processing supersets, as
            supersets need extra processing to make the parents deterministic.

        is_superset_titles (bool): Set to `True` if processing supersets.

        is_compilations (bool): Set to `True` if processing compilations.

        title_set (set[DatNode]): A list of DatNodes to choose a parent from.

    Returns:
        dict (dict[str, set[DatNode]]): A dictionary of DatNodes with parents selected.
    """
    # Check if a system config is in play
    language_order: list[str] = []

    if config.languages_filter:
        language_order = config.language_order_user

        if config.system_language_order_user:
            if {'override': 'true'} in config.system_language_order_user:
                language_order = [
                    str(x) for x in config.system_language_order_user if 'override' not in x
                ]
    else:
        language_order = config.region_order_languages_user

    region_order: list[str] = config.region_order_user

    if config.system_region_order_user:
        if {'override': 'true'} in config.system_region_order_user:
            region_order = [str(x) for x in config.system_region_order_user if 'override' not in x]

    # Do some manipulation to convert from set to the expected dictionary
    group_name = next(iter(title_set)).group_name

    original_titles: dict[str, set[DatNode]] = {group_name: title_set}
    processed_titles: dict[str, set[DatNode]] = {group_name: title_set}

    cross_region_parent_titles: set[DatNode] = set()

    # Set up title tracking
    report_on_match: bool = False

    if config.user_input.trace:
        report_on_match = TraceTools.trace_enable(set(title_set), config.user_input.trace)

    if report_on_match:
        if is_superset_titles:
            eprint(f'Stage: Superset parent selection\nGroup: {group_name}', level='heading')
        elif is_compilations:
            eprint(f'Stage: Compilation parent selection\nGroup: {group_name}', level='heading')
        else:
            eprint(f'Stage: Parent selection\nGroup: {group_name}', level='heading')

    highest_language_priority: int = 0
    top_language: str = ''

    # Find the highest priority languages in the set, taking short names into account
    short_names: set[str] = {x.short_name for x in title_set}
    short_name_groups: list[tuple[str, list[DatNode]]] = []
    short_name_titles: dict[str, list[DatNode]] = {}
    short_name_top_languages: set[tuple[str, int, str]] = set()

    # Filter out bad dumps, pirate, and preproduction titles
    for short_name in short_names:
        for title in title_set:
            if title.short_name == short_name and not re.search(config.regex.bad, title.full_name):
                regex_match: bool = False

                for regex_pattern in config.regex.preproduction:
                    if re.search(regex_pattern, title.full_name):
                        regex_match = True

                if re.search(config.regex.pirate, title.full_name):
                    regex_match = True

                if not regex_match:
                    if short_name not in short_name_titles:
                        short_name_titles[short_name] = []
                    if title not in short_name_titles[short_name]:
                        short_name_titles[short_name].append(title)

        # Add preproduction titles back in if they are the only ones in the set
        if not short_name_titles:
            for title in title_set:
                if title.short_name == short_name:
                    for regex_pattern in config.regex.preproduction:
                        if re.search(regex_pattern, title.full_name):
                            if short_name not in short_name_titles:
                                short_name_titles[short_name] = []
                            if title not in short_name_titles[short_name]:
                                short_name_titles[short_name].append(title)

        # Add pirate titles back in if they are the only ones in the set
        if not short_name_titles:
            for title in title_set:
                if title.short_name == short_name:
                    if re.search(config.regex.pirate, title.full_name):
                        if short_name not in short_name_titles:
                            short_name_titles[short_name] = []
                        if title not in short_name_titles[short_name]:
                            short_name_titles[short_name].append(title)

        # Add bad dumps back in if they are the only ones in the set
        if not short_name_titles:
            for title in title_set:
                if title.short_name == short_name and re.search(config.regex.bad, title.full_name):
                    if short_name not in short_name_titles:
                        short_name_titles[short_name] = []
                    if title not in short_name_titles[short_name]:
                        short_name_titles[short_name].append(title)

        for key, values in short_name_titles.items():
            short_name_groups.append((key, values))

    for short_name_group in short_name_groups:
        highest_language_priority = sorted(short_name_group[1], key=lambda i: i.language_priority)[
            0
        ].language_priority

        for title in [
            x
            for x in sorted(short_name_group[1], key=lambda i: i.region_priority)
            if x.language_priority == highest_language_priority
        ]:
            for language in language_order:
                if re.search(language, ''.join(title.languages)):
                    top_language = language
                    break

            if top_language:
                break

        short_name_top_languages.add((short_name_group[0], highest_language_priority, top_language))

    for region in region_order:
        parent_titles: set[DatNode] = {x for x in title_set if region in x.primary_region}

        # Split group into short names to avoid needless comparison work
        titles_by_short_name: dict[str, set[DatNode]] = {}

        for title in parent_titles:
            if title.short_name not in titles_by_short_name:
                titles_by_short_name[title.short_name] = set()

            titles_by_short_name[title.short_name].add(title)

        for short_name, titles in titles_by_short_name.items():
            if titles and len(titles) > 1:
                if report_on_match:
                    eprint(
                        f'Region: {region} | Group: {group_name} | Short name: {short_name}',
                        level='subheading',
                    )
                    TraceTools.trace_title('REF0001', [], titles, keep_remove=False)

                # 0) Select RetroAchievements
                if len(titles) > 1 and config.user_input.retroachievements:
                    titles = choose_retroachievements(titles, report_on_match)

                # 1) Clean up preproduction/bad/pirate/mixed version-revision titles
                if len(titles) > 1:
                    titles = choose_good(titles, config)

                if report_on_match:
                    TraceTools.trace_title('REF0003', [], titles, keep_remove=False)

                # 2) Cycle through language order until one title doesn't have the required language
                if len(titles) > 1:
                    titles = choose_language(titles, config, report_on_match)

                if report_on_match:
                    TraceTools.trace_title('REF0005', [], titles, keep_remove=False)

                # 3) Select supersets
                if len(titles) > 1:
                    titles = choose_superset(titles, config, report_on_match)

                if report_on_match:
                    TraceTools.trace_title('REF0076', [], titles, keep_remove=False)

                # 4) Reference clone list priorities
                if len(titles) > 1:
                    titles = choose_priority(titles, config, report_on_match)

                if report_on_match:
                    TraceTools.trace_title('REF0002', [], titles, keep_remove=False)

                # 5) Handle modern titles like Virtual Console, Mini Console, and other
                # collections ripped from other platforms
                if len(titles) > 1:
                    for edition in config.tags_modern_editions:
                        match_string: Any = ''

                        if edition[1] == 'regex':
                            match_string = re.compile(edition[0])
                        elif edition[1] == 'string':
                            match_string = edition[0]

                        if not config.user_input.modern:
                            titles = choose_string(
                                match_string,
                                titles,
                                report_on_match,
                                choose_title_with_string=False,
                            )
                        elif config.user_input.modern:
                            titles = choose_string(
                                match_string,
                                titles,
                                report_on_match,
                                choose_title_with_string=True,
                            )

                if report_on_match:
                    TraceTools.trace_title('REF0004', [], titles, keep_remove=False)

                # 6) Prefer production versions over unlicensed/aftermarket
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.unlicensed,
                        titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.aftermarket,
                        titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )

                if report_on_match:
                    TraceTools.trace_title('REF0060', [], titles, keep_remove=False)

                # 7) Select special editions
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.sega32x,
                        titles,
                        report_on_match,
                        choose_title_with_string=True,
                    )
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.fmtowns_marty,
                        titles,
                        report_on_match,
                        choose_title_with_string=True,
                    )

                if report_on_match:
                    TraceTools.trace_title('REF0006', [], titles, keep_remove=False)

                # 8) Select budget editions
                if len(titles) > 1:
                    for edition in config.tags_budget_editions:
                        match_string = ''

                        if edition[1] == 'regex':
                            match_string = re.compile(edition[0])
                        elif edition[1] == 'string':
                            match_string = edition[0]

                        if not config.user_input.oldest:
                            titles = choose_string(
                                match_string,
                                titles,
                                report_on_match,
                                choose_title_with_string=True,
                            )
                        else:
                            titles = choose_string(
                                match_string,
                                titles,
                                report_on_match,
                                choose_title_with_string=False,
                            )

                    if report_on_match:
                        TraceTools.trace_title('REF0113', [], titles, keep_remove=False)

                # 9) Check for versions and revisions, and select the highest of each
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'version', config, report_on_match)
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'revision', config, report_on_match)
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'firmware', config, report_on_match)
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'beta', config, report_on_match)
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'alpha', config, report_on_match)
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'proto', config, report_on_match)
                if len(titles) > 1:
                    titles = choose_version_revision(
                        titles,
                        'sega',
                        config,
                        report_on_match,
                    )
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'playstation', config, report_on_match)
                if len(titles) > 1:
                    titles = choose_version_revision(
                        titles,
                        'nec',
                        config,
                        report_on_match,
                    )
                if len(titles) > 1:
                    titles = choose_version_revision(
                        titles,
                        'benesse',
                        config,
                        report_on_match,
                    )

                if report_on_match:
                    TraceTools.trace_title('REF0007', [], titles, keep_remove=False)

                # 10 Choose video standard
                video_order: list[str] = config.video_order_user

                if config.system_video_order_user:
                    if {'override': 'true'} in config.system_video_order_user:
                        video_order = [
                            str(x) for x in config.system_video_order_user if 'override' not in x
                        ]

                if len(titles) > 1:
                    for video_standard in video_order:
                        titles = choose_video_standard(
                            video_standard.lower(), titles, config, report_on_match
                        )

                    if report_on_match:
                        TraceTools.trace_title('REF0096', [], titles, keep_remove=False)

                # 11) Second language pass -- required to allow versions/revisions to be correctly selected
                if len(titles) > 1:
                    titles = choose_language(titles, config, report_on_match, first_time=False)

                    if report_on_match:
                        TraceTools.trace_title('REF0043', [], titles, keep_remove=False)

                # 12) Preference titles with more regions that are higher up the region priority
                if len(titles) > 1:
                    titles = choose_region(
                        titles,
                        region_order,
                        world_is_usa_europe_japan=False,
                        report_on_match=report_on_match,
                    )

                    if report_on_match:
                        TraceTools.trace_title('REF0008', [], titles, keep_remove=False)

                # 13) Choose original versions over alternatives
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.alt,
                        titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.oem,
                        titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(titles) > 1:
                    parent_titles = choose_string(
                        config.regex.not_for_resale,
                        titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.covermount,
                        titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.rerelease,
                        titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(titles) > 1:
                    titles = choose_string(
                        config.regex.edc,
                        titles,
                        report_on_match,
                        choose_title_with_string=True,
                    )

                if report_on_match:
                    TraceTools.trace_title('REF0010', [], titles, keep_remove=False)

                # 14) Handle promotion and demotion editions
                if len(titles) > 1:
                    for edition in config.tags_promote_editions:
                        match_string = ''

                        if edition[1] == 'regex':
                            match_string = re.compile(edition[0])
                        elif edition[1] == 'string':
                            match_string = edition[0]

                        titles = choose_string(
                            match_string,
                            titles,
                            report_on_match,
                            choose_title_with_string=True,
                        )

                    for edition in config.tags_demote_editions:
                        match_string = ''

                        if edition[1] == 'regex':
                            match_string = re.compile(edition[0])
                        elif edition[1] == 'string':
                            match_string = edition[0]

                        titles = choose_string(
                            match_string,
                            titles,
                            report_on_match,
                            choose_title_with_string=False,
                        )

                    if report_on_match:
                        TraceTools.trace_title('REF0011', [], titles, keep_remove=False)

                # 15) Choose dates
                if len(titles) > 1:
                    titles = choose_date(titles, config, report_on_match)

                    if report_on_match:
                        TraceTools.trace_title('REF0009', [], titles, keep_remove=False)

                # 16) Choose builds
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'build', config, report_on_match)

                # 17) Handle "Made in" titles
                if len(titles) > 1:
                    titles = choose_made_in(config.regex.madein, titles, report_on_match)

                    if report_on_match:
                        TraceTools.trace_title('REF0012', [], titles, keep_remove=False)

                # 18) Another version check just in case multiple Alts are the only titles left
                if len(titles) > 1:
                    titles = choose_version_revision(titles, 'alt', config, report_on_match)

                    if report_on_match:
                        TraceTools.trace_title('REF0061', [], titles, keep_remove=False)

                # 19) As a fail-safe, do a string comparison. This compares character by character,and when
                # a title has a higher comparative character than another title, it wins.
                if not is_compilations:
                    if len(titles) > 1:
                        titles = choose_highest_string(titles, report_on_match)

                if report_on_match:
                    TraceTools.trace_title('REF0059', [], titles, keep_remove=False)

            elif len(titles) == 1:
                if report_on_match:
                    eprint(
                        f'Region: {region} | Group: {group_name} | Short name: {list(titles)[0].short_name}',
                        level='subheading',
                        wrap=False,
                    )
                    TraceTools.trace_title('REF0074', [], titles, keep_remove=False)

            # Add remaining titles from multiple regions to a single set
            cross_region_parent_titles = cross_region_parent_titles | titles

    if report_on_match:
        eprint(f'Region: All [{group_name}]', level='subheading')
        TraceTools.trace_title('REF0013', [], cross_region_parent_titles, keep_remove=False)

    if len(cross_region_parent_titles) > 1:
        # Select titles that support RetroAchievements
        if config.user_input.retroachievements:
            cross_region_parent_titles = choose_retroachievements(
                cross_region_parent_titles.copy(), report_on_match
            )

        # Remove titles that don't support the top language in the set
        if not config.user_input.region_bias:
            cross_region_parent_titles = choose_language_top(
                cross_region_parent_titles,
                short_name_top_languages,
                report_on_match,
            )

        # Prefer good dump/production/retail titles
        def production_retail(
            titles: set[DatNode], patterns: tuple[Pattern[str], ...], report_on_match: bool
        ) -> set[DatNode]:
            """
            Removes titles if they match a certain regex pattern, but only if doing so
            wouldn't remove all titles in the set.

            Args:
                titles (set[DatNode]): The titles to iterate over.

                patterns (tuple[Pattern[str], ...]): The pattern to match against the
                    title full names.

                report_on_match (bool): Whether Retool needs to report any titles being
                    traced.
            """
            cross_region_temp = titles.copy()

            for title_1, title_2 in itertools.combinations(cross_region_temp, 2):
                if TitleTools.check_title_equivalence(title_1, title_2):
                    pattern_1_found: bool = False
                    pattern_2_found: bool = False

                    patterns_found: list[Pattern[str]] = []

                    for pattern in patterns:
                        if pattern2string(pattern, title_1.full_name) and pattern2string(
                            pattern, title_2.full_name
                        ):
                            break
                        if pattern2string(pattern, title_1.full_name) and not pattern2string(
                            pattern, title_2.full_name
                        ):
                            pattern_1_found = True
                            patterns_found.append(pattern)
                        if pattern2string(pattern, title_2.full_name) and not pattern2string(
                            pattern, title_1.full_name
                        ):
                            pattern_2_found = True
                            patterns_found.append(pattern)

                    if patterns_found:
                        regex_string: str = (
                            str(patterns_found[0])
                            .replace('re.compile(', '')
                            .replace(', re.IGNORECASE)', '')
                        )
                        regex_string = re.sub('\'\\)$', '\'', regex_string)

                        if pattern_1_found and not pattern_2_found:
                            if title_1 in titles:
                                if report_on_match:
                                    TraceTools.trace_title(
                                        'REF0117',
                                        [
                                            f'{Font.subheading_bold}{regex_string}{Font.end} {title_2.full_name}',
                                            f'{Font.subheading_bold}{regex_string}{Font.disabled} {title_1.full_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )
                                titles.remove(title_1)

                        if pattern_2_found and not pattern_1_found:
                            if title_2 in titles:
                                if report_on_match:
                                    TraceTools.trace_title(
                                        'REF0118',
                                        [
                                            f'{Font.subheading_bold}{regex_string}{Font.end} {title_1.full_name}',
                                            f'{Font.subheading_bold}{regex_string}{Font.disabled} {title_2.full_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )
                                titles.remove(title_2)

            return titles

        cross_region_parent_titles = production_retail(
            cross_region_parent_titles, config.regex.preproduction, report_on_match
        )
        cross_region_parent_titles = production_retail(
            cross_region_parent_titles, (config.regex.bad,), report_on_match
        )
        cross_region_parent_titles = production_retail(
            cross_region_parent_titles, (config.regex.pirate,), report_on_match
        )

        if not config.user_input.modern:
            # Convert modern edition tags to full regex
            modern_edition_regex_tags: list[Pattern[str]] = []

            for tag in config.tags_modern_editions:
                if tag[1] == 'string':
                    modern_edition_regex_tags.append(
                        re.compile(
                            str(tag[0])
                            .replace("(", "\\(")
                            .replace(")", "\\)")
                            .replace("[", "\\[")
                            .replace("]", "\\]")
                        )
                    )
                elif tag[1] == 'regex':
                    modern_edition_regex_tags.append(re.compile(tag[0]))

            cross_region_parent_titles = production_retail(
                cross_region_parent_titles.copy(),
                tuple(modern_edition_regex_tags),
                report_on_match,
            )

        if config.user_input.demote_unl:
            cross_region_parent_titles = production_retail(
                cross_region_parent_titles.copy(),
                tuple(config.regex.unl_group),
                report_on_match,
            )

        if report_on_match:
            TraceTools.trace_title('REF0119', [], cross_region_parent_titles, keep_remove=False)

        # Remove titles with the same name in different regions
        cross_region_temp = cross_region_parent_titles.copy()

        for title_1, title_2 in itertools.combinations(cross_region_temp, 2):
            if TitleTools.check_title_equivalence(title_1, title_2, cross_region_parent_titles):
                if not config.user_input.region_bias:
                    # Leave supersets alone if the user doesn't specify region priority
                    if not title_1.is_superset and not title_2.is_superset:
                        if title_1.region_priority < title_2.region_priority:
                            cross_region_parent_titles.remove(title_2)
                        elif title_2.region_priority < title_1.region_priority:
                            cross_region_parent_titles.remove(title_1)
                else:
                    # Supersets can be removed if the user does specify region priority,
                    # except for "World" supersets where USA, Europe, or Japan are involved
                    if title_1.region_priority < title_2.region_priority:
                        if not (
                            (
                                title_1.primary_region == 'USA'
                                or title_1.primary_region == 'Europe'
                                or title_1.primary_region == 'Japan'
                            )
                            and title_2.primary_region == 'World'
                        ):
                            cross_region_parent_titles.remove(title_2)
                    elif title_2.region_priority < title_1.region_priority:
                        if not (
                            (
                                title_2.primary_region == 'USA'
                                or title_2.primary_region == 'Europe'
                                or title_2.primary_region == 'Japan'
                            )
                            and title_1.primary_region == 'World'
                        ):
                            cross_region_parent_titles.remove(title_1)

        if report_on_match:
            TraceTools.trace_title('REF0014', [], cross_region_parent_titles, keep_remove=False)

        # Choose supersets over titles
        cross_region_temp = set()

        if len(cross_region_parent_titles) > 1:
            cross_region_temp = cross_region_parent_titles.copy()

            for title_1, title_2 in itertools.combinations(cross_region_temp, 2):
                if TitleTools.check_title_equivalence(title_1, title_2, cross_region_parent_titles):
                    if title_1.is_superset and not title_2.is_superset:
                        cross_region_parent_titles.remove(title_2)
                    elif title_2.is_superset and not title_1.is_superset:
                        cross_region_parent_titles.remove(title_1)

            if report_on_match:
                TraceTools.trace_title('REF0103', [], cross_region_parent_titles, keep_remove=False)

        # Check supersets early for clonelist priority
        if len(cross_region_parent_titles) > 1:
            cross_region_temp = cross_region_parent_titles.copy()

            for title_1, title_2 in itertools.combinations(cross_region_temp, 2):
                if title_1.is_superset and title_2.is_superset:
                    if title_1.clonelist_priority < title_2.clonelist_priority:

                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0106',
                                [title_1.full_name, title_2.full_name],
                                set(),
                                keep_remove=True,
                            )

                        if title_2 in cross_region_parent_titles:
                            cross_region_parent_titles.remove(title_2)

                    elif title_2.clonelist_priority < title_1.clonelist_priority:

                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0107',
                                [title_2.full_name, title_1.full_name],
                                set(),
                                keep_remove=True,
                            )

                        if title_1 in cross_region_parent_titles:
                            cross_region_parent_titles.remove(title_1)

        # Check if a system config is in play
        region_order = config.region_order_user

        if config.system_region_order_user:
            if {'override': 'true'} in config.system_region_order_user:
                region_order = [
                    str(x) for x in config.system_region_order_user if 'override' not in x
                ]

        # Check if there's a shared region between titles. If so, check which title has more of the user's languages
        if len(cross_region_parent_titles) > 1:
            remove_titles: set[str] = set()
            language_winner: set[DatNode] = set()

            for region in region_order:
                for title_1, title_2 in itertools.combinations(
                    [x for x in cross_region_parent_titles if region in x.regions], 2
                ):
                    if TitleTools.check_title_equivalence(title_1, title_2):
                        language_winner = choose_language(
                            {title_1, title_2}, config, report_on_match
                        )

                        if len(language_winner) == 1:
                            if title_1.full_name == language_winner.pop().full_name:
                                remove_titles.add(title_2.full_name)
                            else:
                                remove_titles.add(title_1.full_name)

            cross_region_parent_titles = {
                x for x in cross_region_parent_titles if x.full_name not in remove_titles
            }

            if report_on_match:
                TraceTools.trace_title('REF0104', [], cross_region_parent_titles, keep_remove=False)

        # Choose a title that has more regions, or higher priority regions
        if len(cross_region_parent_titles) > 1:
            cross_region_parent_titles = choose_region(
                cross_region_parent_titles,
                region_order,
                world_is_usa_europe_japan=False,
                report_on_match=report_on_match,
            )

            if report_on_match:
                TraceTools.trace_title('REF0102', [], cross_region_parent_titles, keep_remove=False)

        # Choose a title that has more of the user's languages
        if len(cross_region_parent_titles) > 1:
            cross_region_parent_titles = choose_language(
                cross_region_parent_titles, config, report_on_match
            )

            if report_on_match:
                TraceTools.trace_title('REF0101', [], cross_region_parent_titles, keep_remove=False)

        # Do a full superset filter
        superset_titles: set[DatNode] = {
            title for title in cross_region_parent_titles if title.is_superset
        }

        if superset_titles:
            # Split by tag-free name
            short_name_superset_titles: dict[str, set[DatNode]] = {}

            for superset_title in superset_titles:
                if superset_title.short_name not in short_name_superset_titles:
                    short_name_superset_titles[superset_title.short_name] = set()

                short_name_superset_titles[superset_title.short_name].add(superset_title)

            superset_titles_final: set[DatNode] = set()

            for (
                short_name_superset_key,
                short_name_superset_set,
            ) in short_name_superset_titles.items():
                # Find the highest priority superset
                top_priority: int = sorted(
                    short_name_superset_set, key=lambda i: i.clonelist_priority
                )[0].clonelist_priority

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0016',
                        [str(top_priority), short_name_superset_key],
                        short_name_superset_set,
                        keep_remove=False,
                    )

                # Remove lower priority superset titles
                tag_free_superset_group_trimmed = {
                    title
                    for title in short_name_superset_set
                    if title.clonelist_priority == top_priority
                }

                # If there's multiple regions represented, take the highest priority
                region_found: bool = False

                for region in region_order:
                    for title in tag_free_superset_group_trimmed:
                        if region in title.regions:
                            region_found = True
                            superset_titles_final.add(title)

                    if region_found:
                        break

                if report_on_match:
                    TraceTools.trace_title('REF0079', [], superset_titles_final, keep_remove=False)

                # Integrate superset titles back into the main set
                cross_region_parent_titles = {
                    title for title in cross_region_parent_titles if not title.is_superset
                }

                cross_region_temp = cross_region_parent_titles.copy()

                superset_removes: set[DatNode] = set()

                for title in cross_region_temp:
                    for superset_title in superset_titles_final:
                        if TitleTools.check_title_equivalence(title, superset_title):
                            if title in cross_region_parent_titles:
                                if config.user_input.region_bias:
                                    if title.region_priority < superset_title.region_priority:
                                        superset_removes.add(superset_title)
                                        if report_on_match:
                                            TraceTools.trace_title(
                                                'REF0086',
                                                [title.full_name, superset_title.full_name],
                                                set(),
                                                keep_remove=True,
                                            )
                                    else:
                                        cross_region_parent_titles.remove(title)
                                        if report_on_match:
                                            TraceTools.trace_title(
                                                'REF0088',
                                                [superset_title.full_name, title.full_name],
                                                set(),
                                                keep_remove=True,
                                            )
                                else:
                                    cross_region_parent_titles.remove(title)
                                    if report_on_match:
                                        TraceTools.trace_title(
                                            'REF0087',
                                            [superset_title.full_name, title.full_name],
                                            set(),
                                            keep_remove=True,
                                        )

                superset_titles_final = superset_titles_final - superset_removes

                cross_region_parent_titles = cross_region_parent_titles | superset_titles_final

            if report_on_match:
                TraceTools.trace_title('REF0017', [], superset_titles_final, keep_remove=False)
        else:
            cross_region_parent_titles = cross_region_parent_titles - {
                title for title in cross_region_parent_titles if title.is_superset
            }

        if report_on_match:
            TraceTools.trace_title('REF0018', [], cross_region_parent_titles, keep_remove=False)

    # Assign clones
    if report_on_match:
        clone_report: dict[str, set[str]] = {}

    for cross_region_title in cross_region_parent_titles:
        for title in original_titles[group_name]:
            if (
                TitleTools.check_title_equivalence(title, cross_region_title)
                and title.full_name != cross_region_title.full_name
            ):
                if is_superset_titles and title.full_name not in potential_parents:
                    potential_parents[title.full_name] = set()

                if report_on_match:
                    if cross_region_title.full_name not in clone_report:
                        clone_report[cross_region_title.full_name] = set()

                    # Make sure the title is only assigned a parent once
                    clone_check: bool = False

                    for clone_values in clone_report.values():
                        for value in clone_values:
                            if title.full_name == value:
                                clone_check = True

                    if not clone_check:
                        clone_report[cross_region_title.full_name].add(title.full_name)

                if not is_superset_titles:
                    if is_numbered:
                        title.cloneof = cross_region_title.numbered_name
                    else:
                        title.cloneof = cross_region_title.full_name
                else:
                    if not next(
                        (
                            x
                            for x in potential_parents[title.full_name]
                            if x.full_name == cross_region_title.full_name
                        ),
                        None,
                    ):
                        potential_parents[title.full_name].add(cross_region_title)

    if report_on_match and clone_report:
        TraceTools.trace_title('REF0019', [], keep_remove=False)

        for parent, clones in sorted(clone_report.items()):
            eprint(f'+ [1G1R title]\t{Font.b}{parent}{Font.be}', wrap=False)

            for clone in sorted(clones):
                tree_symbol: str = '├'

                if clone == sorted(clones)[-1]:
                    tree_symbol = '└'

                eprint(
                    f'{tree_symbol} [clone]\t{Font.b}{clone}{Font.be}',
                    level='disabled',
                    wrap=False,
                )

            eprint(pause=True)

    return processed_titles
