from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config import Config
    from modules.dats import Dat, DatNode

from modules.titletools import TitleTools, TraceTools
from modules.utils import eprint


def clone_list_mias(
    processed_titles: dict[str, set[DatNode]], config: Config, input_dat: Dat
) -> dict[str, set[DatNode]]:
    """
    Applies MIA tags to a dictionary of DatNode titles, defined by the related
    clone list.

    Args:
        processed_titles (dict[str, set[DatNode]]): A work in progress dictionary
        of DatNodes, originally populated from the input DAT and actively being worked
        on by Retool.

        config (Config): The Retool config object.

        input_dat (Dat): The Retool input_dat object.

    Returns:
        dict[str, set[DatNode]]: A dictionary of DatNodes with MIA tags applied
        based on the related clone list.
    """
    if input_dat.clone_list.mias:
        eprint('• Applying clone list MIA tags... ')

        report_on_match: bool = False
        warning_given: bool = False
        missing_titles: set[str] = set()

        name_type = 'full'

        # Find the MIA titles
        for mia in input_dat.clone_list.mias:
            if not isinstance(mia, str):
                if config.user_input.verbose:  # type: ignore[unreachable]
                    warning_given = True
                    eprint(
                        '• The following MIA title entry isn\'t a string and will be skipped:',
                        level='warning',
                    )
                    eprint(f'  {mia}', level='warning')

                    if config.user_input.warningpause:
                        eprint(pause=True)
                continue

            # Look up the title in the dictionary, then process the required changes
            found_titles = TitleTools.find_title(
                mia, name_type, processed_titles, missing_titles, config
            )

            if config.user_input.trace:
                report_on_match = TraceTools.trace_enable(
                    set(found_titles), config.user_input.trace
                )

            for title in found_titles:
                if title in processed_titles[title.group_name]:
                    title.is_mia = True

                    for rom in title.roms:
                        rom['mia'] = 'yes'

                        if report_on_match:
                            eprint('')
                            TraceTools.trace_title(
                                'REF0085', [title.full_name], set(), keep_remove=False
                            )
                            eprint(f'• {rom["name"]}', wrap=False)

                    if report_on_match:
                        eprint('')
                        TraceTools.trace_title('REF0063', [], {title}, keep_remove=False)

        if missing_titles and config.user_input.verbose:
            eprint(
                '\n• The following MIA titles in the clone list can\'t be found in '
                'the input DAT and will be skipped:\n',
                level='warning',
            )

            for missing_title in sorted(missing_titles):
                eprint(f'  •  {missing_title}', level='warning', wrap=False)

            if config.user_input.warningpause:
                eprint(pause=True)

        if (warning_given or missing_titles) and config.user_input.verbose:
            eprint('• Applying clone list MIA tags... done')
        else:
            eprint('• Applying clone list MIA tags... done', overwrite=True)

    return processed_titles
