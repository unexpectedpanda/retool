from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.titletools import TraceTools
from modules.utils import Font


def choose_superset(title_set: set[DatNode], config: Config, report_on_match: bool) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes, and if one is a superset, chooses it.

    Args:
        title_set (set[DatNode]): A set of titles as DatNode instances.

        config (Config): The Retool config object.

        report_on_match (bool): Whether Retool needs to report any titles being traced.

    Returns:
        set[DatNode]: A set of DatNodes where supersets get chosen over normal titles. If
        neither title is a superset, both titles are kept.
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

            keep_title_name: str = ''
            remove_title_name: str = ''

            if title_1.is_superset and not title_2.is_superset:
                if title_1 in title_set:
                    if config.user_input.oldest:
                        keep_title_name = title_2.full_name
                        remove_title_name = title_1.full_name

                        remove_titles.add(title_1)
                    else:
                        keep_title_name = title_1.full_name
                        remove_title_name = title_2.full_name

                        remove_titles.add(title_2)

                    if report_on_match and keep_title_name:
                        TraceTools.trace_title(
                            'REF0077',
                            [f'{keep_title_name}', f'{remove_title_name}{Font.end}'],
                            keep_remove=True,
                        )

                    continue

            if title_2.is_superset and not title_1.is_superset:
                if title_2 in title_set:
                    if config.user_input.oldest:
                        keep_title_name = title_1.full_name
                        remove_title_name = title_2.full_name

                        remove_titles.add(title_2)
                    else:
                        keep_title_name = title_2.full_name
                        remove_title_name = title_1.full_name

                        remove_titles.add(title_1)

                    if report_on_match:
                        TraceTools.trace_title(
                            'REF0078',
                            [f'{keep_title_name}', f'{remove_title_name}{Font.end}'],
                            keep_remove=True,
                        )

                    continue

    for title in remove_titles:
        if title in title_set:
            title_set.remove(title)

    return title_set
