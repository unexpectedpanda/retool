from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.clone_lists.clone_list import CloneList
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.titletools import TraceTools
from modules.utils import eprint


def retroachievements(
    quick_lookup: dict[str, dict[str, set[DatNode]]], config: Config, clone_list: CloneList
) -> None:
    """
    Applies RetroAchievements attributes to a dictionary of DatNode titles.

    Args:
        quick_lookup (dict[str, set[DatNode]]): A dictionary keyed by multiple title
            properties that enables quick lookup of titles. Due to the way Python
            references variables, changes made here are also reflected in
            `processed_titles`.

        config (Config): The Retool config object.

        clone_list (CloneList): The clone list for the current system.

    Returns:
        dict (dict[str, set[DatNode]]): A dictionary of DatNodes with RetroAchievements
        attributes applied.
    """
    if clone_list.retroachievements:
        eprint('• Applying RetroAchievements attributes... ')

        report_on_match: bool = False
        warning_given: bool = False
        missing_titles: set[str] = set()

        # Find the RetroAchievements titles
        for retroachievement in clone_list.retroachievements:
            if not isinstance(retroachievement, dict):
                if config.user_input.verbose:
                    warning_given = True
                    eprint(
                        '• The RetroAchievements file isn\'t in a dictionary and will be skipped. ',
                        level='warning',
                    )

                    if config.user_input.warningpause:
                        eprint(pause=True)
                continue

            found_titles: set[DatNode] = set()

            if 'sha256' in retroachievement:
                if retroachievement['sha256'] in quick_lookup['sha256_index']:
                    found_titles = quick_lookup['sha256_index'][retroachievement['sha256']]
            elif 'sha1' in retroachievement:
                if retroachievement['sha1'] in quick_lookup['sha1_index']:
                    found_titles = quick_lookup['sha1_index'][retroachievement['sha1']]
            elif 'md5' in retroachievement:
                if retroachievement['md5'] in quick_lookup['md5_index']:
                    found_titles = quick_lookup['md5_index'][retroachievement['md5']]
            elif 'crc' in retroachievement:
                if retroachievement['crc'] in quick_lookup['crc_index']:
                    found_titles = quick_lookup['crc_index'][retroachievement['crc']]

            if not found_titles:
                if 'name' in retroachievement:
                    missing_titles.add(retroachievement['name'])

            if config.user_input.trace:
                report_on_match = TraceTools.trace_enable(found_titles, config.user_input.trace)

            for title in found_titles:
                # Mark titles that support RetroAchievements
                title.is_retroachievement = True

                if report_on_match:
                    eprint('')
                    TraceTools.trace_title(
                        'REF0136',
                        [title.full_name],
                        set(),
                        keep_remove=False,
                    )

        if missing_titles and config.user_input.verbose:
            eprint(
                '\n• The following RetroAchievements titles can\'t be found in the input DAT file and '
                'won\'t be marked:\n',
                level='warning',
            )

            for missing_title in sorted(missing_titles):
                eprint(f'  •  {missing_title}', level='warning', wrap=False)

            eprint(
                '\n• These might be reported because Retool is searching for both CHD and ISO/BIN digests for these titles',
                level='warning',
            )

            if config.user_input.warningpause:
                eprint(pause=True)

        if (warning_given or missing_titles) and config.user_input.verbose:
            eprint('• Applying RetroAchievements attributes... done')
        else:
            eprint('• Applying RetroAchievements attributes... done', overwrite=True)
