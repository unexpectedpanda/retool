from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.clone_lists.clone_list import CloneList
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.titletools import TraceTools
from modules.utils import eprint


def mias(
    quick_lookup: dict[str, dict[str, set[DatNode]]], config: Config, clone_list: CloneList
) -> None:
    """
    Applies MIA attributes to a dictionary of DatNode titles.

    Args:
        quick_lookup (dict[str, set[DatNode]]): A dictionary keyed by multiple title
            properties that enables quick lookup of titles. Due to the way Python
            references variables, changes made here are also reflected in
            `processed_titles`.

        config (Config): The Retool config object.

        clone_list (CloneList): The clone list for the current system.

    Returns:
        dict (dict[str, set[DatNode]]): A dictionary of DatNodes with MIA attributes
            applied.
    """
    if clone_list.mias:
        eprint('• Applying MIA attributes... ')

        report_on_match: bool = False
        warning_given: bool = False
        missing_titles: set[str] = set()

        # Find the MIA titles
        for mia in clone_list.mias:
            if not isinstance(mia, dict):
                if config.user_input.verbose:
                    warning_given = True
                    eprint(
                        '• The following MIA file isn\'t in a dictionary and will be skipped:',
                        level='warning',
                    )
                    eprint(f'  {mia}', level='warning')

                    if config.user_input.warningpause:
                        eprint(pause=True)
                continue

            # Look up the title in the dictionary, then process the required changes
            crc: str = ''
            found_titles: set[DatNode] = set()

            if 'crc' in mia:
                crc = mia['crc']

            if crc in quick_lookup['crc_index']:
                found_titles = quick_lookup['crc_index'][crc]

            if not found_titles:
                if 'name' in mia:
                    missing_titles.add(mia['name'])

            if config.user_input.trace:
                report_on_match = TraceTools.trace_enable(found_titles, config.user_input.trace)

            for title in found_titles:
                # Mark individual ROMs that are MIA
                for rom in title.roms:
                    # The best scenario, name and CRC match
                    if mia['crc'] == rom['crc'] and mia['name'] == rom['name']:
                        rom['mia'] = 'yes'
                        title.is_mia = True

                        if report_on_match:
                            eprint('')
                            TraceTools.trace_title(
                                'REF0135',
                                [title.full_name, rom['crc'], rom['name']],
                                set(),
                                keep_remove=False,
                            )
                            eprint(f'• {rom["name"]}', wrap=False)
                    # The second best scenario, CRC is the same, but file got renamed
                    elif mia['crc'] == rom['crc']:
                        rom['mia'] = 'yes'
                        title.is_mia = True

                        if report_on_match:
                            eprint('')
                            TraceTools.trace_title(
                                'REF0134',
                                [title.full_name, rom['crc']],
                                set(),
                                keep_remove=False,
                            )
                            eprint(f'• {rom["name"]}', wrap=False)
                    # It's not a trustworthy situation to use just the name if a file gets
                    # redumped

        if missing_titles and config.user_input.verbose:
            eprint(
                '\n• The following MIA files can\'t be found in the input DAT file and '
                'won\'t be marked:\n',
                level='warning',
            )

            for missing_title in sorted(missing_titles):
                eprint(f'  •  {missing_title}', level='warning', wrap=False)

            if config.user_input.warningpause:
                eprint(pause=True)

        if (warning_given or missing_titles) and config.user_input.verbose:
            eprint('• Applying MIA attributes... done')
        else:
            eprint('• Applying MIA attributes... done', overwrite=True)

