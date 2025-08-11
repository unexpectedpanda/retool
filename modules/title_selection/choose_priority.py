from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.titletools import TraceTools
from modules.utils import eprint


def choose_priority(title_set: set[DatNode], config: Config, report_on_match: bool) -> set[DatNode]:
    """
    Compare any two titles from a set of DatNodes, and select the one with the lowest
    priority number set in a clone list.

    Args:
        title_set (set[DatNode]): A set of titles as DatNode instances.

        config (Config): The Retool config object.

        report_on_match (bool): Whether Retool needs to report any titles being traced.

    Returns:
        set[DatNode]: A set of DatNodes filtered by clone list priority.
    """
    title_set_temp: set[DatNode] = title_set.copy()

    for title_1, title_2 in itertools.combinations(title_set_temp, 2):
        if (
            title_1.short_name == title_2.short_name
            and title_1 in title_set
            and title_2 in title_set
        ):
            if config.user_input.oldest:
                if title_1.is_oldest or title_2.is_oldest:
                    if title_1.is_oldest:
                        if report_on_match:
                            TraceTools.trace_title('REF0130')
                            eprint(
                                f'+ Keeping:  ((Oldest) {title_1.full_name}',
                                wrap=False,
                            )
                            eprint(
                                f'- Removing: {title_2.full_name}',
                                level='disabled',
                                wrap=False,
                                pause=True,
                            )

                        title_set.remove(title_2)
                    elif title_2.is_oldest:
                        if report_on_match:
                            TraceTools.trace_title('REF0131')
                            eprint(
                                f'+ Keeping:  ((Oldest) {title_2.full_name}',
                                wrap=False,
                            )
                            eprint(
                                f'- Removing: {title_1.full_name}',
                                level='disabled',
                                wrap=False,
                                pause=True,
                            )

                        title_set.remove(title_1)

                    continue

            if not (
                # Compare non-superset priority titles
                title_1.is_superset
                and title_2.is_superset
            ):
                if title_1.clonelist_priority < title_2.clonelist_priority:
                    if report_on_match:
                        TraceTools.trace_title('REF0020')
                        eprint(
                            f'+ Keeping:  ({title_1.clonelist_priority}) {title_1.full_name}',
                            wrap=False,
                        )
                        eprint(
                            f'- Removing: ({title_2.clonelist_priority}) {title_2.full_name}',
                            level='disabled',
                            wrap=False,
                            pause=True,
                        )

                    title_set.remove(title_2)
                elif title_2.clonelist_priority < title_1.clonelist_priority:
                    if report_on_match:
                        TraceTools.trace_title('REF0021')
                        eprint(
                            f'+ Keeping:  ({title_2.clonelist_priority}) {title_2.full_name}',
                            wrap=False,
                        )
                        eprint(
                            f'- Removing: ({title_1.clonelist_priority}) {title_1.full_name}',
                            level='disabled',
                            wrap=False,
                            pause=True,
                        )

                    title_set.remove(title_1)
            else:
                # Compare superset titles
                if title_1.clonelist_priority < title_2.clonelist_priority:
                    if report_on_match:
                        TraceTools.trace_title('REF0022')
                        eprint(
                            f'+ Keeping:  ({title_1.clonelist_priority}) {title_1.full_name}',
                            wrap=False,
                        )
                        eprint(
                            f'- Removing: ({title_2.clonelist_priority}) {title_2.full_name}',
                            level='disabled',
                            wrap=False,
                            pause=True,
                        )

                    title_set.remove(title_2)
                elif title_2.clonelist_priority < title_1.clonelist_priority:
                    if report_on_match:
                        TraceTools.trace_title('REF0023')
                        eprint(
                            f'+ Keeping:  ({title_2.clonelist_priority}) {title_2.full_name}',
                            wrap=False,
                        )
                        eprint(
                            f'- Removing: ({title_1.clonelist_priority}) {title_1.full_name}',
                            level='disabled',
                            wrap=False,
                            pause=True,
                        )

                    title_set.remove(title_1)

    return title_set
