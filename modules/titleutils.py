import functools
import itertools
import operator
import re
import sys

from modules.utils import Font, old_windows, printverbose

def check_date(string, title):
    """ Basic date validation """

    months = [
        'January', 'February', 'March',
        'April', 'May', 'June',
        'July', 'August', 'September',
        'October', 'November', 'December'
    ]

    if re.search('|'.join(months), title) != None:
        for i, month in enumerate(months):
            if (i < 8):
                title = re.sub(f'{month}, ', f'0{i + 1}-01-', title)
            else:
                title = re.sub(f'{month}, ', f'{i + 1}-01-', title)

    if re.search('\(\d{2}-\d{2}-\d{4}\)', title) != None:
        us_date = True
    else:
        us_date = False

    if re.search('\(\d{2}-\d{2}-\d{2}\)', title) != None:
        short_date = True
    else:
        short_date = False

    title = title.replace(re.search(string, title)[0], re.search(string, title)[0].replace('-', ''))

    if short_date == True:
        string = '\(\d{6}\)'
        year = 1900 + int(re.search(string, title).group()[1:-5])
        month = re.search(string, title).group()[3:-3]
        day = re.search(string, title).group()[5:-1]
    elif us_date == True:
        year = re.search(string, title).group()[5:-1]
        month = re.search(string, title).group()[1:-7]
        day = re.search(string, title).group()[3:-5]
    else:
        year = re.search(string, title).group()[1:-5]
        month = re.search(string, title).group()[5:-3]
        day = re.search(string, title).group()[7:-1]

    if (
        int(year) >= 1970
        and int(month) >= 1
        and int(month) <= 12
        and int(day) >= 1
        and int(day) <= 31):
            return int(year + month + day)
    else:
        return False


def get_title_count(titles, is_folder):
    """ Gets the final title count """
    final_title_count = 0
    if len(titles.all) == 0:
        if is_folder == False:
            sys.exit()
        else:
            return 0
    else:
        for group, disc_titles in titles.all.items():
            for title in disc_titles:
                final_title_count += 1

    return final_title_count


def report_stats(stats, titles, user_input, input_dat, region_data):
    """ Print the final stats to screen """

    print(
        '\nStats:\no  Original title count: '
        f'{str("{:,}".format(stats.original_title_count))}')

    if user_input.legacy == True:
        print(f'o  Clones found: {str("{:,}".format(stats.clone_count))}')
    if user_input.no_applications == True:
        print(
            '-  Applications removed: '
            f'{str("{:,}".format(stats.applications_count))}')
    if user_input.no_bad_dumps == True:
        print(
            '-  Bad dumps removed: '
            f'{str("{:,}".format(stats.bad_dump_count))}')
    if user_input.no_coverdiscs == True:
        print(
            '-  Coverdiscs removed: '
            f'{str("{:,}".format(stats.coverdiscs_count))}')
    if user_input.no_demos == True:
        print(
            '-  Demos removed: '
            f'{str("{:,}".format(stats.demos_count))}')
    if user_input.no_educational == True:
        print(
            '-  Educational titles removed: '
            f'{str("{:,}".format(stats.educational_count))}')
    if user_input.no_multimedia == True:
        print(
            '-  Multimedia titles removed: '
            f'{str("{:,}".format(stats.multimedia_count))}')
    if user_input.no_pirate == True:
        print(
            '-  Pirate titles removed: '
            f'{str("{:,}".format(stats.pirate_count))}')
    if user_input.no_preproduction == True:
        print(
            '-  Preproduction titles removed: '
            f'{str("{:,}".format(stats.preproduction_count))}')
    if user_input.no_promotional == True:
        print(
            '-  Promotional titles removed: '
            f'{str("{:,}".format(stats.promotional_count))}')
    if input_dat.clone_lists != None:
        if user_input.no_compilations == True:
            print(
                '-  Compilations removed: '
                f'{str("{:,}".format(stats.compilations_count))}')
    if user_input.no_unlicensed == True:
        print(
            '-  Unlicensed titles removed: '
            f'{str("{:,}".format(stats.unlicensed_count))}')
    if user_input.legacy == False:
        print(f'-  Clones removed: {str("{:,}".format(stats.clone_count))}')

    if 'Unknown' in user_input.user_region_order:
        if len(titles.regions['Unknown']) > 1:
            print(
                '+  Titles without regions included: '
                f'{str("{:,}".format(len(titles.regions["Unknown"])))}')
    print(f'\n-  Total titles removed: {str("{:,}".format(stats.original_title_count - stats.final_title_count))}')
    print(f'{Font.bold}---------------------------')
    print(f'=  New title count: {str("{:,}".format(stats.final_title_count))}{Font.end}')


def get_raw_title(title):
    """ Returns the raw title, or 'group' of the input title """

    if title.find('(') != -1:
        return title[:(title.find('(') - 1)].rstrip()
    else:
        return title.rstrip()


def get_languages(title, REGEX_LANGUAGES):
    """ Returns the languages from the input title """

    languages = re.search(REGEX_LANGUAGES, title)

    if languages != None:
        return languages[0][2:-1]
    else:
        return ''


def remove_languages(title, REGEX_LANGUAGES):
    """ Removes languages from the input title """

    no_languages = re.search(REGEX_LANGUAGES, title)

    if no_languages != None:
        return title.replace(no_languages[0], '')
    else:
        return title


def remove_regions(title, region_data):
    """ Removes regions from the input title, given the title and region_data object """

    return title.replace(re.search(' \(((.*?,){0,} {0,})(' + '|'.join(region_data.all) + ').*?\)', title)[0],'')


def remove_tags(title, user_input, REGEX):
    """ Removes tags from the input title that are in tags.json """

    for string in user_input.tag_strings.ignore:
        if re.search(string, title) != None:
            if string == REGEX.dates_whitespace and check_date(REGEX.dates, title) != False:
                title = title.replace(re.search(REGEX.dates_whitespace, title)[0], '')
            else:
                title = title.replace(re.search(string, title)[0],'')

    return title


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
            choose_string(edition, user_input, region_data, parents, REGEX, False, clonelist)
        else:
            choose_string(edition, user_input, region_data, parents, REGEX, True, clonelist)

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
                and title_1.short_name == title_2.short_name
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
            title_1.short_name == title_2.short_name
            and '[BIOS]' not in title_1.full_name
            and '[BIOS]' not in title_2.full_name):
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
        choose_string(edition, user_input, region_data, parents, REGEX, True, clonelist)

    for edition in user_input.tag_strings.demote_editions:
        choose_string(edition, user_input, region_data, parents, REGEX, False, clonelist)

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
                    and title.short_name == parent.short_name
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
                    if (
                        not include.startswith('/')
                        and not include.startswith('|')):
                            if include in title.full_name:
                                title.cloneof = ''
                                title.group = ''
                    elif include.startswith('/'):
                        try:
                            re.compile(include[1:])
                            regex_valid = True
                        except:
                            regex_valid = False

                        if (
                            regex_valid == True
                            and re.search(include[1:], title.full_name) != None):
                                title.cloneof = ''
                                title.group = ''
                    elif include.startswith('|'):
                        if include[1:] == title.full_name:
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
                title_1.short_name == title_2.short_name
                and title_1.regions != title_2.regions
                and '[BIOS]' not in title_1.full_name
                and '[BIOS]' not in title_2.full_name):

                # Check to see if titles are preproduction/bad or not. If so, favour
                # production titles
                preprod_title_1 = bool(re.search(REGEX.preproduction_bad, title_1.full_name))
                preprod_title_2 = bool(re.search(REGEX.preproduction_bad, title_2.full_name))

                if preprod_title_1 == True and preprod_title_2 == False:
                    if title_1 in parents: parents.remove(title_1)
                elif preprod_title_2 == True and preprod_title_1 == False:
                    if title_2 in parents: parents.remove(title_2)

                # Check to see if titles are unlicensed or not. If so, favour
                # production titles
                unl_title_1 = bool(re.search('\(Unl\)', title_1.full_name))
                unl_title_2 = bool(re.search('\(Unl\)', title_2.full_name))

                if unl_title_1 == True and unl_title_2 == False:
                    if title_1 in parents: parents.remove(title_1)
                elif unl_title_2 == True and unl_title_1 == False:
                    if title_2 in parents: parents.remove(title_2)

        for title_1, title_2 in itertools.combinations(parents, 2):
            if (
                title_1.short_name == title_2.short_name
                and title_1.regions != title_2.regions
                and '[BIOS]' not in title_1.full_name
                and '[BIOS]' not in title_2.full_name):
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
                    and title.short_name == parent.short_name
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
            title_1.short_name == title_2.short_name
            and '[BIOS]' not in title_1.full_name
            and '[BIOS]' not in title_2.full_name):
            if (
                re.search(string, title_1.full_name) != None
                and re.search(string, title_2.full_name) == None
                and check_date(string, title_1.full_name) != False):
                    if title_2 in title_list: title_list.remove(title_2)
            elif (
                re.search(string, title_2.full_name) != None
                and re.search(string, title_1.full_name) == None
                and check_date(string, title_2.full_name) != False):
                    if title_1 in title_list: title_list.remove(title_1)
            elif (
                re.search(string, title_1.full_name) != None
                and re.search(string, title_2.full_name) != None
                and check_date(string, title_1.full_name) != False
                and check_date(string, title_2.full_name) != False):
                    if check_date(string, title_1.full_name) > check_date(string, title_2.full_name):
                        if title_2 in title_list: title_list.remove(title_2)
                    elif check_date(string, title_2.full_name) > check_date(string, title_1.full_name):
                        if title_1 in title_list: title_list.remove(title_1)


def choose_ring_code(REGEX, title_list, user_input, region_data):
    """ Checks two titles from a list and removes the one with the
    lowest ring code.
    """

    choose_string(REGEX.sega_ring_code, user_input, region_data, title_list, REGEX, True)

    title_list_temp = title_list.copy()

    for title_1, title_2 in itertools.combinations(title_list_temp, 2):
        if title_1.short_name == title_2.short_name:
            if (
                re.search(REGEX.sega_ring_code, title_1.full_name) != None
                and re.search(REGEX.sega_ring_code, title_2.full_name) != None):
                    title_1_ring_code = re.search(REGEX.sega_ring_code, title_1.full_name)[0]
                    title_2_ring_code = re.search(REGEX.sega_ring_code, title_2.full_name)[0]

                    # Get the highest version ring code
                    if (
                        re.search(REGEX.sega_ring_code_re, title_1_ring_code) == None
                        and re.search(REGEX.sega_ring_code_re, title_2_ring_code) == None):
                            title_1_highest_ring_code = int(re.search('[0-9]{1,2}[A-Z]\)', title_1_ring_code)[0][:-2])
                            title_2_highest_ring_code = int(re.search('[0-9]{1,2}[A-Z]\)', title_2_ring_code)[0][:-2])

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
                title_1.short_name == title_2.short_name
                and clonelist == False)
        or (
            clonelist == True)):
                if (
                    '[BIOS]' not in title_1.full_name
                    and '[BIOS]' not in title_2.full_name):
                        if (
                            re.search(string, title_1.full_name) != None
                            and re.search(string, title_2.full_name) == None):
                            if choose_title_with_string == False:
                                if title_1 in title_list: title_list.remove(title_1)
                            else:
                                if title_2 in title_list: title_list.remove(title_2)
                        elif (
                            re.search(string, title_2.full_name) != None
                            and re.search(string, title_1.full_name) == None):
                                if choose_title_with_string == False:
                                    if title_2 in title_list: title_list.remove(title_2)
                                else:
                                    if title_1 in title_list: title_list.remove(title_1)
                        elif (
                            # If both titles have the specified string
                            re.search(string, title_2.full_name) != None
                            and re.search(string, title_1.full_name) != None
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
                                        and '[BIOS]' not in title_1.full_name
                                        and '[BIOS]' not in title_2.full_name)
                                    and (
                                        'Gentei' in str(string)
                                        or 'OEM' in str(string))):
                                        for region in region_data.all:
                                            if len(title_2.full_name) < len(title_1.full_name):
                                                if title_2 in title_list: title_list.remove(title_2)
                                            elif len(title_1.full_name) < len(title_2.full_name):
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
        preprod_title_1 = bool(re.search(REGEX.preproduction_bad, title_1.full_name))
        preprod_title_2 = bool(re.search(REGEX.preproduction_bad, title_2.full_name))

        preprod_check.extend([preprod_title_1, preprod_title_2])

        if functools.reduce(lambda a,b: a + b, preprod_check) > 0:
            preproduction = True

        if (
            (
                title_1.short_name == title_2.short_name
                and '[BIOS]' not in title_1.full_name
                and '[BIOS]' not in title_2.full_name
                and (
                    functools.reduce(lambda a,b: a + b, preprod_check) == 2
                    or functools.reduce(lambda a,b: a + b, preprod_check) == 0))):

                    # Deal with mixed versions and revisions
                    if (
                        re.search(REGEX.revision, title_1.full_name) != None
                        and re.search(REGEX.version, title_2.full_name) != None):
                            if title_1 in title_list: title_list.remove(title_1)
                    elif (
                        re.search(REGEX.revision, title_2.full_name) != None
                        and re.search(REGEX.version, title_1.full_name) != None):
                            if title_2 in title_list: title_list.remove(title_2)

                    # Now the normal version comparisons
                    elif (
                            re.search(string, title_1.region_free_name) != None
                            and re.search(string, title_2.region_free_name) != None):

                            # Find the highest version
                            ver_1 = re.search(string, title_1.region_free_name)[0][trim_start:trim_end]
                            ver_2 = re.search(string, title_2.region_free_name)[0][trim_start:trim_end]

                            if string == re.compile('\(DV [0-9].*?\)'):
                                ver_1 = int(re.search('\d+\)', title_1.full_name)[0][:-1])
                                ver_2 = int(re.search('\d+\)', title_2.full_name)[0][:-1])
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
                        re.search(string, title_1.region_free_name) != None
                        or re.search(string, title_2.region_free_name) != None):
                            if (
                                re.search(string, title_1.full_name) != None
                                and re.search(string, title_2.full_name) == None):
                                    if preproduction == False or functools.reduce(lambda a,b: a + b, preprod_check) == 2:
                                        if title_2 in title_list: title_list.remove(title_2)
                                    else:
                                        if title_1 in title_list: title_list.remove(title_1)
                            elif (
                                re.search(string, title_1.full_name) == None
                                and re.search(string, title_2.full_name) != None):
                                    if preproduction == False or functools.reduce(lambda a,b: a + b, preprod_check) == 2:
                                        if title_1 in title_list: title_list.remove(title_1)
                                    else:
                                        if title_2 in title_list: title_list.remove(title_2)
        elif (
            functools.reduce(lambda a,b: a + b, preprod_check) == 1
            and '[BIOS]' not in title_1.full_name
            and '[BIOS]' not in title_2.full_name):

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
        '[BIOS]' not in title_1.full_name
        and '[BIOS]' not in title_2.full_name):
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

            if get_raw_title(key) in titles.all:
                group = []

                for title in titles.all[get_raw_title(key)]:
                    group.append(title.short_name)
                    if title.short_name == key:
                        clones.append((title, 1))

                if key not in group:
                    printverbose(
                        user_input.verbose,
                        f'{Font.warning}* Title in clone list not found in dat or selected regions: '
                        f'{Font.warning_bold}{key}{Font.end}')

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
                                group.append(title.short_name)
                                if title.short_name == clone_title:
                                    clones.append((title, clone_priority))

                            if clone_title not in group:
                                printverbose(
                                    user_input.verbose,
                                    f'{Font.warning}* Title in clone list not found in dat or selected regions: '
                                    f'{Font.warning_bold}{clone_title}{Font.end}')
                        else:
                            printverbose(
                                user_input.verbose,
                                f'{Font.warning}* Title in clone list not found in dat or selected regions: '
                                f'{Font.warning_bold}{clone_title}{Font.end}')
            else:
                printverbose(
                    user_input.verbose,
                    f'{Font.warning}* Title in clone list not found in dat or selected regions: '
                    f'{Font.warning_bold}{key}{Font.end}')

            # Figure out which clone to make a parent, based on region and language
            priority_range = range(-1, 10) if user_input.supersets == True else range(0, 10)

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
                                                    if bool(re.search(REGEX.preproduction_bad, clone_title.full_name)) == True:
                                                        for another_clone in sorted(clones, key=operator.itemgetter(1)):
                                                            if bool(re.search(REGEX.preproduction_bad, another_clone[0].full_name)) == False:
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
                                        if bool(re.search(REGEX.preproduction_bad, clone_title.full_name)) == True:
                                            for another_clone in sorted(clones, key=operator.itemgetter(1)):
                                                if bool(re.search(REGEX.preproduction_bad, another_clone[0].full_name)) == False:
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
                        and clone[0].full_name != parent[0].full_name
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
                                clone_title.full_name == disc_title.full_name
                                and clone_title.full_name == parent[0].full_name
                                and clone_priority >= priority_range[0]):
                                    disc_title.cloneof = ''
                                    disc_title.cloneof_group = ''
                            elif (
                                clone_title.full_name == disc_title.full_name
                                and clone_title.full_name != parent[0].full_name
                                and clone_priority >= priority_range[0]):

                                    if dat_numbered == False:
                                        disc_title.cloneof = parent[0].full_name
                                    else:
                                        disc_title.cloneof = parent[0].numbered_name

                                    disc_title.cloneof_group = parent[0].group
    return titles