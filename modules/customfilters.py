import re
import sys

from modules.classes import DatNode
from modules.titleutils import get_raw_title
from modules.utils import old_windows


def check_include_match(user_input, title):
    exclude_match = False
    include_match = False

    # Make sure no system excludes override the match
    for item in user_input.system_excludes:
        if item.startswith('/'):
            if (
                re.search(item[1:], title) != None
                and title not in user_input.system_excludes):
                    exclude_match = True
        elif item.startswith('|'):
            if item[1:] == title:
                exclude_match = True
        else:
            if item in title:
                exclude_match = True

    if exclude_match == True:
        includes = user_input.system_includes
    else:
        includes = user_input.global_includes + user_input.system_includes


    for include in includes:
        include = include.lower()

        if (
            not include.startswith('/')
            and not include.startswith('|')):
                if include in title.lower():
                    include_match = True
        elif include.startswith('/'):
            if re.search(include[1:], title.lower()) != None:
                    include_match = True
        elif include.startswith('|'):
            if include[1:] == title.lower():
                include_match = True

    return include_match


def custom_exclude_filters(user_input, node, filter_list_exclude, exclude_name_for_log, filter_list_include):
    """ Figure out custom global/system filter includes and excludes """

    if user_input.removed_titles.get(exclude_name_for_log) == None:
        user_input.removed_titles[exclude_name_for_log] = []

    exclude_match = False

    for item in filter_list_exclude:
        # First test if the title matches any exclude strings
        if item.startswith('/'):
            if (
                re.search(item[1:], node.description.parent['name']) != None
                and node.description.parent['name'] not in filter_list_include):
                    exclude_match = True
        elif item.startswith('|'):
            if item[1:] == node.description.parent['name']:
                exclude_match = True
        else:
            if item in node.description.parent['name']:
                exclude_match = True

    # Now make sure there are no includes that override it. If not,
    # add the title to the remove log
    if exclude_match == True:
        for item in filter_list_include:
            if item.startswith('/'):
                if (
                    re.search(item[1:], node.description.parent['name']) != None
                    and node.description.parent['name'] not in filter_list_include):
                        return False
            elif item.startswith('|'):
                if item[1:] == node.description.parent['name']:
                    return False
            elif item in node.description.parent['name']:
                    return False

    if exclude_match == True:
        user_input.removed_titles[exclude_name_for_log].append(node.description.parent['name'])

    return exclude_match


def recover_titles_for_custom_filters(user_input, input_dat, dat_numbered, recovered_groups, region_data, REGEX):
    """ Recovers removed titles when global/system includes are used.
        This can't be in titleutils.py due to circular import. """

    if user_input.global_includes != [] or user_input.system_includes != []:
        recover_xml = input_dat.soup.find_all('game')

        recover_xml_list = []

        for node in recover_xml:
            recover_xml_list.append(node)

        progress = 0
        progress_old = 0
        progress_total = len(recover_xml_list)

        print('* Checking already excluded titles for includes... ', sep='', end='\r', flush=True)

        # Check titles excluded by region
        for node in recover_xml_list:
            progress += 1
            progress_percent = int(progress/progress_total*100)

            if progress_old != progress_percent:
                if old_windows() != True:
                    print(
                            f'* Checking already excluded titles for includes... [{progress_percent}%]',
                            sep='', end='\r', flush=True
                        )
                else:
                    print(
                            f'* Checking already excluded titles for includes... [{progress_percent}%]',
                            end='\r', flush=True
                        )

            include_match = check_include_match(user_input, node.description.parent['name'])

            if include_match == True:
                # Get the group name for the current node, then add it to the groups list
                if dat_numbered == False:
                    group_name = get_raw_title(node.description.parent['name'])
                else:
                    group_name = get_raw_title(node.description.parent['name'][7:])

                if group_name not in recovered_groups:
                    recovered_groups[group_name] = []

                # Figure out what region the title is in
                region = ''

                for region in region_data.all:
                    if re.search('\((.*?,){0,} {0,}' + region + '(,.*?){0,}\)', node.description.parent['name']) != None:
                        region = re.search('\((.*?,){0,} {0,}' + region + '(,.*?){0,}\)', node.description.parent['name'])[0][1:-1]
                        break

                if region == '': region = 'Unknown'

                recovered_groups[group_name].append(
            DatNode(node, region, region_data, user_input, input_dat, dat_numbered, REGEX))

            progress_old = progress_percent

    # Check other excluded titles
    for recovered in user_input.recovered_titles:
        for title in user_input.recovered_titles[recovered]:
            include_match = check_include_match(user_input, title.full_name)

            if include_match == True:
                # Get the group name for the current title, then add it to the groups list
                group_name = title.group
                if group_name not in recovered_groups:
                    recovered_groups[group_name] = []

                if title not in recovered_groups[group_name]:
                    recovered_groups[group_name].append(title)

    if old_windows() != True:
        sys.stdout.write("\033[K")
    print('* Checking already excluded titles for includes... done. ') # Intentional trailing space for Win 7
    return recovered_groups