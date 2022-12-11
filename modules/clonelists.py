from __future__ import annotations

import copy
import hashlib
import itertools
import json
import pathlib
import sys

from typing import Any, TYPE_CHECKING

from modules.titletools import Removes, TitleTools, TraceTools
from modules.utils import download, eprint, ExitRetool, Font, printwrap, regex_test

if TYPE_CHECKING:
    from hashlib import _Hash
    from modules.config import Config
    from modules.dats import Dat, DatNode
    from modules.input import UserInput


class CloneList:
    def __init__(self,
                 min_retool_version: str='2.00',
                 categories: dict[str, dict[str, Any]] = {},
                 mias: list[str] = [],
                 overrides: dict[str, dict[str, Any]] = {},
                 renames: dict[str, list[dict[str, Any]]] = {},
                 removes: dict[str, dict[str, Any]] = {}):
        """ Creates an object that contains data originally stored in a clone list.

        Args:
            `min_retool_version (str, optional)`: The minimum Retool version required to
            process the imported clone list. Defaults to `2.00`.
            `categories (dict[str, dict[str, Any]], optional)`: A dictionary to store the
            `categories` object found in a related clone list, if it exists. Defaults to
            `{}`.
            `mias (list[str], optional)`: A list to store the `mias` arrary found in a
            related clone list, if it exists. Defaults to `[]`.
            `overrides (dict[str, dict[str, Any]], optional)`: A dictionary to store the
            `overrides` object found in a related clone list, if it exists. Defaults to
            `{}`.
            `renames (dict[str, list[dict[str, Any]]], optional)`: A dictionary to store
            the `renames` object found in a related clone list, if it exists. Defaults to
            `{}`.
            `removes (dict[str, dict[str, Any]], optional)`: A dictionary to store the
            `removes` object found in a related clone list, if it exists. Defaults to
            `{}`.
        """

        self.min_retool_version: str = min_retool_version
        self.categories: dict[str, dict[str, Any]] = categories
        self.mias: list[str] = mias
        self.overrides: dict[str, dict[str, Any]] = overrides
        self.renames: dict[str, list[dict[str, Any]]] = renames
        self.removes: dict[str, dict[str, Any]] = removes


class CloneListTools(object):
    """ Methods for applying clone list entries to a dictionary of DatNode titles. """


    @staticmethod
    def categories(processed_titles: dict[str, list[DatNode]], config: Config, input_dat: Dat) -> dict[str, list[DatNode]]:
        """ Applies new categories to a dictionary of DatNode titles, defined by the
        related clone list.

        Args:
            `processed_titles (dict[str, list[DatNode]])`: A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.
            `config (Config)`: The Retool config object.
            `input_dat (Dat)`: The Retool input_dat object.

        Returns:
            `dict[str, list[DatNode]]`: A dictionary of DatNodes with new categories
            assigned based on the related clone list.
        """

        if input_dat.clone_list.categories:
            eprint('* Applying clone list categories... ', sep=' ', end='', flush=True)

            report_on_match: bool = False
            warning_given: bool = False
            match_type: str = 'tag free'
            categories: list[str] = []

            # Check the name type we're matching for, and the categories to change the
            # title to
            missing_titles: set[str] = set()

            for key, values in input_dat.clone_list.categories.items():
                if 'match' in values:
                    match_type = values['match']

                    if not (match_type == 'full'
                        or match_type == 'short'
                        or match_type == 'tag free'
                        or match_type == 'regex'):
                            match_type = 'tag free'

                if 'categories' in values:
                    if type(values['categories']) is list:
                        categories = values['categories']
                    else:
                        if config.user_input.verbose:
                            warning_given = True
                            printwrap(
                                f'{Font.warning}* The following category title\'s '
                                f'"categories" key isn\'t an array and will be skipped:',
                                'error')
                            eprint(f'  {key}{Font.end}')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()
                        continue
                else:
                    if config.user_input.verbose:
                        warning_given = True
                        printwrap(
                            f'{Font.warning}* The following category title has no '
                            f'"categories" key and will be skipped:', 'error')
                        eprint(f'  {key}{Font.end}')

                        if config.user_input.warningpause:
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()
                    continue

                # Look up the title in the dictionary, then process the required changes
                if match_type == 'regex':
                    valid_regex:list[str] = regex_test([key], 'categories', is_user_filter=False)

                    if not valid_regex:
                        continue

                    found_titles = TitleTools.find_title(key, match_type, processed_titles, missing_titles, config, deep_search=True)
                else:
                    found_titles = TitleTools.find_title(key, match_type, processed_titles, missing_titles, config)

                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                for title in found_titles:
                    if title in processed_titles[title.group_name]:
                        if report_on_match:
                            eprint('')
                            TraceTools.trace_title('REF0053')
                            eprint(f'* {title.full_name}')
                            eprint(f'  New categories: {categories}\n{Font.disabled}  Old categories: {title.categories}{Font.end}')
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()

                        title.categories = categories

            if missing_titles and config.user_input.verbose:
                eprint('')
                printwrap(
                    f'{Font.warning}* The following category titles in the '
                    'clone list can\'t be found in the input DAT and will '
                    'be skipped:', 'error')

                eprint('')

                for missing_title in sorted(missing_titles):
                    eprint(f'  *  {missing_title}')

                eprint(f'{Font.end}')

                if config.user_input.warningpause:
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

            if (
                (warning_given
                 or missing_titles)
                and config.user_input.verbose):
                eprint('* Applying clone list categories... done')
            else:
                eprint('done.')

        return processed_titles


    @staticmethod
    def compare_priorities(title_set: set[DatNode], report_on_match: bool) -> set[DatNode]:
        """ Compare any two titles from a set of DatNodes, and select the one
        with the lowest priority number set in a clone list.

        Args:
            `title_set (set[DatNode])`: A set of titles as DatNode instances.
            `report_on_match (bool)`: Whether Retool needs to report any titles being
            traced.

        Returns:
            `set[DatNode]`: A set of DatNodes filtered by clone list priority.
        """

        title_set_temp: set[DatNode] = title_set.copy()

        for title_1, title_2 in itertools.combinations(title_set_temp, 2):
            if (
                title_1.short_name == title_2.short_name
                and title_1 in title_set
                and title_2 in title_set):
                    if not (
                        # Compare non-superset priority titles
                        title_1.is_superset
                        and title_2.is_superset):
                            if title_1.clonelist_priority < title_2.clonelist_priority:
                                if report_on_match:
                                    TraceTools.trace_title('REF0020')
                                    eprint(f'+ Keeping:  ({title_1.clonelist_priority}) {title_1.full_name}')
                                    eprint(f'{Font.disabled}- Removing: ({title_2.clonelist_priority}) {title_2.full_name}{Font.end}')
                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                    input()

                                title_set.remove(title_2)
                            elif title_2.clonelist_priority < title_1.clonelist_priority:
                                if report_on_match:
                                    TraceTools.trace_title('REF0021')
                                    eprint(f'+ Keeping:  ({title_2.clonelist_priority}) {title_2.full_name}')
                                    eprint(f'{Font.disabled}- Removing: ({title_1.clonelist_priority}) {title_1.full_name}{Font.end}')
                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                    input()

                                title_set.remove(title_1)
                    else:
                        # Compare superset titles
                        if title_1.clonelist_priority < title_2.clonelist_priority:
                            if report_on_match:
                                TraceTools.trace_title('REF0022')
                                eprint(f'+ Keeping:  ({title_1.clonelist_priority}) {title_1.full_name}')
                                eprint(f'{Font.disabled}- Removing: ({title_2.clonelist_priority}) {title_2.full_name}{Font.end}')
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()

                            title_set.remove(title_2)
                        elif title_2.clonelist_priority < title_1.clonelist_priority:
                            if report_on_match:
                                TraceTools.trace_title('REF0023')
                                eprint(f'+ Keeping:  ({title_2.clonelist_priority}) {title_2.full_name}')
                                eprint(f'{Font.disabled}- Removing: ({title_1.clonelist_priority}) {title_1.full_name}{Font.end}')
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()

                            title_set.remove(title_1)

        return title_set


    @staticmethod
    def mias(processed_titles: dict[str, list[DatNode]], config: Config, input_dat: Dat) -> dict[str, list[DatNode]]:
        """ Applies MIA tags to a dictionary of DatNode titles, defined by the related
        clone list.

        Args:
            `processed_titles (dict[str, list[DatNode]])`: A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.
            `config (Config)`: The Retool config object.
            `input_dat (Dat)`: The Retool input_dat object.

        Returns:
            `dict[str, list[DatNode]]`: A dictionary of DatNodes with MIA tags applied
            based on the related clone list.
        """

        if input_dat.clone_list.mias:
            eprint('* Applying clone list MIA tags... ', sep=' ', end='', flush=True)

            report_on_match: bool = False
            warning_given: bool = False
            missing_titles: set[str] = set()

            match_type = 'full'

            # Find the MIA titles
            for mia in input_dat.clone_list.mias:
                if type(mia) is not str:
                    if config.user_input.verbose:
                        warning_given = True
                        printwrap(
                            f'{Font.warning}* The following MIA title entry isn\'t a '
                            f'string and will be skipped:',
                            'error')
                        eprint(f'  {mia}{Font.end}')

                        if config.user_input.warningpause:
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()
                    continue

                # Look up the title in the dictionary, then process the required changes
                found_titles = TitleTools.find_title(mia, match_type, processed_titles, missing_titles, config)

                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                for title in found_titles:
                    if title in processed_titles[title.group_name]:
                        title.is_mia = True

                        for rom in title.roms:
                            rom['mia'] = 'yes'

                            if report_on_match:
                                eprint('')
                                TraceTools.trace_title('REF0085', [title.full_name], set(), keep_remove=False)
                                eprint(f'* {rom["name"]}')

                        if report_on_match:
                            eprint('')
                            TraceTools.trace_title('REF0063', [], set([title]), keep_remove=False)

            if missing_titles and config.user_input.verbose:
                eprint('')
                printwrap(
                    f'{Font.warning}* The following MIA titles in the '
                    'clone list can\'t be found in the input DAT and will '
                    'be skipped:', 'error')

                eprint('')

                for missing_title in sorted(missing_titles):
                    eprint(f'  *  {missing_title}')

                eprint(f'{Font.end}')

                if config.user_input.warningpause:
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

            if (
                (warning_given
                or missing_titles)
                and config.user_input.verbose):
                eprint('* Applying clone list MIA tags... done')
            else:
                eprint('done.')

        return processed_titles


    @staticmethod
    def overrides(processed_titles: dict[str, list[DatNode]], config: Config, input_dat: Dat) -> dict[str, list[DatNode]]:
        """ Overrides the default groups assigned to titles by Retool as defined by the
        related clone list. Overridden groups can either be applied directly, or
        conditionally based on the user's region order.

        Args:
            `processed_titles (dict[str, list[DatNode]])`: A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.
            `config (Config)`: The Retool config object.
            `input_dat (Dat)`: The Retool input_dat object.

        Returns:
            `dict[str, list[DatNode]]`: A dictionary of DatNodes with groups overriden as
            defined by the related clone list.
        """

        if input_dat.clone_list.overrides:
            eprint('* Applying clone list overrides... ', sep=' ', end='', flush=True)

            report_on_match: bool = False
            warning_given: bool = False

            # Check the name type we're matching for, and the group to move the title to
            missing_titles: set[str] = set()

            for key, values in input_dat.clone_list.overrides.items():
                condition_processed: bool = True
                match_type: str = 'tag free'
                else_group: str = ''

                if 'match' in values:
                    match_type = values['match']

                    if not (
                        match_type == 'full'
                        or match_type == 'short'
                        or match_type == 'tag free'
                        or match_type == 'regex'):
                            match_type = 'tag free'

                if 'new group' in values:
                    if type(values['new group']) is not str:
                        if config.user_input.verbose:
                            warning_given = True
                            printwrap(
                                f'{Font.warning}* The following override\'s "new '
                                f'group" key isn\'t a string and will be skipped:', 'error')
                            eprint(f'  {key}{Font.end}')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()
                        continue
                else:
                    if config.user_input.verbose:
                        warning_given = True
                        printwrap(
                            f'{Font.warning}* The following override has no "new group" '
                            f'key and will be skipped:', 'error')
                        eprint(f'  {key}{Font.end}')
                        if config.user_input.warningpause:
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()
                    continue

                # Look up the title in the dictionary, then process the required changes
                if match_type == 'regex':
                    valid_regex:list[str] = regex_test([key], 'overrides', is_user_filter=False)

                    if not valid_regex:
                        continue

                    found_titles = TitleTools.find_title(key, match_type, processed_titles, missing_titles, config, deep_search=True)
                else:
                    found_titles = TitleTools.find_title(key, match_type, processed_titles, missing_titles, config)

                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                for title in found_titles:
                    if report_on_match:
                        eprint('')
                        TraceTools.trace_title('REF0056')
                        eprint(f'\n* {title.full_name}')

                    # Get the new group the title will be moved to
                    new_group = values['new group'].lower()

                    # Check if the override is conditional
                    if 'condition' in values:
                        regions: list[str] = []
                        higher_than_regions: list[str] = []
                        condition_processed = False

                        # Look for the regions that need to be higher in priority than
                        # those defined in "higher than"
                        if 'region' in values['condition']:
                            if type(values['condition']['region']) is list:
                                regions = values['condition']['region']

                                if report_on_match:
                                    eprint('  IF any of these regions:')

                                    for condition_region in regions:
                                        eprint(f'    * {condition_region}')
                            else:
                                warning_given = True
                                printwrap(
                                    f'{Font.warning}* The following override\'s "region" '
                                    f'key isn\'t an array and will be skipped:', 'error')
                                eprint(f'  {key}{Font.end}')

                                if config.user_input.warningpause:
                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                    input()
                                continue
                        else:
                            warning_given = True
                            printwrap(
                                f'{Font.warning}* The following override has no "region" '
                                f'key inside its condition and will be skipped:', 'error')
                            eprint(f'  {key}{Font.end}')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()
                            continue

                        # Look for the regions that need to be lower in priority than the
                        # those defined in "region"
                        if 'higher than' in values['condition']:
                            if type(values['condition']['higher than']) is list:
                                higher_than_regions = values['condition']['higher than']

                                if report_on_match:
                                    eprint('  Are higher than all of these regions:')

                                    for condition_region in higher_than_regions:
                                        eprint(f'    * {condition_region}')
                            else:
                                warning_given = True
                                printwrap(
                                    f'{Font.warning}* The following override\'s "higher '
                                    f'than" key isn\'t an array and will be skipped:',
                                    'error')
                                eprint(f'  {key}{Font.end}')

                                if config.user_input.warningpause:
                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                    input()
                                continue
                        else:
                            warning_given = True
                            printwrap(
                                f'{Font.warning}* The following override has no "higher '
                                f'than" key inside its condition and will be skipped:',
                                'error')
                            eprint(f'  {key}{Font.end}')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()
                            continue

                        # Look for an "else group" entry, which reassigns a title's group
                        # if the condition isn't true
                        if report_on_match:
                            eprint(f'  THEN move to this group:\n    * {new_group}')

                        if 'else group' in values['condition']:
                            if type(values['condition']['else group']) is str:
                                else_group = values['condition']['else group'].lower()

                                if report_on_match:
                                    eprint(f'  ELSE move to this group:\n    * {else_group}')
                            else:
                                if report_on_match:
                                    eprint(f'  ELSE use the default group')

                        # Check that the regions are available in the user's current region
                        # order, and store their priority if so
                        higher_regions: list[int] = [i for i, region in enumerate(config.region_order_user) if region in regions]
                        lower_regions: list[int] = [i for i, region in enumerate(config.region_order_user) if region in higher_than_regions]

                        # If any of the higher regions is higher than ALL of the lower regions
                        # move the title to the new group. If this isn't the case, and there's
                        # an "else group" entry, move the title to the "else group". Otherwise,
                        # do nothing.
                        if higher_regions and lower_regions:
                            lower_regions_lowest: int = int(sorted(lower_regions)[0])

                            for higher_region in higher_regions:
                                if higher_region < lower_regions_lowest:
                                    condition_processed = True
                                    if report_on_match:
                                        eprint(f'\n  CONDITION is true, moving to group:\n    * {new_group}')

                            if not condition_processed:
                                if else_group:
                                    new_group = else_group
                                    condition_processed = True

                                    if report_on_match:
                                        eprint(f'\n  CONDITION is false, moving to group:\n    * {new_group}')
                    else:
                        if report_on_match:
                            eprint(f'  New group: {new_group}\n{Font.disabled}  Old group: {title.group_name}{Font.end}')

                    # Assign the new group
                    if condition_processed:
                        if report_on_match:

                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()

                        if title in processed_titles[title.group_name]:
                            if new_group not in processed_titles:
                                processed_titles[new_group] = []

                            processed_titles[title.group_name].remove(title)

                            title.group_name = new_group
                            if title.short_name.endswith('(demo)'):
                                title.short_name = f'{new_group} (demo)'
                            else:
                                title.short_name = new_group

                            processed_titles[new_group].append(title)
                    else:
                        if report_on_match:
                            eprint(f'\n  CONDITION is false, group isn\'t changing')
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()

            if missing_titles and config.user_input.verbose:
                eprint('')
                printwrap(
                    f'{Font.warning}* The following override titles in the '
                    'clone list can\'t be found in the input DAT and will '
                    'be skipped:', 'error')

                eprint('')

                for missing_title in sorted(missing_titles):
                    eprint(f'  *  {missing_title}')

                eprint(f'{Font.end}')

                if config.user_input.warningpause:
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

            if (
                (warning_given
                or missing_titles)
                and config.user_input.verbose):
                eprint('* Applying clone list overrides... done')
            else:
                eprint('done.')

        return processed_titles


    @staticmethod
    def removes(processed_titles: dict[str, list[DatNode]], config: Config, input_dat: Dat, removes: Removes) -> dict[str, list[DatNode]]:
        """ Removes titles from a dictionary of DatNodes, as defined by the related clone
        list. As a general rule, removes are a nuclear option, as they completely take the
        title out of contention, destroying any relationships set up by Retool. Another
        method should be attempted first.

        Args:
            `processed_titles (dict[str, list[DatNode]])`: A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.
            `config (Config)`: The Retool config object.
            `input_dat (Dat)`: The Retool input_dat object.
            `removes (Removes)`: A Removes object that contains and categorizes all the
            titles that have been removed from consideration. Is used for stats and other
            output files generated by Retool.

        Returns:
            `dict[str, list[DatNode]]`: A dictionary of DatNodes with titles removed as
            defined by the related clone list.
        """

        report_on_match: bool = False

        if input_dat.clone_list.removes:
            eprint('* Applying clone list removes... ', sep=' ', end='', flush=True)

            match_type: str = 'tag free'

            # Check the name type we're matching for, and the categories to change the
            # title to
            missing_titles: set[str] = set()
            removes_count: int = 0

            for key, values in input_dat.clone_list.removes.items():
                if 'match' in values:
                    match_type = values['match']

                    if not (match_type == 'full'
                        or match_type == 'short'
                        or match_type == 'tag free'):
                            match_type = 'tag free'

                # Look up the title in the dictionary, then process the required changes
                found_titles = TitleTools.find_title(key, match_type, processed_titles, missing_titles, config)

                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                for title in found_titles:
                    if title in processed_titles[TitleTools.get_group_name(key, config)]:

                        if report_on_match:
                            eprint('')
                            TraceTools.trace_title('REF0054')
                            eprint(f'{Font.disabled}- Remove: {title.full_name}{Font.end}')
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()

                        processed_titles[TitleTools.get_group_name(key, config)].remove(title)
                        title.exclude_reason = 'Clone list remove'
                        removes.clonelist_removes.add(title)
                        removes_count += 1

            if missing_titles and config.user_input.verbose:
                eprint('')
                printwrap(
                    f'{Font.warning}* The following remove titles in the '
                    'clone list can\'t be found in the input DAT and will '
                    'be skipped:', 'error')

                eprint('')

                for missing_title in sorted(missing_titles):
                    eprint(f'  *  {missing_title}')

                eprint(f'{Font.end}')

                if config.user_input.warningpause:
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

                eprint('* Applying clone list removes... done')
            else:
                eprint('done.')

            config.stats.removes_count = removes_count

        return processed_titles


    @staticmethod
    def renames(processed_titles: dict[str, list[DatNode]], config: Config, input_dat: Dat, is_includes: bool = False) -> dict[str, list[DatNode]]:
        """ Processes a dictionary of DatNodes and groups titles together that are the
        same, but have different names as defined by the related clone list.

        This is the primary function that deals with the fact that, for example,
        Title, The (USA) is equivalent to Title, Le (France).

        Args:
            `processed_titles (dict[str, list[DatNode]])`: A work in progress dictionary
            of DatNodes, originally populated from the input DAT and actively being worked
            on by Retool.
            `config (Config)`: The Retool config object.
            `input_dat (Dat)`: The Retool input_dat object.
            `is_includes (bool, optional)`: Set to `True` when processing includes. Is
            only used to produce reliable reporting when performing a trace. Defaults to
            `False`.

        Returns:
            `dict[str, list[DatNode]]`: A dictionary of DatNodes that has had all like
            titles grouped together as defined by the related clone list.
        """

        if input_dat.clone_list.renames:
            eprint('* Applying clone list renames... ', sep=' ', end='', flush=True)

            report_on_match: bool = False
            warning_given: bool = False
            missing_titles: set[str] = set()
            delete_titles: set[tuple[DatNode, str]] = set()

            for key, values in input_dat.clone_list.renames.items():
                for value in values:
                    if type(value) is dict:
                        if not (
                            'title' in value
                            or 'compilation' in value
                            or 'superset' in value):
                                if config.user_input.verbose:
                                    warning_given = True
                                    printwrap(
                                        f'{Font.warning}* The following rename entry is invalid, '
                                        'and should be in the format {"title": "<name>"}, '
                                        '{"compilation": "<name>", or "superset": "<name>"}',
                                        'error')
                                    eprint(f'  {value}{Font.end}')
                                continue
                    else:
                        if config.user_input.verbose:
                            warning_given = True
                            printwrap(
                                f'{Font.warning}* The following rename entry isn\'t an object '
                                f'and will be skipped:',
                                'error')
                            eprint(f'  {value}{Font.end}')
                        continue

                    rename_title: str

                    if 'title' in value:
                        rename_title = value['title']
                    elif 'compilation' in value:
                        rename_title = value['compilation']
                    elif 'superset' in value:
                        rename_title = value['superset']
                    else:
                        continue

                    match_type: str = ''

                    if 'match' in value:
                        match_type = value['match']
                    else:
                        match_type: str = 'short'

                    # Look up the title in the dictionary, then process the required changes
                    if match_type == 'regex':
                        valid_regex:list[str] = regex_test([rename_title], 'renames', is_user_filter=False)

                        if not valid_regex:
                            continue

                        found_titles: list[DatNode] = TitleTools.find_title(rename_title, match_type, processed_titles, missing_titles, config, deep_search=True)
                    else:
                        found_titles: list[DatNode] = TitleTools.find_title(rename_title, match_type, processed_titles, missing_titles, config)

                    old_group_name: str = TitleTools.get_group_name(rename_title, config)
                    new_group_name: str = TitleTools.get_group_name(key, config)

                    new_group_name = new_group_name.lower()

                    if new_group_name not in processed_titles:
                        processed_titles[new_group_name] = []

                    # If the title's not found in the DAT, add it to missing_titles,
                    # otherwise add it to the delete list, then move it to the new
                    # group
                    if not found_titles:
                        if 'title' in value:
                            missing_titles.add(value['title'])
                        elif 'compilation' in value:
                            missing_titles.add(value['compilation'])
                        elif 'superset' in value:
                            missing_titles.add(value['superset'])
                    else:
                        if config.user_input.trace:
                            report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                        for title in found_titles:
                            if title in processed_titles[old_group_name]:
                                if (
                                    report_on_match
                                    and new_group_name != title.group_name
                                    and not is_includes):
                                        eprint('')
                                        TraceTools.trace_title('REF0055')
                                        eprint(f'* {title.full_name}')
                                        eprint(f'  New group: {new_group_name}\n{Font.disabled}  Old group: {title.group_name}{Font.end}')
                                        eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                        input()

                                if (
                                    'title' in value
                                    or 'superset' in value):
                                    new_title: DatNode = copy.deepcopy(title)
                                    new_title.group_name = new_group_name
                                    new_title.short_name = key.lower()

                                    if 'priority' in value:
                                        new_title.clonelist_priority = value['priority']
                                    else:
                                        new_title.clonelist_priority = 1

                                    if 'superset' in value:
                                        new_title.is_superset = True

                                    processed_titles[new_group_name].append(new_title)

                                    delete_titles.add((title, old_group_name))

                                elif 'compilation' in value:
                                    for compilation_title in processed_titles[old_group_name]:
                                        if compilation_title.full_name == title.full_name:
                                            title_position: int = 1
                                            if 'title_position' in value:
                                                title_position = value['title_position']

                                            if 'priority' in value:
                                                clonelist_priority: int = value['priority']
                                            else:
                                                clonelist_priority = 1

                                            compilation_title.contains_titles[key] = {"position": title_position, "priority": clonelist_priority}

            # Delete titles from old groups, and clean up empty groups
            for title, old_group_name in delete_titles:
                if title in processed_titles[old_group_name]:
                    processed_titles[old_group_name].remove(title)

                if not processed_titles[old_group_name]:
                    del processed_titles[old_group_name]

            if missing_titles and config.user_input.verbose:
                eprint('')
                printwrap(
                    f'{Font.warning}* The following rename titles in the '
                    'clone list can\'t be found in the input DAT and will '
                    'be skipped:', 'error')

                eprint('')

                for missing_title in sorted(missing_titles):
                    eprint(f'  *  {missing_title}')

                eprint(f'{Font.end}')

                if config.user_input.warningpause:
                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                    input()

            if (
                (warning_given
                 or missing_titles)
                and config.user_input.verbose):
                    eprint('* Applying clone list renames... done')
            else:
                eprint('done.')

        return processed_titles


    @staticmethod
    def update_clonelists_metadata(config: Config, gui_input: UserInput) -> None:
        """ Downloads the latest clone lists and support files

        Args:
            `config (Config)`: The Retool config object.
            `gui_input (UserInput)`: Used to determine whether or not the update is being
            run from the GUI. If so, check if a custom download location has been set in
            user-config.yaml.

        Raises:
            `ExitRetool`: Silently exit if run from the GUI, so UI elements can
            re-enable.
        """

        # Download the latest internal-config.json and datafile.dtd
        download_location: str = config.clone_list_metadata_download_location

        if gui_input:
            download_location = config.user_input.user_clone_list_metadata_download_location

        failed: bool = False

        eprint(f'* Downloading {Font.bold}{config.config_file}{Font.end}... ')

        failed = download(f'{download_location}/{config.config_file}', pathlib.Path(f'{config.config_file}'))

        if not failed:
            eprint(f'\033[F\033[K* Downloading {Font.bold}{config.config_file}{Font.end}... done.')

        eprint(f'* Downloading {Font.bold}datafile.dtd{Font.end}... ')

        failed = download(f'{download_location}/datafile.dtd', pathlib.Path('datafile.dtd'))

        if not failed:
            eprint(f'\033[F\033[K* Downloading {Font.bold}datafile.dtd{Font.end}... done.')


        def get_updates(local_path: str, update_name: str, download_url: str, file_count: int) -> int:
            """ An online updater for clone lists and metadata. Downloads a specific
            hash.json file, which contains names and hashes for a set of files.
            Then compares these details with the hashes of local files found in
            `local_path`, and download new files if there's a hash mismatch.

            Args:
                `local_path (str)`: The directory that contains the files that need
                hashing.
                `update_name (str)`: The name of the update being performed, to report to
                the user.
                `download_url (str)`: The download directory where the online version of
                the file is found.
                `file_count (int)`: A counter for how many files have been downloaded, so
                this can be reported to the user.

            Returns:
                `int`: The final count of how many files have been downloaded.
            """

            # Create folders if they're missing
            pathlib.Path(local_path).mkdir(parents=True, exist_ok=True)

            # Get the hash.json
            eprint(f'* Checking for updated {update_name}...')
            download(f'{download_url}/hash.json', pathlib.Path(f'{local_path}/hash.json'))

            if pathlib.Path(f'{local_path}/hash.json').exists():
                try:
                    with open(pathlib.Path(f'{local_path}/hash.json'), 'r', encoding='utf-8') as file_hash:
                        file_hash_str: str = file_hash.read()
                except OSError as e:
                    eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
                    raise

                # Use the filenames and hash values in hash.json to determine if updates
                # need to be downloaded
                pathlib.Path(local_path).mkdir(parents=True, exist_ok=True)

                for file_name, hash_value in json.loads(file_hash_str).items():
                    if pathlib.Path(f'{local_path}/{file_name}').resolve().exists():
                        hash_md5: _Hash = hashlib.md5()

                        # Convert files from CRLF to LF to verify if they need updating
                        try:
                            with open(pathlib.Path(f'{local_path}/{file_name}'), 'r+', newline='\n') as file:
                                contents: str = file.read()

                                file.seek(0)
                                file.write(contents)
                                file.truncate()
                        except OSError as e:
                            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
                            raise

                        # Get the hash of the new file
                        try:
                            with open (pathlib.Path(f'{local_path}/{file_name}').resolve(), 'rb') as file:
                                for chunk in iter(lambda: file.read(4096), b''):
                                    hash_md5.update(chunk)
                        except OSError as e:
                                eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
                                raise

                        if hash_md5.hexdigest() != hash_value:
                            eprint(f'  * Found an updated {update_name[:-1]}, {Font.bold}{file_name}{Font.end}. Downloading... ')
                            file_count += 1
                            failed = download(f'{download_url}/{file_name}', pathlib.Path(f'{local_path}/{file_name}'))
                            if not failed:
                                eprint(f'\033[F\033[K  * Found an updated {update_name[:-1]}, {Font.bold}{file_name}{Font.end}. Downloading... done.')
                    else:
                        eprint(f'  * Found a new {update_name[:-1]}, {Font.bold}{file_name}{Font.end}. Downloading... ')
                        file_count += 1
                        failed = download(f'{download_url}/{file_name}', pathlib.Path(f'{local_path}/{file_name}'))
                        if not failed:
                            eprint(f'\033[F\033[K  * Found a new {update_name[:-1]}, {Font.bold}{file_name}{Font.end}. Downloading... done.')
            else:
                eprint(f'{Font.warning}{str(pathlib.Path(f"{local_path}/{file_name}"))} doesn\'t exist, can\'t update {update_name}.{Font.end}')

            return file_count

        file_count: int = 0
        file_count = get_updates(config.path_clone_list, 'clone lists', f'{download_location}/clonelists', file_count)
        file_count = get_updates(config.path_metadata, 'metadata files', f'{download_location}/metadata', file_count)

        if file_count == 0:
            eprint(f'{Font.success}\n* Done. No new updates are available.{Font.end}')
        elif file_count == 1:
            eprint(f'{Font.success}\n* Done. Downloaded {file_count} file.{Font.end}')
        else:
           eprint(f'{Font.success}\n* Done. Downloaded {file_count} files.{Font.end}')

        if gui_input:
            raise ExitRetool
        else:
            sys.exit()