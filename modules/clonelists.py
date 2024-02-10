from __future__ import annotations

import copy
import hashlib
import itertools
import json
import pathlib
import re
import sys

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from hashlib import _Hash
    from modules.config import Config
    from modules.dats import Dat, DatNode
    from modules.input import UserInput

from modules.titletools import Removes, TitleTools, TraceTools
from modules.utils import download, eprint, ExitRetool, Font, pattern2string, printwrap, regex_test


class CloneList:
    def __init__(self,
                 min_retool_version: str='2.02',
                 mias: list[str] = [],
                 variants: list[dict[str, Any]] = []):
        """ Creates an object that contains data originally stored in a clone list.

        Args:
            - `min_retool_version (str, optional)` The minimum Retool version required to
              process the imported clone list. Defaults to `2.00`.

            - `mias (list[str], optional)` A list to store the `mias` arrary found in a
              related clone list, if it exists. Defaults to `[]`.

            - `variants (dict[str, list[dict[str, Any]]], optional)` A dictionary to store
              the `variants` object found in a related clone list, if it exists. Defaults to
              `{}`.
        """

        self.min_retool_version: str = min_retool_version
        self.mias: list[str] = mias
        self.variants: list[dict[str, Any]] = variants


class CloneListTools(object):
    """ Methods for applying clone list entries to a dictionary of DatNode titles. """


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
    def local_name(variant_title: dict[str, Any], new_title: DatNode, config: Config, report_on_match: bool) -> None:
        """ Applies local names from a clone list to a variant

        Args:
            - `variant_title (dict[str, Any])`: The variant entry from the clone list.

            - `new_title (DatNode)`: The new title DatNode object to apply the local name to.

            - `report_on_match (bool)` Whether Retool needs to report any
                titles being traced.
        """

        if variant_title['localNames']:
            # Check if a system config is in play
            local_name_user_order_language_codes: list[str] = []

            if config.system_localization_order_user:
                if {'override': 'true'} in config.system_localization_order_user:
                    local_name_user_order_language_codes = [str(x) for x in config.system_localization_order_user if 'override' not in x]
            elif config.localization_order_user:
                local_name_user_order_language_codes = [x for x in config.localization_order_user]

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

            # Readd the tags to the local name where appropriate
            if new_title.local_name:
                tags = pattern2string(re.compile(' \\(.*'), new_title.full_name)
                new_title.local_name = f'{new_title.local_name}{tags}'

            if report_on_match:
                eprint('')
                TraceTools.trace_title('REF0111')
                eprint(f'  New name: {new_title.local_name}\n{Font.disabled}  Old name: {new_title.full_name}{Font.end}')
                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                input()


    @staticmethod
    def process_variants(variant_titles: list[dict[str, Any]], variant_type: str, value: dict[str, Any], processed_titles: dict[str, set[DatNode]], missing_titles: set[str], delete_titles: set[tuple[DatNode, str]], removes: Removes, is_includes: bool, config: Config, report_on_match: bool) -> None:
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

            new_group_name: str = value['group'].lower()

            if new_group_name not in processed_titles:
                processed_titles[new_group_name] = set()

            # If the title's not found in the DAT, add it to missing_titles,
            # otherwise add it to the delete list, then move it to the new
            # group with any new properties defined by the clone list
            if not found_titles:
                missing_titles.add(variant_name)
            else:
                if config.user_input.trace:
                    report_on_match = TraceTools.trace_enable(set(found_titles), config.user_input.trace)

                for title in found_titles:
                    # Manage ignores
                    if 'ignore' in variant_title:
                        if type(variant_title['ignore']) is bool:
                            if variant_title['ignore'] == True:
                                if title in processed_titles[title.group_name]:
                                    if report_on_match:
                                        eprint('')
                                        TraceTools.trace_title('REF0054')
                                        eprint(f'{Font.disabled}- Remove: {title.full_name}{Font.end}')
                                        eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                        input()

                                    processed_titles[title.group_name].remove(title)
                                    title.exclude_reason = 'Clone list remove'
                                    removes.clone_list_removes.add(title)
                        else:
                            if config.user_input.verbose:
                                printwrap(
                                    f'{Font.warning}* The following variant title\'s '
                                    f'"ignore" key isn\'t a boolean, so it has been kept:',
                                    'error')
                                eprint(f'\n  {variant_title["searchTerm"]}{Font.end}')

                                if config.user_input.warningpause:
                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                    input()

                    # Manage categories
                    if 'categories' in variant_title:
                        if type(variant_title['categories']) is list:
                            if title in processed_titles[title.group_name]:
                                if report_on_match:
                                    eprint('')
                                    TraceTools.trace_title('REF0053')
                                    eprint(f'* {title.full_name}')
                                    eprint(f'  New categories: {variant_title["categories"]}\n{Font.disabled}  Old categories: {title.categories}{Font.end}')
                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                    input()

                                title.categories = variant_title['categories']
                        else:
                            if config.user_input.verbose:
                                printwrap(
                                    f'{Font.warning}* The following variant title\'s '
                                    f'"categories" key isn\'t an array, so no category has been assigned:',
                                    'error')
                                eprint(f'\n  {variant_title["searchTerm"]}{Font.end}')

                                if config.user_input.warningpause:
                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                    input()

                    # Work through the remaining variants
                    for old_group_name in old_group_names:
                        if title in processed_titles[old_group_name]:
                            if (
                                variant_type == 'title'
                                or variant_type == 'superset'):
                                    new_title: DatNode = copy.deepcopy(title)

                                    if 'priority' in variant_title:
                                        if new_title.clonelist_priority == 1:
                                            new_title.clonelist_priority = variant_title['priority']

                                    if variant_type == 'superset':
                                        new_title.is_superset = True

                                    for old_group_name in old_group_names:
                                        if title in processed_titles[old_group_name]:
                                            delete_titles.add((title, old_group_name))

                                    # Manage local names
                                    if 'localNames' in variant_title:
                                        CloneListTools.local_name(variant_title, new_title, config, report_on_match)

                                    # Manage English-friendly titles
                                    if 'englishFriendly' in variant_title:
                                        if type(variant_title['englishFriendly']) is bool:
                                            if variant_title['englishFriendly']:
                                                if title in processed_titles[title.group_name]:
                                                    if report_on_match:
                                                        eprint('')
                                                        TraceTools.trace_title('REF0112')
                                                        eprint(f'* {new_title.full_name}')

                                                        if config.user_input.warningpause:
                                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                            input()

                                                    if 'En' not in new_title.languages:
                                                        new_title.languages = (*new_title.languages, 'En')

                                    # Manage filters
                                    if 'filters' in variant_title:
                                        # Check if at least one condition and result keys exist
                                        exception_condition_found: bool = False
                                        exception_result_found: bool = False

                                        try:
                                            variant_title['filters'][0]['conditions']
                                            exception_condition_found = True
                                        except:
                                            pass

                                        try:
                                            variant_title['filters'][0]['results']
                                            exception_result_found = True
                                        except:
                                            pass

                                        exception_error_message: str = ''

                                        if exception_condition_found==False and exception_result_found==False:
                                            print(f'\n{exception_condition_found}\n')
                                            print(f'\n{exception_result_found}\n')
                                            exception_error_message = 'conditions and results object'
                                        elif not exception_condition_found:
                                            exception_error_message = 'conditions object'
                                        elif not exception_result_found:
                                            exception_error_message = 'results object'

                                        if exception_error_message:
                                            printwrap(
                                                f'{Font.warning}* The following variant title\'s '
                                                f'"filters" array is missing a {exception_error_message}, so no '
                                                'changes have been made:',
                                                'error')
                                            eprint(f'\n  {variant_title["searchTerm"]}{Font.end}')

                                            if config.user_input.warningpause:
                                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                input()

                                        # Make sure all filters are true for them to be processed
                                        if exception_condition_found and exception_result_found:
                                            for filter_condition in variant_title['filters']:
                                                condition_match_languages: bool = True
                                                condition_match_regions: bool = True
                                                condition_match_string: bool = True
                                                condition_region_order: bool = True

                                                if 'matchLanguages' in filter_condition['conditions']:
                                                    if not all([x in title.languages for x in filter_condition['conditions']['matchLanguages']]):
                                                        condition_match_languages = False
                                                if 'matchRegions' in filter_condition['conditions']:
                                                    if not all([x in title.regions for x in filter_condition['conditions']['matchRegions']]):
                                                        condition_match_regions = False
                                                if 'matchString' in filter_condition['conditions']:
                                                    if not pattern2string(re.compile(filter_condition['conditions']['matchString']), title.full_name):
                                                        condition_match_string = False
                                                if 'regionOrder' in filter_condition['conditions']:
                                                    # Look for the regions that need to be higher in priority than
                                                    # those defined in "higher than"
                                                    if 'higherRegions' in filter_condition['conditions']['regionOrder']:
                                                        regions: list[str] = filter_condition['conditions']['regionOrder']['higherRegions']
                                                    else:
                                                        printwrap(
                                                            f'{Font.warning}* The following exception\'s '
                                                            f'"higherRegions" key isn\'t an array and will be '
                                                            'skipped:', 'error')
                                                        eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                                        if config.user_input.warningpause:
                                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                            input()

                                                    # Look for the regions that need to be lower in priority than the
                                                    # those defined in "region"
                                                    if 'lowerRegions' in filter_condition['conditions']['regionOrder']:
                                                        higher_than_regions: list[str] = filter_condition['conditions']['regionOrder']['lowerRegions']
                                                    else:
                                                        printwrap(
                                                            f'{Font.warning}* The following exception\'s '
                                                            f'"lowerRegions" key isn\'t an array and will be '
                                                            'skipped:', 'error')
                                                        eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                                        if config.user_input.warningpause:
                                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                            input()

                                                    # Check if a system config is in play
                                                    region_order: list[str] = config.region_order_user

                                                    if config.system_region_order_user:
                                                        if {'override': 'true'} in config.system_region_order_user:
                                                            region_order = [str(x) for x in config.system_region_order_user if 'override' not in x]

                                                    # Parse the "All other regions" entry
                                                    if (
                                                        "All other regions" in regions
                                                        and "All other regions" in higher_than_regions
                                                        ):
                                                            printwrap(
                                                                f'{Font.warning}* The following exception has "All other regions" '
                                                                f'in both the "higherRegions" and "lowerRegions" keys, and will be '
                                                                f'skipped:', 'error')
                                                            eprint(f'\n  {value["searchTerm"]}{Font.end}')

                                                            if config.user_input.warningpause:
                                                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                                input()
                                                            continue

                                                    # Fix UK problem
                                                    if 'UK' in regions:
                                                            if 'United Kingdom' not in regions:
                                                                regions.append('United Kingdom')
                                                    if 'United Kingdom' in regions:
                                                        if 'UK' not in regions:
                                                            regions.append('UK')

                                                    if 'UK' in higher_than_regions:
                                                            if 'United Kingdom' not in higher_than_regions:
                                                                higher_than_regions.append('United Kingdom')
                                                    if 'United Kingdom' in higher_than_regions:
                                                        if 'UK' not in higher_than_regions:
                                                            higher_than_regions.append('UK')

                                                    # Import all other regions if needed
                                                    if regions == ["All other regions"]:
                                                        regions = [x for x in config.region_order_default if x not in higher_than_regions]

                                                    if higher_than_regions == ["All other regions"]:
                                                        higher_than_regions = [x for x in config.region_order_default if x not in regions]

                                                    # Check that the regions are available in the user's current region
                                                    # order, and store their priority if so
                                                    higher_regions: list[int] = [i for i, region in enumerate(region_order) if region in regions]
                                                    lower_regions: list[int] = [i for i, region in enumerate(region_order) if region in higher_than_regions]

                                                    # If any of the higher regions is higher than ALL of the lower regions
                                                    # move the title to the new group.
                                                    if higher_regions and lower_regions:
                                                        lower_regions_lowest: int = int(sorted(lower_regions)[0])

                                                        condition_region_order = False

                                                        for higher_region in higher_regions:
                                                            if higher_region < lower_regions_lowest:
                                                                condition_region_order = True

                                                if (
                                                    condition_match_languages
                                                    and condition_match_regions
                                                    and condition_match_string
                                                    and condition_region_order
                                                ):
                                                    if 'categories' in filter_condition['results']:
                                                        if report_on_match:
                                                            eprint('')
                                                            TraceTools.trace_title('REF0108')
                                                            eprint(f'* {title.full_name}')
                                                            eprint(f'  New categories: {variant_title["categories"]}\n{Font.disabled}  Old categories: {title.categories}{Font.end}')
                                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                            input()

                                                        new_title.categories = filter_condition['results']['categories']

                                                    if 'group' in filter_condition['results']:
                                                        if not new_title.group_moved_by_condition:
                                                            if (
                                                                report_on_match
                                                                and new_title.group_name != filter_condition['results']['group'].lower()
                                                                and not is_includes):
                                                                    eprint('')
                                                                    TraceTools.trace_title('REF0109')
                                                                    eprint(f'* {new_title.full_name}')
                                                                    eprint(f'  New group: {filter_condition["results"]["group"].lower()}\n{Font.disabled}  Old group: {new_title.group_name}{Font.end}')
                                                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                                    input()

                                                            new_title.group_name_conditional = filter_condition['results']['group'].lower()
                                                            new_title.group_moved_by_condition = True

                                                    if 'localNames' in filter_condition['results']:
                                                        if report_on_match:
                                                            eprint('')
                                                            TraceTools.trace_title('REF0115')
                                                            eprint(f'  New name: {new_title.local_name}\n{Font.disabled}  Old name: {new_title.full_name}{Font.end}')
                                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                            input()

                                                        CloneListTools.local_name(filter_condition['results'], new_title, config, report_on_match)

                                                    if 'englishFriendly' in filter_condition['results']:
                                                        if type(filter_condition['results']['englishFriendly']) is bool:
                                                            if filter_condition['results']['englishFriendly']:
                                                                if report_on_match:
                                                                    eprint('')
                                                                    TraceTools.trace_title('REF0113')
                                                                    eprint(f'* {new_title.full_name}')

                                                                if 'En' not in title.languages:
                                                                    new_title.languages = (*new_title.languages, 'En')

                                                    if 'priority' in filter_condition['results']:
                                                        if report_on_match:
                                                            eprint('')
                                                            TraceTools.trace_title('REF0110')
                                                            eprint(f'* {new_title.full_name}')
                                                            eprint(f'  New priority: {filter_condition["results"]["priority"]}\n{Font.disabled}  Old priority: {new_title.clonelist_priority}{Font.end}')
                                                            eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                            input()

                                                        new_title.clonelist_priority = filter_condition['results']['priority']

                                                    if 'superset' in filter_condition['results']:
                                                        if filter_condition['results']['superset']:
                                                            if report_on_match:
                                                                eprint('')
                                                                TraceTools.trace_title('REF0116')
                                                                eprint(f'* {title.full_name}')
                                                                eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                                                input()

                                                            new_title.is_superset = True

                                    variants.append(new_title)

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

                                        if 'localNames' in variant_title:
                                            CloneListTools.local_name(variant_title, compilation_title, config, report_on_match)

        config.stats.removes_count = len(removes.clone_list_removes)

        # Set these variant properties after the processing, to make sure they
        # don't mess with title look ups
        for variant in variants:
            if variant.group_name_conditional:
                variant.group_name = variant.group_name_conditional
                variant.short_name = variant.group_name_conditional.lower()
                if not variant.group_name_conditional in processed_titles:
                    processed_titles[variant.group_name_conditional] = set()
                processed_titles[variant.group_name_conditional].add(variant)
            else:
                if (
                    report_on_match
                    and variant.group_name != new_group_name
                    and not is_includes):
                        eprint('')
                        TraceTools.trace_title('REF0055')
                        eprint(f'* {variant.full_name}')
                        eprint(f'  New group: {new_group_name}\n{Font.disabled}  Old group: {variant.group_name}{Font.end}')
                        eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                        input()
                variant.group_name = new_group_name
                variant.short_name = value['group'].lower()
                processed_titles[new_group_name].add(variant)


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
                            with open(pathlib.Path(f'{local_path}/{file_name}'), 'r+', newline='\n', encoding='utf-8') as file:
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
    def variants(processed_titles: dict[str, set[DatNode]], config: Config, input_dat: Dat, removes: Removes, is_includes: bool = False) -> dict[str, set[DatNode]]:
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

                title_types: list[str] = ['titles', 'compilations', 'supersets']

                for title_type in title_types:
                    # Assign group-level ignores
                    if 'ignore' in value:
                        if title_type in value:
                            for variant_title in value[title_type]:
                                if not 'ignore' in variant_title:
                                    variant_title['ignore'] = True

                    # Assign group-level categories
                    if 'categories' in value:
                        if type(value['categories']) is list:
                            if title_type in value:
                                for variant_title in value[title_type]:
                                    if not 'categories' in variant_title:
                                        variant_title['categories'] = value['categories']
                        else:
                            if config.user_input.verbose:
                                printwrap(
                                    f'{Font.warning}* The following variant title\'s '
                                    f'"categories" key isn\'t an array, so no category has been assigned:',
                                    'error')
                                eprint(f'\n  {variant_title["searchTerm"]}{Font.end}')

                                if config.user_input.warningpause:
                                    eprint(f'\n{Font.disabled}Press enter to continue{Font.end}')
                                    input()

                    # Process the variants
                    if title_type in value:
                        CloneListTools.process_variants(value[title_type], title_type[:-1], value, processed_titles, missing_titles, delete_titles, removes, is_includes, config, report_on_match)

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
