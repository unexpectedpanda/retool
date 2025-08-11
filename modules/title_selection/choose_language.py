from __future__ import annotations

import itertools
import re
from functools import reduce
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.titletools import TraceTools
from modules.utils import Font, eprint


def choose_language(
    title_set: set[DatNode], config: Config, report_on_match: bool, first_time: bool = True
) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes, looking for languages based on the
    user language order.

    Args:
        title_set (set[DatNode]): A set of titles as DatNode instances.

        config (Config): The Retool config object.

        report_on_match (bool): Whether Retool needs to report any titles being traced.

        first_time (bool, optional): Whether this is the first time the `choose_language`
            function has been run. If `True`, the comparison stops at the first language
            match. If `False`, the language order is used to determine which is the more
            desired title.

            For example, if a user has a language order of En > Fr > De > Zh > and the
            following titles are passed in:

            • Title 1 (En,Fr,De)
            • Title 2 (En,Fr,Zh)

            With `first_time` set to `True`, both titles are selected, as Retool finds
            `En` in both titles and stops. When `first_time` is `False`, the comparison
            continues. Both have Fr, but only Title 1 has De, and so it is selected.
            If both titles contain all the desired languages, as a fallback the title
            with the most languages is selected. Defaults to `True`.

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
                            if re.search(language, ','.join(title_1.languages)) and not re.search(
                                language, ','.join(title_2.languages)
                            ):
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
                            elif re.search(language, ','.join(title_2.languages)) and not re.search(
                                language, ','.join(title_1.languages)
                            ):
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
                    implied_languages: list[str] = [x[0] for x in config.languages_implied.values()]

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


def choose_language_top(
    title_set: set[DatNode],
    short_name_top_languages: set[tuple[str, int, str]],
    report_on_match: bool,
) -> set[DatNode]:
    """
    Checks a set of DatNodes for which titles support the top language in a group, split
    by short name.

    Args:
        title_set (set[DatNode]): A set of titles as DatNode instances.

        short_name_top_languages (set[tuple[str, int, str]]): The top languages for each
            title in a group split by short name, in the format
            `{short name, language priority, language code regex}`.

            For example, with a language priority of En > Ja:

            {('title 1 (disc 1)', 1, 'Ja'), ('title 1 (disc 2)', 1, 'Ja'),
            ('title 1 - special edition', 0, 'En(?:-[A-Z][A-Z])?')}

        group_name (str): The name of the group being processed, only used as part of a
            trace.

        report_on_match (bool): Whether Retool needs to report any titles being traced.

    Returns:
        set[DatNode]: A set of DatNodes that contain titles that only support the top
        language for a group, split by short name. If there's only one title in the set
        and it doesn't support the top language, it isn't removed.
    """
    if report_on_match:
        TraceTools.trace_title('REF0015', [], keep_remove=False)
        eprint('Highest language priority per short name:\n')

    language_keep: set[DatNode] = set()
    language_remove: set[DatNode] = set()

    remove_titles: set[DatNode] = set()

    for short_name_top_language in short_name_top_languages:

        if report_on_match:
            eprint(
                f'• {short_name_top_language[0]} | ({short_name_top_language[1]}) {short_name_top_language[2]}',
                wrap=False,
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
        eprint('\nTitles that match the highest language priority:\n')
        for keep in sorted(language_keep, key=lambda x: x.short_name):
            eprint(
                f'+ Keeping: {Font.i}({",".join(keep.languages) + ")":<20}{Font.ie} [{keep.short_name}] {keep.full_name}',
                wrap=False,
            )
        for remove in sorted(language_remove, key=lambda x: x.short_name):
            eprint(
                f'- Removing: {Font.i}({",".join(remove.languages) + ")":<20}[{remove.short_name}] {Font.ie}{remove.full_name}',
                level='disabled',
                wrap=False,
            )

        eprint(pause=True)

    for title in remove_titles:
        if title in title_set:
            title_set.remove(title)

    return title_set
