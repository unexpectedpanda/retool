from __future__ import annotations

import itertools
from copy import deepcopy
from itertools import combinations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.title_selection.choose_1g1r import choose_1g1r
from modules.title_selection.choose_good import choose_good
from modules.title_selection.choose_language import choose_language
from modules.title_selection.choose_priority import choose_priority
from modules.title_selection.choose_region import choose_region
from modules.title_selection.choose_superset import choose_superset
from modules.titletools import TitleTools, TraceTools
from modules.utils import Font, eprint


def choose_compilation(
    compilations: set[DatNode],
    all_titles: dict[str, set[DatNode]],
    quick_lookup: dict[str, dict[str, set[DatNode]]],
    config: Config,
    is_numbered: bool,
) -> dict[str, set[DatNode]]:
    """
    When choosing 1G1R titles from compilations and individual titles, selects titles
    based on user preferences.

    Args:
        compilations (set[DatNode]): A set of compilation titles to be considered as
            DatNode instances.

        all_titles (dict[str, set[DatNode]]): All non-compilation titles to be considered.

        quick_lookup (dict[str, set[DatNode]]): A dictionary keyed by multiple title
            properties that enables quick lookup of titles. Due to the way Python
            references variables, changes made here are also reflected in
            `processed_titles`.

        config (Config): The Retool config object.

        is_numbered (bool): Whether the DAT file prefixes its title names with numbers.

    Returns:
        dict (dict[str, set[DatNode]]): Compilations that have been reintegrated into
        `all_titles`, with new 1G1R titles set accordingly.
    """
    # Get the previously set individual 1G1R titles related to the compilations
    individual_titles: set[DatNode] = set()

    if config.user_input.compilations != 'k':
        for compilation in compilations:
            for contains_title in list(compilation.contains_titles.keys()):
                group = contains_title.lower()
                if group in all_titles:
                    parent_names: list[str] = [
                        x.full_name for x in all_titles[group] if not x.cloneof
                    ]
                    parent_titles: list[DatNode] = [
                        x for x in all_titles[group] if x.full_name in parent_names
                    ]

                    for parent_title in parent_titles:
                        if parent_title.group_name == group:
                            individual_titles.add(parent_title)

    compilation_comparison: set[DatNode] = compilations | individual_titles

    # Set up title tracking
    report_on_match: bool = False

    if config.user_input.trace:
        report_on_match = TraceTools.trace_enable(compilation_comparison, config.user_input.trace)

    if report_on_match:
        eprint('Stage: Compilations', level='heading')

    # Get all the title short names in consideration from both compilations and
    # individual titles
    title_names_in_consideration: set[str] = set()

    for compilation in compilations:
        for contains_title in list(compilation.contains_titles):
            title_names_in_consideration.add(contains_title.lower())

    for individual_title in individual_titles:
        title_names_in_consideration.add(individual_title.short_name)

    # Group the title short names into a dictionary as keys, and populate them with
    # the DatNodes of related titles as the values. Convert compilations to
    # virtual individual titles along the way, so each of the constituent titles can
    # be fairly compared.
    #
    # For example, for the title full names Title A (USA), Title A + Title B (USA):
    #
    # {
    #   Title A: {DatNode('Title A (USA)'), DatNode(':V: Title A (USA) • Title A + Title B')},
    #   Title B: {DatNode(':V: Title B (USA) • Title A + Title B (USA)')}
    # }

    grouped_titles: dict[str, set[DatNode]] = {}
    filtered_titles: dict[str, set[DatNode]] = {}

    for short_name in title_names_in_consideration:
        if short_name not in grouped_titles:
            grouped_titles[short_name] = set()

        TitleTools.convert_to_virtual_titles(compilations, grouped_titles, short_name, config)

        for individual_title in individual_titles:
            if short_name == individual_title.short_name:
                grouped_titles[short_name].add(individual_title)

    # Select winners for each title short name
    for key, titles in grouped_titles.items():
        comparison_set: set[DatNode] = deepcopy(titles)
        comparison_report_on_match: bool = False

        if config.user_input.trace:
            comparison_report_on_match = TraceTools.trace_enable(
                comparison_set, config.user_input.trace
            )

        if comparison_report_on_match:
            eprint(f'Comparing titles with {key} short name', level='heading')

            TraceTools.trace_title('REF0067', [key], comparison_set, keep_remove=False)

        # Filter by preproduction and pirate
        if len(comparison_set) > 1:
            comparison_set = choose_good(comparison_set, config)

            if comparison_report_on_match:
                TraceTools.trace_title('REF0092', [key], comparison_set, keep_remove=False)

        # Choose individual titles if the user requests it
        if len(comparison_set) > 1:
            if config.user_input.compilations == 'i':
                # Find out if there's any individual titles in the set
                if any(x for x in comparison_set if not x.contains_titles):
                    # Remove the compilations
                    for title in [x for x in comparison_set if x.contains_titles]:
                        comparison_set.remove(title)

                if comparison_report_on_match:
                    TraceTools.trace_title('REF0126', [key], comparison_set, keep_remove=False)

        # Choose supersets
        if len(comparison_set) > 1:
            comparison_set = choose_superset(comparison_set, config, comparison_report_on_match)

            if comparison_report_on_match:
                TraceTools.trace_title('REF0127', [key], comparison_set, keep_remove=False)

        # Filter by user language order, temporarily hijack the primary region to do
        # so
        if len(comparison_set) > 1:
            for title in comparison_set:
                title.primary_region = 'compilation'

            comparison_set = choose_language(
                comparison_set, config, comparison_report_on_match, first_time=True
            )

            if comparison_report_on_match:
                TraceTools.trace_title('REF0068', [key], comparison_set, keep_remove=False)

        # Return primary regions and languages to their original state
        for title in comparison_set:
            title.languages = title.languages_original
            title.primary_region = title.primary_region_original

        # Filter by priority
        if len(comparison_set) > 1:
            comparison_set = choose_priority(comparison_set, config, comparison_report_on_match)

            if comparison_report_on_match:
                TraceTools.trace_title('REF0080', [key], comparison_set, keep_remove=False)

        # Filter by user region order
        if len(comparison_set) > 1:
            region_order: list[str] = config.region_order_user

            if config.system_region_order_user:
                if {'override': 'true'} in config.system_region_order_user:
                    region_order = [
                        str(x) for x in config.system_region_order_user if 'override' not in x
                    ]

            comparison_set = choose_region(
                comparison_set,
                region_order,
                world_is_usa_europe_japan=True,
                report_on_match=comparison_report_on_match,
            )

            if comparison_report_on_match:
                TraceTools.trace_title('REF0069', [key], comparison_set, keep_remove=False)

        # Rename virtual titles back to their original compilation titles
        for title in comparison_set:
            title.full_name = title.full_name_original

        if comparison_report_on_match:
            TraceTools.trace_title('REF0070', [key], comparison_set, keep_remove=False)

        # Tie breaker - choose the individual title
        if len(comparison_set) > 1 and config.user_input.compilations != 'o':
            remove_compilations: set[DatNode] = set()

            for title_1, title_2 in itertools.combinations(comparison_set, 2):
                if title_1.short_name == title_2.short_name:
                    if title_1.contains_titles and not title_2.contains_titles:
                        remove_compilations.add(title_1)

                        if comparison_report_on_match:
                            TraceTools.trace_title(
                                'REF0075',
                                [title_2.full_name, title_1.full_name],
                                keep_remove=True,
                            )

                    if title_2.contains_titles and not title_1.contains_titles:
                        remove_compilations.add(title_2)

                        if comparison_report_on_match:
                            TraceTools.trace_title(
                                'REF0093',
                                [title_1.full_name, title_2.full_name],
                                keep_remove=True,
                            )

            for remove_compilation in remove_compilations:
                if remove_compilation in comparison_set:
                    comparison_set.remove(remove_compilation)

        if len(comparison_set) > 1:
            # Tie breaker - filter by user language order, taking region into account
            # This is run now because doing a full language filter earlier selects compilations over individual titles
            comparison_set = choose_language(
                comparison_set, config, comparison_report_on_match, first_time=False
            )

        if len(comparison_set) > 1:
            # Tie breaker - check if a compilation entirely contains another compilation
            for title_1, title_2 in itertools.combinations(comparison_set, 2):
                if title_1.contains_titles and title_2.contains_titles:
                    # Check if title_2 contains title_1
                    if (
                        len(title_1.contains_titles) < len(title_2.contains_titles)
                        and title_1.primary_region == title_2.primary_region
                        and all(item in title_2.contains_titles for item in title_1.contains_titles)
                    ):
                        if title_1 in comparison_set:
                            comparison_set.remove(title_1)

                        if comparison_report_on_match:
                            TraceTools.trace_title(
                                'REF0090',
                                [title_2.full_name, title_1.full_name],
                                keep_remove=True,
                            )
                    # Check if title_1 contains title_2
                    elif (
                        len(title_2.contains_titles) < len(title_1.contains_titles)
                        and title_1.primary_region == title_2.primary_region
                        and all(item in title_1.contains_titles for item in title_2.contains_titles)
                    ):
                        if title_2 in comparison_set:
                            comparison_set.remove(title_2)

                        if comparison_report_on_match:
                            TraceTools.trace_title(
                                'REF0091',
                                [title_1.full_name, title_2.full_name],
                                keep_remove=True,
                            )
                    # If title_1 and title_2 contain the same individual titles, put them through individual title filtering
                    elif title_1.contains_titles == title_2.contains_titles:
                        # Fake the short names to use existing filtering tools
                        title_1_original_short_name: str = title_1.short_name
                        title_2_original_short_name: str = title_2.short_name

                        title_1.short_name = 'compilation'
                        title_2.short_name = 'compilation'

                        # Put the individual titles through the filter process
                        filtered: dict[str, set[DatNode]] = choose_1g1r(
                            config,
                            is_numbered,
                            {},
                            is_superset_titles=False,
                            is_compilations=True,
                            title_set={title_1, title_2},
                        )

                        # Convert the result back into a set of titles
                        filtered_set = {y for y in list(filtered.values())[0] if not y.cloneof}

                        # Recover the original short names
                        title_1.short_name = title_1_original_short_name
                        title_2.short_name = title_2_original_short_name

                        # Remove titles that didn't pass the filter process
                        if title_1 not in filtered_set:
                            if title_1 in comparison_set:
                                comparison_set.remove(title_1)

                        if title_2 not in filtered_set:
                            if title_2 in comparison_set:
                                comparison_set.remove(title_2)

            if comparison_report_on_match:
                TraceTools.trace_title('REF0128', [key], comparison_set, keep_remove=False)

        if key not in filtered_titles:
            filtered_titles[key] = set()

        filtered_titles[key] = comparison_set

    # ================================================================================
    # Group titles with partial or completely shared contents together to find
    # the optimal combination of titles
    # ================================================================================

    # Get the title names each remaining compilation contains.
    #
    # For example, a compilation of the name Title A + Title B (USA), and a
    # compilation of the name Title A + Title C (USA) returns:
    #
    # [{'Title A', 'Title B'}, {'Title A', 'Title C'}]

    short_names_in_compilations: list[set[str]] = []

    for titles in filtered_titles.values():
        for title in titles:
            if title.contains_titles:
                short_names_in_compilations.append(set(title.contains_titles))
            else:
                if config.user_input.compilations != 'o':
                    short_names_in_compilations.append({title.short_name})

    # Merge title names that have elements in common.
    #
    # For example, [{'Title A', 'Title B'}, {'Title A', 'Title C'}] returns:
    #
    # [{Title A, Title B, Title C}]

    for a, b in itertools.product(short_names_in_compilations, short_names_in_compilations):
        if a.intersection(b):
            a.update(b)
            b.update(a)

    # Remove duplicate title groups
    short_names_in_compilations_list: list[list[str]] = sorted(
        [sorted(x) for x in short_names_in_compilations]
    )

    short_names_in_compilations_list = [
        sublist for sublist, _ in itertools.groupby(short_names_in_compilations_list)
    ]

    # Get things in a format that matches short names
    short_names_in_compilations_list = [
        [x.lower() for x in sublst] for sublst in short_names_in_compilations_list
    ]

    # Add titles to a dictionary to find the optimal combination across shared
    # titles
    #
    # For example:
    #
    # {
    #   title a, title b: {DatNode('Title A (USA)'), DatNode('Title A + Title B')},
    # }
    #
    # Select DatNode('Title A + Title B')

    related_titles: dict[str, set[DatNode]] = {}

    for short_names in short_names_in_compilations_list:
        key = ', '.join(short_names)

        if key not in related_titles:
            related_titles[key] = set()

        for short_name in short_names:
            for title in filtered_titles[short_name]:
                if title.full_name not in [
                    existing_title.full_name for existing_title in related_titles[key]
                ]:
                    related_titles[key].add(title)

    # Deal with supersets being among individual titles. Handling is very basic, as
    # we don't support compilations that contain supersets yet.
    remove_titles: set[DatNode] = set()

    for key, titles in related_titles.items():
        supersets: set[DatNode] = set()

        for title in titles:
            if not title.contains_titles and title.is_superset:
                supersets.add(title)

        if supersets:
            # Find if the superset short name is in any of the compilations
            for superset in supersets:
                replace_titles_with_superset: set[DatNode] = set()

                for title in titles:
                    contains_titles: list[str] = [
                        contains_title.lower() for contains_title in title.contains_titles
                    ]

                    if superset.short_name in contains_titles:
                        replace_titles_with_superset = replace_titles_with_superset | {title}

                # See if the rest of the compilation can be satisfied by other titles
                if replace_titles_with_superset:
                    for title in replace_titles_with_superset:
                        contains_titles = [
                            contains_title.lower() for contains_title in title.contains_titles
                        ]
                        contains_titles.remove(superset.short_name)

                        satisfied: int = 0

                        for contain_title in contains_titles:
                            for other_title in related_titles[key]:
                                if (
                                    other_title.full_name != title.full_name
                                    and other_title.full_name != superset.full_name
                                ):
                                    if other_title.contains_titles:
                                        other_title_contains_titles = [
                                            other_contains_title.lower()
                                            for other_contains_title in other_title.contains_titles
                                        ]

                                        if contain_title in other_title_contains_titles:
                                            satisfied += 1
                                    else:
                                        if other_title.short_name == contain_title:
                                            satisfied += 1

                        if satisfied == len(contains_titles):
                            for related_title in related_titles[key]:
                                if related_title.full_name == title.full_name:
                                    remove_titles.add(title)

    temp_dict: dict[str, set[DatNode]] = deepcopy(related_titles)

    # Remove the unwanted titles
    for remove_title in remove_titles:
        for key, titles in temp_dict.items():
            for title in titles:
                if title.full_name == remove_title.full_name:
                    related_titles[key] = {
                        x for x in related_titles[key] if x.full_name != remove_title.full_name
                    }

    # Now break things down into the following format, so we know what short names and
    # regions must be included in the final selection:
    #
    # (('title 1', 'USA'), ('title 2', 'USA'))
    available_groupings: dict[str, set[tuple[tuple[str, ...], str]]] = {}

    if 'retool_compilations_winners' not in all_titles:
        all_titles['retool_compilations_winners'] = set()

    for key, titles in related_titles.items():
        # Set up title tracking
        report_on_match = False

        if config.user_input.trace:
            report_on_match = TraceTools.trace_enable(titles, config.user_input.trace)

        if len(titles) > 1:
            if report_on_match:
                TraceTools.trace_title('REF0071', [key], keep_remove=False)
                eprint('Titles in contention:\n')
                for title in titles:
                    eprint(f'• [{title.short_name}] {title.full_name}', wrap=False)

            # Get the short names of every title in contention. Compilations group names
            # are based on their constituent titles.
            contention_group_set: set[str] = set()

            for title in titles:
                if title.contains_titles:
                    for contains_title in title.contains_titles.keys():
                        contention_group_set.add(contains_title.lower())
                else:
                    contention_group_set.add(title.short_name)

            if report_on_match:
                TraceTools.trace_title('REF0120')
                eprint(str(contention_group_set), wrap=False, pause=True)

            # Find titles that we have to keep, including their regions
            required_titles: dict[str, list[DatNode]] = {}
            compare_group: set[DatNode] = set()

            for contention_group in contention_group_set:
                if contention_group.lower() in filtered_titles:
                    compare_group = filtered_titles[contention_group.lower()]
                elif TitleTools.get_group_name(contains_title, config) in filtered_titles:
                    compare_group = filtered_titles[
                        TitleTools.get_group_name(contains_title, config)
                    ]

                for title in compare_group:
                    if contention_group not in required_titles:
                        required_titles[contention_group] = []
                    required_titles[contention_group].append(title)

            required_titles_and_regions: tuple[tuple[str, str], ...] = tuple(
                [(k, required_titles[k][0].primary_region) for k in required_titles]
            )

            if report_on_match:
                TraceTools.trace_title('REF0121')
                eprint(str(required_titles_and_regions), wrap=False, pause=True)

            unique_title_names: set[str] = set()
            keep_these_titles: set[DatNode] = set()

            for title in titles:
                if title.full_name not in unique_title_names:
                    unique_title_names.add(title.full_name)
                    keep_these_titles.add(title)

                    if key not in available_groupings:
                        available_groupings[key] = set()

                    if title.contains_titles:
                        available_groupings[key].add(
                            (
                                tuple([x.lower() for x in title.contains_titles]),
                                title.primary_region,
                            )
                        )
                    else:
                        available_groupings[key].add(((title.group_name,), title.primary_region))

            # Get all viable combinations for this group
            candidates: list[tuple[tuple[tuple[str, ...], str], ...]] = []

            for i in range(1, len(contention_group_set)):
                combos = list(combinations(sorted(available_groupings[key]), i))

                if report_on_match:
                    TraceTools.trace_title('REF0122', [str(i)])
                    eprint(str(combos), wrap=False, pause=True)

                for combo in combos:
                    # Reformat the list to see if all the needed groups and regions are there.
                    full_combo: set[str] = set()

                    for subcombo in combo:
                        full_combo = full_combo | ({(x, subcombo[1]) for x in subcombo[0]})  # type: ignore

                    if all(item in full_combo for item in required_titles_and_regions):  # type: ignore
                        candidates.append(combo)

            # Prefer individual titles if not finding the most optimized combination of titles
            if not candidates or config.user_input.compilations != 'o':
                candidates = [tuple(available_groupings[key])]

            if report_on_match:
                TraceTools.trace_title('REF0124')
                eprint(str(candidates), wrap=False, pause=True)

            # Find the combination with the fewest elements
            least_elements: int = len(sorted(candidates, key=lambda x: len(x))[0])

            # Out of those combinations, find the grouping that has the least number of individual titles in it including duplicates
            smallest_number_of_titles_including_duplicates: int = 0
            number_of_individual_titles_represented_including_duplicates: int = 0
            number_of_candidates_in_group: int = 0
            stage_1_candidates = []

            for candidate in sorted(candidates):
                number_of_individual_titles_represented_including_duplicates = len(
                    [item for sublist in [x[0] for x in candidate] for item in sublist]
                )
                number_of_candidates_in_group = len(candidate)

                if report_on_match:
                    TraceTools.trace_title('REF0125')
                    eprint(f'Candidate: {candidate}')
                    eprint(
                        f'Number of titles including dupes: {number_of_individual_titles_represented_including_duplicates} (based on {[item for sublist in [x[0] for x in candidate] for item in sublist]})'
                    )
                    eprint(f'Candidate length: {number_of_candidates_in_group}')
                    eprint(f'Least possible elements in potential candidate: {least_elements}')
                    if number_of_candidates_in_group == least_elements:
                        eprint('Good candidate, goes to next stage', level='success')
                    else:
                        eprint(f'{Font.error}Bad candidate, doesn\'t go to next stage{Font.end}')

                    eprint(pause=True)

                # For the candidates with the fewest elements, find the one with the least title duplication
                if number_of_candidates_in_group == least_elements:
                    if (
                        number_of_individual_titles_represented_including_duplicates
                        < smallest_number_of_titles_including_duplicates
                        or smallest_number_of_titles_including_duplicates == 0
                    ):
                        smallest_number_of_titles_including_duplicates = (
                            number_of_individual_titles_represented_including_duplicates
                        )

            # Add the combination with the least title duplication
            for candidate in sorted(candidates):
                number_of_individual_titles_represented_including_duplicates = len(
                    [item for sublist in [x[0] for x in candidate] for item in sublist]
                )

                if (
                    number_of_individual_titles_represented_including_duplicates
                    == smallest_number_of_titles_including_duplicates
                ):
                    stage_1_candidates.append(candidate)

            # Of the remaining candidates, select those with the longest grouping of titles
            # Find the value for the longest grouping of titles
            longest_grouping: int = max(
                [len(item[0]) for sublist in stage_1_candidates for item in sublist]
            )

            stage_2_candidates = []

            for candidate in stage_1_candidates:
                if (
                    max([len(y[0]) for sublist in list(candidates) for y in sublist])
                    == longest_grouping
                ):
                    stage_2_candidates.append(candidate)

            # If there are still multiple candidates, make sure to always select the
            # same one by sorting and ordering
            ideal_combination = tuple(
                sorted([sorted(x, key=lambda y: (len, y)) for x in stage_2_candidates])[0]
            )

            # Map the groupings back to the original titles
            final_titles: set[DatNode] = set()

            if ideal_combination:
                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(
                        set(related_titles[key]), config.user_input.trace
                    )

                for title in related_titles[key]:
                    if title.contains_titles:
                        if (
                            tuple([x.lower() for x in title.contains_titles]),
                            title.primary_region,
                        ) in ideal_combination:
                            final_titles.add(title)

                            # Add it to the compilations group
                            all_titles['retool_compilations_winners'].add(title)
                    else:
                        if ((title.group_name,), title.primary_region) in ideal_combination:
                            final_titles.add(title)

                            # Remove the original title
                            remove: DatNode | None = None
                            remove_found: bool = False

                            for remove_titles in all_titles.values():
                                for remove_title in remove_titles:
                                    if remove_title.full_name == title.full_name:
                                        remove_found = True
                                        remove = remove_title
                                        break
                                if remove_found:
                                    break

                            if remove is not None:
                                all_titles[remove.group_name].remove(remove)

                            # Add it to the compilations group
                            all_titles['retool_compilations_winners'].add(title)

            if report_on_match:
                TraceTools.trace_title('REF0123')
                eprint(
                    f'Stage 1 candidates (least number of duplicate titles):\t{stage_1_candidates}'
                )
                eprint(
                    f'Stage 2 candidates (longest grouping of titles):\t{stage_2_candidates}',
                    pause=True,
                )

            if report_on_match:
                TraceTools.trace_title(
                    'REF0072',
                    [str(x) for x in ideal_combination],
                    final_titles,
                    keep_remove=False,
                )
        else:
            # Add the individual title to the compilations group
            for title in titles:
                if title.full_name not in [
                    x.full_name for x in all_titles['retool_compilations_winners']
                ]:
                    # Remove the original title
                    remove = None
                    remove_found = False

                    for remove_titles in all_titles.values():
                        for remove_title in remove_titles:
                            if remove_title.full_name == title.full_name:
                                remove_found = True
                                remove = remove_title
                                break
                        if remove_found:
                            break

                    if remove is not None:
                        all_titles[remove.group_name].remove(remove)

                    # Add it to the compilations group
                    all_titles['retool_compilations_winners'].add(title)

    # Add compilations back that were removed earlier
    all_titles['retool_compilations_discards'] = {
        x
        for x in compilation_comparison
        if x.full_name not in [y.full_name for y in all_titles['retool_compilations_winners']]
    }

    # Assign clones
    for title in sorted(all_titles['retool_compilations_discards'], key=lambda x: x.full_name):
        for winner_title in sorted(
            all_titles['retool_compilations_winners'], key=lambda x: x.full_name
        ):
            if not title.cloneof:
                clone_set: bool = False

                if is_numbered:
                    winner_title_name: str = winner_title.numbered_name
                else:
                    winner_title_name = winner_title.full_name

                if winner_title.contains_titles:
                    # If the winner is a compilation...
                    for contains_title in winner_title.contains_titles:
                        if not title.contains_titles:
                            # Assign individual title discards to compilation winners
                            if contains_title.lower() == title.short_name:
                                title.cloneof = winner_title_name
                                clone_set = True
                                break
                        else:
                            # Assign compilation title discards to compilation winners
                            if contains_title.lower() in [x.lower() for x in title.contains_titles]:
                                title.cloneof = winner_title_name
                                clone_set = True
                                break
                else:
                    # If the winner is an individual title...
                    if not title.contains_titles:
                        # Assign individual title discards to individual winners
                        if winner_title.short_name == title.short_name:
                            title.cloneof = winner_title_name
                            clone_set = True
                            break
                    else:
                        # Assign compilation title discards to individual winners
                        if winner_title.short_name in [x.lower() for x in title.contains_titles]:
                            title.cloneof = winner_title_name
                            clone_set = True
                            break

                # Reconcile clones that have already been set
                if clone_set:
                    for clone_titles in all_titles.values():
                        for clone_title in clone_titles:
                            if is_numbered:
                                if clone_title.cloneof == title.numbered_name:
                                    clone_title.cloneof = winner_title_name
                            else:
                                if clone_title.cloneof == title.full_name:
                                    clone_title.cloneof = winner_title_name

    # Report assignments
    for winner_title in sorted(
        all_titles['retool_compilations_winners'], key=lambda x: x.full_name
    ):
        if is_numbered:
            winner_title_name = winner_title.numbered_name
        else:
            winner_title_name = winner_title.full_name

        if config.user_input.trace:
            report_on_match = TraceTools.trace_enable({winner_title}, config.user_input.trace)

        if report_on_match:
            TraceTools.trace_title('REF0073', [], keep_remove=False)
            eprint(f'+ [1G1R title]\t{Font.b}{winner_title.full_name}{Font.be}', wrap=False)

            for clone_title in sorted(
                all_titles['retool_compilations_discards'], key=lambda x: x.full_name
            ):
                if clone_title.cloneof == winner_title_name:
                    tree_symbol: str = '├'

                    if (
                        clone_title
                        == sorted(
                            all_titles['retool_compilations_discards'],
                            key=lambda x: x.full_name,
                        )[-1]
                    ):
                        tree_symbol = '└'

                    eprint(
                        f'{tree_symbol} [clone]\t{Font.b}{clone_title.full_name}{Font.be}',
                        level='disabled',
                        wrap=False,
                    )

            eprint(pause=True)

    return all_titles
