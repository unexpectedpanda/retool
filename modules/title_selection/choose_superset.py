from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.dats import DatNode

from modules.titletools import TraceTools
from modules.utils import Font


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
