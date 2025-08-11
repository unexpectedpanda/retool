from __future__ import annotations

import itertools
import re
from re import Pattern
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.dat.process_dat import DatNode

from modules.titletools import TraceTools
from modules.utils import Font, pattern2string


def choose_made_in(
    pattern: Pattern[str], title_set: set[DatNode], report_on_match: bool
) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes, and removes the title that contains
    `pattern`.

    Args:
        pattern (Pattern[str]): The "made in" regex pattern.

        title_set (set[DatNode]): A set of titles as DatNode instances.

        report_on_match (bool): Whether Retool needs to report any titles being traced.

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
