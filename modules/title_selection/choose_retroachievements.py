from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.dat.process_dat import DatNode

from modules.titletools import TitleTools, TraceTools
from modules.utils import Font


def choose_retroachievements(title_set: set[DatNode], report_on_match: bool) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes, and if one supports RetroAchievements,
    chooses it.

    Args:
        title_set (set[DatNode]): A set of titles as DatNode instances.

        report_on_match (bool): Whether Retool needs to report any titles being traced.

    Returns:
        set[DatNode]: A set of DatNodes where RetroAchievements get chosen over normal
        titles. If neither title supports RetroAchievements, both titles are kept.
    """
    remove_titles: set[DatNode] = set()

    for title_1, title_2 in itertools.combinations(title_set, 2):
        if TitleTools.check_title_equivalence(title_1, title_2, title_set):
            keep_title_name: str = ''
            remove_title_name: str = ''

            if title_1.is_retroachievement and not title_2.is_retroachievement:
                if title_1 in title_set:
                    keep_title_name = title_1.full_name
                    remove_title_name = title_2.full_name

                    remove_titles.add(title_2)

                    if report_on_match and keep_title_name:
                        TraceTools.trace_title(
                            'REF0137',
                            [f'{keep_title_name}', f'{remove_title_name}{Font.end}'],
                            keep_remove=True,
                        )

                    continue

            if title_2.is_retroachievement and not title_1.is_retroachievement:
                if title_2 in title_set:
                    keep_title_name = title_2.full_name
                    remove_title_name = title_1.full_name

                    remove_titles.add(title_1)

                    if report_on_match:
                        TraceTools.trace_title(
                            'REF0138',
                            [f'{keep_title_name}', f'{remove_title_name}{Font.end}'],
                            keep_remove=True,
                        )

                    continue

    for title in remove_titles:
        if title in title_set:
            title_set.remove(title)

    return title_set
