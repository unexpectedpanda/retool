import json
import os
import sys

from modules.classes import CloneList, Regions, Tags
from modules.utils import printwrap, Font


def build_tags(TAGS):
    """ Imports a list of tags from a file, to strip from titles during processing """

    tag_strings = Tags()

    if (
        os.path.exists(TAGS.filename) == True
        and os.path.isfile(TAGS.filename) == True):
        try:
            with open(TAGS.filename, 'r') as input_file_read:
                tag_file = json.load(input_file_read)

                if TAGS.ignore in tag_file:
                    tag_strings.ignore = tag_file[TAGS.ignore]
                    for tag in tag_file[TAGS.demote_editions] + tag_file[TAGS.promote_editions]:
                        if tag not in tag_file[TAGS.ignore]:
                            tag_strings.ignore.append(tag)
                if TAGS.disc_rename in tag_file:
                    tag_strings.disc_rename = tag_file[TAGS.disc_rename]
                if TAGS.promote_editions in tag_file:
                    tag_strings.promote_editions = tag_file[TAGS.promote_editions]
                if TAGS.demote_editions in tag_file:
                    tag_strings.demote_editions = tag_file[TAGS.demote_editions]

                # Error handling
                for section in [
                    TAGS.ignore, TAGS.disc_rename,
                    TAGS.promote_editions, TAGS.demote_editions]:
                        if section not in tag_file:
                            printwrap(
                                f'{Font.warning}* The {Font.bold}{section}{Font.warning}'
                                f' key is missing from {Font.bold}{TAGS.filename}'
                                f'{Font.warning}. Clone matching won\'t be accurate.'
                                f'{Font.end}')
                input_file_read.close()

                return tag_strings

        except OSError as e:
            print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise
    else:
        printwrap(
            f'{Font.error_bold}* Error:{Font.error} The {Font.bold}{TAGS.filename}'
            f'{Font.error} file is missing.{Font.end}')
        sys.exit()


def build_regions(REGIONS):
    """ Imports regions and languages from a file """

    regions = Regions()

    if (
        os.path.exists(REGIONS.filename) == True
        and os.path.isfile(REGIONS.filename) == True):
        try:
            with open(REGIONS.filename, 'r') as input_file_read:
                regiondata = json.load(input_file_read)

                # Set the implied languages
                if REGIONS.region_order in regiondata:
                    for region, language in regiondata[REGIONS.region_order].items():
                        regions.all.append(region)
                    regions.implied_language = regiondata[REGIONS.region_order]

                    # Set the default region order
                    regions.region_order = [region for region in regiondata[REGIONS.region_order]]
                else:
                    printwrap(
                        f'{Font.error_bold}* Error: {Font.error}The {Font.bold}'
                        f'{REGIONS.region_order}{Font.error} key is missing '
                        f'from {Font.bold}{REGIONS.filename}{Font.error}. It\'s needed '
                        'for Retool to know what regions and languages are available.'
                        f'{Font.end}', 'error')
                    sys.exit()

                # Set the other language details
                if REGIONS.languages in regiondata:
                    regions.languages_key = regiondata[REGIONS.languages]
                    regions.languages_long = [language for language in regiondata[REGIONS.languages]]
                    regions.languages_short = []
                    for long_language, short_language in regiondata[REGIONS.languages].items():
                        regions.languages_short.append(short_language)

                input_file_read.close()
                return regions

        except OSError as e:
            print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise
    else:
        printwrap(
            f'{Font.error_bold}* Error: {Font.error}The {Font.bold}'
            f'{REGIONS.filename}{Font.error} file is missing. Retool can\'t continue.'
            f'{Font.end}', 'error')
        sys.exit()


def build_clone_lists(dat_name):
    """ Formats a clone list appriopriately """

    # Import JSON files that have the same name as dat_name + .json
    if 'GameCube' in dat_name and (
        'NKit GCZ' in dat_name or
        'NKit ISO' in dat_name or
        'NASOS' in dat_name
        ):
        clone_file = './clonelists/Nintendo - GameCube.json'
    elif 'Wii U' in dat_name and 'WUX' in dat_name:
        clone_file = './clonelists/Nintendo - Wii U.json'
    elif 'Wii' in dat_name and (
        'NKit GCZ' in dat_name or
        'NKit ISO' in dat_name or
        'NASOs' in dat_name
        ):
        clone_file = './clonelists/Nintendo - Wii.json'
    else:
        clone_file = './clonelists/' + dat_name + '.json'
    if os.path.exists(clone_file) == True and os.path.isfile(clone_file) == True:
        try:
            with open(clone_file, 'r') as input_file_read:
                clonedata = json.load(input_file_read)

        except OSError as e:
            print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

        except ValueError as e:
            printwrap(f'\n{Font.error_bold}* Error: "{os.path.abspath(clone_file)}"{Font.error} isn\'t valid JSON. Exiting...{Font.end}', 'error')
            print('\n')
            raise

        compilations = set()
        conditional_overrides = {}
        overrides = {}
        renames = {}

        if 'compilations' in clonedata:
            compilations.update(clonedata['compilations'])
        if 'overrides' in clonedata:
            overrides = clonedata['overrides']
        if 'conditional_overrides' in clonedata:
            conditional_overrides = clonedata['conditional_overrides']
        if 'renames' in clonedata:
            renames = clonedata['renames']

        return CloneList(
            compilations,
            overrides,
            conditional_overrides,
            renames
        )


def import_metadata(dat_name):
    """ Imports title metadata scraped from Redump """

    if 'GameCube' in dat_name and (
        'NKit GCZ' in dat_name or
        'NKit ISO' in dat_name or
        'NASOS' in dat_name
        ):
        metadata_file = './metadata/Nintendo - GameCube.json'
    elif 'Wii U' in dat_name and 'WUX' in dat_name:
        metadata_file = './metadata/Nintendo - Wii U.json'
    elif 'Wii' in dat_name and (
        'NKit GCZ' in dat_name or
        'NKit ISO' in dat_name or
        'NASOs' in dat_name
        ):
        metadata_file = './metadata/Nintendo - Wii.json'
    else:
        metadata_file = './metadata/' + dat_name + '.json'

    if os.path.exists(metadata_file) == True and os.path.isfile(metadata_file) == True:
        try:
            with open(metadata_file, 'r', encoding='utf-8') as input_file_read:
                return json.load(input_file_read)
        except OSError as e:
            print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise
    else:
        return ''