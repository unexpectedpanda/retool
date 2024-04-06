from __future__ import annotations

import itertools
import os
import re
import sys
from contextlib import nullcontext
from copy import deepcopy
from functools import partial, reduce
from itertools import combinations
from re import Pattern
from typing import TYPE_CHECKING, Any

import psutil
from alive_progress import alive_bar  # type: ignore

if TYPE_CHECKING:
    from modules.config import Config
    from modules.dats import DatNode

from modules.clonelists import CloneListTools
from modules.interruptible_pool import InterruptiblePool
from modules.titletools import TitleTools, TraceTools
from modules.utils import Font, eprint, pattern2string


class ParentTools:
    """Methods for selecting a parent from a list of DatNode titles."""

    @staticmethod
    def choose_compilations(
        compilations: set[DatNode], all_titles: dict[str, set[DatNode]], config: Config
    ) -> dict[str, set[DatNode]]:
        """
        When choosing 1G1R titles from compilations and individual titles, selects titles
        based on user preferences.

        Args:
            compilations (set[DatNode]): A set of compilation titles to be considered as
            DatNode instances.

            all_titles (dict[str, set[DatNode]]): All non-compilation titles to be
            considered.

            config (Config): The Retool config object.

        Returns:
            dict[str, set[DatNode]]: Compilations that have been reintegrated into
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
            report_on_match = TraceTools.trace_enable(
                compilation_comparison, config.user_input.trace
            )

        if report_on_match:
            eprint(f'\n\n{Font.heading_bold}Stage: Compilations{Font.end}')

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
                eprint(f'{Font.heading_bold}Comparing titles with {key} short name{Font.end}')

                TraceTools.trace_title('REF0067', [key], comparison_set, keep_remove=False)

            # Filter by preproduction and pirate
            if len(comparison_set) > 1:
                comparison_set = ParentTools.remove_preprod_bad(comparison_set, config)

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
                comparison_set = ParentTools.choose_superset(
                    comparison_set, comparison_report_on_match
                )

                if comparison_report_on_match:
                    TraceTools.trace_title('REF0127', [key], comparison_set, keep_remove=False)

            # Filter by user language order, temporarily hijack the primary region to do
            # so
            if len(comparison_set) > 1:
                for title in comparison_set:
                    title.primary_region = 'compilation'

                comparison_set = ParentTools.choose_language(
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
                comparison_set = CloneListTools.compare_priorities(
                    comparison_set, comparison_report_on_match
                )

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

                comparison_set = ParentTools.choose_multi_regions(
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
                comparison_set = ParentTools.choose_language(
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
                            and all(
                                item in title_2.contains_titles for item in title_1.contains_titles
                            )
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
                            and all(
                                item in title_1.contains_titles for item in title_2.contains_titles
                            )
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
                            filtered: dict[str, set[DatNode]] = ParentTools.choose_parent_process(
                                config,
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

        short_names_in_compilations: list[str] = []

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
        short_names_in_compilations = sorted([sorted(x) for x in short_names_in_compilations])

        short_names_in_compilations = [
            sublist for sublist, _ in itertools.groupby(short_names_in_compilations)
        ]

        # Get things in a format that matches short names
        short_names_in_compilations = [
            [x.lower() for x in sublst] for sublst in short_names_in_compilations
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

        for short_names in short_names_in_compilations:
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
                report_on_match = TraceTools.trace_enable(set(titles), config.user_input.trace)

            if len(titles) > 1:
                if report_on_match:
                    TraceTools.trace_title('REF0071', [key], keep_remove=False)
                    eprint('Titles in contention:\n')
                    for title in titles:
                        eprint(f'* [{title.short_name}] {title.full_name}')

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
                    eprint(contention_group_set)
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

                # Find titles that we have to keep, including their regions
                required_titles: dict[str, list[DatNode]] = {}
                compare_group: list[DatNode] = []

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
                    eprint(required_titles_and_regions)
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

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
                            available_groupings[key].add(
                                ((title.group_name,), title.primary_region)
                            )

                # Get all viable combinations for this group
                candidates: list = []

                for i in range(1, len(contention_group_set)):
                    combos = list(combinations(sorted(available_groupings[key]), i))

                    if report_on_match:
                        TraceTools.trace_title('REF0122', [i])
                        eprint(combos)
                        eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                        input()

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
                    eprint(candidates)
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

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
                            eprint(f'{Font.success}Good candidate, goes to next stage{Font.end}')
                        else:
                            eprint(
                                f'{Font.error}Bad candidate, doesn\'t go to next stage{Font.end}'
                            )

                        eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                        input()

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
                                remove_title: set[DatNode] = TitleTools.find_title(
                                    title.full_name,
                                    'full',
                                    all_titles,
                                    set(),
                                    config,
                                    deep_search=True,
                                )
                                all_titles[next(iter(remove_title)).group_name].remove(
                                    list(remove_title)[0]
                                )

                                # Add it to the compilations group
                                all_titles['retool_compilations_winners'].add(title)

                if report_on_match:
                    TraceTools.trace_title('REF0123')
                    eprint(
                        f'Stage 1 candidates (least number of duplicate titles):\t{stage_1_candidates}'
                    )
                    eprint(
                        f'Stage 2 candidates (longest grouping of titles):\t{stage_2_candidates}'
                    )
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

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
                        remove_title = TitleTools.find_title(
                            title.full_name, 'full', all_titles, set(), config, deep_search=True
                        )

                        if remove_title:
                            all_titles[next(iter(remove_title)).group_name].remove(
                                list(remove_title)[0]
                            )

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

                    if winner_title.contains_titles:
                        # If the winner is a compilation...
                        for contains_title in winner_title.contains_titles:
                            if not title.contains_titles:
                                # Assign individual title discards to compilation winners
                                if contains_title.lower() == title.short_name:
                                    title.cloneof = winner_title.full_name
                                    clone_set = True
                                    break
                            else:
                                # Assign compilation title discards to compilation winners
                                if contains_title.lower() in [
                                    x.lower() for x in title.contains_titles
                                ]:
                                    title.cloneof = winner_title.full_name
                                    clone_set = True
                                    break
                    else:
                        # If the winner is an individual title...
                        if not title.contains_titles:
                            # Assign individual title discards to individual winners
                            if winner_title.short_name == title.short_name:
                                title.cloneof = winner_title.full_name
                                clone_set = True
                                break
                        else:
                            # Assign compilation title discards to individual winners
                            if winner_title.short_name in [
                                x.lower() for x in title.contains_titles
                            ]:
                                title.cloneof = winner_title.full_name
                                clone_set = True
                                break

                    # Reconcile clones that have already been set
                    if clone_set:
                        for clone_titles in all_titles.values():
                            for clone_title in clone_titles:
                                if clone_title.cloneof == title.full_name:
                                    clone_title.cloneof = winner_title.full_name

        # Report assignments
        for winner_title in sorted(
            all_titles['retool_compilations_winners'], key=lambda x: x.full_name
        ):
            if config.user_input.trace:
                report_on_match = TraceTools.trace_enable({winner_title}, config.user_input.trace)

            if report_on_match:
                TraceTools.trace_title('REF0073', [], keep_remove=False)
                eprint(
                    f'+ {Font.bold}{winner_title.full_name}{Font.end} is the 1G1R title{Font.end}'
                )

                for clone_title in sorted(
                    all_titles['retool_compilations_discards'], key=lambda x: x.full_name
                ):
                    if clone_title.cloneof == winner_title.full_name:
                        eprint(
                            f'- {Font.disabled}{Font.bold}{clone_title.full_name}{Font.end}{Font.disabled} is a clone of {Font.bold}{clone_title.cloneof}{Font.end}'
                        )

                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                input()

        return all_titles

    @staticmethod
    def choose_date(title_set: set[DatNode], config: Config, report_on_match: bool) -> set[DatNode]:
        """
        Compare any two titles from a set of DatNodes, and select the one with the
        highest specified date.

        Args:
            title_set (set[DatNode]): A set of titles as DatNode instances.

            config (Config): The Retool config object.

            report_on_match (bool): Whether Retool needs to report any titles being
            traced.

        Returns:
            set[DatNode]: A set of DatNodes filtered by date priority.
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
                title_1_date: int = TitleTools.get_date(title_1.full_name, config)
                title_2_date: int = TitleTools.get_date(title_2.full_name, config)

                if title_1_date and not title_2_date:
                    if title_2 in title_set:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0024',
                                [
                                    f'({title_1_date}) {title_1.full_name}',
                                    f'({title_2_date}) {title_2.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_titles.add(title_2)
                elif title_2_date and not title_1_date:
                    if title_1 in title_set:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0025',
                                [
                                    f'({title_2_date}) {title_2.full_name}',
                                    f'({title_1_date}) {title_1.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_titles.add(title_1)
                elif title_1_date > title_2_date:
                    if title_2 in title_set:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0026',
                                [
                                    f'({title_1_date}) {title_1.full_name}',
                                    f'({title_2_date}) {title_2.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_titles.add(title_2)
                elif title_2_date > title_1_date:
                    if title_1 in title_set:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0027',
                                [
                                    f'({title_2_date}) {title_2.full_name}',
                                    f'({title_1_date}) {title_1.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_titles.add(title_1)

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_language(
        title_set: set[DatNode], config: Config, report_on_match: bool, first_time: bool = True
    ) -> set[DatNode]:
        """
        Compares any two titles from a set of DatNodes, looking for languages based on
        the user language order.

        Args:
            title_set (set[DatNode]): A set of titles as DatNode instances.

            config (Config): The Retool config object.

            report_on_match (bool): Whether Retool needs to report any titles being
            traced.

            first_time (bool, optional): Whether this is the first time the
            `choose_language` function has been run. If `True`, the comparison stops at
            the first language match. If `False`, the language order is used to
            determine which is the more desired title.

            For example, if a user has a language order of En > Fr > De > Zh > and the
            following titles are passed in:

            • Title 1 (En,Fr,De)

            • Title 2 (En,Fr,Zh)

            With `first_time` set to `True`, both titles are selected, as Retool finds
            En in both titles and stops. When `first_time` is `False`, the comparison
            continues. Both have Fr, but only Title 1 has De, and so it is selected.
            If both titles contain all the desired languages, as a fallback the title
            with the most languages is selected.

            Defaults to `True`.

        Returns:
            set[DatNode]: A set of DatNodes filtered by language priority.
        """
        # Check if a system config is in play
        language_order: list[str] = []

        if config.languages_filter:
            if config.system_language_order_user:
                if {'override': 'true'} in config.system_language_order_user:
                    language_order = [
                        str(x) for x in config.system_language_order_user if 'override' not in x
                    ]
                elif {'override': 'true'} in config.system_region_order_user:
                    for region in [
                        str(x) for x in config.system_region_order_user if x != {'override': 'true'}
                    ]:
                        language_order.extend(config.languages_filter[region])
                else:
                    language_order = config.language_order_user
            else:
                language_order = config.language_order_user

        # Select titles based on language
        remove_titles: set[DatNode] = set()

        for title_1, title_2 in itertools.combinations(title_set, 2):
            language_found: bool = False

            if (
                title_1.short_name == title_2.short_name
                and title_1 in title_set
                and title_2 in title_set
                and 'BIOS' not in title_1.categories
                and 'BIOS' not in title_2.categories
            ):
                for language in language_order:
                    if (
                        title_1.primary_region == title_2.primary_region
                        and title_1.languages
                        and title_2.languages
                    ):

                        if re.search(language, ','.join(title_1.languages)) and not re.search(
                            language, ','.join(title_2.languages)
                        ):
                            if title_2 in title_set:
                                if report_on_match:
                                    TraceTools.trace_title('REF0028', [', '.join(language_order)])
                                    TraceTools.trace_title(
                                        '',
                                        [
                                            f'{Font.italic}({",".join(title_1.languages) + ")":<30}{Font.end} [{title_1.short_name}] {title_1.full_name}',
                                            f'{Font.italic}({",".join(title_2.languages) + ")":<30}{Font.end}{Font.disabled} [{title_2.short_name}] {title_2.full_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )

                                remove_titles.add(title_2)
                                language_found = True
                                break
                        elif re.search(language, ','.join(title_2.languages)) and not re.search(
                            language, ','.join(title_1.languages)
                        ):
                            if title_1 in title_set:
                                if report_on_match:
                                    TraceTools.trace_title('REF0029', [', '.join(language_order)])
                                    TraceTools.trace_title(
                                        '',
                                        [
                                            f'{Font.italic}({",".join(title_2.languages) + ")":<30}{Font.end} [{title_2.short_name}] {title_2.full_name}',
                                            f'{Font.italic}({",".join(title_1.languages) + ")":<30}{Font.end}{Font.disabled} [{title_1.short_name}] {title_1.full_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )

                                remove_titles.add(title_1)
                                language_found = True
                                break
                        elif (
                            re.search(language, ','.join(title_2.languages))
                            and re.search(language, ','.join(title_1.languages))
                            and first_time
                        ):

                            language_found = True
                            break

                if not language_found:
                    if not (title_1.is_superset or title_2.is_superset):
                        if config.languages_filter:
                            # Cycle through implied languages from region order as the first fallback
                            fallback_language_order: list[str] = []

                            # Use the system region order if there is one
                            if {'override': 'true'} in config.system_region_order_user:
                                for region in [
                                    str(x)
                                    for x in config.system_region_order_user
                                    if x != {'override': 'true'}
                                ]:
                                    fallback_language_order.extend(config.languages_filter[region])
                            else:
                                fallback_language_order = config.region_order_languages_user

                            for language in fallback_language_order:
                                if re.search(
                                    language, ','.join(title_1.languages)
                                ) and not re.search(language, ','.join(title_2.languages)):
                                    if title_2 in title_set:
                                        if report_on_match:
                                            TraceTools.trace_title(
                                                'REF0097', [', '.join(fallback_language_order)]
                                            )
                                            TraceTools.trace_title(
                                                '',
                                                [
                                                    f'{Font.italic}({",".join(title_1.languages) + ")":<30}{Font.end} [{title_1.short_name}] {title_1.full_name}',
                                                    f'{Font.italic}({",".join(title_2.languages) + ")":<30}{Font.end}{Font.disabled} [{title_2.short_name}] {title_2.full_name}{Font.end}',
                                                ],
                                                keep_remove=True,
                                            )

                                        remove_titles.add(title_2)
                                        language_found = True
                                        break
                                elif re.search(
                                    language, ','.join(title_2.languages)
                                ) and not re.search(language, ','.join(title_1.languages)):
                                    if title_1 in title_set:
                                        if report_on_match:
                                            TraceTools.trace_title(
                                                'REF0098',
                                                [', '.join(list(fallback_language_order))],
                                            )
                                            TraceTools.trace_title(
                                                '',
                                                [
                                                    f'{Font.italic}({",".join(title_2.languages) + ")":<30}{Font.end} [{title_2.short_name}] {title_2.full_name}',
                                                    f'{Font.italic}({",".join(title_1.languages) + ")":<30}{Font.end}{Font.disabled} [{title_1.short_name}] {title_1.full_name}{Font.end}',
                                                ],
                                                keep_remove=True,
                                            )

                                        remove_titles.add(title_1)
                                        language_found = True
                                        break

                if not language_found:
                    if not (title_1.is_superset or title_2.is_superset):
                        # Cycle through implied languages from the default region order as the second fallback
                        implied_languages: list[str] = [
                            x[0] for x in config.languages_implied.values()
                        ]

                        # Make sure language entries are unique
                        implied_languages = reduce(
                            lambda x, y: [*x, y] if y not in x else x, implied_languages, []
                        )
                        for language in implied_languages:
                            if re.search(language, ','.join(title_1.languages)) and not re.search(
                                language, ','.join(title_2.languages)
                            ):
                                if title_2 in title_set:
                                    if report_on_match:
                                        TraceTools.trace_title(
                                            'REF0083', [', '.join(implied_languages)]
                                        )
                                        TraceTools.trace_title(
                                            '',
                                            [
                                                f'{Font.italic}({",".join(title_1.languages) + ")":<30}{Font.end} [{title_1.short_name}] {title_1.full_name}',
                                                f'{Font.italic}({",".join(title_2.languages) + ")":<30}{Font.end}{Font.disabled} [{title_2.short_name}] {title_2.full_name}{Font.end}',
                                            ],
                                            keep_remove=True,
                                        )

                                    remove_titles.add(title_2)
                                    language_found = True
                                    break
                            elif re.search(language, ','.join(title_2.languages)) and not re.search(
                                language, ','.join(title_1.languages)
                            ):
                                if title_1 in title_set:
                                    if report_on_match:
                                        TraceTools.trace_title(
                                            'REF0084', [', '.join(list(implied_languages))]
                                        )
                                        TraceTools.trace_title(
                                            '',
                                            [
                                                f'{Font.italic}({",".join(title_2.languages) + ")":<30}{Font.end} [{title_2.short_name}] {title_2.full_name}',
                                                f'{Font.italic}({",".join(title_1.languages) + ")":<30}{Font.end}{Font.disabled} [{title_1.short_name}] {title_1.full_name}{Font.end}',
                                            ],
                                            keep_remove=True,
                                        )

                                    remove_titles.add(title_1)
                                    language_found = True
                                    break

                if not language_found:
                    if not (title_1.is_superset or title_2.is_superset):
                        # Choose the title with more languages as the third fallback
                        if len(title_1.languages) > len(title_2.languages):
                            if report_on_match:
                                TraceTools.trace_title(
                                    'REF0081',
                                    [title_1.full_name, title_2.full_name],
                                    set(),
                                    keep_remove=True,
                                )

                            if title_2 in title_set:
                                remove_titles.add(title_2)
                                language_found = True
                                break
                        elif len(title_2.languages) > len(title_1.languages):
                            if report_on_match:
                                TraceTools.trace_title(
                                    'REF0082',
                                    [title_2.full_name, title_1.full_name],
                                    set(),
                                    keep_remove=True,
                                )

                            if title_1 in title_set:
                                remove_titles.add(title_1)
                                language_found = True
                                break

                if language_found:
                    continue

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_language_top(
        title_set: set[DatNode],
        short_name_top_languages: set[tuple[str, int, str]],
        group_name: str,
        report_on_match: bool,
    ) -> set[DatNode]:
        """
        Checks a set of DatNodes for which titles support the top language in a
        group, split by short name.

        Args:
            title_set (set[DatNode]): A set of titles as DatNode instances.

            short_name_top_languages (set[tuple[str, int, str]]): The top
            languages for each title in a group split by short name, in the
            format `{short name, language priority, language code regex}`.

            For example, with a language priority of En > Ja:

            `{('title 1 (disc 1)', 1, 'Ja'), ('title 1 (disc 2)', 1, 'Ja'),
            ('title 1 - special edition', 0, 'En(?:-[A-Z][A-Z])?')}`.

            group_name (str): The name of the group being processed, only used
            as part of a trace.

            report_on_match (bool): Whether Retool needs to report any titles
            being traced.

        Returns:
            set[DatNode]: A set of DatNodes that contain titles that only
            support the top language for a group, split by short name. If
            there's only one title in the set and it doesn't support the top
            language, it isn't removed.
        """
        if report_on_match:
            TraceTools.trace_title('REF0015', [group_name], keep_remove=False)
            eprint('Highest language priority per short name:')

        language_keep: set[DatNode] = set()
        language_remove: set[DatNode] = set()

        remove_titles: set[DatNode] = set()

        for short_name_top_language in short_name_top_languages:

            if report_on_match:
                eprint(
                    f'* {short_name_top_language[0]} | ({short_name_top_language[1]}) {short_name_top_language[2]}'
                )

            for title in title_set:
                if title.short_name == short_name_top_language[0]:
                    # Remove titles that don't match the top language, but don't let the last title in the set be removed
                    if (
                        not re.search(short_name_top_language[2], ''.join(title.languages))
                        and len(title_set) != 1
                        and title not in language_keep
                    ):
                        remove_titles.add(title)

                        if report_on_match:
                            language_remove.add(title)
                    else:
                        if report_on_match:
                            language_keep.add(title)

        if report_on_match:
            eprint('\nTitles that match the highest language priority:')
            for keep in sorted(language_keep, key=lambda x: x.short_name):
                eprint(
                    f'+ Keeping: {Font.italic}({",".join(keep.languages) + ")":<30}{Font.end} [{keep.short_name}] {keep.full_name}'
                )
            for remove in sorted(language_remove, key=lambda x: x.short_name):
                eprint(
                    f'{Font.disabled}- Removing: {Font.italic}({",".join(remove.languages) + ")":<30}[{remove.short_name}] {Font.disabled}{remove.full_name}{Font.end}'
                )

            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
            input()

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_highest_string(title_set: set[DatNode], report_on_match: bool) -> set[DatNode]:
        """
        Compares any two titles from a set of DatNodes, and selects the title with the
        longest name. Should only ever be used as a fail-safe tiebreaker.

        Args:
            title_set (set[DatNode]): A set of titles as DatNode instances.

            report_on_match (bool): Whether Retool needs to report any titles being
            traced.

        Returns:
            set[DatNode]: A set of DatNodes that contain titles only with the longest
            name.
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
                if title_1.full_name < title_2.full_name:
                    if report_on_match:
                        TraceTools.trace_title(
                            'REF0057', [title_2.full_name, title_1.full_name], keep_remove=True
                        )

                    remove_titles.add(title_1)
                elif title_2.full_name < title_1.full_name:
                    if report_on_match:
                        TraceTools.trace_title(
                            'REF0058', [title_1.full_name, title_2.full_name], keep_remove=True
                        )

                    remove_titles.add(title_2)

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_made_in(
        pattern: Pattern[str], title_set: set[DatNode], report_on_match: bool
    ) -> set[DatNode]:
        """
        Compares any two titles from a set of DatNodes, and removes the title that contains `pattern`.

        Args:
            pattern (Pattern[str]): The "made in" regex pattern.

            title_set (set[DatNode]): A set of titles as DatNode instances.

            report_on_match (bool): Whether Retool needs to report any titles being
            traced.

        Returns:
            set[DatNode]: A set of DatNodes that contain titles that don't match the
            `pattern`.
        """
        remove_titles: set[DatNode] = set()

        for title_1, title_2 in itertools.combinations(title_set, 2):

            regex_search_str_1 = pattern2string(pattern, title_1.full_name)
            regex_search_str_2 = pattern2string(pattern, title_2.full_name)

            if re.search(pattern, title_1.full_name) and re.search(pattern, title_2.full_name):
                if title_1.primary_region in regex_search_str_1.replace('.', '').replace(
                    'EU', 'Europe'
                ) and title_1.primary_region not in regex_search_str_2.replace('.', '').replace(
                    'EU', 'Europe'
                ):
                    if title_2 in title_set:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0036',
                                [
                                    f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}',
                                    f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_titles.add(title_2)
                if title_2.primary_region in regex_search_str_2.replace('.', '').replace(
                    'EU', 'Europe'
                ) and title_2.primary_region not in regex_search_str_1.replace('.', '').replace(
                    'EU', 'Europe'
                ):
                    if title_1 in title_set:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0037',
                                [
                                    f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}',
                                    f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_titles.add(title_1)

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_multi_regions(
        title_set: set[DatNode],
        user_region_order: list[str],
        world_is_usa_europe_japan: bool,
        report_on_match: bool,
    ) -> set[DatNode]:
        """
        Compares any two titles from a set of DatNodes against the user region order.
        Preferences titles with more regions and that are higher up the region priority.

        Args:
            title_set (set[DatNode]): A set of titles as DatNode instances.

            user_region_order (list[str]): The region order as defined by the user.

            world_is_usa_europe_japan (bool): Whether to treat World as an equivalent
            region to USA, Europe, and Japan.

            report_on_match (bool): Whether Retool needs to report any titles being
            traced.

        Returns:
            set[DatNode]: A set of DatNodes filtered by region priority.
        """
        remove_titles: set[DatNode] = set()

        for title_1, title_2 in itertools.combinations(title_set, 2):
            if (
                title_1.short_name == title_2.short_name
                and title_1 in title_set
                and title_2 in title_set
            ):
                if world_is_usa_europe_japan:
                    if (
                        (title_1.primary_region == 'World' and 'USA' in title_2.regions)
                        or ('USA' in title_1.regions and title_2.primary_region == 'World')
                        or (title_1.primary_region == 'World' and 'Europe' in title_2.regions)
                        or ('Europe' in title_1.regions and title_2.primary_region == 'World')
                        or (title_1.primary_region == 'World' and 'Japan' in title_2.regions)
                        or ('Japan' in title_1.regions and title_2.primary_region == 'World')
                    ):
                        continue

                # An exception for compilation titles -- we only want to check the
                # primary region if a compilation is being compared against an
                # individual title
                if (title_1.contains_titles and not title_2.contains_titles) or (
                    title_2.contains_titles and not title_1.contains_titles
                ):
                    if title_1.region_priority < title_2.region_priority:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0094',
                                [
                                    f'({title_1.region_priority}) {title_1.full_name}',
                                    f'({title_2.region_priority}) {title_2.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_titles.add(title_2)

                    if title_2.region_priority < title_1.region_priority:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0095',
                                [
                                    f'({title_2.region_priority}) {title_2.full_name}',
                                    f'({title_1.region_priority}) {title_1.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_titles.add(title_1)
                else:
                    for region in user_region_order:
                        if region in title_1.regions and region not in title_2.regions:
                            if title_2 in title_set:
                                if report_on_match:
                                    TraceTools.trace_title(
                                        'REF0030',
                                        [
                                            f'({", ".join(title_1.regions)}) {title_1.full_name}',
                                            f'({", ".join(title_2.regions)}) {title_2.full_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )

                                remove_titles.add(title_2)
                                break
                        elif region in title_2.regions and region not in title_1.regions:
                            if title_1 in title_set:
                                if report_on_match:
                                    TraceTools.trace_title(
                                        'REF0031',
                                        [
                                            f'({", ".join(title_2.regions)}) {title_2.full_name}',
                                            f'({", ".join(title_1.regions)}) {title_1.full_name}{Font.end}',
                                        ],
                                        keep_remove=True,
                                    )

                                remove_titles.add(title_1)
                                break

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_string(
        match: Pattern[str] | str,
        title_set: set[DatNode],
        report_on_match: bool,
        choose_title_with_string: bool,
    ) -> set[DatNode]:
        """
        Compares any two titles from a set of DatNodes for a string. Can choose the
        title with or without the string.

        Args:
            match (Pattern[str]|str): The regex pattern or string to search for in the
            title name.

            title_set (set[DatNode]): A set of titles as DatNode instances.

            report_on_match (bool): Whether Retool needs to report any titles being
            traced.

            choose_title_with_string (bool): If `True`, chooses the title that contains
            `string`. If `False`, chooses the title that doesn't contain `string`.

        Returns:
            set[DatNode]: A set of DatNodes that either does or doesn't contain the
            specified `pattern`.
        """
        remove_titles: set[DatNode] = set()

        remove_title: DatNode

        for title_1, title_2 in itertools.combinations(title_set, 2):
            if (
                title_1.short_name == title_2.short_name
                and title_1 in title_set
                and title_2 in title_set
                and 'BIOS' not in title_1.categories
                and 'BIOS' not in title_2.categories
            ):
                title_1_match: bool = False
                title_2_match: bool = False

                if type(match) is re.Pattern:
                    if re.search(match, title_1.full_name) and not re.search(
                        match, title_2.full_name
                    ):
                        title_1_match = True

                    if re.search(match, title_2.full_name) and not re.search(
                        match, title_1.full_name
                    ):
                        title_2_match = True

                elif isinstance(match, str):
                    if match in title_1.tags and match not in title_2.tags:
                        title_1_match = True
                    elif match in title_2.tags and match not in title_1.tags:
                        title_2_match = True

                regex_string: str = (
                    str(match).replace('re.compile(', '').replace(', re.IGNORECASE)', '')
                )
                regex_string = re.sub('\'\\)$', '\'', regex_string)

                if title_1_match and not title_2_match:
                    if choose_title_with_string:
                        if report_on_match:

                            TraceTools.trace_title(
                                'REF0032',
                                [
                                    f'{Font.subheading_bold}{regex_string}{Font.end} {title_1.full_name}',
                                    f'{Font.subheading_bold}{regex_string}{Font.disabled} {title_2.full_name}{Font.end}',
                                ],
                                keep_remove=True,
                            )

                        remove_title = title_2
                    else:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0033',
                                [
                                    f'{Font.subheading_bold}{regex_string}{Font.end} {title_2.full_name}',
                                    f'{Font.subheading_bold}{regex_string}{Font.disabled} {title_1.full_name}',
                                ],
                                keep_remove=True,
                            )

                        remove_title = title_1

                    if remove_title in title_set:
                        remove_titles.add(remove_title)
                elif title_2_match and not title_1_match:
                    if choose_title_with_string:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0034',
                                [
                                    f'{Font.subheading_bold}{regex_string}{Font.end} {title_2.full_name}',
                                    f'{Font.subheading_bold}{regex_string}{Font.disabled} {title_1.full_name}',
                                ],
                                keep_remove=True,
                            )

                        remove_title = title_1
                    else:
                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0035',
                                [
                                    f'{Font.subheading_bold}{regex_string}{Font.end} {title_1.full_name}',
                                    f'{Font.subheading_bold}{regex_string}{Font.disabled} {title_2.full_name}',
                                ],
                                keep_remove=True,
                            )

                        remove_title = title_2

                    if remove_title in title_set:
                        remove_titles.add(remove_title)

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_superset(title_set: set[DatNode], report_on_match: bool) -> set[DatNode]:
        """
        Compares any two titles from a set of DatNodes, and if one is a superset,
        chooses it.

        Args:
            title_set (set[DatNode]): A set of titles as DatNode instances.

            report_on_match (bool): Whether Retool needs to report any titles being
            traced.

        Returns:
            set[DatNode]: A set of DatNodes where supersets get chosen over normal
            titles. If neither title is a superset, both titles are kept.
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
                if title_1.is_superset and not title_2.is_superset:
                    if title_1 in title_set:
                        remove_titles.add(title_2)

                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0077',
                                [f'{title_1.full_name}', f'{title_2.full_name}{Font.end}'],
                                keep_remove=True,
                            )

                        continue

                if title_2.is_superset and not title_1.is_superset:
                    if title_2 in title_set:
                        remove_titles.add(title_1)

                        if report_on_match:
                            TraceTools.trace_title(
                                'REF0078',
                                [f'{title_2.full_name}', f'{title_1.full_name}{Font.end}'],
                                keep_remove=True,
                            )

                        continue

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
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
            title_1_name_normalized: str = re.sub(
                ' Version ((\\d\\.?)+)', ' (v\\1)', title_1.full_name
            )
            title_2_name_normalized: str = re.sub(
                ' Version ((\\d\\.?)+)', ' (v\\1)', title_2.full_name
            )
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
                if re.search(pattern, title_1_name_normalized) and not re.search(
                    pattern, title_2_name_normalized
                ):
                    if pattern in config.regex.preproduction:
                        if title_1 in title_set:
                            if report_on_match:
                                TraceTools.trace_title(
                                    'REF0038',
                                    [
                                        f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}',
                                        f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}{Font.end}',
                                    ],
                                    keep_remove=True,
                                )

                            remove_titles.add(title_1)
                    else:
                        if title_2 in title_set:
                            if report_on_match:
                                TraceTools.trace_title(
                                    'REF0064',
                                    [
                                        f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}',
                                        f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}{Font.end}',
                                    ],
                                    keep_remove=True,
                                )

                            remove_titles.add(title_2)
                elif re.search(pattern, title_2_name_normalized) and not re.search(
                    pattern, title_1_name_normalized
                ):
                    if pattern in config.regex.preproduction:
                        if title_2 in title_set:
                            if report_on_match:
                                TraceTools.trace_title(
                                    'REF0039',
                                    [
                                        f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}',
                                        f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}{Font.end}',
                                    ],
                                    keep_remove=True,
                                )

                            remove_titles.add(title_2)

                    else:
                        if title_1 in title_set:
                            if report_on_match:
                                TraceTools.trace_title(
                                    'REF0065',
                                    [
                                        f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}',
                                        f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}{Font.end}',
                                    ],
                                    keep_remove=True,
                                )

                            remove_titles.add(title_1)
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
                                itertools.zip_longest(
                                    ver_1_normalized, ver_2_normalized, fillvalue=[0]
                                )
                            )

                            # Convert tuples to list
                            for version_pairs in version_compare_zip:
                                version_compare_normalize.append(list(version_pairs))

                            # Equalize the list lengths
                            for version_pairs_normalized in version_compare_normalize:
                                shorter: int
                                longer: int

                                if len(version_pairs_normalized[0]) != len(
                                    version_pairs_normalized[1]
                                ):
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
                            title_1_ver = str(
                                max([int(i) for i in re.findall('\\d+', title_1_ver)])
                            )
                            title_2_ver = str(
                                max([int(i) for i in re.findall('\\d+', title_2_ver)])
                            )
                        elif re.search('\\d+', title_1_ver) and not re.search('\\d+', title_2_ver):
                            title_1_ver = '1'
                            title_2_ver = '0'
                        elif re.search('\\d+', title_2_ver) and not re.search('\\d+', title_1_ver):
                            title_1_ver = '0'
                            title_2_ver = '1'

                    # Preprocess double versions that turn up in 3DS (Digital), Commodore Amiga, PS3 (Digital) (Content),
                    # and IBM - PC and Compatibles (Flux)
                    title_1_ver = (
                        title_1_ver.replace('PS3 ', '').replace('-to-', ', ').replace(' - AGI', ',')
                    )
                    title_2_ver = (
                        title_2_ver.replace('PS3 ', '').replace('-to-', ', ').replace('- AGI', ',')
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

                        title_1_ver = '.'.join([i[0][0] for i in primary_version_zip])
                        title_2_ver = '.'.join([i[1][0] for i in primary_version_zip])

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
                    version_compare_normalize: list[Any] = process_versions(
                        title_1_ver, title_2_ver
                    )

                    # Compare the normalized versions
                    for subversion in version_compare_normalize:
                        try:
                            if subversion[0] < subversion[1]:
                                if title_1 in title_set:
                                    if report_on_match:
                                        TraceTools.trace_title(
                                            'REF0041',
                                            [
                                                f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}',
                                                f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}{Font.end}',
                                            ],
                                            keep_remove=True,
                                        )

                                    remove_titles.add(title_1)
                                break

                            if subversion[1] < subversion[0]:
                                if title_2 in title_set:
                                    if report_on_match:
                                        TraceTools.trace_title(
                                            'REF0040',
                                            [
                                                f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}',
                                                f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}{Font.end}',
                                            ],
                                            keep_remove=True,
                                        )

                                    remove_titles.add(title_2)
                                break
                        except Exception:
                            # If there's a combination string and int, convert the int as a fallback.
                            # This might result in the wrong version being chosen.
                            if str(subversion[0]) < str(subversion[1]):
                                if title_1 in title_set:
                                    if report_on_match:
                                        TraceTools.trace_title(
                                            'REF0041',
                                            [
                                                f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}',
                                                f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}{Font.end}',
                                            ],
                                            keep_remove=True,
                                        )

                                    remove_titles.add(title_1)
                                break

                            if str(subversion[1]) < str(subversion[0]):
                                if title_2 in title_set:
                                    if report_on_match:
                                        TraceTools.trace_title(
                                            'REF0040',
                                            [
                                                f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_1.full_name}',
                                                f'({str(pattern).replace("re.compile(", "").replace(", re.IGNORECASE)", "")}) {title_2.full_name}{Font.end}',
                                            ],
                                            keep_remove=True,
                                        )

                                    remove_titles.add(title_2)
                                break

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_video_standard(
        standard: str, title_set: set[DatNode], config: Config, report_on_match: bool
    ) -> set[DatNode]:
        """
        Compares any two titles from a set of DatNodes to see which one has the
        highest priority video standard.

        Args:
            standard (str): The video standard. MPAL, NTSC, PAL, PAL 60Hz, SECAM

            title_set (set[DatNode]): A set of titles as DatNode instances.

            config (Config): The Retool config object.

            report_on_match (bool): Whether Retool needs to report any titles being
            traced.

        Returns:
            set[DatNode]: A set of DatNodes filtered by video standard.
        """
        standard = standard.replace(' ', '_')

        for pattern in config.regex[standard]:
            title_set = ParentTools.choose_string(
                pattern, title_set, report_on_match, choose_title_with_string=True
            )

        return title_set

    @staticmethod
    def detect_parent_clone_clash(
        processed_titles: dict[str, set[DatNode]], config: Config
    ) -> dict[str, set[DatNode]]:
        """
        Makes sure a title isn't assigned as both a parent and a clone. This can only
        happen when exporting a DAT in legacy mode.

        This is usually caused by duplicate entries in a clone list.

        The solution is simple: if any title is marked as a parent, but happens to also
        marked as a clone, remove its clone status.

        Args:
            processed_titles (dict[str, set[DatNode]]): A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.

            config (Config): The Retool config object.

        Returns:
            dict[str, set[DatNode]]: A dictionary of DatNodes that have had parent/clone
            errors corrected.
        """
        parent_clash: dict[str, Any] = {}

        # Find all parent titles
        for titles in processed_titles.values():
            for title in titles:
                if title.cloneof:
                    if title.cloneof not in parent_clash:
                        parent_clash[title.cloneof] = {'clones': set(), 'assigned_clone': ''}

        # Find if parent titles are set as clones
        for titles in processed_titles.values():
            for title in titles:
                if title.full_name in parent_clash and title.cloneof:
                    parent_clash[title.full_name]['assigned_clone'] = title.cloneof

                    title.cloneof = ''

        # Find the titles that have set the parents as clones
        for key in parent_clash.keys():
            for titles in processed_titles.values():
                for title in titles:
                    if parent_clash[key]['assigned_clone']:
                        if title.cloneof == key:
                            parent_clash[key]['clones'].add(title.full_name)

        if config.user_input.verbose:
            for key, values in parent_clash.items():
                if values['assigned_clone']:
                    eprint(
                        f'\n{Font.warning}* {Font.warning_bold}{key}{Font.warning} should be a parent, but is set as a clone of\n  {Font.warning_bold}{values["assigned_clone"]}{Font.warning}{Font.end}'
                    )
                    eprint(
                        f'\n  {Font.warning}Sometimes this can happen because there\'s a duplicate entry in the clone list.\n  Other times it\'s just a side effect of region and language settings.{Font.end}'
                    )

                if values['clones']:
                    eprint(
                        f'\n  {Font.warning}Titles that have {Font.warning_bold}{key}{Font.warning} as a parent:{Font.end}\n'
                    )

                    for value in values['clones']:
                        eprint(f'    {Font.disabled}- {value}{Font.end}')

                if values['assigned_clone']:
                    eprint(
                        f'\n  {Font.warning}Removing clone from {Font.warning_bold}{key}{Font.end}\n'
                    )

        return processed_titles

    @staticmethod
    def remove_preprod_bad(title_set: set[DatNode], config: Config) -> set[DatNode]:
        """
        Compares any two titles from a set of DatNodes to see if one is
        preproduction/bad/pirate, and the other is not. Also cleans up mixed
        version/revision titles in groups.

        Args:
            title_set (set[DatNode]): A set of titles as DatNode instances.

            config (Config): The Retool config object.

        Returns:
            set[DatNode]: A set of DatNodes with preproduction and bad titles
            removed, if a better title exists to take their place.
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
                # Deal with preproduction and bad titles
                title_1_check: bool = False
                title_2_check: bool = False

                pattern_list: list[Pattern[str]] = list(config.regex.preproduction)
                pattern_list.append(config.regex.bad)
                pattern_list.append(config.regex.pirate)

                for regex_pattern in pattern_list:
                    if re.search(regex_pattern, title_1.full_name) and not re.search(
                        regex_pattern, title_2.full_name
                    ):
                        title_1_check = True
                    if re.search(regex_pattern, title_2.full_name) and not re.search(
                        regex_pattern, title_1.full_name
                    ):
                        title_2_check = True

                if title_1_check and not title_2_check:
                    if title_1 in title_set:
                        remove_titles.add(title_1)
                        continue

                if title_2_check and not title_1_check:
                    if title_2 in title_set:
                        remove_titles.add(title_2)
                        continue

                # Deal with mixed versions and revisions
                if re.search(config.regex.revision, title_1.full_name) and re.search(
                    config.regex.version, title_2.full_name
                ):
                    if title_1 in title_set:
                        remove_titles.add(title_1)
                elif re.search(config.regex.revision, title_2.full_name) and re.search(
                    config.regex.version, title_1.full_name
                ):
                    if title_2 in title_set:
                        remove_titles.add(title_2)

        for title in remove_titles:
            if title in title_set:
                title_set.remove(title)

        return title_set

    @staticmethod
    def choose_parent(
        processed_titles: dict[str, set[DatNode]], config: Config
    ) -> dict[str, set[DatNode]]:
        """
        Sets up parent selection using either single or multiprocessor, then executes
        parent selection in one of those modes.

        Args:
            processed_titles (dict[str, set[DatNode]]): A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.

            config (Config): The Retool config object.

        Returns:
            dict[str, set[DatNode]]: A dictionary of DatNodes with 1G1R processing
            complete.
        """
        # Don't enable the progress bar if the user is doing a trace
        if config.user_input.trace or config.user_input.single_cpu:
            alive_bar_context = nullcontext()
            eprint('* Selecting 1G1R titles...')
        else:
            progress_bar: str = 'smooth'
            spinner: str = 'waves'
            parent_processes: list[str] = [
                str(x).lower() for x in psutil.Process(os.getpid()).parents()
            ]

            if any(
                s
                for s in parent_processes
                if 'cmd.exe' in s or 'powershell.exe' in s or 'explorer.exe' in s
            ):
                if not any(
                    s for s in parent_processes if 'code.exe' in s or 'windowsterminal.exe' in s
                ):
                    progress_bar = 'classic2'
                    spinner = 'classic'

            alive_bar_context = alive_bar(
                4,
                title='* Selecting 1G1R titles',
                length=20,
                enrich_print=False,
                stats=False,
                bar=progress_bar,
                spinner=spinner,
                file=sys.stderr,
            )

        with alive_bar_context as bar:
            # Take supersets and compilations out, as they mess up multiprocessing with
            # non-deterministic results.
            superset_processed_titles: dict[str, set[DatNode]] = {}
            compilations: set[DatNode] = set()

            for group, titles in processed_titles.items():
                for title in titles:
                    if title.is_superset:
                        superset_processed_titles[group] = deepcopy(processed_titles[group])
                    if title.contains_titles:
                        compilations.add(title)

            for group in superset_processed_titles.keys():
                if group in processed_titles:
                    del processed_titles[group]

            for compilation_title in compilations:
                if compilation_title.group_name in processed_titles:
                    if compilation_title in processed_titles[compilation_title.group_name]:
                        processed_titles[compilation_title.group_name].remove(compilation_title)

                if not processed_titles[compilation_title.group_name]:
                    del processed_titles[compilation_title.group_name]

            if not (config.user_input.trace or config.user_input.single_cpu):
                bar()  # type: ignore

            # Define choose_parent_process as the function to run on multiple processors,
            # and use a partial to prepush arg values into it as a sort of prepackaged
            # function so we can use it in a map later.
            #
            # You can't set a kwarg name on a partial or the multiprocessing breaks, so
            # only the values for is_superset_titles and is_compilations are passed in.
            func = partial(ParentTools.choose_parent_process, config, {}, False, False)

            # Need to use an iterable, not a dictionary for multiprocessing
            parent_titles: list[dict[str, set[DatNode]]] = []

            if config.user_input.trace or config.user_input.single_cpu:
                parent_titles = list(map(func, processed_titles.values()))
            else:
                with InterruptiblePool(int(str(os.cpu_count()))) as p:
                    parent_titles = p.map(func, processed_titles.values())

            if not (config.user_input.trace or config.user_input.single_cpu):
                bar()  # type: ignore

            # Now process superset groups
            potential_parents: dict[str, set[DatNode]] = {}

            func = partial(
                ParentTools.choose_parent_process, config, potential_parents, True, False
            )

            superset_parent_titles = list(map(func, superset_processed_titles.values()))

            if not (config.user_input.trace or config.user_input.single_cpu):
                bar()  # type: ignore

            # Get the set back into the required dictionary form
            temp_dict: dict[str, set[DatNode]] = {}

            for parent_title in parent_titles:
                for key, values in parent_title.items():
                    temp_dict[key] = values

            for superset_parent_title in superset_parent_titles:
                for key, values in superset_parent_title.items():
                    for value in values:
                        for clone_title, potential_parent_titles in potential_parents.items():
                            if value.full_name == clone_title:
                                # Reassign deterministic clones for superset titles
                                if len(potential_parent_titles) > 1:
                                    # Deal with superset parents first
                                    if next(
                                        (x for x in potential_parent_titles if x.is_superset), None
                                    ):
                                        value.cloneof = [
                                            x
                                            for x in sorted(
                                                potential_parent_titles,
                                                key=lambda x: (x.clonelist_priority, x.full_name),
                                                reverse=True,
                                            )
                                            if x.is_superset
                                        ][0].full_name
                                        break
                                    else:
                                        value.cloneof = [
                                            x
                                            for x in sorted(
                                                potential_parent_titles,
                                                key=lambda x: (x.clonelist_priority, x.full_name),
                                            )
                                            if not x.is_superset
                                        ][0].full_name
                                        break
                                else:
                                    value.cloneof = list(potential_parent_titles)[0].full_name
                                    break

                    temp_dict[key] = values

            processed_titles = temp_dict

            # Make sure supersets aren't set as both parent and clone throughout the DAT,
            # which can happen with some region combinations
            superset_clones: dict[str, str] = {}

            # Set up title tracking
            report_on_match: bool = False

            # Find if a superset title is set as a clone, and record its relationship
            for titles in processed_titles.values():
                for title in titles:
                    if title.is_superset and title.cloneof:
                        superset_clones[title.full_name] = title.cloneof

            # Switch any titles where the superset is a parent to the superset's clone
            for titles in processed_titles.values():
                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(titles, config.user_input.trace)

                for title in titles:
                    if title.cloneof in superset_clones:
                        if not title.is_superset:
                            old_cloneof: str = title.cloneof

                            title.cloneof = superset_clones[title.cloneof]

                            if report_on_match:
                                eprint('')
                                TraceTools.trace_title('REF0114')
                                eprint(f'* {title.full_name}')
                                eprint(
                                    f'  New clone: {title.cloneof}\n{Font.disabled}  Old clone: {old_cloneof}{Font.end}'
                                )
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()

            # Now process compilations
            processed_titles = ParentTools.choose_compilations(
                compilations, processed_titles, config
            )

            if not (config.user_input.trace or config.user_input.single_cpu):
                bar()  # type: ignore

        eprint('\033[F\033[K* Selecting 1G1R titles... done.\n', end='')

        return processed_titles

    @staticmethod
    def choose_parent_process(
        config: Config,
        potential_parents: dict[str, set[DatNode]],
        is_superset_titles: bool,
        is_compilations: bool,
        title_set: set[DatNode],
    ) -> dict[str, set[DatNode]]:
        """
        Determines a parent, given a dictionary of DatNode objects.

        Args:
            config (Config): The Retool config object.

            potential_parents (dict[str, set[DatNode]]): A dictionary of DatNodes that
            contains non-finalized parents. Only needed when processing supersets, as
            supersets need extra processing to make the parents deterministic.

            is_superset_titles (bool): Set to `True` if processing supersets.

            is_compilations (bool): Set to `True` if processing compilations.

            title_set (set[DatNode]): A list of DatNodes to choose a parent from.

        Returns:
            dict[str, set[DatNode]]: A dictionary of DatNodes with parents selected.
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
                region_order = [
                    str(x) for x in config.system_region_order_user if 'override' not in x
                ]

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
                eprint(
                    f'\n\n{Font.heading_bold}Stage: Superset parent selection\nGroup: {group_name}{Font.end}'
                )
            elif is_compilations:
                eprint(
                    f'\n\n{Font.heading_bold}Stage: Compilation parent selection\nGroup: {group_name}{Font.end}'
                )
            else:
                eprint(
                    f'\n\n{Font.heading_bold}Stage: Parent selection\nGroup: {group_name}{Font.end}'
                )

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
                if title.short_name == short_name and not re.search(
                    config.regex.bad, title.full_name
                ):
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
                    if title.short_name == short_name and re.search(
                        config.regex.bad, title.full_name
                    ):
                        if short_name not in short_name_titles:
                            short_name_titles[short_name] = []
                        if title not in short_name_titles[short_name]:
                            short_name_titles[short_name].append(title)

            for key, values in short_name_titles.items():
                short_name_groups.append((key, values))

        for short_name_group in short_name_groups:
            highest_language_priority = sorted(
                short_name_group[1], key=lambda i: i.language_priority
            )[0].language_priority

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

            short_name_top_languages.add(
                (short_name_group[0], highest_language_priority, top_language)
            )

        # Title comparisons per region
        for region in region_order:
            parent_titles: set[DatNode] = {x for x in title_set if region in x.primary_region}

            if parent_titles and len(parent_titles) > 1:
                if report_on_match:
                    eprint(f'\n{Font.subheading}Region: {region}{Font.end}')
                    TraceTools.trace_title(
                        'REF0001', [group_name], parent_titles, keep_remove=False
                    )

                # 1) Clean up preproduction/bad/pirate/mixed version-revision titles
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.remove_preprod_bad(parent_titles, config)

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0003', [group_name], parent_titles, keep_remove=False
                    )

                # 2) Cycle through language order until one title doesn't have the required language
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_language(
                        parent_titles, config, report_on_match
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0005', [group_name], parent_titles, keep_remove=False
                    )

                # 3) Select supersets
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_superset(parent_titles, report_on_match)

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0076', [group_name], parent_titles, keep_remove=False
                    )

                # 4) Reference clone list priorities
                if len(parent_titles) > 1:
                    parent_titles = CloneListTools.compare_priorities(
                        parent_titles, report_on_match
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0002', [group_name], parent_titles, keep_remove=False
                    )

                # 5) Handle modern titles like Virtual Console, Mini Console, and other
                # collections ripped from other platforms
                if len(parent_titles) > 1:
                    for edition in config.tags_modern_editions:
                        match_string: Any = ''

                        if edition[1] == 'regex':
                            match_string = re.compile(edition[0])
                        elif edition[1] == 'string':
                            match_string = edition[0]

                        if not config.user_input.modern:
                            parent_titles = ParentTools.choose_string(
                                match_string,
                                parent_titles,
                                report_on_match,
                                choose_title_with_string=False,
                            )
                        elif config.user_input.modern:
                            parent_titles = ParentTools.choose_string(
                                match_string,
                                parent_titles,
                                report_on_match,
                                choose_title_with_string=True,
                            )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0004', [group_name], parent_titles, keep_remove=False
                    )

                # 6) Prefer production versions over unlicensed/aftermarket
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.unlicensed,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.aftermarket,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0060', [group_name], parent_titles, keep_remove=False
                    )

                # 7) Select special editions
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.sega32x,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=True,
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.fmtowns_marty,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=True,
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0006', [group_name], parent_titles, keep_remove=False
                    )

                # 8) Check for versions and revisions, and select the highest of each
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.version, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.dreamcast_version, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.fmtowns_pippin_version, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.long_version, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.fds_version, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.hyperscan_version, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.nintendo_mastering_code, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.revision, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.beta, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.alpha, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.proto, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.sega_panasonic_ring_code,
                        parent_titles,
                        config,
                        report_on_match,
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.nec_mastering_code, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.ps_firmware, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.ps1_2_id, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.ps3_id, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.ps4_id, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.psp_id, parent_titles, config, report_on_match
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.psv_id, parent_titles, config, report_on_match
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0007', [group_name], parent_titles, keep_remove=False
                    )

                # 9 Choose video standard
                video_order: list[str] = config.video_order_user

                if config.system_video_order_user:
                    if {'override': 'true'} in config.system_video_order_user:
                        video_order = [
                            str(x) for x in config.system_video_order_user if 'override' not in x
                        ]

                if len(parent_titles) > 1:
                    for video_standard in video_order:
                        parent_titles = ParentTools.choose_video_standard(
                            video_standard.lower(), parent_titles, config, report_on_match
                        )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0096', [group_name], parent_titles, keep_remove=False
                    )

                # 10) Second language pass -- required to allow versions/revisions to be correctly selected
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_language(
                        parent_titles, config, report_on_match, first_time=False
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0043', [group_name], parent_titles, keep_remove=False
                    )

                # 11) Preference titles with more regions that are higher up the region priority
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_multi_regions(
                        parent_titles,
                        region_order,
                        world_is_usa_europe_japan=False,
                        report_on_match=report_on_match,
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0008', [group_name], parent_titles, keep_remove=False
                    )

                # 12) Choose original versions over alternatives
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.alt,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.oem,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.not_for_resale,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.covermount,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.rerelease,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=False,
                    )
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_string(
                        config.regex.edc,
                        parent_titles,
                        report_on_match,
                        choose_title_with_string=True,
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0010', [group_name], parent_titles, keep_remove=False
                    )

                # 13) Handle promotion and demotion editions
                if len(parent_titles) > 1:
                    for edition in config.tags_promote_editions:
                        match_string = ''

                        if edition[1] == 'regex':
                            match_string = re.compile(edition[0])
                        elif edition[1] == 'string':
                            match_string = edition[0]

                        parent_titles = ParentTools.choose_string(
                            match_string,
                            parent_titles,
                            report_on_match,
                            choose_title_with_string=True,
                        )

                    for edition in config.tags_demote_editions:
                        match_string = ''

                        if edition[1] == 'regex':
                            match_string = re.compile(edition[0])
                        elif edition[1] == 'string':
                            match_string = edition[0]

                        parent_titles = ParentTools.choose_string(
                            match_string,
                            parent_titles,
                            report_on_match,
                            choose_title_with_string=False,
                        )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0011', [group_name], parent_titles, keep_remove=False
                    )

                # 14) Choose dates
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_date(parent_titles, config, report_on_match)

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0009', [group_name], parent_titles, keep_remove=False
                    )

                # 15) Choose builds
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.build, parent_titles, config, report_on_match
                    )

                # 16) Handle "Made in" titles
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_made_in(
                        config.regex.madein, parent_titles, report_on_match
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0012', [group_name], parent_titles, keep_remove=False
                    )

                # 17) Another version check just in case multiple Alts are the only titles left
                if len(parent_titles) > 1:
                    parent_titles = ParentTools.choose_version_revision(
                        config.regex.alt, parent_titles, config, report_on_match
                    )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0061', [group_name], parent_titles, keep_remove=False
                    )

                # 18) As a fail-safe, do a string comparison. This compares character by character,and when
                # a title has a higher comparative character than another title, it wins.
                if not is_compilations:
                    if len(parent_titles) > 1:
                        parent_titles = ParentTools.choose_highest_string(
                            parent_titles, report_on_match
                        )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0059', [group_name], parent_titles, keep_remove=False
                    )

            elif len(parent_titles) == 1:
                if report_on_match:
                    eprint(f'\n{Font.subheading}Region: {region}{Font.end}')
                    TraceTools.trace_title(
                        'REF0074', [group_name], parent_titles, keep_remove=False
                    )

            # Add remaining titles from multiple regions to a single set
            cross_region_parent_titles = cross_region_parent_titles | parent_titles

        if report_on_match:
            eprint(f'\n{Font.subheading}Region: All{Font.end}')
            TraceTools.trace_title(
                'REF0013', [group_name], cross_region_parent_titles, keep_remove=False
            )

        if len(cross_region_parent_titles) > 1:
            # Remove titles that don't support the top language in the set
            if not config.user_input.region_bias:
                cross_region_parent_titles = ParentTools.choose_language_top(
                    cross_region_parent_titles,
                    short_name_top_languages,
                    group_name,
                    report_on_match,
                )

            # Prefer good dump/production/retail titles
            def production_retail(
                titles: set[DatNode], patterns: tuple[Pattern[str], ...], report_on_match: bool
            ):
                """
                Removes titles if they match a certain regex pattern, but only if
                    doing so wouldn't remove all titles in the set.

                Args:
                    titles (set[DatNode]): The titles to iterate over.

                    patterns (tuple[Pattern[str], ...]): The pattern to match against the
                    title full names.

                    report_on_match (bool): Whether Retool needs to report any titles
                    being traced.
                """
                cross_region_temp = titles.copy()

                for title_1, title_2 in itertools.combinations(cross_region_temp, 2):
                    if title_1.short_name == title_2.short_name:
                        pattern_1_found: bool = False
                        pattern_2_found: bool = False

                        patterns_found: list[str] = []

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
                cross_region_parent_titles.copy(), tuple(modern_edition_regex_tags), report_on_match
            )

            if config.user_input.demote_unl:
                cross_region_parent_titles = production_retail(
                    cross_region_parent_titles.copy(),
                    tuple(config.regex.unl_group),
                    report_on_match,
                )

            if report_on_match:
                TraceTools.trace_title(
                    'REF0119', [group_name], cross_region_parent_titles, keep_remove=False
                )

            # Remove titles with the same name in different regions
            cross_region_temp = cross_region_parent_titles.copy()

            for title_1, title_2 in itertools.combinations(cross_region_temp, 2):
                if (
                    title_1.short_name == title_2.short_name
                    and title_1 in cross_region_parent_titles
                    and title_2 in cross_region_parent_titles
                    and 'BIOS' not in title_1.categories
                    and 'BIOS' not in title_2.categories
                ):
                    if not config.user_input.region_bias:
                        # Leave supersets alone if the user doesn't specify region priority
                        if (not title_1.is_superset
                            and not title_2.is_superset):
                                if title_1.region_priority < title_2.region_priority:
                                    cross_region_parent_titles.remove(title_2)
                                elif title_2.region_priority < title_1.region_priority:
                                    cross_region_parent_titles.remove(title_1)
                    else:
                        # Supersets can be removed if the user does specify region priority,
                        # except for "World" supersets where USA, Europe, or Japan are involved
                        if title_1.region_priority < title_2.region_priority:
                            if not ((
                                title_1.primary_region == 'USA'
                                or title_1.primary_region == 'Europe'
                                or title_1.primary_region == 'Japan')
                                and title_2.primary_region == 'World'):
                                    cross_region_parent_titles.remove(title_2)
                        elif title_2.region_priority < title_1.region_priority:
                            if not ((
                                title_2.primary_region == 'USA'
                                or title_2.primary_region == 'Europe'
                                or title_2.primary_region == 'Japan')
                                and title_1.primary_region == 'World'):
                                    cross_region_parent_titles.remove(title_1)

            if report_on_match:
                TraceTools.trace_title(
                    'REF0014', [group_name], cross_region_parent_titles, keep_remove=False
                )

            # Choose supersets over titles
            cross_region_temp = set()

            if len(cross_region_parent_titles) > 1:
                cross_region_temp = cross_region_parent_titles.copy()

                for title_1, title_2 in itertools.combinations(cross_region_temp, 2):
                    if (
                        title_1.short_name == title_2.short_name
                        and title_1 in cross_region_parent_titles
                        and title_2 in cross_region_parent_titles
                        and 'BIOS' not in title_1.categories
                        and 'BIOS' not in title_2.categories
                    ):
                        if title_1.is_superset and not title_2.is_superset:
                            cross_region_parent_titles.remove(title_2)
                        elif title_2.is_superset and not title_1.is_superset:
                            cross_region_parent_titles.remove(title_1)

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0103', [group_name], cross_region_parent_titles, keep_remove=False
                    )

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
                        if title_1.short_name == title_2.short_name:
                            language_winner = ParentTools.choose_language(
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
                    TraceTools.trace_title(
                        'REF0104', [group_name], cross_region_parent_titles, keep_remove=False
                    )

            # Choose a title that has more regions, or higher priority regions
            if len(cross_region_parent_titles) > 1:
                cross_region_parent_titles = ParentTools.choose_multi_regions(
                    cross_region_parent_titles,
                    region_order,
                    world_is_usa_europe_japan=False,
                    report_on_match=report_on_match,
                )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0102', [group_name], cross_region_parent_titles, keep_remove=False
                    )

            # Choose a title that has more of the user's languages
            if len(cross_region_parent_titles) > 1:
                cross_region_parent_titles = ParentTools.choose_language(
                    cross_region_parent_titles, config, report_on_match
                )

                if report_on_match:
                    TraceTools.trace_title(
                        'REF0101', [group_name], cross_region_parent_titles, keep_remove=False
                    )

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
                        TraceTools.trace_title(
                            'REF0079', [group_name], superset_titles_final, keep_remove=False
                        )

                    # Integrate superset titles back into the main set
                    cross_region_parent_titles = {
                        title for title in cross_region_parent_titles if not title.is_superset
                    }

                    cross_region_temp = cross_region_parent_titles.copy()

                    superset_removes: set[DatNode] = set()

                    for title in cross_region_temp:
                        for superset_title in superset_titles_final:
                            if title.short_name == superset_title.short_name:
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
                TraceTools.trace_title(
                    'REF0018', [group_name], cross_region_parent_titles, keep_remove=False
                )

        # Assign clones
        if report_on_match:
            clone_report: dict[str, set[str]] = {}

        for cross_region_title in cross_region_parent_titles:
            for title in original_titles[group_name]:
                if (
                    title.full_name != cross_region_title.full_name
                    and title.short_name == cross_region_title.short_name
                    and 'BIOS' not in title.categories
                    and 'BIOS' not in cross_region_title.categories
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
            TraceTools.trace_title('REF0019', [group_name], keep_remove=False)

            for parent, clones in sorted(clone_report.items()):
                eprint(f'+ {Font.bold}{parent}{Font.end} is the 1G1R title{Font.end}')

                for clone in sorted(clones):
                    eprint(
                        f'- {Font.disabled}{Font.bold}{clone}{Font.end}{Font.disabled} is a clone of {Font.bold}{parent}{Font.end}'
                    )

                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                input()

        return processed_titles
