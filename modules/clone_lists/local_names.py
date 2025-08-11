from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.titletools import TraceTools
from modules.utils import Font, eprint, pattern2string


def clone_list_local_names(
    variant_title: dict[str, Any], new_title: DatNode, config: Config, report_on_match: bool
) -> None:
    """
    Applies local names from a clone list to a variant.

    Args:
        variant_title (dict[str, Any]): The variant entry from the clone list.

        new_title (DatNode): The new title DatNode object to apply the local name to.

        config (Config): The Retool config object.

        report_on_match (bool): Whether Retool needs to report any titles being traced.
    """
    if variant_title['localNames']:
        # Check if a system config is in play
        local_name_user_order_language_codes: list[str] = []

        if config.system_localization_order_user:
            if {'override': 'true'} in config.system_localization_order_user:
                local_name_user_order_language_codes = [
                    str(x) for x in config.system_localization_order_user if 'override' not in x
                ]
        elif config.localization_order_user:
            local_name_user_order_language_codes = list(config.localization_order_user)

        # Map language codes to full language names
        local_name_user_order_language_names: list[str] = []

        for language_code in local_name_user_order_language_codes:
            for language_name, language_value in config.languages.items():
                if language_code == language_value:
                    local_name_user_order_language_names.append(language_name.lower())
                    break

        # Make sure the language is in the user's local language order
        for language in local_name_user_order_language_names:
            if language in variant_title['localNames'].keys():
                new_title.local_name = variant_title['localNames'][language]
                break

        # Re-add the tags to the local name where appropriate
        if new_title.local_name:
            tags = pattern2string(re.compile(' \\(.*'), new_title.full_name)
            new_title.local_name = f'{new_title.local_name}{tags}'

        if report_on_match:
            eprint('')
            TraceTools.trace_title('REF0111')
            eprint(
                f'  New name: {new_title.local_name}\n{Font.d}  Old name: {new_title.full_name}{Font.end}',
                pause=True,
            )
