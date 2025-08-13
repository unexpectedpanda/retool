from __future__ import annotations

import os
import sys
from contextlib import nullcontext
from copy import deepcopy
from functools import partial
from typing import TYPE_CHECKING

import psutil
from alive_progress import alive_bar

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.interruptible_pool import InterruptiblePool
from modules.title_selection.choose_1g1r import choose_1g1r
from modules.title_selection.choose_compilation import choose_compilation
from modules.titletools import TraceTools
from modules.utils import Font, eprint


def choose_1g1r_orchestrator(
    processed_titles: dict[str, set[DatNode]],
    quick_lookup: dict[str, dict[str, set[DatNode]]],
    config: Config,
    is_numbered: bool,
) -> dict[str, set[DatNode]]:
    """
    Sets up 1G1R selection using either single or multiprocessor, then executes 1G1R
    selection in one of those modes.

    Args:
        processed_titles (dict[str, set[DatNode]]): A work in progress dictionary of
            DatNodes, originally populated from the input DAT and actively being worked on
            by Retool.

        quick_lookup (dict[str, set[DatNode]]): A dictionary keyed by multiple title
            properties that enables quick lookup of titles. Due to the way Python
            references variables, changes made here are also reflected in
            `processed_titles`.

        config (Config): The Retool config object.

        is_numbered (bool): Whether the DAT file prefixes its title names with numbers.

    Returns:
        dict (dict[str, set[DatNode]]): A dictionary of DatNodes with 1G1R processing
        complete.
    """
    # Take supersets and compilations out, as they mess up multiprocessing with
    # non-deterministic results.
    superset_processed_titles: dict[str, set[DatNode]] = {}
    compilations: set[DatNode] = set()

    for group, titles in processed_titles.items():
        for title in titles:
            if title.is_superset:
                superset_processed_titles[group] = deepcopy(processed_titles[group])
            if title.contains_titles:
                compilations.add(title)

    for group in superset_processed_titles.keys():
        if group in processed_titles:
            del processed_titles[group]

    for compilation_title in compilations:
        if compilation_title.group_name in processed_titles:
            if compilation_title in processed_titles[compilation_title.group_name]:
                processed_titles[compilation_title.group_name].remove(compilation_title)

        if not processed_titles[compilation_title.group_name]:
            del processed_titles[compilation_title.group_name]

    # Don't enable the progress bar if the user is doing a trace
    if config.user_input.single_cpu:
        alive_bar_context = nullcontext()
        eprint('• Selecting 1G1R titles...')
    else:
        progress_bar: str = 'smooth'
        spinner: str = 'waves'
        parent_processes: list[str] = [
            str(x).lower() for x in psutil.Process(os.getpid()).parents()
        ]

        if any(
            s
            for s in parent_processes
            if 'cmd.exe' in s or 'powershell.exe' in s or 'explorer.exe' in s
        ):
            if not any(
                s for s in parent_processes if 'code.exe' in s or 'windowsterminal.exe' in s
            ):
                progress_bar = 'classic2'
                spinner = 'classic'

        alive_bar_context = alive_bar(
            total=len(processed_titles) + len(superset_processed_titles) + len(compilations),
            title='• Selecting 1G1R titles',
            length=20,
            enrich_print=False,
            stats=False,
            monitor='{percent:.2%}',
            receipt_text=True,
            bar=progress_bar,
            spinner=spinner,
            file=sys.stderr,
        )

    # Define choose_1g1r as the function to run on multiple processors,
    # and use a partial to prepush arg values into it as a sort of prepackaged
    # function so we can use it in a map later.
    #
    # You can't set a kwarg name on a partial or the multiprocessing breaks, so
    # only the values for is_superset_titles and is_compilations are passed in.
    func = partial(choose_1g1r, config, is_numbered, {}, False, False)

    # Need to use an iterable, not a dictionary for multiprocessing
    parent_titles: list[dict[str, set[DatNode]]] = []

    with alive_bar_context as bar:
        if config.user_input.single_cpu:
            parent_titles = list(map(func, processed_titles.values()))
        else:
            chunk_size: int = int(len(processed_titles) / config.cpu_count)
            chunk_size = chunk_size if chunk_size >= 1 else 1

            with InterruptiblePool(config.cpu_count) as p:
                for result in p.imap_unordered(
                    func, processed_titles.values(), chunksize=chunk_size
                ):
                    parent_titles.append(result)
                    if bar:
                        bar()

        # Now process superset groups on single processor
        potential_parents: dict[str, set[DatNode]] = {}

        func = partial(choose_1g1r, config, is_numbered, potential_parents, True, False)

        for _ in (superset_parent_titles := list(map(func, superset_processed_titles.values()))):
            if not config.user_input.single_cpu and bar:
                bar()

        # Get the set back into the required dictionary form
        temp_dict: dict[str, set[DatNode]] = {}

        for parent_title in parent_titles:
            for key, values in parent_title.items():
                temp_dict[key] = values

        for superset_parent_title in superset_parent_titles:
            for key, values in superset_parent_title.items():
                for value in values:
                    for clone_title, potential_parent_titles in potential_parents.items():
                        if value.full_name == clone_title:
                            # Reassign deterministic clones for superset titles
                            if len(potential_parent_titles) > 1:
                                # Deal with superset parents first
                                if next(
                                    (x for x in potential_parent_titles if x.is_superset), None
                                ):
                                    if is_numbered:
                                        value.cloneof = [
                                            x
                                            for x in sorted(
                                                potential_parent_titles,
                                                key=lambda x: (
                                                    x.clonelist_priority,
                                                    x.numbered_name,
                                                ),
                                                reverse=True,
                                            )
                                            if x.is_superset
                                        ][0].numbered_name
                                    else:
                                        value.cloneof = [
                                            x
                                            for x in sorted(
                                                potential_parent_titles,
                                                key=lambda x: (x.clonelist_priority, x.full_name),
                                                reverse=True,
                                            )
                                            if x.is_superset
                                        ][0].full_name
                                    break
                                else:
                                    if is_numbered:
                                        value.cloneof = [
                                            x
                                            for x in sorted(
                                                potential_parent_titles,
                                                key=lambda x: (
                                                    x.clonelist_priority,
                                                    x.numbered_name,
                                                ),
                                            )
                                            if not x.is_superset
                                        ][0].numbered_name
                                    else:
                                        value.cloneof = [
                                            x
                                            for x in sorted(
                                                potential_parent_titles,
                                                key=lambda x: (x.clonelist_priority, x.full_name),
                                            )
                                            if not x.is_superset
                                        ][0].full_name
                                    break
                            else:
                                if is_numbered:
                                    value.cloneof = list(potential_parent_titles)[0].numbered_name
                                else:
                                    value.cloneof = list(potential_parent_titles)[0].full_name
                                break

                temp_dict[key] = values

        processed_titles = temp_dict

        # Make sure supersets aren't set as both parent and clone throughout the DAT,
        # which can happen with some region combinations
        superset_clones: dict[str, str] = {}

        # Set up title tracking
        report_on_match: bool = False

        # Find if a superset title is set as a clone, and record its relationship
        for titles in processed_titles.values():
            for title in titles:
                if title.is_superset and title.cloneof:
                    if is_numbered:
                        superset_clones[title.numbered_name] = title.cloneof
                    else:
                        superset_clones[title.full_name] = title.cloneof

        # Switch any titles where the superset is a parent to the superset's clone
        for titles in processed_titles.values():
            if config.user_input.trace:
                report_on_match = TraceTools.trace_enable(titles, config.user_input.trace)

            for title in titles:
                if title.cloneof in superset_clones:
                    if not title.is_superset:
                        old_cloneof: str = title.cloneof

                        title.cloneof = superset_clones[title.cloneof]

                        if report_on_match:
                            TraceTools.trace_title('REF0114')
                            eprint(f'\n• {title.full_name}', wrap=False)
                            eprint(
                                f'  New clone: {title.cloneof}\n{Font.disabled}  Old clone: {old_cloneof}{Font.end}',
                                wrap=False,
                                pause=True,
                            )

        # Now process compilations
        processed_titles = choose_compilation(
            compilations, processed_titles, quick_lookup, config, is_numbered
        )

        if not config.user_input.single_cpu and bar:
            for _ in compilations:
                bar()

    eprint('• Selecting 1G1R titles... done.', overwrite=True)

    return processed_titles
