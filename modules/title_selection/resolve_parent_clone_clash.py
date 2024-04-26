from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modules.config import Config
    from modules.dats import DatNode

from modules.utils import Font, eprint


def resolve_parent_clone_clash(
    processed_titles: dict[str, set[DatNode]], config: Config
) -> dict[str, set[DatNode]]:
    """
    Makes sure a title isn't assigned as both a parent and a clone. This can only
    happen when exporting a DAT in legacy mode.

    This is usually caused by duplicate entries in a clone list.

    The solution is simple: if any title is marked as a parent, but happens to also
    marked as a clone, remove its clone status.

    Args:
        processed_titles (dict[str, set[DatNode]]): A work in progress dictionary
        of DatNodes, originally populated from the input DAT and actively being worked
        on by Retool.

        config (Config): The Retool config object.

    Returns:
        dict[str, set[DatNode]]: A dictionary of DatNodes that have had parent/clone
        errors corrected.
    """
    parent_clash: dict[str, Any] = {}

    # Find all parent titles
    for titles in processed_titles.values():
        for title in titles:
            if title.cloneof:
                if title.cloneof not in parent_clash:
                    parent_clash[title.cloneof] = {'clones': set(), 'assigned_clone': ''}

    # Find if parent titles are set as clones
    for titles in processed_titles.values():
        for title in titles:
            if title.full_name in parent_clash and title.cloneof:
                parent_clash[title.full_name]['assigned_clone'] = title.cloneof

                title.cloneof = ''

    # Find the titles that have set the parents as clones
    for key in parent_clash.keys():
        for titles in processed_titles.values():
            for title in titles:
                if parent_clash[key]['assigned_clone']:
                    if title.cloneof == key:
                        parent_clash[key]['clones'].add(title.full_name)

    if config.user_input.verbose:
        for key, values in parent_clash.items():
            if values['assigned_clone']:
                eprint(
                    f'\n• {Font.b}{key}{Font.be} should be a parent, but is set as a clone of\n  {Font.b}{values["assigned_clone"]}{Font.be}',
                    level='warning',
                )
                eprint(
                    '\n  Sometimes this can happen because there\'s a duplicate entry in the clone list.\n  Other times it\'s just a side effect of region and language settings.',
                    level='warning',
                )

            if values['clones']:
                eprint(
                    f'\n  Titles that have {Font.b}{key}{Font.be} as a parent:\n',
                    level='warning',
                )

                for value in values['clones']:
                    eprint(f'    - {value}', level='disabled')

            if values['assigned_clone']:
                eprint(f'\n  Removing clone from {Font.b}{key}{Font.be}\n', level='warning')

    return processed_titles
