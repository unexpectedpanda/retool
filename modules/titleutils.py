import re
import sys

from modules.utils import Font


def check_date(string, title):
    """ Basic date validation """

    months = [
        'january', 'february', 'march',
        'april', 'may', 'june',
        'july', 'august', 'september',
        'october', 'november', 'december'
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


def get_languages(title, REGEX_LANGUAGES):
    """ Returns the languages from the input title """

    languages = re.search(REGEX_LANGUAGES, title)

    if languages != None:
        return languages[0][2:-1]
    else:
        return ''


def get_raw_title(title):
    """ Returns the raw title, or 'group' of the input title """

    if title.find('(') != -1:
        return title[:(title.find('(') - 1)].rstrip().lower()
    else:
        return title.rstrip().lower()


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


def report_stats(stats, titles, user_input, input_dat):
    """ Print the final stats to screen """

    print(
        '\nStats:\no  Original title count: '
        f'{str("{:,}".format(stats.original_title_count))}')

    if user_input.legacy == True:
        print(f'o  Titles assigned as clones: {str("{:,}".format(stats.clone_count))}')
    else:
        print(f'   -  Clones removed: {str("{:,}".format(stats.clone_count))}')
    if user_input.no_add_ons == True:
        print(
            '   -  Add-on titles removed: '
            f'{str("{:,}".format(stats.add_on_count))}')
    if user_input.no_applications == True:
        print(
            '   -  Applications removed: '
            f'{str("{:,}".format(stats.applications_count))}')
    if user_input.no_audio == True:
        print(
            '   -  Audio titles removed: '
            f'{str("{:,}".format(stats.audio_count))}')
    if user_input.no_bad_dumps == True:
        print(
            '   -  Bad dumps removed: '
            f'{str("{:,}".format(stats.bad_dump_count))}')
    if user_input.no_bios == True:
        print(
            '   -  BIOSes and other chips removed: '
            f'{str("{:,}".format(stats.bios_count))}')
    if user_input.no_bonus_discs == True:
        print(
            '   -  Bonus discs removed: '
            f'{str("{:,}".format(stats.bonus_discs_count))}')
    if user_input.no_coverdiscs == True:
        print(
            '   -  Coverdiscs removed: '
            f'{str("{:,}".format(stats.coverdiscs_count))}')
    if user_input.no_demos == True:
        print(
            '   -  Demos removed: '
            f'{str("{:,}".format(stats.demos_count))}')
    if user_input.no_educational == True:
        print(
            '   -  Educational titles removed: '
            f'{str("{:,}".format(stats.educational_count))}')
    if user_input.no_manuals == True:
        print(
            '   -  Manuals removed: '
            f'{str("{:,}".format(stats.manuals_count))}')
    if user_input.no_multimedia == True:
        print(
            '   -  Multimedia titles removed: '
            f'{str("{:,}".format(stats.multimedia_count))}')
    if user_input.no_pirate == True:
        print(
            '   -  Pirate titles removed: '
            f'{str("{:,}".format(stats.pirate_count))}')
    if user_input.no_preproduction == True:
        print(
            '   -  Preproduction titles removed: '
            f'{str("{:,}".format(stats.preproduction_count))}')
    if user_input.no_promotional == True:
        print(
            '   -  Promotional titles removed: '
            f'{str("{:,}".format(stats.promotional_count))}')
    if user_input.no_unlicensed == True:
        print(
            '   -  Unlicensed titles removed: '
            f'{str("{:,}".format(stats.unlicensed_count))}')
    if user_input.no_video == True:
        print(
            '   -  Video titles removed: '
            f'{str("{:,}".format(stats.video_count))}')
    if stats.remove_count > 0:
        print(
            '   -  Titles removed as defined by clone list: '
            f'{str("{:,}".format(stats.remove_count))}')
    if stats.custom_global_exclude_filter_count > 0:
        print(
            '   -  Titles removed due to custom global filter: '
            f'{str("{:,}".format(stats.custom_global_exclude_filter_count))}')
    if stats.custom_system_exclude_filter_count > 0:
        print(
            '   -  Titles removed due to custom system filter: '
            f'{str("{:,}".format(stats.custom_system_exclude_filter_count))}')
    if (len(input_dat.soup.find_all('game'))) > 0:
        print(
            '   -  Titles removed due to country filters: '
            f'{str("{:,}".format(len(input_dat.soup.find_all("game"))))}')
    if 'Filtered languages' in user_input.recovered_titles:
        if (len(user_input.recovered_titles['Filtered languages'])) > 0:
            print(
                '   -  Titles removed due to language filters: '
                f'{str("{:,}".format(len(user_input.recovered_titles["Filtered languages"])))}')
    if (stats.recovered_count) > 0:
        print(
            '   +  Titles recovered due to include filters: '
            f'{str("{:,}".format(stats.recovered_count))}')

    if 'Unknown' in user_input.user_region_order:
        if len(titles.regions['Unknown']) > 1:
            print(
                '   +  Titles without regions included: '
                f'{str("{:,}".format(len(titles.regions["Unknown"])))}')

    print(f'\n-  Total titles removed: {str("{:,}".format(stats.original_title_count - stats.final_title_count))}')
    print(f'{Font.bold}---------------------------')
    print(f'=  New title count: {str("{:,}".format(stats.final_title_count))}{Font.end}')