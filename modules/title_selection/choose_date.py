from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config import Config
    from modules.dats import DatNode

from modules.titletools import TitleTools, TraceTools
from modules.utils import Font


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
