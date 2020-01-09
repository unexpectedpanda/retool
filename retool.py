# Dedupes [Redump](http://redump.org/) dats. This is not an official Redump
# project.

import datetime
import html
import itertools
import os
import sys
import re
import textwrap
import time

from lxml import etree
from bs4 import BeautifulSoup, Doctype # For XML parsing

if os.path.exists('_test.py'):
    import _test as _renames
else:
    import _renames # Dupes that have different names in different regions

# Require at least Python 3.5
assert sys.version_info >= (3, 5)

def main():
    # Splash screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(font.bold + '\nReTOOL 0.5' + font.end)
    print('----------')
    if len(sys.argv) == 1:
        print(
            textwrap.fill(
            'Dedupes Redump (' + font.underline + 'http://redump.org/'
            + font.end + ') dats. This is not an official Redump project.', 80
            )
        )

    # Check user input
    user_input = check_input()

    # Start a time from when the process started
    start_time = time.time()

    # Define regions where English is a primary language. Order from most to
    # least important.
    region_list_english = [
        'USA',
        'World',
        'UK',
        'Canada',
        'Australia',
        'New Zealand',
        'Singapore',
        'Ireland'
    ]

    # Define regions where titles might have an English version. Order from
    # most to least important.
    region_list_other = [
        'Europe',
        'Japan',
        'Asia',
        'Scandinavia',
        'Argentina',
        'Austria',
        'Belgium',
        'Brazil',
        'China',
        'Croatia',
        'Czech',
        'Denmark',
        'Finland',
        'France',
        'Germany',
        'Greece',
        'Hungary',
        'India',
        'Israel',
        'Italy',
        'Korea',
        'Latin America',
        'Netherlands',
        'Norway',
        'Poland',
        'Portugal',
        'Russia',
        'Slovakia',
        'South Africa',
        'Spain',
        'Sweden',
        'Switzerland',
        'Taiwan',
        'Thailand',
        'Turkey',
        'Ukraine',
        'United Arab Emirates'
    ]

    # Define tag strings that could cause issues when looking for dupes
    tag_strings = [
        '\s?\(Rev [0-9A-Z].*?\)\s?',
        '\s?\(v[0-9A-Z].*?\)\s?',
        '\s?\(Alt.*?\)\s?',
        '\s?\(OEM\)\s?',
        '\s?\(Rerelease\)\s?',
        '\(Disco [A-Z0-9]\)',
        '\s?\(\d{8}\)\s?',
        '\(Disc [A-Z]\)',
        '\s?\(Covermount\)\s?',
        '\s?\(Sold Out Software\)\s?'
        ]

    # If the user has defined an output folder
    if os.path.isdir(user_input.file_input) == True:
        file_count = 0
        input_folder = user_input.file_input

        # Find out how many dat files are in the folder, then process the dat
        for file in os.listdir(input_folder):
            if file.endswith('.dat'):
                file_count += 1
                user_input.file_input = os.path.join(input_folder, file)
                process_dats(user_input, tag_strings, region_list_english, region_list_other, True)

    # If the user has not defined an output folder
    else:
        input_folder = ''
        # Process the dat
        file_name_title_count = process_dats(user_input, tag_strings, region_list_english, region_list_other, False)

    # Do the work to generate a final output message for the user
    stop_time = time.time()
    total_time_elapsed = str('{0:.2f}'.format(round(stop_time - start_time,2)))

    # Set the color of the final output message. Override in case of error or warning.
    message_color = font.green

    # Set up the final output message strings
    if input_folder != '':
        if file_count != 0:
            if file_count == 1:
                file_noun = 'file'
            else:
                file_noun = 'files'

            file_count = str('{:,}'.format(file_count))

            if user_input.split_regions_no_dupes == True:
                finish_message = ('* Finished processing ' + file_count + ' ' + file_noun + ' in the "' + font.bold + input_folder + font.end + message_color + '" folder in ' + total_time_elapsed + 's. Unique titles have been added to regional dats in the\n"' + font.bold + user_input.file_output + font.end + message_color + '"\nfolder.')
            elif user_input.split_regions == True:
                finish_message = '* Finished processing ' + file_count + ' ' + file_noun + ' in the "' + font.bold + input_folder + font.end + message_color + '" folder in ' + total_time_elapsed + 's. All dats have been split into regions in the\n"' + font.bold + user_input.file_output + font.end + message_color + '"\nfolder.'
            else:
                finish_message = '* Finished processing ' + file_count + ' ' + file_noun + ' in the "' + font.bold + input_folder + font.end + message_color + '" folder in ' + total_time_elapsed + 's. Unique titles have been added to dats in the\n"' + font.bold + user_input.file_output + font.end + message_color + '"\nfolder.'
        else:
            message_color = font.yellow
            finish_message = '* No files found to process in the "' + font.bold + user_input.file_input + font.end + message_color + '" folder.'
    else:
        if user_input.english_only == True:
            english_status = ' English'
        else:
            english_status = ''

        if user_input.split_regions_no_dupes == True:
            finish_message = '* Finished adding unique' + english_status + ' titles to regional dats in ' + total_time_elapsed + 's.'
        elif user_input.split_regions == True:
            finish_message = '* Finished splitting "' + font.bold + user_input.file_input + font.end + message_color + '" into regional dats in ' + total_time_elapsed + 's.'
        else:
            finish_message = '* Finished adding ' + str('{:,}'.format(file_name_title_count['new_title_count'])) + ' unique' + english_status + ' titles to "' +  font.bold + file_name_title_count['output_file'] + font.end + message_color + '" in ' + total_time_elapsed + 's.'

    # Print the final output message
    print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(message_color + finish_message + font.end) + '\n')

    return

############### Classes and methods ###############
# Console text formatting
class font:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    white = '\033[37m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    blink = '\033[5m'

# Establish a class for user input
class UserInput:
    def __init__(self, file_input, file_output, one_game_one_rom, no_demos, no_apps, no_protos, no_alts, no_multi, no_edu, split_regions, split_regions_no_dupes, english_only):
        self.file_input = file_input
        self.file_output = file_output
        self.no_demos = no_demos
        self.no_apps = no_apps
        self.no_alts = no_alts
        self.no_multi = no_multi
        self.no_protos = no_protos
        self.no_edu = no_edu
        self.one_game_one_rom = one_game_one_rom
        self.split_regions = split_regions
        self.split_regions_no_dupes = split_regions_no_dupes
        self.english_only = english_only

# Establish a class for title data
class DatNode:
    def __init__(self, full_title, region, category, description, roms, cloneof, tag_strings):
        self.full_title = full_title

        # Set regionless title
        if re.findall(' \(' + region + '.*?\)', full_title) != []:
            remove_region = full_title.replace(re.findall(' \(' + region + '.*?\)', full_title)[0],'')
            remove_languages = re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', remove_region)
            if len(remove_languages) > 0:
                try:
                    self.regionless_title = remove_region.replace(remove_languages[0][0], '')
                except:
                    self.regionless_title = ''
            else:
                try:
                    self.regionless_title = remove_region
                except:
                    self.regionless_title = ''
        else:
            self.regionless_title = ''
            remove_languages = ''

        # Set title with minimal tags
        tag_strip_title = self.full_title
        for string in tag_strings:
            if re.findall(string, tag_strip_title) != []:
                if 'Disco' in string:
                    disc_alternative = re.search('\(Disco [A-Z0-9]\)', tag_strip_title).group()
                    # Change things so discs are ordered consistently
                    disc_alternative = disc_alternative.replace('Disco', 'Disc')
                    disc_alternative = disc_alternative.replace('Disc A', 'Disc 1')
                    disc_alternative = disc_alternative.replace('Disc B', 'Disc 2')
                    disc_alternative = disc_alternative.replace('Disc C', 'Disc 3')
                    disc_alternative = disc_alternative.replace('Disc D', 'Disc 4')
                    disc_alternative = disc_alternative.replace('Disc E', 'Disc 5')
                    disc_alternative = disc_alternative.replace('Disc F', 'Disc 6')
                    disc_alternative = disc_alternative.replace('Disc G', 'Disc 7')
                    disc_alternative = disc_alternative.replace('Disc H', 'Disc 8')
                    disc_alternative = disc_alternative.replace('Disc I', 'Disc 9')
                    disc_alternative = disc_alternative.replace('Disc J', 'Disc 10')
                    disc_alternative = disc_alternative.replace('Disc K', 'Disc 11')
                    disc_alternative = disc_alternative.replace('Disc L', 'Disc 12')
                    tag_strip_title = tag_strip_title.replace(re.findall('\(Disco [A-Z0-9]\)', tag_strip_title)[0], disc_alternative)
                elif 'Disc' in string and 'Disco' not in string:
                    disc_alternative = re.search('\(Disc [A-Z]\)', tag_strip_title).group()
                    # Change things so discs are ordered consistently
                    disc_alternative = disc_alternative.replace('Disc A', 'Disc 1')
                    disc_alternative = disc_alternative.replace('Disc B', 'Disc 2')
                    disc_alternative = disc_alternative.replace('Disc C', 'Disc 3')
                    disc_alternative = disc_alternative.replace('Disc D', 'Disc 4')
                    disc_alternative = disc_alternative.replace('Disc E', 'Disc 5')
                    disc_alternative = disc_alternative.replace('Disc F', 'Disc 6')
                    disc_alternative = disc_alternative.replace('Disc G', 'Disc 7')
                    disc_alternative = disc_alternative.replace('Disc H', 'Disc 8')
                    disc_alternative = disc_alternative.replace('Disc I', 'Disc 9')
                    disc_alternative = disc_alternative.replace('Disc J', 'Disc 10')
                    disc_alternative = disc_alternative.replace('Disc K', 'Disc 11')
                    disc_alternative = disc_alternative.replace('Disc L', 'Disc 12')
                    tag_strip_title = tag_strip_title.replace(re.findall('\(Disc [A-Z]\)', tag_strip_title)[0], disc_alternative)
                elif string == '\s?\(\d{8}\)\s?':
                    # Really basic date validation
                    tag_year = re.search('\(\d{8}\)', tag_strip_title).group()[1:-5]
                    tag_month = re.search('\(\d{8}\)', tag_strip_title).group()[5:-3]
                    tag_day = re.search('\(\d{8}\)', tag_strip_title).group()[7:-1]

                    if int(tag_year) > 1970 and int(tag_month) >= 1 and int(tag_month) < 13 and int(tag_day) >= 1 and int(tag_day) < 32:
                        tag_strip_title = tag_strip_title.replace(re.findall('\s?\(\d{8}\)\s?', tag_strip_title)[0], '')
                else:
                    tag_strip_title = tag_strip_title.replace(re.findall('' + string + '', tag_strip_title)[0],'')

        self.tag_strip_title = tag_strip_title

        # Set regionless title with minimal tags
        if re.findall(' \(' + region + '.*?\)', full_title) != []:
            remove_region = tag_strip_title.replace(re.findall(' \(' + region + '.*?\)', tag_strip_title)[0],'')
            remove_languages = re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', remove_region)
            if len(remove_languages) > 0:
                try:
                    self.rf_tag_strip_title = remove_region.replace(remove_languages[0][0], '')
                except:
                    self.rf_tag_strip_title = ''
            else:
                try:
                    self.rf_tag_strip_title = remove_region
                except:
                    self.rf_tag_strip_title = ''
        else:
            self.rf_tag_strip_title = ''
            remove_languages = ''

        self.regions = region

        if len(remove_languages) > 0:
            self.languages = remove_languages[0][0][2:-1]
        else:
            self.languages = ''

        self.category = category
        self.description = description
        self.cloneof = cloneof
        self.roms = roms

    def __str__(self):
        ret_str = ['','']
        ret_str = '  ○ full_title:\t\t' + self.full_title + '\n'
        ret_str += '  ├ description:\t' + self.description + '\n'
        ret_str += '  ├ regionless_title:\t' + self.regionless_title + '\n'
        ret_str += '  ├ tag_strip_title:\t' + self.tag_strip_title + '\n'
        ret_str += '  ├ rf_tag_strip_title:\t' + self.rf_tag_strip_title + '\n'
        ret_str += '  ├ regions:\t\t' + self.regions + '\n'
        if self.languages == '':
            ret_str += '  ├ languages:\t\tNone\n'
        else:
            ret_str += '  ├ languages:\t\t' + self.languages + '\n'
        ret_str += '  ├ cloneof:\t\t' + self.cloneof + '\n'
        ret_str += '  ├ category:\t\t' + self.category + '\n'
        ret_str += '  └ roms ┐' + '\n'
        for i, rom in enumerate(self.roms):
            if i == len(self.roms) - 1:
                ret_str += '         └ ' + 'name: ' + rom.name + ' | size: ' + rom.size + ' | crc: ' + rom.crc + ' | md5: ' + rom.md5 + ' | sha1: ' + rom.sha1 + ' | size: ' + rom.size
            else:
                ret_str += '         ├ ' + 'name: ' + rom.name + ' | size: ' + rom.size + ' | crc: ' + rom.crc + ' | md5: ' + rom.md5 + ' | sha1: ' + rom.sha1 + ' | size: ' + rom.size + '\n'
        return ret_str

class DatNodeRom:
    def __init__(self, rom, crc, md5, name, sha1, size):
        self.crc = crc
        self.md5 = md5
        self.name = name
        self.sha1 = sha1
        self.size = size

# Generic error message, also shown when the user doesn't provide any options
def help():
    command = ''
    if 'retool.py' in sys.argv[0]:
        command = 'python '

    print('\nUSAGE: ' + font.bold + command + os.path.basename(sys.argv[0]) + ' -i ' + font.end + '<input dat/folder> <options>')
    print('\nA new file is automatically generated, the original file isn\'t altered.')
    print('\nOPTIONS:')
    print(font.bold + '-o' + font.end + '    Set an output folder            ' + font.bold + ' -a' + font.end + '   Don\'t include applications')
    print(font.bold + '-1' + font.end + '    Generate a CLRMAMEPro 1G1R dat  ' + font.bold + ' -d' + font.end + '   Don\'t include demos and coverdiscs')
    print(font.bold + '-en' + font.end + '   Only include English titles     ' + font.bold + ' -e' + font.end + '   Don\'t include educational titles')
    print(font.bold + '-s' + font.end + '    Split into regional dats only,  ' + font.bold + ' -l' + font.end + '   Don\'t include titles with (Alt) tags')
    print('      don\'t look for clones            ' + font.bold + '-m' + font.end + '   Don\'t include multimedia titles')
    print('                                       ' + font.bold + '-p' + font.end + '   Don\'t include betas and prototypes\n')
    sys.exit()

# Check user input
def check_input():
    error_state = False

    # Handle most user options
    flag_1g1r = True if len([x for x in sys.argv if x == '-1']) > 0 else False
    flag_no_apps = True if len([x for x in sys.argv if x == '-a']) > 0 else False
    flag_no_demos = True if len([x for x in sys.argv if x == '-d']) > 0 else False
    flag_no_edu = True if len([x for x in sys.argv if x == '-e']) > 0 else False
    flag_no_alts = True if len([x for x in sys.argv if x == '-l']) > 0 else False
    flag_no_multi = True if len([x for x in sys.argv if x == '-m']) > 0 else False
    flag_no_protos = True if len([x for x in sys.argv if x == '-p']) > 0 else False
    flag_english_only = True if len([x for x in sys.argv if x == '-en']) > 0 else False

    # The -s option isn't compatible with -r or -en, so tell the user if they've combined them
    if len([x for x in sys.argv if x=='-s']) > 0 and len([x for x in sys.argv if x=='-r']) > 0:
        print(font.red + '* The -s and -r options can\'t be combined' + font.end)
        error_state = True
    if len([x for x in sys.argv if x=='-s']) > 0 and len([x for x in sys.argv if x=='-en']) > 0:
        print(font.red + '* The -s and -en options can\'t be combined' + font.end)
        error_state = True
    # The -1 option isn't compatible with -r, -s, or -en, so tell the user if they've combined them
    if len([x for x in sys.argv if x=='-1']) > 0 and len([x for x in sys.argv if x=='-en']) > 0:
        print(font.red + '* The -1 and -en options can\'t be combined' + font.end)
        error_state = True
    if len([x for x in sys.argv if x=='-1']) > 0 and len([x for x in sys.argv if x=='-r']) > 0:
        print(font.red + '* The -1 and -r options can\'t be combined' + font.end)
        error_state = True
    if len([x for x in sys.argv if x=='-1']) > 0 and len([x for x in sys.argv if x=='-s']) > 0:
        print(font.red + '* The -1 and -s options can\'t be combined' + font.end)
        error_state = True

    # If there are no invalid combinations, set the appropriate regional options
    else:
        flag_split_regions_no_dupes = True if len([x for x in sys.argv if x == '-r']) >= 1 else False
        flag_split_regions = True if len([x for x in sys.argv if x == '-s']) >= 1 else False

    # Handle input, output, and invalid options
    for i, x in enumerate(sys.argv):
        # Check that the options entered are valid
        if x.startswith('-'):
            if not ((x == '-i') or (x == '-o') or (x == '-1') or (x == '-a') or (x == '-d') or (x == '-e') or (x == '-l') or (x == '-m') or (x == '-p') or (x == '-r') or (x == '-s') or (x == '-en')):
                print(font.red + '* Invalid option ' + sys.argv[i] + font.end)
                error_state = True

        # Check for and handle -i
        if x == '-i':
            # Check for invalid or empty input
            if i+1 == len(sys.argv) or bool(re.search('^-([ioademprs]|en]$)', sys.argv[i+1])):
                print(font.red + '* No input file specified' + font.end)
                error_state = True
            else:
                input_file_name = os.path.abspath(sys.argv[i+1])

                if not os.path.exists(input_file_name):
                    print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.red + '* Input file "' + font.bold + input_file_name + font.end + font.red + '" does not exist.' + font.end))
                    error_state = True

        # Check for and handle -o
        if x == '-o':
                # Check for invalid or empty input
                if i+1 == len(sys.argv) or bool(re.search('^-([ioademprs]|en]$)', sys.argv[i+1])):
                    print(font.red + '* No output folder specified' + font.end)
                    error_state = True
                else:
                    output_folder_name = os.path.abspath(sys.argv[i+1])

                    # Check if the output is a folder
                    if os.path.isdir(output_folder_name) == False:
                        print(font.red + '* Output must be set to an existing folder' + font.end)
                        error_state = True

    # Check if no options have been provided
    if len(sys.argv) == 1:
        error_state = True

    # Check if -i is missing
    if len([x for x in sys.argv if x=='-i']) == 0 and len(sys.argv) != 1:
        print(font.red + '* Missing -i, no input file specified' + font.end)
        error_state = True

    # Check if the user has entered more than one -i
    if len([x for x in sys.argv if x=='-i']) > 1:
        print(font.red + '* Can\'t have more than one -i' + font.end)
        error_state = True

    # Check if the user has entered more than one -o
    if len([x for x in sys.argv if x=='-o']) > 1:
        print(font.red + '* Can\'t have more than one -o' + font.end)
        error_state = True

    # Set the ouput folder name if the user hasn't specified -o
    if len([x for x in sys.argv if x=='-o']) == 0:
            output_folder_name = os.path.abspath('.')

    # Exit if there was an error in user input
    if error_state == True:
        help()

    return UserInput(input_file_name, output_folder_name, flag_1g1r, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_alts, flag_no_multi, flag_no_edu, flag_split_regions, flag_split_regions_no_dupes, flag_english_only)

# Converts CLRMAMEPro format to XML
def convert_clr_logiqx(clrmame_header, checkdat, is_folder):
    # Get header details
    dat_name = re.sub('name |(\")', '', re.search('^\s.?name .*?$', clrmame_header[0], re.M|re.S)[0].strip())
    dat_description = re.sub('description |(\")', '', re.search('^\s.?description .*?$', clrmame_header[0], re.M|re.S)[0].strip())
    clrmame_category = re.sub('category |(\")', '', re.search('^\s.?category .*?$', clrmame_header[0], re.M|re.S)[0].strip())
    dat_version = re.sub('version |(\")', '', re.search('^\s.?version .*?$', clrmame_header[0], re.M|re.S)[0].strip())
    dat_author = re.sub('author |(\")', '', re.search('^\s.?author .*?$', clrmame_header[0], re.M|re.S)[0].strip())

    xml_convert = '<?xml version="1.0"?>\n<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd"><datafile>\n\t<header>\n'
    xml_convert += '\t\t<name>' + dat_name + '</name>\n'
    xml_convert += '\t\t<description>' + dat_description + '</description>\n'
    xml_convert += '\t\t<version>' + dat_version + '</version>\n'
    xml_convert += '\t\t<author>' + dat_author + '</author>\n\t</header>\n'

    # Get title details
    clrmame_contents = re.findall('^game \($.*?^\)$', checkdat, re.M|re.S)
    if clrmame_contents:
        for item in clrmame_contents:
            xml_node = re.split('\n', item)
            xml_convert += '\t<game name="' + re.sub('name |(\")', '', xml_node[1].strip()) + '">\n\t\t<category>' + clrmame_category + '</category>\n\t\t<description>' + re.sub('name |(\")', '', xml_node[1].strip()) + '</description>\n'
            for node in xml_node:
                if node.strip().startswith('rom'):
                    node = node
                    node = re.sub('^rom \( name ', '<rom name="', node.strip())
                    node = re.sub(' size ', '" size="', node.strip())
                    node = re.sub(' crc ', '" crc="', node.strip())
                    node = re.sub(' md5 ', '" md5="', node.strip())
                    node = re.sub('sha1 ', '" sha1="', node.strip())
                    node = re.sub(' md5 ', '" md5="', node.strip())
                    node = re.sub(' \)$', '" />', node.strip())
                    xml_convert += '\t\t' + node + '\n'
            xml_convert += '\t</game>\n'
        xml_convert += '</datafile>'
    else:
        print(font.red + 'file isn\'t Logiqx XML or CLRMAMEPro dat.' + font.end)
        if is_folder == False:
            sys.exit()
        else:
            return 'end_batch'
    return xml_convert, dat_name, dat_description, dat_author

# Creates a header for dat files
def header(dat_name, dat_version, dat_author, dat_url, dat_header_exclusion, regional_title_count, new_title_count, region, user_input):
    if new_title_count == False:
        new_title_count = ' '
    else:
        new_title_count = str('{:,}'.format(new_title_count))

    if regional_title_count == False:
        regional_title_count = ' '
    else:
        regional_title_count = str('{:,}'.format(regional_title_count))

    english_status = ''

    if user_input.english_only == True: english_status = ' (English)'

    if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
        name = '\n\t\t<name>' + dat_name + ' (Retool)' + '</name>'
        description = '\n\t\t<description>' + dat_name  + ' (' + region + ')' + english_status + dat_header_exclusion + ' (' + regional_title_count + ' of ' + new_title_count + ') (' + dat_version + ')' + '</description>'
    else:
        name = '\n\t\t<name>' + dat_name + ' (Retool)' + '</name>'
        description = '\n\t\t<description>' + dat_name + english_status + dat_header_exclusion + ' (' + new_title_count + ') (' + dat_version + ')' + '</description>'

    if dat_author != '':
        dat_author = dat_author + ' &amp; Retool'
    else:
        dat_author = 'Unknown &amp; Retool'

    header = ['<?xml version="1.0"?>',
        '\n<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">',
        '\n<datafile>',
        '\n\t<header>',
        name,
        description,
        '\n\t\t<version>' + dat_version + '</version>',
        '\n\t\t<date>' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '</date>',
        '\n\t\t<author>' + dat_author + '</author>',
        '\n\t\t<homepage>redump.org</homepage>',
        '\n\t\t<url>' + dat_url + '</url>',
        '\n\t</header>\n']
    return header

# Splits dat into regions
def localized_titles(region, native, soup, user_input):
    sys.stdout.write("\033[K")
    if native != 'Unknown':
        print('* Checking dat for titles in known regions... ' + region, sep='', end='\r', flush=True)
    if native == True:
        return soup.find_all('game', {'name':re.compile('(\(' + region + '\))')}) + soup.find_all('game', {'name':re.compile('(\(' + region + ',.*?\))')})
    elif native == 'Unknown':
        return soup.find_all('game', {'name':re.compile('^(?!.*(\(.*?(' + region + ').*?\))).*(.*)')})
    else:
        if user_input.english_only == True:
            if region == 'Europe':
                # Grab all European games that don't have languages listed, as well as those that specify English
                return soup.find_all('game', {'name':re.compile('^(?!.*(\(.*?(En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)(,|\)))).*(\(.*?' + region + '.*?\))')}) + soup.find_all('game', {'name':re.compile('(\(.*' + region + '.*?\) \(En,)')})
            else:
                return soup.find_all('game', {'name':re.compile('(\(.*' + region + '.*?\) \(.*?En(,|\)))')})
        else:
            return soup.find_all('game', {'name':re.compile('(\(' + region + '\))')}) + soup.find_all('game', {'name':re.compile('(\(' + region + ',.*?\))')})

# Adds titles in Logiqx XML dat form
def add_titles(region_list, region_list_english, region_list_other, titles, unique_list, unique_regional_titles, dupe_list, user_input, global_parent_list, tag_strings, all_titles_data):
    if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
        title_xml = {}
    else:
        title_xml = ''

    for region in region_list:
        unique_regional_titles[region] = localized_titles_unique(region, region_list_english, region_list_other, titles[region], unique_list, unique_regional_titles, dupe_list, user_input, global_parent_list, tag_strings, all_titles_data)

        if unique_regional_titles[region]['unique_titles'] != []:
            if user_input.one_game_one_rom == True:
                print('  * Adding parents from ' + region + '...', sep='', end='\r', flush=True)
            else:
                print('  * Adding titles from ' + region + '...', sep='', end='\r', flush=True)
            for title in unique_regional_titles[region]['unique_titles']:
                unique_list.append(title)

            # Add titles to XML
            if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
                title_xml[region] = convert_to_xml(region, unique_regional_titles, titles, user_input)
            else:
                title_xml += convert_to_xml(region, unique_regional_titles, titles, user_input)

            sys.stdout.write("\033[K")
            if user_input.one_game_one_rom == True:

                print('  * Adding parents from ' + region + '... done.')
            else:
                print('  * Adding titles from ' + region + '... done.')
    return title_xml

# Removes dupes that are the same title, but support different languages
def remove_by_language(language, subtitle1, subtitle2, title, regional_titles_data, remove_list):
    # If there's a title from Europe that has unspecified languages, or languages without English, take the unspecified version
    if 'Europe' in subtitle1.regions and 'Europe' in subtitle2.regions and subtitle1.languages == '' and subtitle2.languages != '' and 'En' not in subtitle2.languages:
        if subtitle2 in regional_titles_data[title]: remove_list.append(subtitle2)
        return
    elif  'Europe' in subtitle1.regions and 'Europe' in subtitle2.regions and subtitle2.languages == '' and subtitle1.languages != '' and 'En' not in subtitle1.languages:
        if subtitle1 in regional_titles_data[title]: remove_list.append(subtitle1)
        return
    # Otherwise take the title that has the language we're looking for
    if language != []:
        if re.search('\(.*' + language[0] + '.*\)', subtitle1.full_title) != None and re.search('\(.*' + language[0] + '.*\)', subtitle2.full_title) == None:
            if subtitle2 in regional_titles_data[title]: remove_list.append(subtitle2)
        elif re.search('\(.*' + language[0] + '.*\)', subtitle1.full_title) == None and re.search('\(.*' + language[0] + '.*\)', subtitle2.full_title) != None:
            if subtitle1 in regional_titles_data[title]: remove_list.append(subtitle1)
        # If both titles support the selected language, but are different lengths, take the one that supports more langauges
        elif re.search('\(.*' + language[0] + '.*\)', subtitle1.full_title) != None and re.search('\(.*' + language[0] + '.*\)', subtitle2.full_title) != None:
            if len(subtitle1.full_title) > len(subtitle2.full_title):
                if subtitle2 in regional_titles_data[title]: remove_list.append(subtitle2)
            elif len(subtitle1.full_title) < len(subtitle2.full_title):
                if subtitle1 in regional_titles_data[title]: remove_list.append(subtitle1)
            else:
                language.pop(0)
                remove_by_language(language, subtitle1, subtitle2, title, regional_titles_data, remove_list)
        else:
            language.pop(0)
            remove_by_language(language, subtitle1, subtitle2, title, regional_titles_data, remove_list)

def parent_compare_more(test1, test2, parent_list, already_tested, x, y):
    if test1 > test2:
        # print('Removing: ' + y.full_title)
        # print('Keeping: ' + x.full_title)
        if y in parent_list: del parent_list[y]
        already_tested.append(y.full_title)
        # input('>')
        return True
    elif test2 > test1:
        # print('Removing: ' + x.full_title)
        # print('Keeping: ' + y.full_title)
        if x in parent_list: del parent_list[x]
        already_tested.append(x.full_title)
        # input('>')
        return True

def parent_compare_bool(test1, test2, parent_list, already_tested, x, y, date):
    if date == '':
        if test1 == True and test2 == False:
            # print('Removing: ' + y.full_title)
            # print('Keeping: ' + x.full_title)
            if y in parent_list: del parent_list[y]
            already_tested.append(y.full_title)
            # input('>')
            return True
        elif test2 == True and test1 == False:
            # print('Removing: ' + x.full_title)
            # print('Keeping: ' + y.full_title)
            if x in parent_list: del parent_list[x]
            already_tested.append(x.full_title)
            # input('>')
            return True
    elif date == 'date':
        if test1 == True or test2 == True:
            clone_year = re.search('\(\d{8}\)', x.full_title).group()[1:-5]
            clone_month = re.search('\(\d{8}\)', x.full_title).group()[5:-3]
            clone_day = re.search('\(\d{8}\)', x.full_title).group()[7:-1]

            if int(clone_year) > 1970 and int(clone_month) >= 1 and int(clone_month) < 13 and int(clone_day) >= 1 and int(clone_day) < 32:
                if test1 == True and test2 == False:
                    # print('Removing: ' + x.full_title)
                    # print('Keeping: ' + y.full_title)
                    # input('>')
                    if x in parent_list: del parent_list[x]
                    already_tested.append(x.full_title)
                    return True
                elif test1 == False and test2 == True:
                    # print('Removing: ' + y.full_title)
                    # print('Keeping: ' + x.full_title)
                    # input('>')
                    if y in parent_list: del parent_list[y]
                    already_tested.append(y.full_title)
                    return True


# Finds unique titles in regions, removes dupes
def localized_titles_unique(region, region_list_english, region_list_other, titles, unique_list, unique_regional_titles, dupe_list, user_input, global_parent_list, tag_strings, all_titles_data):
    already_tested = []
    regional_titles = []
    regional_titles_data = {}

    for title in titles:
        # Extract each title name, with no tags
        if region !='Unknown':
            region_start = [m.span()[0] for m in re.finditer('(\(.*' + region + '.*\))', title.category.parent['name'])][0]
            region_end = [m.span()[1] for m in re.finditer('(\(.*' + region + '.*\))', title.category.parent['name'])][0]
            raw_title = title.category.parent['name'][:region_end - (region_end - region_start + 1)]
        else:
            raw_title = title.category.parent['name']

        regional_titles.append(raw_title)

        # Filter out titles based on user input flags
        if user_input.no_alts == True and re.search('(\(Alt\)|\(Alt [0-9]\))', title.category.parent['name']) != None: continue
        if user_input.no_apps == True and (title.category.contents[0] == 'Applications'): continue
        if user_input.no_demos == True and (title.category.contents[0] == 'Demos' or title.category.contents[0] == 'Coverdiscs'): continue
        if user_input.no_edu == True and (title.category.contents[0] == 'Educational'): continue
        if user_input.no_multi == True and (title.category.contents[0] == 'Multimedia'): continue
        if user_input.no_protos == True and (title.category.contents[0] == 'Preproduction'): continue

        # Build a dictionary so we don't have to go searching the XML again later
        roms = title.findChildren('rom', recursive=False)
        newroms = []
        for rom in roms:
            newroms.append(DatNodeRom('rom', rom['crc'], rom['md5'], rom['name'], rom['sha1'], rom['size']))

        # If the title doesn't already exist, add it to the regional_titles_data dictionary as a one entry list
        if regional_titles_data.get(raw_title, -1) == -1:
            regional_titles_data[raw_title] = [DatNode(str(title.category.parent['name']), region, title.category.contents[0], title.description.contents[0], newroms, 'None', tag_strings)]
        # Otherwise there must be multiple discs or revisions present, so append the title to the existing list
        else:
            regional_titles_data[raw_title].append(DatNode(str(title.category.parent['name']), region, title.category.contents[0], title.description.contents[0], newroms, 'None', tag_strings))

    # Find the uniques
    if user_input.split_regions == False:
        if user_input.one_game_one_rom == False:
            unique_regional_list = [x for x in regional_titles if x not in unique_list and x not in dupe_list]
        else:
            unique_regional_list = [x for x in regional_titles]

        # Sort and dedupe unique_regional_list
        if len(unique_regional_list) > 1:
            unique_regional_list = sorted(unique_regional_list, key=str.lower)
            unique_regional_temp = []
            for i, x in enumerate(unique_regional_list):
                if  unique_regional_list[i] != unique_regional_list[i-1]:
                    unique_regional_temp.append(unique_regional_list[i])
            unique_regional_list = unique_regional_temp

        # If not in 1G1R mode, trim the dictionary so only unique titles are in there
        regional_titles_data_temp = {}

        for x in unique_regional_list:
            if x in regional_titles_data:
                regional_titles_data_temp[x] = regional_titles_data[x]

        # Create list to remove titles later that are OEM, and dupes with alternate languages
        remove_list = []

        # Create a complete dictionary of titles across regions
        for x in regional_titles_data:
            if x in all_titles_data:
                for y in regional_titles_data[x]:
                    all_titles_data[x].append(y)
            else:
                all_titles_data[x] = regional_titles_data[x]

        for title in regional_titles_data:
            for x, y in itertools.combinations(regional_titles_data[title], 2):
                # Add titles that are just OEM versions of commercial titles to the remove list
                oem_string = re.findall(' \(OEM\).*', y.regionless_title)
                if oem_string != []:
                    if y.regionless_title == x.regionless_title + oem_string[0] or y.regionless_title.replace(oem_string[0],'') == x.regionless_title.replace(' (Rerelease)', ''):
                        remove_list.append(y)

                # Add titles that have dupes with additional regions or languages to the remove list
                if x.regionless_title == y.regionless_title and x.full_title != y.full_title:
                    # First, if we're in a native English region, take the longest title
                    if x.regions in region_list_english:
                        # Don't select titles that have more languages, but not English
                        if x.languages == '' and y.languages != '' and 'En' not in y.languages:
                            if y in regional_titles_data[title]: remove_list.append(y)
                        elif len(x.full_title) > len(y.full_title):
                            if y in regional_titles_data[title]: remove_list.append(y)
                        else:
                            if x in regional_titles_data[title]: remove_list.append(x)
                    # Now process the other regions
                    else:
                        remove_by_language(['En', 'Es', 'Fr', 'Ja', 'Pt', 'De', 'It', 'Sv', 'Da', 'No', 'Pl', 'Gr', 'Nl', 'Fi', 'Ch', 'Hr', 'Ru'], x, y, title, regional_titles_data, remove_list)

            # Now process OEM and additional region/language titles
            parent_titles = [x for x in regional_titles_data[title] if x not in remove_list]

            for item in remove_list:
                if item in regional_titles_data[title]:
                    # If not in 1G1R mode, remove the item
                    if user_input.one_game_one_rom == False:
                        regional_titles_data[title].remove(item)
                    # Otherwise, set the cloneof property instead
                    else:
                        for parent in parent_titles:
                            if item.regionless_title == parent.regionless_title and item.cloneof == 'None':
                                item.cloneof = parent.full_title

            # Remove or set clone status of older versions and revisions of titles
            highest_version = {}
            highest_revision = {}

            # Get the highest version
            for subtitle in regional_titles_data[title]:
                if bool(re.match('.*?\(v[0-9].*?$', subtitle.full_title)):
                    ver_title = re.findall('.*?\(v[0-9]', subtitle.regionless_title)[0][:-4]

                    highest_version.setdefault(ver_title, [])

                    highest_version[ver_title].append(re.findall('\(v[0-9].*?\)', str(subtitle.regionless_title))[0][2:-1])

                    highest_version[ver_title].sort(reverse = True)

            ver_title_keep = []
            ver_title_delete = []

            # Process older versions
            if len(highest_version) > 0:
                for key, value in highest_version.items():
                    for subtitle in regional_titles_data[title]:
                        if key + ' (v' + str(value[0]) in subtitle.regionless_title:
                            ver_title_keep.append(subtitle.full_title)
                        # Add original, unrevised title and its alts to delete list
                        if key == subtitle.regionless_title or bool(re.match(re.escape(key) + ' \(Alt.*?\)', subtitle.regionless_title)):
                            ver_title_delete.append(subtitle.full_title)
                    # If there are multiple titles with the same version but different languages, take the one
                    # with English. If more than one has English, take the one with the most languages
                    ver_title_keep_temp = []
                    for item in ver_title_keep:
                        ver_title_keep_temp.append(item)

                    for x, y in itertools.combinations(ver_title_keep_temp, 2):
                        x2 = x.replace(re.findall(' \(' + region + '.*?\)', x)[0],'')
                        remove_languages = re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', x)
                        if len(remove_languages) > 0:
                            try:
                                x2 = x.replace(remove_languages[0][0], '')
                            except:
                                pass

                        y2 = y.replace(re.findall(' \(' + region + '.*?\)', y)[0],'')
                        remove_languages = re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', y)
                        if len(remove_languages) > 0:
                            try:
                                y2 = y.replace(remove_languages[0][0], '')
                            except:
                                pass

                        if x2 == y2:
                            if bool(re.search('\*.?En.*?\)', x)) == True and bool(re.search('\*.?En.*?\)', y)) == False:
                                for actual_highest in ver_title_keep:
                                    if actual_highest != x:
                                        ver_title_keep.pop(ver_title_keep.index(actual_highest))
                                        ver_title_delete.append(actual_highest)
                            elif bool(re.search('\*.?En.*?\)', y)) == True and bool(re.search('\*.?En.*?\)', x)) == False:
                                for actual_highest in ver_title_keep:
                                    if actual_highest != y:
                                        ver_title_keep.pop(ver_title_keep.index(actual_highest))
                                        ver_title_delete.append(actual_highest)
                            elif len(re.findall(',', str(re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', x)))) > len(re.findall(',', str(re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', y)))):
                                for actual_highest in ver_title_keep:
                                    if actual_highest != x:
                                        ver_title_keep.pop(ver_title_keep.index(actual_highest))
                                        ver_title_delete.append(actual_highest)
                            elif len(re.findall(',', str(re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', y)))) > len(re.findall(',', str(re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', x)))):
                                for actual_highest in ver_title_keep:
                                    if actual_highest != y:
                                        ver_title_keep.pop(ver_title_keep.index(actual_highest))
                                        ver_title_delete.append(actual_highest)

                    # Add previous versions to delete list
                    for i, x in enumerate(highest_version[key]):
                        if i < len(highest_version[key]):
                            for subtitle in regional_titles_data[title]:
                                if key + ' (v' + str(x) in subtitle.regionless_title:
                                    ver_title_delete.append(subtitle.full_title)

                # Dedupe delete list. It's a hack, but a more elegant solution will have to come another time.
                ver_title_delete = [x for x in ver_title_delete if x not in ver_title_keep]
                ver_title_delete = merge_identical_list_items(ver_title_delete)

                # If not in 1G1R mode, delete lower versions
                if len(ver_title_delete) > 0 and user_input.one_game_one_rom == False:
                    for x in ver_title_delete:
                        for something in regional_titles_data[title]:
                            if something.full_title == x:
                                    regional_titles_data[title].remove(something)

            # Get the highest revision
            for subtitle in regional_titles_data[title]:
                if '(Rev ' in str(subtitle.full_title) and subtitle.full_title not in ver_title_delete:
                    rev_title = re.findall('.*?\(Rev ', subtitle.regionless_title)[0][:-6]

                    highest_revision.setdefault(rev_title, [])

                    try:
                        highest_revision[rev_title].append(int(re.findall('\(Rev [0-9]\)', str(subtitle.regionless_title))[0][4:-1]))
                    except:
                        highest_revision[rev_title].append(re.findall('\(Rev [A-Z]\)', str(subtitle.regionless_title))[0][5:-1])

                    highest_revision[rev_title].sort(reverse = True)

            rev_title_keep = []
            rev_title_delete = []

            # Process older revisions
            if len(highest_revision) > 0:
                for key, value in highest_revision.items():
                    for subtitle in regional_titles_data[title]:
                        if key + ' (Rev ' + str(value[0]) in subtitle.regionless_title:
                            rev_title_keep.append(subtitle.full_title)
                        # Add original, unrevised title and its alts to delete list
                        if key == subtitle.regionless_title or bool(re.match(re.escape(key) + ' \(Alt.*?\)', subtitle.regionless_title)):
                            rev_title_delete.append(subtitle.full_title)
                    # Add previous versions to delete list
                    for i, x in enumerate(highest_revision[key]):
                        if i > 0 and i < len(highest_revision[key]) and value[0] != 1:
                            for subtitle in regional_titles_data[title]:
                                if key + ' (Rev ' + str(x) in subtitle.regionless_title:
                                    rev_title_delete.append(subtitle.full_title)

                # Dedupe delete list. It's a hack, but a more elegant solution will have to come another time.
                rev_title_delete = merge_identical_list_items(rev_title_delete)

                rev_title_keep.sort()

                # If not in 1G1R mode, delete lower revisions
                if len(rev_title_delete) > 0 and user_input.one_game_one_rom == False:
                    for x in rev_title_delete:
                        for something in regional_titles_data[title]:
                            if something.full_title == x:
                                    regional_titles_data[title].remove(something)

            # Find parents and set clones if 1G1R mode is on
            if user_input.one_game_one_rom == True:
                rev_title_keep.sort(reverse=True)
                ver_title_keep.sort(reverse=True)

                # Strip alts from keep lists if the same title exists without the alt tag
                for x, y in itertools.combinations(rev_title_keep + ver_title_keep, 2):
                    if re.search(' \(Alt.*?\)', y) != None:
                        string1 = re.sub(' \(Alt.*?\)', '', y)
                        if string1 == x:
                            if y in rev_title_keep:
                                rev_title_keep.remove(y)
                            if y in ver_title_keep:
                                ver_title_keep.remove(y)

                # Strip clones from keep lists, figure out remainders that haven't been marked as keep or delete
                title_remainder = []

                for x in regional_titles_data[title]:
                    if x.cloneof == 'None':
                        if x in rev_title_keep: rev_title_keep.remove(x)
                        if x in ver_title_keep: ver_title_keep.remove(x)
                        title_remainder.append(x.full_title)

                title_remainder = [x for x in title_remainder if x not in rev_title_keep and x not in rev_title_delete and x not in ver_title_keep and x not in ver_title_delete]

                # Create a rough parent list so we can refine it later, reducing the amount of work done
                rough_parent_list = []
                for x in ver_title_keep + rev_title_keep + title_remainder:
                        rough_parent_list.append(x)

                # Dedupe list
                rough_parent_list = merge_identical_list_items(rough_parent_list)

                # Create refined parent list
                parent_list = {}

                for x in regional_titles_data[title]:
                    if x.full_title in rough_parent_list:
                        parent_list[x] = regional_titles_data[title]

                # Build yet another dict, because we can't alter the original on the fly in the loop below
                parent_list_temp = {}

                for x in parent_list:
                    parent_list_temp[x] = parent_list[x]

                # Determine which titles are truly parents
                for x, y in itertools.combinations(parent_list_temp, 2):
                    if x.full_title not in already_tested and y.full_title not in already_tested:
                        if x.full_title != y.full_title and x.cloneof == 'None' and y.cloneof == 'None':
                            if x.rf_tag_strip_title == y.rf_tag_strip_title:
                                # Lock comparisons to the same region for this loop
                                if bool(re.search(' \(.*?' + region + '.*?\)', x.full_title)) == True and bool(re.search(' \(.*?' + region + '.*?\)', y.full_title)) == True:
                                    # If one has a version but the other doesn't, take it
                                    test = parent_compare_bool(bool(re.search('\(v[0-9].*?\)', x.full_title)), bool(re.search('\(v[0-9].*?\)', y.full_title)), parent_list, already_tested, x, y, '')
                                    if test == True: continue

                                    # Else if one has a revision but the other doesn't, take it
                                    test = parent_compare_bool(bool(re.search('\(Rev [0-9A-Z].*?\)', x.full_title)), bool(re.search('\(Rev [0-9A-Z].*?\)', y.full_title)), parent_list, already_tested, x, y, '')
                                    if test == True: continue

                                    # Else if one title has more regions than the other, take it.
                                    test = parent_compare_more(len(re.findall(',', re.findall('\(.*?' + region + '.*?\)', x.full_title)[0])), len(re.findall(',', re.findall('\(.*?' + region + '.*?\)', y.full_title)[0])), parent_list, already_tested, x, y)
                                    if test == True: continue

                                    # Else if one supports English and the other doesn't, take the English version
                                    test = parent_compare_bool(bool('En' in x.languages), bool('En' in y.languages), parent_list, already_tested, x, y, '')
                                    if test == True: continue

                                    # Else if one has more languages than the other, take it
                                    test = parent_compare_more(len(re.findall(',', str(re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', x.tag_strip_title)))), len(re.findall(',', str(re.findall('( (\((En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)\.*?)(,.*?\)|\)))', y.tag_strip_title)))), parent_list, already_tested, x, y)
                                    if test == True: continue

                                    # Else if one has a rerelease tag, take the one that doesn't
                                    test = parent_compare_bool(bool('(Rerelease)' in y.full_title), bool('(Rerelease)' in x.full_title), parent_list, already_tested, x, y, '')
                                    if test == True: continue

                                    # Else if one has an Alt tag, take the one that doesn't
                                    test = parent_compare_bool(bool(re.search('\(Alt.*?\)', y.full_title)), bool(re.search('\(Alt.*?\)', x.full_title)), parent_list, already_tested, x, y, '')
                                    if test == True: continue

                                    # Else if one has a date tag and the other doesn't, take the one that doesn't
                                    test = parent_compare_bool(bool(re.search('\s?\(\d{8}\)\s?', x.full_title)), bool(re.search('\s?\((\d){8}\)\s?', y.full_title)), parent_list, already_tested, x, y, 'date')
                                    if test == True: continue

                for x in parent_list:
                    global_parent_list[x] = parent_list[x]
    else:
        unique_regional_list = [x for x in regional_titles]

    # Add unique list to the dictionary
    regional_titles_data['unique_titles'] = unique_regional_list

    return regional_titles_data

def merge_identical_list_items(list_dupes):
    list_dupes_temp = []
    list_dupes.sort()
    for i in range(len(list_dupes)):
        if i != 0:
            if list_dupes[i] != list_dupes[i - 1]:
                list_dupes_temp.append(list_dupes[i])
        else:
            list_dupes_temp.append(list_dupes[i])

    list_dupes = list_dupes_temp
    return list_dupes

# The actual file operations on the dat files
def process_dats(user_input, tag_strings, region_list_english, region_list_other, is_folder):
    print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill('* Reading dat file: "' + font.bold + user_input.file_input + font.end + '"'))
    try:
        with open(user_input.file_input, 'r') as input_file_read:
            print('* Validating dat file... ', sep=' ', end='', flush=True)
            checkdat = input_file_read.read()
            # Remove encoding declaration from the file so we can check validity later
            checkdat = checkdat.replace('encoding="UTF-8"','')
    except OSError as e:
        print('\n' + font.bold + font.red + '* Error: ' + font.end + str(e) + '\n')
        raise

    # Make sure the dat file isn't a CLRMAMEPro dat, if it is, check it's valid and convert it
    clrmame_header = re.findall('^clrmamepro \($.*?^\)$', checkdat, re.M|re.S)
    if clrmame_header:
        print('file is a CLRMAMEPro dat file.')
        converted_dat = convert_clr_logiqx(clrmame_header, checkdat, is_folder)

        # Process the next file in a batch operation if something went wrong
        if converted_dat == 'end_batch': return

        xml_convert = converted_dat[0]
        dat_name = converted_dat[1]
        dat_description = converted_dat[2]
        dat_author = converted_dat[3]
        dat_url = 'redump.org'
        dat_version = ''
        soup = BeautifulSoup(xml_convert, "lxml-xml")
    else:
        soup = BeautifulSoup(checkdat, "lxml-xml")

        # Check for a valid Redump XML dat that follows the Logiqx dtd, then grab the dat details
        valid_dat_file = False

        if ('<datafile>' in str(soup.contents) and '</datafile>' in str(soup.contents)):
            try:
                with open('datafile.dtd') as dtdfile:
                    dtd = etree.DTD(dtdfile)
                    root = etree.XML(checkdat)
                    if dtd.validate(root) == False:
                        print('\n' + font.bold + font.red + '* Error: XML file doesn\'t conform to Logiqx dtd' + font.end + '\n')
                        print(dtd.error_log.filter_from_errors()[0])
                        sys.exit()

            except OSError as e:
                print('\n' + font.bold + font.red + '* Error: ' + font.end + str(e) + '\n')
                raise

            valid_dat_file = True
            print('file is a Logiqx dat file.')

            if ('<header>' in str(soup.contents) and '</header>' in str(soup.contents)):
                dat_name = soup.find('name').string
                dat_description = soup.find('description').string
                dat_author = soup.find('author').string
                dat_url = soup.find('url').string
                dat_version = soup.find('version').string
            else:
                dat_name = 'Unknown'
                dat_description = 'Unknown'
                dat_author = 'Unknown'
                dat_url = None
                dat_version = '1.0'

            # Sanitize characters for output filename
            dat_name = dat_name.replace(':', '-')
            dat_version = dat_version.replace(':', '-')

            if dat_name == None: dat_name = ''
            if dat_description == None: dat_description = ''
            if dat_author == None: dat_author = ''
            if dat_url == None: dat_url = ''
            if dat_version == None: dat_version = ''

        if valid_dat_file == False:
            print(font.red + '\n* "' + user_input.file_input + '" isn\'t a CLRMAMEPro compatible dat file.' + font.end)
            if is_folder == False:
                sys.exit()
            else:
                return

    print('\n|  Description: ' + dat_description)
    print('|  Author: ' + dat_author)
    print('|  URL: ' + dat_url)
    print('|  Version: ' + dat_version + '\n')

    # Find out how many titles are in the dat file
    original_title_count = len(soup.find_all('game'))

    # Tally the other tag counts if the options have been set
    alt_count = 0
    apps_count = 0
    demos_count = 0
    edu_count = 0
    multi_count = 0
    protos_count = 0

    if user_input.no_alts == True: alt_count = len(soup.find_all('game', {'name':re.compile('(\(Alt\)|\(Alt [0-9]\))')}))
    if user_input.no_apps == True: apps_count = len(soup.find_all('category', string='Applications'))
    if user_input.no_demos == True:  demos_count = len(soup.find_all('category', string='Demos')) + len(soup.find_all('category', string='Coverdiscs'))
    if user_input.no_edu == True: edu_count = len(soup.find_all('category', string='Educational'))
    if user_input.no_multi == True: multi_count = len(soup.find_all('category', string='Multimedia'))
    if user_input.no_protos == True: protos_count = len(soup.find_all('category', string='Preproduction'))

    # Store regions in a dictionary
    titles = {}
    unique_regional_titles = {}

    # Move regions with more titles to the top for quicker processing. USA is always at [0].
    # Order mostly based on Redump's IBM dat, with Japan hoisted for other dats.
    region_lists = region_list_english + region_list_other
    region_lists_temp = ['Europe','Japan','Germany','Italy','Poland','Norway','China']

    for i, region in enumerate(region_lists_temp):
        if region in region_lists:
            region_lists.remove(region)
        region_lists.insert(i + 1, region)

    # Populate region titles
    for region in region_lists:
        if region in region_list_english:
            titles[region] = localized_titles(region, True, soup, user_input)
        else:
            titles[region] = localized_titles(region, user_input.split_regions, soup, user_input)
        # Remove found items from the soup object so processing for other regions is quicker
        for items in titles[region]:
            items.extract()

    sys.stdout.write("\033[K")
    print('* Checking dat for titles in known regions... done.')

    print('* Checking dat for titles without regions... ', sep=' ', end='', flush=True)

    # Finally, titles without regions
    region_list = ''
    for i, region in enumerate(region_list_english + region_list_other):
        if i < len(region_list_english + region_list_other) - 1:
            region_list += region + '|'
        else:
            region_list += region

    titles['Unknown'] = localized_titles(region_list, 'Unknown', soup, user_input)

    if titles['Unknown'] == []:
        print('none found.')
    else:
        print('done.')

    # Variable that holds each title's XML. Titles get added one by one to be written to a file later
    final_title_xml= ''

    # Create a list to store unique titles
    unique_list = []

    # Start work on the other regions
    if user_input.split_regions == True or user_input.split_regions_no_dupes == True:
        print('* Splitting dat into regional dats...')
    else:
        if user_input.english_only == True:
            print('* Looking for English non-dupes...')
        elif user_input.one_game_one_rom == True:
            print('* Looking for parent titles...')
        else:
            print('* Looking for non-dupes...')

    # Set up dupe lists for titles that have the same content, but different names in different regions
    dupe_list = {}

    if dat_name == 'Apple - Macintosh':
        dupe_list = _renames.mac_rename_list()
    elif dat_name == 'DVD-Video':
        dupe_list = _renames.dvd_video_rename_list()
    elif dat_name == 'Microsoft - Xbox':
        dupe_list = _renames.xbox_rename_list()
    elif dat_name == 'Microsoft - Xbox 360':
        dupe_list = _renames.x360_rename_list()
    elif dat_name == 'Microsoft - Xbox One':
        dupe_list = _renames.xbone_rename_list()
    elif dat_name == 'NEC - PC Engine CD & TurboGrafx CD':
        dupe_list = _renames.pce_rename_list()
    elif (dat_name == 'Nintendo - GameCube'
        or dat_name == 'Nintendo - GameCube - NKit GCZ'
        or dat_name == 'Nintendo - GameCube - NKit ISO'
        or dat_name == 'Nintendo - GameCube - NASOS'):
            dupe_list = _renames.gamecube_rename_list()
    elif (
        dat_name == 'Nintendo - Wii'
        or dat_name =='Nintendo - Wii - NKit GCZ'
        or dat_name =='Nintendo - Wii - NKit ISO'
        or dat_name =='Nintendo - Wii - NASOS'
        ):
            dupe_list = _renames.wii_rename_list()
    elif (
        dat_name == 'Nintendo - Wii U'
        or dat_name =='Nintendo - Wii U - WUX'
        ):
            dupe_list = _renames.wii_u_rename_list()
    elif dat_name == 'Panasonic - 3DO Interactive Multiplayer':
        dupe_list = _renames.threedo_rename_list()
    elif dat_name == 'Philips - CD-i':
        dupe_list = _renames.cdi_rename_list()
    elif dat_name == 'Sega - Dreamcast':
        dupe_list = _renames.dreamcast_rename_list()
    elif dat_name == 'Sega - Mega CD & Sega CD':
        dupe_list = _renames.segacd_rename_list()
    elif dat_name == 'Sega - Saturn':
        dupe_list = _renames.saturn_rename_list()
    elif dat_name == 'Sony - PlayStation':
        dupe_list = _renames.psx_rename_list()
    elif dat_name == 'Sony - PlayStation 2':
        dupe_list = _renames.ps2_rename_list()
    elif dat_name == 'Sony - PlayStation 3':
        dupe_list = _renames.ps3_rename_list()
    elif dat_name == 'Sony - PlayStation 4':
        dupe_list = _renames.ps4_rename_list()
    elif dat_name == 'Sony - PlayStation Portable':
        dupe_list = _renames.psp_rename_list()

    # Find unique parents in each region
    global_parent_list = {}
    all_titles_data = {}

    for region in region_list_english + region_list_other:
        if titles[region] != []:
            if user_input.one_game_one_rom == True:
                print('  * Adding parents from ' + region + '...', sep='', end='\r', flush=True)
            else:
                print('  * Adding titles from ' + region + '...', sep='', end='\r', flush=True)
        unique_regional_titles[region] = localized_titles_unique(region, region_list_english, region_list_other, titles[region], unique_list, unique_regional_titles, dupe_list, user_input, global_parent_list, tag_strings, all_titles_data)
        if titles[region] != []:
            if user_input.one_game_one_rom == True:
                print('  * Adding parents from ' + region + '... done.')
            else:
                print('  * Adding titles from ' + region + '... done.')

    unique_regional_titles['Unknown'] = localized_titles_unique('Unknown', region_list_english, region_list_other, titles['Unknown'], unique_list, unique_regional_titles, dupe_list, user_input, global_parent_list, tag_strings, all_titles_data)

    if len(unique_regional_titles['Unknown']) > 1:
        unknown_region_title_count = len(unique_regional_titles['Unknown']['unique_titles'])
    else:
        unknown_region_title_count = 0

    # Compare the parents cross-region once we're at the last region in the list
    if user_input.one_game_one_rom == True:
        # Set the temp dictionary for global parent titles
        global_parent_list_temp = {}

        parent_list_chunk = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z', 'other']

        for x in parent_list_chunk:
            global_parent_list_temp[x] = {}

        for x in global_parent_list:
            if x.full_title.lower().startswith('a') == True:
                global_parent_list_temp['a'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('b') == True:
                global_parent_list_temp['b'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('c') == True:
                global_parent_list_temp['c'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('d') == True:
                global_parent_list_temp['d'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('e') == True:
                global_parent_list_temp['e'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('f') == True:
                global_parent_list_temp['f'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('g') == True:
                global_parent_list_temp['g'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('h') == True:
                global_parent_list_temp['h'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('i') == True:
                global_parent_list_temp['i'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('j') == True:
                global_parent_list_temp['j'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('k') == True:
                global_parent_list_temp['k'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('l') == True:
                global_parent_list_temp['l'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('m') == True:
                global_parent_list_temp['m'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('n') == True:
                global_parent_list_temp['n'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('o') == True:
                global_parent_list_temp['o'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('p') == True:
                global_parent_list_temp['p'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('q') == True:
                global_parent_list_temp['q'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('r') == True:
                global_parent_list_temp['r'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('s') == True:
                global_parent_list_temp['s'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('t') == True:
                global_parent_list_temp['t'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('u') == True:
                global_parent_list_temp['u'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('v') == True:
                global_parent_list_temp['v'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('w') == True:
                global_parent_list_temp['w'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('x') == True:
                global_parent_list_temp['y'][x] = global_parent_list[x]
            elif x.full_title.lower().startswith('z') == True:
                global_parent_list_temp['z'][x] = global_parent_list[x]
            else:
                global_parent_list_temp['other'][x] = global_parent_list[x]

        progress = 0
        progress_total = 0

        # Get the proper number of parent comparisons so we can accurately show percentage
        for letter in global_parent_list_temp:
            for x, y in itertools.combinations(global_parent_list_temp[letter], 2):
                progress_total += 1

        for letter in global_parent_list_temp:
            for x, y in itertools.combinations(global_parent_list_temp[letter], 2):
                progress += 1
                progress_percent = (progress/progress_total*100)

                sys.stdout.write("\033[K")
                print('  * Comparing parents across regions... ' + str(int(progress_percent)) + '%', sep='', end='\r', flush=True)
                if x.full_title != y.full_title:
                    if x.rf_tag_strip_title == y.rf_tag_strip_title:
                        for another_region in region_list_english + region_list_other:
                            if another_region in x.full_title and another_region not in y.full_title:
                                if y in global_parent_list:
                                    # print('Remove: ' + y.full_title)
                                    # print('Keep: ' + x.full_title)
                                    del global_parent_list[y]
                                    break

        print('  * Comparing parents across regions... done.')

        progress = 0
        progress_total = len(all_titles_data)

        # Now mark the remaining clones
        if len(global_parent_list) > 0:
            for title in all_titles_data:
                print('* Finding clones... ', sep='', end='\r', flush=True)
                progress += 1
                progress_percent = (progress/progress_total*100)

                sys.stdout.write("\033[K")
                print('* Finding clones... ' + str(int(progress_percent)) + '%', sep='', end='\r', flush=True)
                for x in all_titles_data[title]:
                    for y in global_parent_list:
                        if x.full_title != y.full_title:
                            if x.rf_tag_strip_title == y.rf_tag_strip_title and x.rf_tag_strip_title != '' and y.rf_tag_strip_title != '':
                                x.cloneof = y.full_title
                        else:
                            break

            # sorted(all_titles_data, reverse=True)
            # sorted_dict = {k: all_titles_data[k] for k in sorted(all_titles_data, reverse=True)}
            # print(sorted_dict)

            # Create a list to add exclusion titles that shouldn't be clones.
            exclude_title = []

            # Look up the dupe list raw title entries
            for key, value in dupe_list.items():
                for title in all_titles_data:
                    for x in all_titles_data[title]:
                        if key == x.rf_tag_strip_title and x.cloneof == 'None':
                            # x is the parent title
                            # Now find the full_title of the rf_tag_strip_titles found in dupe_list
                            for y in value:
                                for z in all_titles_data:
                                    for a in all_titles_data[z]:
                                        # If there's a string in dupe_list, just process it
                                        if type(y) is str:
                                            if a.rf_tag_strip_title == y:
                                                # a is the clone title
                                                a.cloneof = x.full_title
                                        # Otherwise it's a list, where [0] is the clone rf_tag_strip_title,
                                        # and all other entries are full_title entries whose cloneof entry
                                        # shouldn't be touched. This is to address the King's Field problem.
                                        else:
                                            # First, if a clone short name is set to the identical short name
                                            # as the parent, append all subsequent full titles in the list to
                                            # exclude_title, and remove them from all_titles_data so it doesn't
                                            # get processed with the rest of the clones.
                                            if y[0] == key:
                                                if a.full_title in y:
                                                    a.cloneof = 'None'
                                                    exclude_title.append(a)
                                                    for j, item2 in enumerate(all_titles_data[z]):
                                                        if item2.full_title == a.full_title:
                                                            del all_titles_data[z][j]
                                            # Otherwise, set the clone so long as the full title isn't
                                            # excluded.
                                            elif a.full_title not in y:
                                                if a.rf_tag_strip_title == y[0]:
                                                    a.cloneof = x.full_title
                                            # Otherwise, if the full title has been excluded, set the
                                            # clone to none.
                                            elif a.full_title in y:
                                                a.cloneof = 'None'

            # Now add back in any titles that should be parents and not clones
            if len(exclude_title) > 0:
                for x in exclude_title:
                    all_titles_data[x.rf_tag_strip_title].append(x)

        print('* Finding clones... done.')

        # Convert to XML
        print('* Converting to XML...', sep='', end='\r', flush=True)

        progress = 0
        progress_total = len(all_titles_data)

        for title in all_titles_data:
            progress += 1
            progress_percent = (progress/progress_total*100)

            sys.stdout.write("\033[K")
            print('* Converting to XML... ' + str(int(progress_percent)) + '%', sep='', end='\r', flush=True)
            for subtitle in all_titles_data[title]:
                if subtitle.cloneof == 'None':
                    final_title_xml += '\t<game name="' + html.escape(subtitle.full_title, quote = False) + '">'
                else:
                    final_title_xml += '\t<game name="' + html.escape(subtitle.full_title, quote = False) + '" cloneof="' + html.escape(subtitle.cloneof, quote = False) + '">'
                final_title_xml += '\n\t\t<category>' + html.escape(subtitle.category, quote = False) + '</category>'
                final_title_xml += '\n\t\t<description>' + html.escape(subtitle.description, quote = False) + '</description>'
                if user_input.one_game_one_rom == True:
                    final_title_xml += '\n\t\t<release name="' + html.escape(subtitle.description, quote = False) + '" region="' + subtitle.regions + '"/>'

                for rom in subtitle.roms:
                    final_title_xml += '\n\t\t<rom crc="' + rom.crc + '" md5="' + rom.md5 + '" name="' + html.escape(rom.name, quote = False) + '" sha1="' + rom.sha1 + '" size="' + rom.size + '"/>'
                final_title_xml += '\n\t</game>\n'

        print('* Converting to XML... done.')

    # Stats so people can see something was done
    new_title_count = 0

    if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
        new_title_count_region = {}
        for region in region_list_english + region_list_other:
            if final_title_xml.get(region, -1) != -1:
                new_title_count_region[region] = final_title_xml[region].count('<game name=')
                new_title_count += int(new_title_count_region[region])
        new_title_count += unknown_region_title_count
    else:
        new_title_count = final_title_xml.count('<game name=')

    if new_title_count == 0:
        print(font.yellow + '\n* No titles found. No dat file has been created.' + font.end)
        if is_folder == False:
            sys.exit()
        else:
            return

    print('\nStats:\n○  Original title count: ' + str('{:,}'.format(original_title_count)))

    if user_input.no_alts == True: print('-  Alternate titles removed: ' + str('{:,}'.format(alt_count)))
    if user_input.no_apps == True: print('-  Applications removed: ' + str('{:,}'.format(apps_count)))
    if user_input.no_demos == True: print('-  Demos removed: ' + str('{:,}'.format(demos_count)))
    if user_input.no_edu == True: print('-  Educational titles removed: ' + str('{:,}'.format(edu_count)))
    if user_input.no_multi == True: print('-  Multimedia titles removed: ' + str('{:,}'.format(multi_count)))
    if user_input.no_protos == True: print('-  Prototypes and betas removed: ' + str('{:,}'.format(protos_count)))
    if len(unique_regional_titles['Unknown']) > 1:  print('+  Titles without regions included (might not be English): ' + str('{:,}'.format(unknown_region_title_count)))

    dupe_count = original_title_count - new_title_count -alt_count -apps_count - demos_count - edu_count - multi_count - protos_count
    if dupe_count < 0: dupe_count = 0

    english_status = ''
    if user_input.one_game_one_rom == False:
        if user_input.english_only == True:
            english_status = ' (English)'
            print('-  Dupes and non-English titles removed: ' + str('{:,}'.format(dupe_count)))
        else:
            print('-  Dupes removed: ' + str('{:,}'.format(dupe_count)))
    else:
        clone_count = 0
        clone_count = final_title_xml.count('cloneof=')
        print('-  Clones identified: ' + str('{:,}'.format(clone_count)))

    print(font.bold + '---------------------------')
    if user_input.one_game_one_rom == False:
        print('=  New title count: ' + str('{:,}'.format(new_title_count)) + font.end + '\n')
    else:
        print('=  New title count: ' + str('{:,}'.format(new_title_count)) + font.end)
        print('   Parents: ' + str('{:,}'.format(new_title_count - clone_count)))
        print('   Clones: ' + str('{:,}'.format(clone_count)) + '\n')

    # Set up final output filename and dat header strings
    if user_input.file_output != '':
        output_folder = user_input.file_output
        user_input.file_output_final = os.path.join(output_folder, dat_name)
    else:
        user_input.file_output_final = dat_name

    dat_version_filename = ''
    if dat_version != '': dat_version_filename = ' (' + dat_version + ')'

    dat_header_exclusion = ''

    if user_input.one_game_one_rom == True:
        dat_header_exclusion += ' [1G1R]'
    if user_input.no_apps == True or user_input.no_demos == True or user_input.no_edu == True or user_input.no_multi == True or user_input.no_protos == True or user_input.no_alts == True or user_input.split_regions == True or user_input.split_regions_no_dupes == True:
        dat_header_exclusion += ' (-'
        if user_input.no_apps == True: dat_header_exclusion += 'a'
        if user_input.no_demos == True: dat_header_exclusion += 'd'
        if user_input.no_edu == True: dat_header_exclusion += 'e'
        if user_input.no_alts == True: dat_header_exclusion += 'l'
        if user_input.no_multi == True: dat_header_exclusion += 'm'
        if user_input.no_protos == True: dat_header_exclusion += 'p'
        if user_input.split_regions_no_dupes == True: dat_header_exclusion += 'r'
        if user_input.split_regions == True: dat_header_exclusion += 's'

        dat_header_exclusion += ')'

    # Write the dat files
    try:
        file_name_title_count = {}
        if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
            print('* Writing regional dat files...\n')
            for region in region_list_english + region_list_other:
                if final_title_xml.get(region, -1) != -1 and new_title_count_region[region] > 0:
                    output_file_suffix = ' (' + region + ')' + english_status + dat_header_exclusion + ' (' + str('{:,}'.format(new_title_count_region[region])) + ' of ' + str('{:,}'.format(new_title_count)) + ')' + dat_version_filename + ' (Retool ' +  datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3] + ')' + '.dat'
                    dat_header = header(dat_name, dat_version, dat_author, dat_url, dat_header_exclusion, new_title_count_region[region], new_title_count, region, user_input)
                    output_file_data = final_title_xml[region]

            if final_title_xml.get('Unknown', -1) != -1:
                output_file_suffix = ' (Unknown)' + english_status + dat_header_exclusion + ' (' + str('{:,}'.format(unknown_region_title_count)) + ' of ' + str('{:,}'.format(new_title_count)) + ')' + dat_version_filename + ' (Retool ' +  datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3] + ')' + '.dat'
                dat_header = header(dat_name, dat_version, dat_author, dat_url, dat_header_exclusion, unknown_region_title_count, new_title_count, 'Unknown', user_input)
                output_file_data = final_title_xml['Unknown']
        else:
            print('* Writing dat file...\n')
            output_file_suffix = english_status + dat_header_exclusion + ' (' + str('{:,}'.format(new_title_count)) + ')' + dat_version_filename + ' (Retool ' +  datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3] + ')' + '.dat'
            dat_header = header(dat_name, dat_version, dat_author, dat_url, dat_header_exclusion, False, new_title_count, False, user_input)
            output_file_data = final_title_xml

        with open(user_input.file_output_final + output_file_suffix, 'w') as output_file:
            output_file.writelines(dat_header)
            output_file.writelines(output_file_data)
            output_file.writelines('</datafile>')
            output_file.close()

        file_name_title_count['output_file'] = output_file.name
        file_name_title_count['new_title_count'] = new_title_count

        return file_name_title_count
    except OSError as e:
        print('\n' + font.bold + font.red + '* Error: ' + font.end + str(e) + '\n')
        raise

if __name__ == '__main__':
    main()