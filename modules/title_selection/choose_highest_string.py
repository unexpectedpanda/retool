from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.dats import DatNode

from modules.titletools import TraceTools


def choose_highest_string(title_set: set[DatNode], report_on_match: bool) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes, and selects the title with the
    highest alphabetical name. Should only ever be used as a fail-safe tiebreaker.

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
