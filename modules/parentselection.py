import functools
import itertools
import operator
import re
import sys

from modules.titleutils import check_date, get_raw_title
from modules.utils import Font, old_windows, printverbose


def choose_parent(titles, region_data, user_input, dat_numbered, REGEX, ring_code, clonelist=False):
    """ Determines a parent, given a list of DatNode objects

    Redump seems to observe the following tagging order:

    Title (Region) (Languages) (Disc #) (Disc details)
    (Edition [Original, Gold, Special, Deluxe, Game of the Year, Demo, Covermount, budget release, publisher/distributor, other])
    (Version/revision) (Dev status [Alpha, Beta, Proto]) (Special [EDC, Serial, Ring/Mastering Code, CRC])
    (License [Unl]) (Rerelease) (OEM/Hibaihin) (Date) (Alt)

    This is an evolution of the existing No-intro tagging order.
    """

    parents = titles.copy()

    # 1) Handle modern titles like Virtual Console, Mini Console, and other
    # collections ripped from other platforms
    for edition in user_input.tag_strings.modern_editions:
        if user_input.modern == False:
            choose_string(re.compile(edition, re.IGNORECASE), user_input, region_data, parents, REGEX, False, clonelist)
        else:
            choose_string(re.compile(edition, re.IGNORECASE), user_input, region_data, parents, REGEX, True, clonelist)

    # 2) Check for versions and revisions, and select the highest of each
    choose_version_revision(REGEX.version, parents, REGEX, 2, -1)
    choose_version_revision(REGEX.long_version, parents, REGEX, 8, -1)
    choose_version_revision(REGEX.fds_version, parents, REGEX, 3, -1)
    choose_version_revision(REGEX.revision, parents, REGEX, 5, -1)
    choose_version_revision(REGEX.beta, parents, REGEX, 6, -1, True)
    choose_version_revision(REGEX.alpha, parents, REGEX, 7, -1, True)
    choose_version_revision(REGEX.proto, parents, REGEX, 7, -1, True)

    # 3) Check for Sega/Panasonic ring codes
    if ring_code == True:
        choose_ring_code(REGEX, parents, user_input, region_data)

    # 4) If one title supports different languages to another, cycle through the implied
    # language order until one title doesn't have the required language
    parents_temp = parents.copy()

    for title_1, title_2 in itertools.combinations(parents_temp, 2):
        if (
            (
                clonelist == False
                and title_1.short_name_lower == title_2.short_name_lower
                )
            or
            (
                clonelist == True
                )):
                    choose_implied_language(title_1, title_2, parents, user_input, region_data)

    # 5) Preference titles with more regions. In the case of equal number of regions,
    # check for the current region as the primary region, then take the title with the
    # highest priority secondary region.
    parents_temp = parents.copy()

    for title_1, title_2 in itertools.combinations(parents_temp, 2):
        if (
            title_1.short_name_lower == title_2.short_name_lower
            and '[bios]' not in title_1.full_name_lower
            and '[bios]' not in title_2.full_name_lower):
            if (
                len(re.findall(',', title_1.regions))
                > len(re.findall(',', title_2.regions))):
                    if title_2 in parents: parents.remove(title_2)
            elif (
                len(re.findall(',', title_2.regions))
                > len(re.findall(',', title_1.regions))):
                    if title_1 in parents: parents.remove(title_1)
            elif (
                len(re.findall(',', title_2.regions))
                == len(re.findall(',', title_1.regions))):
                    if title_1.primary_region != title_2.primary_region:
                        for region in user_input.user_region_order:
                            if region in title_1.primary_region:
                                if title_2 in parents: parents.remove(title_2)
                                break
                            if region in title_2.primary_region:
                                if title_1 in parents: parents.remove(title_1)
                                break
                    elif (
                        title_1.primary_region == title_2.primary_region
                        and title_1.secondary_region != title_2.secondary_region):
                            for region in user_input.user_region_order:
                                if region in title_1.secondary_region:
                                    if title_2 in parents: parents.remove(title_2)
                                    break
                                if region in title_2.secondary_region:
                                    if title_1 in parents: parents.remove(title_1)
                                    break

    # 6) Choose higher dates where possible
    choose_date(REGEX.dates, parents)

    # 7) Choose good, original versions over alternates
    choose_string(REGEX.alt, user_input, region_data, parents, REGEX, False, clonelist)
    choose_string(REGEX.oem, user_input, region_data, parents, REGEX, False, clonelist)
    choose_string(REGEX.bad, user_input, region_data, parents, REGEX, False, clonelist)
    choose_string(REGEX.hibaihin, user_input, region_data, parents, REGEX, False, clonelist)
    choose_string(REGEX.covermount, user_input, region_data, parents, REGEX, False, clonelist)
    choose_string(REGEX.rerelease, user_input, region_data, parents, REGEX, False, clonelist)
    choose_string(REGEX.edc, user_input, region_data, parents, REGEX, True, clonelist)

    # 8) Deal with promotions and demotions of editions
    for edition in user_input.tag_strings.promote_editions:
        choose_string(re.compile(edition, re.IGNORECASE), user_input, region_data, parents, REGEX, True, clonelist)

    for edition in user_input.tag_strings.demote_editions:
        choose_string(re.compile(edition, re.IGNORECASE), user_input, region_data, parents, REGEX, False, clonelist)

    # 9) Deal with "Made in" titles for Sega CD and Sega Saturn
    if ring_code == True:
        for title_1, title_2 in itertools.combinations(parents_temp, 2):
            if 'Made in' in title_1.full_name and 'Made in' in title_2.full_name:
                if (
                    title_1.primary_region in re.search(
                        '\(Made in.*?\)', title_1.full_name)[0].replace('.', '').replace('EU', 'Europe')):
                    if title_2 in parents: parents.remove(title_2)
                if (
                    title_2.primary_region in re.search(
                        '\(Made in.*?\)', title_2.full_name)[0].replace('.', '').replace('EU', 'Europe')):
                    if title_1 in parents: parents.remove(title_1)

    # Assign clones
    for parent in parents:
        for title in titles:
            if (
                (
                    title in [x for x in titles if x not in parents]
                    and title.short_name_lower == parent.short_name_lower
                    and clonelist == False)
                or (
                    title in [x for x in titles if x not in parents]
                    and clonelist == True)):
                        if dat_numbered == False:
                            title.cloneof = parent.full_name
                        else:
                            title.cloneof = parent.numbered_name

                        title.cloneof_group = parent.group

            # Override clones if a string match found in user
            # defined include lists
            if user_input.no_filters == False:
                for include in user_input.global_includes + user_input.system_includes:
                    include = include.lower()

                    if (
                        not include.startswith('/')
                        and not include.startswith('|')):
                            if include in title.full_name_lower:
                                title.cloneof = ''
                                title.group = ''
                    elif include.startswith('/'):
                            if re.search(include[1:], title.full_name_lower) != None:
                                title.cloneof = ''
                                title.group = ''
                    elif include.startswith('|'):
                        if include[1:] == title.full_name_lower:
                            title.cloneof = ''
                            title.group = ''
    return titles


def choose_cross_region_parents(titles, user_input, dat_numbered, REGEX):
    """ Finds parents given a list of DatNode objects from multiple regions.

    This assumes choose_parent has already been run across all regions prior to them
    being processed here.
    """

    # Add titles from all regions into a single dict
    for region, groups in titles.regions.items():
        for group, disc_titles in groups.items():
            if group not in titles.all:
                titles.all[group] = []

            for title in disc_titles:
                titles.all[group].extend([title])

    # Find the cross-region parents
    for key, values in titles.all.items():
        parents = values.copy()

        for title_1, title_2 in itertools.combinations(parents, 2):
            if (
                title_1.short_name_lower == title_2.short_name_lower
                and title_1.regions != title_2.regions
                and '[bios]' not in title_1.full_name_lower
                and '[bios]' not in title_2.full_name_lower):

                # Check to see if titles are preproduction/bad or not. If so, favour
                # production titles
                preprod_title_1 = bool(re.search(REGEX.preproduction_bad, title_1.full_name_lower))
                preprod_title_2 = bool(re.search(REGEX.preproduction_bad, title_2.full_name_lower))

                if preprod_title_1 == True and preprod_title_2 == False:
                    if title_1 in parents: parents.remove(title_1)
                elif preprod_title_2 == True and preprod_title_1 == False:
                    if title_2 in parents: parents.remove(title_2)

                # Check to see if titles are modern rips or not. If so, favour
                # standard titles
                modern_rip_1 = False
                modern_rip_2 = False

                for edition in user_input.tag_strings.modern_editions:
                    if bool(re.search(re.compile(edition, re.IGNORECASE), title_1.full_name_lower)): modern_rip_1 = True
                    if bool(re.search(re.compile(edition, re.IGNORECASE), title_2.full_name_lower)): modern_rip_2 = True

                if not (
                    modern_rip_1 == True
                    and modern_rip_2 == True):
                        for edition in user_input.tag_strings.modern_editions:
                            if user_input.modern == False:
                                if bool(re.search(re.compile(edition, re.IGNORECASE), title_1.full_name_lower)) == True:
                                    for language in title_1.languages:
                                        if language in title_2.languages:
                                            if title_1 in parents: parents.remove(title_1)
                                elif bool(re.search(re.compile(edition, re.IGNORECASE), title_2.full_name_lower)) == True:
                                    for language in title_2.languages:
                                        if language in title_1.languages:
                                            if title_2 in parents: parents.remove(title_2)
                            else:
                                if bool(re.search(re.compile(edition, re.IGNORECASE), title_1.full_name_lower)) == True:
                                    for language in title_1.languages:
                                        if language in title_2.languages:
                                            if title_2 in parents: parents.remove(title_2)
                                elif bool(re.search(re.compile(edition, re.IGNORECASE), title_2.full_name_lower)) == True:
                                    for language in title_2.languages:
                                        if language in title_1.languages:
                                            if title_1 in parents: parents.remove(title_1)

                # Check to see if titles are unlicensed or not. If so, favour
                # production titles
                unl_title_1 = bool(re.search('\(unl\)', title_1.full_name_lower))
                unl_title_2 = bool(re.search('\(unl\)', title_2.full_name_lower))

                if unl_title_1 == True and unl_title_2 == False:
                    if title_1 in parents: parents.remove(title_1)
                elif unl_title_2 == True and unl_title_1 == False:
                    if title_2 in parents: parents.remove(title_2)

        for title_1, title_2 in itertools.combinations(parents, 2):
            if (
                title_1.short_name_lower == title_2.short_name_lower
                and title_1.regions != title_2.regions
                and '[bios]' not in title_1.full_name_lower
                and '[bios]' not in title_2.full_name_lower):
                for region in user_input.user_region_order:
                    if (
                        region in title_1.regions
                        and region not in title_2.regions
                        and title_1.cloneof == ''):
                        if title_2 in parents: parents.remove(title_2)
                        break
                    elif (
                        region in title_2.regions
                        and region not in title_1.regions
                        and title_2.cloneof == ''):
                        if title_1 in parents: parents.remove(title_1)
                        break
                    elif (
                        region in title_1.regions
                        and region in title_2.regions
                        and title_1.primary_region != title_2.primary_region):

                        if title_1.cloneof == '':
                            if title_2 in parents:
                                parents.remove(title_2)
                                break
                        elif title_2.cloneof == '':
                            if title_1 in parents:
                                parents.remove(title_1)
                                break

        # Assign clones
        for parent in parents:
            for title in values:
                if (
                    title in [x for x in values if x not in parents]
                    and title.short_name_lower == parent.short_name_lower
                    and parent.cloneof == ''):
                        if dat_numbered == False:
                            title.cloneof = parent.full_name
                        else:
                            title.cloneof = parent.numbered_name

                        title.cloneof_group = get_raw_title(parent.full_name)

    return titles


def choose_date(string, title_list):
    """ Checks two titles from a list for a date. If one has a date and the other doesn't,
    remove the title without the date.

    If both titles have a date, remove the title with the oldest date."""

    title_list_temp = title_list.copy()

    for title_1, title_2 in itertools.combinations(title_list_temp, 2):
        if (
            title_1.short_name_lower == title_2.short_name_lower
            and '[bios]' not in title_1.full_name_lower
            and '[bios]' not in title_2.full_name_lower):
            if (
                re.search(string, title_1.full_name_lower) != None
                and re.search(string, title_2.full_name_lower) == None
                and check_date(string, title_1.full_name_lower) != False):
                    if title_2 in title_list: title_list.remove(title_2)
            elif (
                re.search(string, title_2.full_name_lower) != None
                and re.search(string, title_1.full_name_lower) == None
                and check_date(string, title_2.full_name_lower) != False):
                    if title_1 in title_list: title_list.remove(title_1)
            elif (
                re.search(string, title_1.full_name_lower) != None
                and re.search(string, title_2.full_name_lower) != None
                and check_date(string, title_1.full_name_lower) != False
                and check_date(string, title_2.full_name_lower) != False):
                    if check_date(string, title_1.full_name_lower) > check_date(string, title_2.full_name_lower):
                        if title_2 in title_list: title_list.remove(title_2)
                    elif check_date(string, title_2.full_name_lower) > check_date(string, title_1.full_name_lower):
                        if title_1 in title_list: title_list.remove(title_1)


def choose_ring_code(REGEX, title_list, user_input, region_data):
    """ Checks two titles from a list and removes the one with the
    lowest ring code.
    """

    choose_string(REGEX.sega_ring_code, user_input, region_data, title_list, REGEX, True)

    title_list_temp = title_list.copy()

    for title_1, title_2 in itertools.combinations(title_list_temp, 2):
        if title_1.short_name_lower == title_2.short_name_lower:
            if (
                re.search(REGEX.sega_ring_code, title_1.full_name_lower) != None
                and re.search(REGEX.sega_ring_code, title_2.full_name_lower) != None):
                    title_1_ring_code = re.search(REGEX.sega_ring_code, title_1.full_name_lower)[0]
                    title_2_ring_code = re.search(REGEX.sega_ring_code, title_2.full_name_lower)[0]

                    # Get the highest version ring code
                    if (
                        re.search(REGEX.sega_ring_code_re, title_1_ring_code) == None
                        and re.search(REGEX.sega_ring_code_re, title_2_ring_code) == None):
                            title_1_highest_ring_code = int(re.search('[0-9]{1,2}[A-Z]\)', title_1_ring_code, re.IGNORECASE)[0][:-2])
                            title_2_highest_ring_code = int(re.search('[0-9]{1,2}[A-Z]\)', title_2_ring_code, re.IGNORECASE)[0][:-2])

                            if title_1_highest_ring_code > title_2_highest_ring_code:
                                if title_2 in title_list: title_list.remove(title_2)
                            elif title_2_highest_ring_code > title_1_highest_ring_code:
                                if title_1 in title_list: title_list.remove(title_1)
                    elif (
                        re.search(REGEX.sega_ring_code_re, title_1_ring_code) == None
                        and re.search(REGEX.sega_ring_code_re, title_2_ring_code) != None):
                            if title_1 in title_list: title_list.remove(title_1)
                    elif (
                        re.search(REGEX.sega_ring_code_re, title_2_ring_code) == None
                        and re.search(REGEX.sega_ring_code_re, title_1_ring_code) != None):
                            if title_2 in title_list: title_list.remove(title_2)
                    elif (
                        re.search(REGEX.sega_ring_code_re, title_2_ring_code) != None
                        and re.search(REGEX.sega_ring_code_re, title_1_ring_code) != None):
                            if (
                                re.search('[0-9]', title_1_ring_code) != None
                                and re.search('[0-9]', title_2_ring_code) == None):
                                    if title_1 in title_list: title_list.remove(title_1)
                            elif (
                                re.search('[0-9]', title_2_ring_code) != None
                                and re.search('[0-9]', title_1_ring_code) == None):
                                    if title_1 in title_list: title_list.remove(title_1)
                            elif (
                                re.search('[0-9]', title_2_ring_code) != None
                                and re.search('[0-9]', title_1_ring_code) != None):
                                    title_1_highest_ring_code = re.search(
                                        '\d+', title_1_ring_code)[0]
                                    title_2_highest_ring_code = re.search(
                                        '\d+', title_2_ring_code)[0]

                                    if title_1_highest_ring_code > title_2_highest_ring_code:
                                        if title_2 in title_list: title_list.remove(title_2)
                                    elif title_2_highest_ring_code > title_1_highest_ring_code:
                                        if title_1 in title_list: title_list.remove(title_1)


def choose_string(string, user_input, region_data, title_list, REGEX, choose_title_with_string=False, clonelist=False):
    """ Checks two titles from a list for a string. Remove the title with the string
    from the supplied list.

    For example:
    This is a title
    This is a title (Alt)

    Feed in the string '(Alt)' to remove 'This is a title (Alt)' from the supplied
    list.
    """

    title_list_temp = title_list.copy()

    for title_1, title_2 in itertools.combinations(title_list_temp, 2):
        if (
            (
                title_1.short_name_lower == title_2.short_name_lower
                and clonelist == False)
        or (
            clonelist == True)):
                if (
                    '[bios]' not in title_1.full_name_lower
                    and '[bios]' not in title_2.full_name_lower):
                        if (
                            re.search(string, title_1.full_name_lower) != None
                            and re.search(string, title_2.full_name_lower) == None):
                            if choose_title_with_string == False:
                                if title_1 in title_list: title_list.remove(title_1)
                            else:
                                if title_2 in title_list: title_list.remove(title_2)
                        elif (
                            re.search(string, title_2.full_name_lower) != None
                            and re.search(string, title_1.full_name_lower) == None):
                                if choose_title_with_string == False:
                                    if title_2 in title_list: title_list.remove(title_2)
                                else:
                                    if title_1 in title_list: title_list.remove(title_1)
                        elif (
                            # If both titles have the specified string
                            re.search(string, title_2.full_name_lower) != None
                            and re.search(string, title_1.full_name_lower) != None
                            and string != REGEX.sega_ring_code
                            and string != REGEX.sega_ring_code_re):
                                implied_languages = []

                                for region in user_input.user_region_order:
                                    if region_data.implied_language[region] != '':
                                        if region_data.implied_language[region] not in implied_languages:
                                            implied_languages.append(region_data.implied_language[region])

                                # Cycle through implied language order until one
                                # title doesn't have the required language
                                choose_implied_language(title_1, title_2, title_list, user_input, region_data)

                                # A terrible hack. At this point we've run out of options, so select the title that's
                                # longest if certain strings are involved
                                if (
                                    (
                                        title_1 in title_list
                                        and title_2 in title_list
                                        and '[bios]' not in title_1.full_name_lower
                                        and '[bios]' not in title_2.full_name_lower)
                                    and (
                                        'gentei' in str(string).lower()
                                        or 'oem' in str(string).lower())):
                                        for region in region_data.all:
                                            if len(title_2.full_name_lower) < len(title_1.full_name_lower):
                                                if title_2 in title_list: title_list.remove(title_2)
                                            elif len(title_1.full_name_lower) < len(title_2.full_name_lower):
                                                    if title_1 in title_list: title_list.remove(title_1)


def choose_version_revision(string, title_list, REGEX, trim_start, trim_end, preproduction=False):
    """ Checks two titles from a list to see which one has a version/revision tag, or
    which has the highest version. Removes the appropriate title from the supplied
    list.
    """

    title_list_temp = title_list.copy()

    for title_1, title_2 in itertools.combinations(title_list_temp, 2):
        # Check to see if titles are preproduction/bad or not. If so, favour
        # production titles
        preprod_check = []
        preprod_title_1 = bool(re.search(REGEX.preproduction_bad, title_1.full_name_lower))
        preprod_title_2 = bool(re.search(REGEX.preproduction_bad, title_2.full_name_lower))

        preprod_check.extend([preprod_title_1, preprod_title_2])

        if functools.reduce(lambda a,b: a + b, preprod_check) > 0:
            preproduction = True

        if (
            (
                title_1.short_name_lower == title_2.short_name_lower
                and '[bios]' not in title_1.full_name_lower
                and '[bios]' not in title_2.full_name_lower
                and (
                    functools.reduce(lambda a,b: a + b, preprod_check) == 2
                    or functools.reduce(lambda a,b: a + b, preprod_check) == 0))):

                    # Deal with mixed versions and revisions
                    if (
                        re.search(REGEX.revision, title_1.full_name_lower) != None
                        and re.search(REGEX.version, title_2.full_name_lower) != None):
                            if title_1 in title_list: title_list.remove(title_1)
                    elif (
                        re.search(REGEX.revision, title_2.full_name_lower) != None
                        and re.search(REGEX.version, title_1.full_name_lower) != None):
                            if title_2 in title_list: title_list.remove(title_2)

                    # Now the normal version comparisons
                    elif (
                            re.search(string, title_1.region_free_name_lower) != None
                            and re.search(string, title_2.region_free_name_lower) != None):

                            # Find the highest version
                            ver_1 = re.search(string, title_1.region_free_name_lower)[0][trim_start:trim_end]
                            ver_2 = re.search(string, title_2.region_free_name_lower)[0][trim_start:trim_end]

                            if string == re.compile('\(DV [0-9].*?\)', re.IGNORECASE):
                                ver_1 = int(re.search('\d+\)', title_1.full_name_lower)[0][:-1])
                                ver_2 = int(re.search('\d+\)', title_2.full_name_lower)[0][:-1])
                            elif (
                                bool(re.search('[A-Za-z]', ver_1)) == False
                                and bool(re.search('[A-Za-z]', ver_2)) == False
                                and (
                                    len(ver_1) == 2
                                    or len(ver_2) == 2
                                )
                            ):
                                ver_1 = float(ver_1)
                                ver_2 = float(ver_2)

                            if ver_1 > ver_2:
                                if title_2 in title_list: title_list.remove(title_2)
                            elif ver_2 > ver_1:
                                if title_1 in title_list: title_list.remove(title_1)
                    elif (
                        re.search(string, title_1.region_free_name_lower) != None
                        or re.search(string, title_2.region_free_name_lower) != None):
                            if (
                                re.search(string, title_1.full_name_lower) != None
                                and re.search(string, title_2.full_name_lower) == None):
                                    if preproduction == False or functools.reduce(lambda a,b: a + b, preprod_check) == 2:
                                        if title_2 in title_list: title_list.remove(title_2)
                                    else:
                                        if title_1 in title_list: title_list.remove(title_1)
                            elif (
                                re.search(string, title_1.full_name_lower) == None
                                and re.search(string, title_2.full_name_lower) != None):
                                    if preproduction == False or functools.reduce(lambda a,b: a + b, preprod_check) == 2:
                                        if title_1 in title_list: title_list.remove(title_1)
                                    else:
                                        if title_2 in title_list: title_list.remove(title_2)
        elif (
            functools.reduce(lambda a,b: a + b, preprod_check) == 1
            and '[bios]' not in title_1.full_name_lower
            and '[bios]' not in title_2.full_name_lower):

            if preprod_title_1 == True and preprod_title_2 == False:
                if title_1 in title_list: title_list.remove(title_1)
            elif preprod_title_2 == True and preprod_title_1 == False:
                if title_2 in title_list: title_list.remove(title_2)


def choose_implied_language(title_1, title_2, title_list, user_input, region_data):
    """ Cycles through the implied language order until one title doesn't have
    the required language """

    implied_languages = []

    for region in user_input.user_region_order:
        if region_data.implied_language[region] != '':
            if region_data.implied_language[region] not in implied_languages:
                implied_languages.append(region_data.implied_language[region])

    if (
        '[bios]' not in title_1.full_name_lower
        and '[bios]' not in title_2.full_name_lower):
            if (
                title_1.languages != ''
                and title_2.languages != ''
                and title_1.title_languages != ''
                and title_2.title_languages != ''
                and implied_languages != []):
                    for implied_language in implied_languages:
                        if(
                            bool(re.search(implied_language, title_1.languages)) == True
                            and bool(re.search(implied_language, title_2.languages)) == False):
                                if title_2 in title_list: title_list.remove(title_2)
                                break
                        elif(
                            bool(re.search(implied_language, title_2.languages)) == True
                            and bool(re.search(implied_language, title_1.languages)) == False):
                                if title_1 in title_list: title_list.remove(title_1)
                                break
            elif (
                # If one title has languages, but the other doesn't, take the one that
                # supports the highest priority implied language and has the most languages
                title_1.languages != ''
                and title_2.languages != ''
                and title_1.languages != title_2.languages
                and (
                    title_1.title_languages == '' or
                    title_2.title_languages == '')):

                    for region in user_input.user_region_order:
                        if region_data.implied_language[region] != '':
                            if (
                                bool(re.search(region_data.implied_language[region], title_1.languages)) == True
                                and bool(re.search(region_data.implied_language[region], title_2.languages)) == False):
                                    if title_2 in title_list: title_list.remove(title_2)
                                    break
                            elif (
                                bool(re.search(region_data.implied_language[region], title_2.languages)) == True
                                and bool(re.search(region_data.implied_language[region], title_1.languages)) == False):
                                    if title_1 in title_list: title_list.remove(title_1)
                                    break

            # Accommodate if the user has a submitted a region order that doesn't
            # include all regions
            if (
                title_1 in title_list
                and title_2 in title_list):
                    for region in region_data.all:
                        if region_data.implied_language[region] != '':
                            if (
                                bool(re.search(region_data.implied_language[region], title_1.languages)) == True
                                and bool(re.search(region_data.implied_language[region], title_2.languages)) == False):
                                    if title_2 in title_list: title_list.remove(title_2)
                                    break
                            elif (
                                bool(re.search(region_data.implied_language[region], title_2.languages)) == True
                                and bool(re.search(region_data.implied_language[region], title_1.languages)) == False):
                                    if title_1 in title_list: title_list.remove(title_1)
                                    break


def assign_clones(titles, input_dat, region_data, user_input, dat_numbered, REGEX):
    """ Assigns clones manually from clone lists """

    if input_dat.clone_lists.renames != None:
        progress = 0
        progress_old = 0
        progress_total = len(input_dat.clone_lists.renames)

        for key, values in input_dat.clone_lists.renames.items():
            # Find the full names of the entries in the clone list
            clones = []

            progress += 1
            progress_percent = int(progress/progress_total*100)

            if progress_old != progress_percent:
                if old_windows() != True:
                    sys.stdout.write("\033[K")
                print(f'* Assigning clones from clone lists... [{str(progress_percent)}%]', sep='', end='\r', flush=True)

            # Compensate if the key title is missing, either because it's been
            # removed by Retool, or doesn't exist in the dat.
            if not get_raw_title(key) in titles.all:
                printverbose(
                    user_input.verbose,
                    f'{Font.warning}* Title in clone list not found in dat or selected regions: '
                    f'{Font.warning_bold}{key}{Font.end}')
                key = f'|* Missing *|: {key}'
                titles.all[get_raw_title(key)] = []

            # Populate groups for the related titles in the clone list
            group = []

            for title in titles.all[get_raw_title(key)]:
                group.append(title.short_name_lower)
                if title.short_name_lower == key.lower():
                    clones.append((title, 1))

            for value in values:
                if len(value) < 2:
                    printverbose(
                        user_input.verbose,
                        f'{Font.warning}* {Font.warning}Problem in clone list: at '
                        f'least two values are required in the array for the '
                        f'{Font.warning_bold}{key}{Font.warning} key to assign a '
                        f'clone. Ignoring the key.{Font.end}')
                elif type(value) != list:
                    printverbose(
                        user_input.verbose,
                        f'{Font.warning}* {Font.warning}Problem in clone list: the '
                        f'following clone is not in a list: '
                        f'{Font.warning_bold}{key}{Font.warning}. Ignoring.{Font.end}')
                else:
                    clone_title, clone_priority = value[0], value[1]

                    if get_raw_title(clone_title) in titles.all:
                        group = []

                        for title in titles.all[get_raw_title(clone_title)]:
                            group.append(title.short_name_lower)
                            if title.short_name_lower == clone_title.lower():
                                clones.append((title, clone_priority))

                        if clone_title.lower() not in group:
                            printverbose(
                                user_input.verbose,
                                f'{Font.warning}* Title in clone list not found in dat or selected regions: '
                                f'{Font.warning_bold}{clone_title}{Font.end}')
                    else:
                        printverbose(
                            user_input.verbose,
                            f'{Font.warning}* Title in clone list not found in dat or selected regions: '
                            f'{Font.warning_bold}{clone_title}{Font.end}')

            # Figure out which clone to make a parent, based on region and language
            priority_range = range(0, 10)

            parent = ''

            for i in priority_range:
                found_parent = False
                found_superset = False

                if len(clones) > 1:
                    for region in user_input.user_region_order:
                        for clone in sorted(clones, key=operator.itemgetter(1)):
                            clone_title, clone_priority = clone[0], clone[1]

                            # If a title priority is set to 0 or -1 and has the same language as a higher region
                            # priority, don't overwrite it.
                            if (
                                clone_title.cloneof == ''
                                and clone_priority >= priority_range[0]):
                                    if clone_priority == -1 or clone_priority == 0:
                                        if (
                                            bool(
                                                re.search(region_data.implied_language[region], # Not sure if this is the right thing to do.
                                                        clone_title.languages)) == True
                                            and region_data.implied_language[region] != ''):
                                                    # Check if title is preproduction or bad. If so, check if
                                                    # production/good titles are available.
                                                    if bool(re.search(REGEX.preproduction_bad, clone_title.full_name_lower)) == True:
                                                        for another_clone in sorted(clones, key=operator.itemgetter(1)):
                                                            if bool(re.search(REGEX.preproduction_bad, another_clone[0].full_name_lower)) == False:
                                                                found_parent = True
                                                                found_superset = True
                                                                parent = another_clone
                                                                break

                                                    # Check for Sega CD 32X vs Mega-CD 32X
                                                    if (
                                                        bool(re.search(REGEX.sega32x, clone_title.full_name_lower)) == True
                                                        and 'USA' in user_input.user_region_order
                                                        and 'Europe' in user_input.user_region_order
                                                        ):
                                                        for another_clone in sorted(clones, key=operator.itemgetter(1)):
                                                            if user_input.user_region_order.index('Europe') < user_input.user_region_order.index('USA'):
                                                                    if 'mega-cd 32x' in another_clone[0].full_name_lower:
                                                                        found_parent = True
                                                                        found_superset = True
                                                                        parent = another_clone
                                                                        break

                                                    if found_parent == True:
                                                        break
                                                    else:
                                                        found_parent = True
                                                        found_superset = True
                                                        parent = clone
                                                        break
                                    elif region in clone_title.regions:
                                        # Check if title is preproduction or bad. If so, check if production/good
                                        # titles are available.
                                        if bool(re.search(REGEX.preproduction_bad, clone_title.full_name_lower)) == True:
                                            for another_clone in sorted(clones, key=operator.itemgetter(1)):
                                                if bool(re.search(REGEX.preproduction_bad, another_clone[0].full_name_lower)) == False:
                                                    found_parent = True
                                                    parent = another_clone
                                                    break
                                        if found_parent == True:
                                            break
                                        else:
                                            found_parent = True
                                            parent = clone
                                            break
                        if found_parent == True: break
                    if found_parent == True: break

            if parent != '':
                # Do extra parent selection if a short name in the clone list
                # has more than one match, or there's more than one clone per
                # region.
                for clone in clones:
                    if (
                        clone[0].primary_region == parent[0].primary_region
                        and clone[1] <= parent[1]
                        and clone[0].full_name_lower != parent[0].full_name_lower
                        and clone[1] >= priority_range[0]
                        and len(clones) > 1
                        and found_superset == False):
                            if (
                                'Dreamcast' in input_dat.name
                                or 'Saturn' in input_dat.name
                                or 'Sega CD' in input_dat.name
                                or 'Panasonic - 3DO' in input_dat.name):
                                ring_code = True
                            else:
                                ring_code = False

                            parents = [clone[0], parent[0]]
                            parents = choose_parent(parents, region_data, user_input, dat_numbered, REGEX, ring_code, True)

                            for new_parent in parents:
                                if new_parent.cloneof == '':
                                    found_parent = True
                                    parent = (new_parent, parent[1])
                                    break

                            if found_parent == True: break

                # Parent/clone assignment
                for clone in sorted(clones, key=operator.itemgetter(1)):
                    clone_title, clone_priority = clone[0], clone[1]

                    if clone_title.group in titles.all:
                        for disc_title in titles.all[clone_title.group]:
                            if (
                                clone_title.full_name_lower == disc_title.full_name_lower
                                and clone_title.full_name_lower == parent[0].full_name_lower
                                and clone_priority >= priority_range[0]):
                                    disc_title.cloneof = ''
                                    disc_title.cloneof_group = ''
                            elif (
                                clone_title.full_name_lower == disc_title.full_name_lower
                                and clone_title.full_name_lower != parent[0].full_name_lower
                                and clone_priority >= priority_range[0]):

                                    if dat_numbered == False:
                                        disc_title.cloneof = parent[0].full_name
                                    else:
                                        disc_title.cloneof = parent[0].numbered_name

                                    disc_title.cloneof_group = parent[0].group
            progress_old = progress_percent
    return titles