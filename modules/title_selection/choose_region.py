from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.dats import DatNode

from modules.titletools import TraceTools
from modules.utils import Font


def choose_region(
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
