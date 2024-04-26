from __future__ import annotations

import itertools
import re
from re import Pattern
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config import Config
    from modules.dats import DatNode


def choose_good(title_set: set[DatNode], config: Config) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes to see if one is
    preproduction/bad/pirate, and the other is not. If so, removes the
    preproduction/bad/pirate title. Also cleans up mixed version/revision titles.

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
