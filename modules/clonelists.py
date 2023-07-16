from __future__ import annotations

import copy
import hashlib
import itertools
import json
import pathlib
import sys

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from hashlib import _Hash
    from modules.config import Config
    from modules.dats import Dat, DatNode
    from modules.input import UserInput

from modules.titletools import Removes, TitleTools, TraceTools
from modules.utils import download, eprint, ExitRetool, Font, printwrap, regex_test


class CloneList:
    def __init__(self,
                 min_retool_version: str='2.00',
                 categories: list[dict[str, Any]] = [],
                 mias: list[str] = [],
                 overrides: list[dict[str, str|dict[str, str|list[str]]]] = [],
                 removes: list[dict[str, str]] = [],
                 variants: list[dict[str, Any]] = []):
        """ Creates an object that contains data originally stored in a clone list.

        Args:
            - `min_retool_version (str, optional)` The minimum Retool version required to
              process the imported clone list. Defaults to `2.00`.

            - `categories (list[dict[str, str|list[str]]], optional)` A dictionary to store the
              `categories` object found in a related clone list, if it exists. Defaults to
              `{}`.

            - `mias (list[str], optional)` A list to store the `mias` arrary found in a
              related clone list, if it exists. Defaults to `[]`.

            - `overrides (list[dict[str, str|dict[str, str|list[str]]]], optional)` A dictionary
              to store the `overrides` object found in a related clone list, if it exists.
              Defaults to `{}`.

            - `removes (dict[str, dict[str, Any]], optional)` A dictionary to store the
              `removes` object found in a related clone list, if it exists. Defaults to
              `{}`.

            - `variants (dict[str, list[dict[str, Any]]], optional)` A dictionary to store
              the `variants` object found in a related clone list, if it exists. Defaults to
              `{}`.
        """

        self.min_retool_version: str = min_retool_version
        self.categories: list[dict[str, Any]] = categories
        self.mias: list[str] = mias
        self.overrides: list[dict[str, Any]] = overrides
        self.removes: list[dict[str, str]] = removes
        self.variants: list[dict[str, Any]] = variants


class CloneListTools(object):
    """ Methods for applying clone list entries to a dictionary of DatNode titles. """


    @staticmethod
    def categories(processed_titles: dict[str, set[DatNode]], config: Config, input_dat: Dat) -> dict[str, set[DatNode]]:
        """ Applies new categories to a dictionary of DatNode titles, defined by the
        related clone list.

        Args:
            - `processed_titles (dict[str, set[DatNode]])` A work in progress dictionary
              of DatNodes, originally populated from the input DAT and actively being worked
              on by Retool.

            - `config (Config)` The Retool config object.

            - `input_dat (Dat)` The Retool input_dat object.

        Returns:
            `dict[str, set[DatNode]]` A dictionary of DatNodes with new categories
            assigned based on the related clone list.
        """

        if input_dat.clone_list.categories:
            eprint('* Applying clone list categories... ', sep=' ', end='', flush=True)

            report_on_match: bool = False
            warning_given: bool = False
            name_type: str = 'tagFree'
            categories: list[str] = []
            missing_titles: set[str] = set()

            # Check the name type we're matching for, and the categories to change the
            # title to
            for value in input_dat.clone_list.categories:
                if 'nameType' in value:
                    name_type = value['nameType']

                    if not (name_type == 'full'
                        or name_type == 'short'
                        or name_type == 'regionFree'
                        or name_type == 'tagFree'
                        or name_type == 'regex'):
                            name_type = 'tagFree'

                if 'categories' in value:
                    if type(value['categories']) is list:
                        categories = value['categories']
                    else:
                        if config.user_input.verbose:
                            warning_given = True
                            printwrap(
                                f'{Font.warning}* The following category title\'s '
                                f'"categories" key isn\'t an array and will be skipped:',
                                'error')
                            eprint(f'\n  {value["searchTerm"]}{Font.end}')

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
                        eprint(f'\n  {value["searchTerm"]}{Font.end}')

                        if config.user_input.warningpause:
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()
                    continue

                # Look up the title in the dictionary, then process the required changes
                if name_type == 'regex':
                    valid_regex: list[str] = regex_test([value['searchTerm']], 'categories', 'clone list')

                    if not valid_regex:
                        continue

                    found_titles = TitleTools.find_title(value['searchTerm'], name_type, processed_titles, missing_titles, config, deep_search=True)
                else:
                    found_titles = TitleTools.find_title(value['searchTerm'], name_type, processed_titles, missing_titles, config)

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
            - `title_set (set[DatNode])` A set of titles as DatNode instances.

            - `report_on_match (bool)` Whether Retool needs to report any titles being
            traced.

        Returns:
            `set[DatNode]` A set of DatNodes filtered by clone list priority.
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
    def mias(processed_titles: dict[str, set[DatNode]], config: Config, input_dat: Dat) -> dict[str, set[DatNode]]:
        """ Applies MIA tags to a dictionary of DatNode titles, defined by the related
        clone list.

        Args:
            - `processed_titles (dict[str, set[DatNode]])` A work in progress dictionary
              of DatNodes, originally populated from the input DAT and actively being worked
              on by Retool.

            - `config (Config)` The Retool config object.

            - `input_dat (Dat)` The Retool input_dat object.

        Returns:
            `dict[str, set[DatNode]]` A dictionary of DatNodes with MIA tags applied
            based on the related clone list.
        """

        if input_dat.clone_list.mias:
            eprint('* Applying clone list MIA tags... ', sep=' ', end='', flush=True)

            report_on_match: bool = False
            warning_given: bool = False
            missing_titles: set[str] = set()

            name_type = 'full'

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
                found_titles = TitleTools.find_title(mia, name_type, processed_titles, missing_titles, config)

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
    def overrides(processed_titles: dict[str, set[DatNode]], config: Config, input_dat: Dat) -> dict[str, set[DatNode]]:
        """ Overrides the default groups and short names assigned to titles by Retool as
        defined by the related clone list. Overridden groups can either be applied
        directly, or conditionally based on the user's region order.

        Args:
            - `processed_titles (dict[str, set[DatNode]])` A work in progress dictionary
              of DatNodes, originally populated from the input DAT and actively being worked
              on by Retool.

            - `config (Config)` The Retool config object.

            - `input_dat (Dat)` The Retool input_dat object.

        Returns:
            `dict[str, set[DatNode]]` A dictionary of DatNodes with groups overriden as
            defined by the related clone list.
        """

        if input_dat.clone_list.overrides:
            eprint('* Applying clone list overrides... ', sep=' ', end='', flush=True)

            report_on_match: bool = False
            warning_given: bool = False

            # Check the name type we're matching for, and the group to move the title to
            missing_titles: set[str] = set()

            for value in input_dat.clone_list.overrides:
                condition_processed: bool = True
                name_type: str = 'tagFree'
                else_group: str = ''
                priority: int = 0

                if 'nameType' in value:
                    name_type = value['nameType']

                    if not (
                        name_type == 'full'
                        or name_type == 'short'
                        or name_type == 'regionFree'
                        or name_type == 'tagFree'
                        or name_type == 'regex'):
                            name_type = 'tagFree'

                if 'newGroup' in value:
                    if type(value['newGroup']) is not str:
                        if config.user_input.verbose:
                            warning_given = True
                            printwrap(
                                f'{Font.warning}* The following override\'s "newGroup" '
                                f'key isn\'t a string and will be skipped:', 'error')
                            eprint(f'\n  {value["searchTerm"]}{Font.end}')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()
                        continue
                else:
                    if config.user_input.verbose:
                        warning_given = True
                        printwrap(
                            f'{Font.warning}* The following override has no "newGroup" '
                            f'key and will be skipped:', 'error')
                        eprint(f'\n  {value["searchTerm"]}{Font.end}')

                        if config.user_input.warningpause:
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()
                    continue

                # Look up the title in the dictionary, then process the required changes
                if name_type == 'regex':
                    valid_regex:list[str] = regex_test([value['searchTerm']], 'overrides', 'clone list')

                    if not valid_regex:
                        continue

                    found_titles = TitleTools.find_title(value['searchTerm'], name_type, processed_titles, missing_titles, config, deep_search=True)
                else:
                    found_titles = TitleTools.find_title(value['searchTerm'], name_type, processed_titles, missing_titles, config)

                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                for title in found_titles:
                    if report_on_match:
                        eprint('')
                        TraceTools.trace_title('REF0056')
                        eprint(f'\n* {title.full_name}')

                    # Get the new group the title will be moved to
                    new_group: str = TitleTools.get_group_name(value['newGroup'], config)

                    # Check if the override is conditional
                    if 'condition' in value:
                        regions: list[str] = []
                        higher_than_regions: list[str] = []
                        condition_processed = False

                        # Look for the regions that need to be higher in priority than
                        # those defined in "higher than"
                        if 'regionOrder' in value['condition']:
                            if type(value['condition']['regionOrder']) is dict:
                                if 'higherRegions' in value['condition']['regionOrder']:
                                    if type(value['condition']['regionOrder']['higherRegions']) is list:
                                        regions = value['condition']['regionOrder']['higherRegions']

                                        if report_on_match:
                                            eprint('\n  IF any of these regions:\n')

                                            for condition_region in regions:
                                                eprint(f'    * {condition_region}')
                                    else:
                                        printwrap(
                                            f'{Font.warning}* The following override\'s '
                                            f'"higherRegions" key isn\'t an array and will be '
                                            'skipped:', 'error')
                                        eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                        if config.user_input.warningpause:
                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                            input()
                                        continue
                                else:
                                    warning_given = True
                                    printwrap(
                                        f'{Font.warning}* The following override has no '
                                        '"higherRegions" key inside the "regionOrder" key, and '
                                        'will be skipped:', 'error')
                                    eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                    if config.user_input.warningpause:
                                        eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                        input()
                                    continue

                                # Look for the regions that need to be lower in priority than the
                                # those defined in "region"
                                if 'lowerRegions' in value['condition']['regionOrder']:
                                    if type(value['condition']['regionOrder']['lowerRegions']) is list:
                                        higher_than_regions = value['condition']['regionOrder']['lowerRegions']

                                        if report_on_match:
                                            eprint('\n  Are higher than all of these regions:\n')

                                            for condition_region in higher_than_regions:
                                                eprint(f'    * {condition_region}')
                                    else:
                                        warning_given = True
                                        printwrap(
                                            f'{Font.warning}* The following override\'s '
                                            '"lowerRegions" key isn\'t an array and will be '
                                            'skipped:', 'error')
                                        eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                        if config.user_input.warningpause:
                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                            input()
                                        continue
                                else:
                                    warning_given = True
                                    printwrap(
                                        f'{Font.warning}* The following override has no '
                                        '"lowerRegions" key inside the "regionOrder" key, '
                                        'and will be skipped:', 'error')
                                    eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                    if config.user_input.warningpause:
                                        eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                        input()
                                    continue

                            # Look for a "priority" entry, which reassigns a title's priority if the condition is true
                            if 'priority' in value['condition']['regionOrder']:
                                if type(value['condition']['regionOrder']['priority']) is not int:
                                    if config.user_input.verbose:
                                        warning_given = True
                                        printwrap(
                                            f'{Font.warning}* The following override\'s "priority" '
                                            f'key isn\'t an integer and will be skipped:', 'error')
                                        eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                        if config.user_input.warningpause:
                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                            input()
                                    continue
                                else:
                                    priority = value['condition']['regionOrder']['priority']

                            # Look for an "elseGroup" entry, which reassigns a title's group
                            # if the condition isn't true
                            if report_on_match:
                                eprint(f'\n  THEN move to this group: {Font.bold}{new_group}{Font.end}')

                                if priority:
                                    eprint(f'  AND set priority to: {Font.bold}{value["condition"]["regionOrder"]["priority"]}{Font.end}\n')

                            if 'elseGroup' in value['condition']['regionOrder']:
                                if type(value['condition']['regionOrder']['elseGroup']) is str:
                                    else_group = TitleTools.get_group_name(value['condition']['regionOrder']['elseGroup'], config)

                                    if report_on_match:
                                        eprint(f'  ELSE move to this group: {Font.bold}{else_group}{Font.end}')
                                        if priority:
                                            eprint(f'  AND set priority to: {Font.bold}2{Font.end}\n')
                                else:
                                    warning_given = True
                                    printwrap(
                                        f'{Font.warning}* The following override\'s '
                                        '"elseGroup" key isn\'t a string and will be '
                                        'skipped:', 'error')
                                    eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                    if config.user_input.warningpause:
                                        eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                        input()
                            else:
                                if report_on_match:
                                    eprint(f'  ELSE use the default group: {Font.bold}{title.group_name}{Font.end}')
                                    if priority:
                                        eprint(f'  AND set priority to: {Font.bold}2{Font.end}\n')
                        else:
                            warning_given = True
                            printwrap(
                                f'{Font.warning}* The following override has no '
                                f'"regionOrder" key inside its condition, and will be '
                                f'skipped:', 'error')
                            eprint(f'\n  {value["searchTerm"]}{Font.end}')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()
                            continue

                        # Check if a system config is in play
                        region_order: list[str] = config.region_order_user

                        if config.system_region_order_user:
                            if {'override': 'true'} in config.system_region_order_user:
                                region_order = [str(x) for x in config.system_region_order_user if 'override' not in x]

                        # Check that the regions are available in the user's current region
                        # order, and store their priority if so
                        higher_regions: list[int] = [i for i, region in enumerate(region_order) if region in regions]
                        lower_regions: list[int] = [i for i, region in enumerate(region_order) if region in higher_than_regions]

                        # If any of the higher regions is higher than ALL of the lower regions
                        # move the title to the new group. If this isn't the case, and there's
                        # an "elseGroup" entry, move the title to the "elseGroup". Otherwise,
                        # do nothing.
                        if higher_regions and lower_regions:
                            lower_regions_lowest: int = int(sorted(lower_regions)[0])

                            for higher_region in higher_regions:
                                if higher_region < lower_regions_lowest:
                                    if not condition_processed:
                                        if report_on_match:
                                            eprint(f'  CONDITION is true, moving to group: {Font.bold}{new_group}{Font.end}')
                                            if priority:
                                                eprint(f'  Changing to priority: {Font.bold}{priority}{Font.end}')

                                    condition_processed = True

                            if not condition_processed:
                                if else_group:
                                    new_group = else_group
                                    condition_processed = True

                                    if report_on_match:
                                        eprint(f'  CONDITION is false, moving to group: {Font.bold}{new_group}{Font.end}')
                                        if priority:
                                            eprint(f'  Changing to priority: {Font.bold}2{Font.end}')
                                if priority:
                                    priority = 2
                    else:
                        if report_on_match:
                            eprint(f'  New group: {Font.bold}{new_group}{Font.end}\n{Font.disabled}  Old group: {Font.bold}{title.group_name}{Font.end}')

                    # Assign the new group and if it's available, priority
                    if condition_processed:
                        if report_on_match:
                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()

                        if title in processed_titles[title.group_name]:
                            if new_group not in processed_titles:
                                processed_titles[new_group] = set()

                            processed_titles[title.group_name].remove(title)

                            title.group_name = new_group

                            if title.short_name.endswith('(demo)'):
                                title.short_name = f'{new_group} (demo)'
                            else:
                                title.short_name = new_group

                            if priority:
                                title.clonelist_priority = priority

                            processed_titles[new_group].add(title)
                    else:
                        if report_on_match:
                            eprint(f'  CONDITION is false, group remains as: {Font.bold}{title.group_name}{Font.end}')
                            if priority:
                                eprint(f'  Changing to priority: 2')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()

                        if title in processed_titles[title.group_name]:
                            if priority:
                                title.clonelist_priority = 2

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
    def removes(processed_titles: dict[str, set[DatNode]], config: Config, input_dat: Dat, removes: Removes) -> dict[str, set[DatNode]]:
        """ Removes titles from a dictionary of DatNodes, as defined by the related clone
        list. As a general rule, removes are a nuclear option, as they completely take the
        title out of contention, destroying any relationships set up by Retool. Another
        method should be attempted first.

        Args:
            - `processed_titles (dict[str, set[DatNode]])` A work in progress dictionary
              of DatNodes, originally populated from the input DAT and actively being worked
              on by Retool.

            - `config (Config)` The Retool config object.

            - `input_dat (Dat)` The Retool input_dat object.

            - `removes (Removes)` A Removes object that contains and categorizes all the
              titles that have been removed from consideration. Is used for stats and other
              output files generated by Retool.

        Returns:
            `dict[str, set[DatNode]]` A dictionary of DatNodes with titles removed as
            defined by the related clone list.
        """

        report_on_match: bool = False

        if input_dat.clone_list.removes:
            eprint('* Applying clone list removes... ', sep=' ', end='', flush=True)

            report_on_match = False
            name_type: str = 'tagFree'
            missing_titles: set[str] = set()
            removes_count: int = 0

            # Check the name type we're matching for, and the titles to remove
            for value in input_dat.clone_list.removes:
                if 'nameType' in value:
                    name_type = value['nameType']

                    if not (name_type == 'full'
                        or name_type == 'short'
                        or name_type == 'regionFree'
                        or name_type == 'tagFree'):
                            name_type = 'tagFree'

                # Look up the title in the dictionary, then process the required changes
                found_titles = TitleTools.find_title(value['searchTerm'], name_type, processed_titles, missing_titles, config)

                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                for title in found_titles:
                    if title in processed_titles[TitleTools.get_group_name(value['searchTerm'], config)]:

                        if report_on_match:
                            eprint('')
                            TraceTools.trace_title('REF0054')
                            eprint(f'{Font.disabled}- Remove: {title.full_name}{Font.end}')
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()

                        processed_titles[TitleTools.get_group_name(value['searchTerm'], config)].remove(title)
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
    def update_clonelists_metadata(config: Config, gui_input: UserInput|None, no_exit: bool = False) -> None:
        """ Downloads the latest clone lists and support files

        Args:
            - `config (Config)` The Retool config object.

            - `gui_input (UserInput)` Used to determine whether or not the update is being
              run from the GUI. If so, check if a custom download location has been set in
              user-config.yaml.

        Raises:
            `ExitRetool` Silently exit if run from the GUI, so UI elements can
            re-enable.
        """

        # Download the latest internal-config.json and datafile.dtd
        download_location: str = config.clone_list_metadata_download_location

        if gui_input:
            download_location = config.user_input.user_clone_list_metadata_download_location

        failed: bool = False

        eprint(f'* Downloading {Font.bold}{config.config_file}{Font.end}... ')

        failed = download(f'{download_location}/{config.config_file}', str(pathlib.Path(f'{config.config_file}')))

        if not failed:
            eprint(f'\033[F\033[K* Downloading {Font.bold}{config.config_file}{Font.end}... done.')

        eprint(f'* Downloading {Font.bold}datafile.dtd{Font.end}... ')

        failed = download(f'{download_location}/datafile.dtd', str(pathlib.Path('datafile.dtd')))

        if not failed:
            eprint(f'\033[F\033[K* Downloading {Font.bold}datafile.dtd{Font.end}... done.')


        def get_updates(local_path: str, update_name: str, download_url: str, file_count: int) -> int:
            """ An online updater for clone lists and metadata. Downloads a specific
            hash.json file, which contains names and hashes for a set of files.
            Then compares these details with the hashes of local files found in
            `local_path`, and download new files if there's a hash mismatch.

            Args:
                - `local_path (str)` The directory that contains the files that need
                  hashing.

                - `update_name (str)` The name of the update being performed, to report to
                  the user.

                - `download_url (str)` The download directory where the online version of
                  the file is found.

                - `file_count (int)` A counter for how many files have been downloaded, so
                  this can be reported to the user.

            Returns:
                `int` The final count of how many files have been downloaded.
            """

            # Create folders if they're missing
            pathlib.Path(local_path).mkdir(parents=True, exist_ok=True)

            # Get the hash.json
            eprint(f'* Checking for updated {update_name}...')
            download(f'{download_url}/hash.json', str(pathlib.Path(f'{local_path}/hash.json')))

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
                        hash_sha256: _Hash = hashlib.sha256()

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
                                    hash_sha256.update(chunk)
                        except OSError as e:
                                eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
                                raise

                        if hash_sha256.hexdigest() != hash_value:
                            eprint(f'  * Found an updated {update_name[:-1]}, {Font.bold}{file_name}{Font.end}. Downloading... ')
                            file_count += 1
                            failed = download(f'{download_url}/{file_name}', str(pathlib.Path(f'{local_path}/{file_name}')))
                            if not failed:
                                eprint(f'\033[F\033[K  * Found an updated {update_name[:-1]}, {Font.bold}{file_name}{Font.end}. Downloading... done.')
                    else:
                        eprint(f'  * Found a new {update_name[:-1]}, {Font.bold}{file_name}{Font.end}. Downloading... ')
                        file_count += 1
                        failed = download(f'{download_url}/{file_name}', str(pathlib.Path(f'{local_path}/{file_name}')))
                        if not failed:
                            eprint(f'\033[F\033[K  * Found a new {update_name[:-1]}, {Font.bold}{file_name}{Font.end}. Downloading... done.')
            else:
                eprint(f'{Font.warning}{str(pathlib.Path(f"{local_path}/hash.json"))} doesn\'t exist, can\'t update {update_name}.{Font.end}')

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

        if not no_exit:
            if gui_input:
                raise ExitRetool
            else:
                sys.exit()

    @staticmethod
    def variants(processed_titles: dict[str, set[DatNode]], config: Config, input_dat: Dat, is_includes: bool = False) -> dict[str, set[DatNode]]:
        """ Processes a dictionary of DatNodes and groups titles together that are the
        same, but have different names as defined by the related clone list.

        This is the primary function that deals with the fact that, for example,
        Title, The (USA) is equivalent to Title, Le (France).

        Args:
            - `processed_titles (dict[str, set[DatNode]])` A work in progress dictionary
              of DatNodes, originally populated from the input DAT and actively being worked
              on by Retool.

            - `config (Config)` The Retool config object.

            - `input_dat (Dat)` The Retool input_dat object.

            - `is_includes (bool, optional)` Set to `True` when processing includes. Is
              only used to produce reliable reporting when performing a trace. Defaults to
              `False`.

        Returns:
            `dict[str, set[DatNode]]` A dictionary of DatNodes that has had all like
            titles grouped together as defined by the related clone list.
        """

        if input_dat.clone_list.variants:
            eprint('* Analyzing clone list variants... ', sep=' ', end='', flush=True)

            report_on_match: bool = False
            warning_given: bool = False
            missing_titles: set[str] = set()
            delete_titles: set[tuple[DatNode, str]] = set()

            for value in input_dat.clone_list.variants:
                if type(value) is dict:
                    if not (
                        'group' and
                        ('titles' in value
                        or 'compilations' in value
                        or 'supersets' in value)):
                            if config.user_input.verbose:
                                warning_given = True
                                printwrap(
                                    f'{Font.warning}* The following variants entry is invalid, '
                                    f'as it\'s missing a {Font.bold}group{Font.warning} key and '
                                    f'one of the following keys: {Font.bold}titles{Font.warning}, '
                                    f'{Font.bold}compilations{Font.warning}, or '
                                    f'{Font.bold}supersets{Font.warning}',
                                    'error')
                                eprint(f'\n  {value}{Font.end}')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()
                            continue
                else:
                    if config.user_input.verbose:
                        warning_given = True
                        printwrap(
                            f'{Font.warning}* The following variants entry isn\'t an object '
                            f'and will be skipped:',
                            'error')
                        eprint(f'\n  {value}{Font.end}')

                        if config.user_input.warningpause:
                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                            input()
                    continue


                def process_variants(variant_titles: list[dict[str, Any]], variant_type: str, report_on_match: bool) -> None:
                    """ Looks up a variant from a clone list and modifies its DatNode entry
                    accordingly.

                    Args:
                        - `variant_titles (list[dict[str, str])` The titles, supersets, or
                          compilations array from a variants object in the clone list.

                        - `variant_type (str)` The type of variant being processed, either
                          'title', 'compilation', or 'superset'.

                        - `report_on_match (bool)` Whether Retool needs to report any
                          titles being traced.
                    """

                    variants: list[DatNode] = []

                    for variant_title in variant_titles:
                        if 'searchTerm' not in variant_title:
                            printwrap(
                                f'{Font.warning}* The following variants entry is missing a '
                                f'{Font.bold}searchTerm{Font.warning} key and will be skipped:',
                                'error')
                            eprint(f'\n  {variant_title}{Font.end}')

                            if config.user_input.warningpause:
                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                input()
                            continue
                        else:
                            variant_name = variant_title['searchTerm']

                        name_type: str = ''

                        if 'nameType' in variant_title:
                            name_type = variant_title['nameType']
                            if not (name_type == 'full'
                                or name_type == 'short'
                                or name_type == 'regionFree'
                                or name_type == 'tagFree'
                                or name_type == 'regex'):
                                    name_type = 'short'
                        else:
                            name_type = 'short'

                        # Look up the title in the dictionary, then process the required changes
                        found_titles: set[DatNode] = set()

                        if name_type == 'regex':
                            valid_regex: list[str] = regex_test([variant_name], 'variants', 'clone list')

                            if not valid_regex:
                                continue

                            found_titles = TitleTools.find_title(variant_name, name_type, processed_titles, missing_titles, config, deep_search=True)
                        else:
                            found_titles = TitleTools.find_title(variant_name, name_type, processed_titles, missing_titles, config)

                        old_group_names: set[str] = set()

                        for title in found_titles:
                            old_group_names.add(title.group_name)

                        new_group_name: str = TitleTools.get_group_name(value['group'], config)

                        new_group_name = new_group_name.lower()

                        if new_group_name not in processed_titles:
                            processed_titles[new_group_name] = set()

                        # If the title's not found in the DAT, add it to missing_titles,
                        # otherwise add it to the delete list, then move it to the new
                        # group
                        if not found_titles:
                            missing_titles.add(variant_name)
                        else:
                            if config.user_input.trace:
                                report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                            for title in found_titles:
                                for old_group_name in old_group_names:
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
                                            variant_type == 'title'
                                            or variant_type == 'superset'):
                                                new_title: DatNode = copy.deepcopy(title)

                                                if 'priority' in variant_title:
                                                    if new_title.clonelist_priority == 1:
                                                        new_title.clonelist_priority = variant_title['priority']

                                                if variant_type == 'superset':
                                                    new_title.is_superset = True

                                                variants.append(new_title)

                                                for old_group_name in old_group_names:
                                                    if title in processed_titles[old_group_name]:
                                                        delete_titles.add((title, old_group_name))

                                        elif variant_type =='compilation':
                                            for compilation_title in processed_titles[old_group_name]:
                                                if compilation_title.full_name == title.full_name:
                                                    title_position: int = 1
                                                    if 'titlePosition' in variant_title:
                                                        title_position = variant_title['titlePosition']

                                                    if 'priority' in variant_title:
                                                        clonelist_priority: int = variant_title['priority']
                                                    else:
                                                        clonelist_priority = 1

                                                    compilation_title.contains_titles[value['group']] = {"position": title_position, "priority": clonelist_priority}

                                                    if 'compilationPriority' in variant_title:
                                                        compilation_title.clonelist_priority = variant_title['compilationPriority']

                    # Set these variant properties after the processing, to make sure they
                    # don't mess with title look ups
                    for variant in variants:
                        variant.group_name = new_group_name
                        variant.short_name = value['group'].lower()
                        processed_titles[new_group_name].add(variant)

                if 'titles' in value:
                    process_variants(value['titles'], 'title', report_on_match)
                if 'compilations' in value:
                    process_variants(value['compilations'], 'compilation', report_on_match)
                if 'supersets' in value:
                    process_variants(value['supersets'], 'superset', report_on_match)

            # Delete titles from old groups, and clean up empty groups
            for title, old_group_name in delete_titles:
                if title in processed_titles[old_group_name]:
                    processed_titles[old_group_name].remove(title)

                if not processed_titles[old_group_name]:
                    del processed_titles[old_group_name]

            if missing_titles and config.user_input.verbose:
                eprint('')
                printwrap(
                    f'{Font.warning}* The following variants titles in the '
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
                    eprint('* Analyzing clone list variants... done')
            else:
                eprint('done.')

        return processed_titles