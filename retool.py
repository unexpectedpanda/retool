# Retool scans [Redump](http://redump.org/) dats, and attempts to
# generate new dats without dupes. Some call this 1G1R.  This is not an
# official Redump project.
#
# Dependencies:
# * bs4
# * lxml

import os
import sys
import re
import datetime
import time
import textwrap
import html
from lxml import etree
from bs4 import BeautifulSoup, Doctype # For XML parsing
import _regional_renames # Duplicate image titles that have different names in different regions

# Require at least Python 3.5
assert sys.version_info >= (3, 5)

version_number = '0.40'

def main():
    # Initial splash screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(font.red + ' ____     _____ ___   ___  _' +
    '\n|  _ \ __|_   _/ _ \ / _ \| |' +
    '\n| |_) / _ \| || | | | | | | |' +
    '\n|  _ <  __/| || |_| | |_| | |___' +
    '\n|_| \_\___||_| \___/ \___/|_____/ ' + font.end + 'v' + version_number)

    print('=======================================\n')
    if len(sys.argv) == 1:
        print(textwrap.fill('Scans Redump (' + font.underline + 'http://redump.org/' + font.end + ') dats, and attempts to generate new dats without dupes. This is not an official Redump project.', 80))

    # Define regions where English is a primary language
    region_list_english = [
        'USA',
        'World',
        'UK',
        'Canada',
        'Australia',
        'New Zealand',
        'Singapore',
        'Ireland',
    ]

    # Define regions where titles might have an English version
    region_list_other = [
        'Europe',
        'Asia',
        'Scandinavia',
        'Japan',
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

    # Check user input
    user_input = check_input(region_list_english, region_list_other)

    # Record when the process started
    start = time.time()

    # Start processing the dats
    if os.path.isdir(user_input.file_input) == True:
        input_folder = user_input.file_input
        file_count = 0

        for file in os.listdir(input_folder):
            if file.endswith('.dat'):
                file_count += 1
                user_input.file_input = os.path.join(input_folder, file)
                process_dats(user_input, region_list_english, region_list_other, True)

        stop = time.time()

        if file_count == 1:
            file_plural_singular = 'file'
        else:
            file_plural_singular = 'files'

        if file_count != 0:
            if user_input.split_regions_no_dupes == True:
                print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished processing ' + str('{:,}'.format(file_count)) + ' ' + file_plural_singular + ' in the "' + font.bold + input_folder + font.end + font.green + '" folder in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's. Unique titles have been added to regional dats in the\n"' + font.bold + user_input.file_output + font.end + font.green + '"\nfolder.' + font.end) + '\n')
            elif user_input.split_regions == True:
                print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished processing ' + str('{:,}'.format(file_count)) + ' ' + file_plural_singular + ' in the "' + font.bold + input_folder + font.end + font.green + '" folder in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's. All dats have been split into regions in the\n"' + font.bold + user_input.file_output + font.end + font.green + '"\nfolder.' + font.end) + '\n')
            else:
                print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished processing ' + str('{:,}'.format(file_count)) + ' ' + file_plural_singular + ' in the "' + font.bold + input_folder + font.end + font.green + '" folder in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's. Unique titles have been added to dats in the\n"' + font.bold + user_input.file_output + font.end + font.green + '"\nfolder.' + font.end) + '\n')
        else:
            print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.yellow + '* No files found to process in the "' + font.bold + input_folder + font.end + font.yellow + '" folder.' + font.end) + '\n')

        sys.exit()
    else:
        file_name_title_count = process_dats(user_input, region_list_english, region_list_other, False)

        stop = time.time()

        english_status = ''
        english_status2 = ''
        if user_input.english_only == True:
            english_status = ' English'
            english_status2 = ' (English)'

        if user_input.split_regions_no_dupes == True:
            print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished adding unique' + english_status + ' titles to regional dats in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's.' + font.end) + '\n')
        elif user_input.split_regions == True:
            print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished splitting "' + font.bold + user_input.file_input + font.end + font.green + '" into regional dats in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's.' + font.end) + '\n')
        else:
            print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished adding ' + str('{:,}'.format(file_name_title_count['new_title_count'])) + ' unique' + english_status + ' titles to "' +  font.bold + file_name_title_count['output_file'] + font.end + font.green + '" in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's.' + font.end) + '\n')
    return

############### Classes and methods ###############

# Console text formatting
# https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
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

# Generic error message
command = ''
if 'retool.py' in sys.argv[0]:
    command = 'python '
def error_instruction():
    print('\nUSAGE:\n ' + font.bold + command + os.path.basename(sys.argv[0]) + ' -i ' + font.end + '<input dat/folder> <options>\n')
    print('\nOPTIONS:')
    print(font.bold + ' -en' + font.end + '  Only include English titles')
    # print(font.bold + ' -1' + font.end + '   Create 1G1R dat (-a -d -e -l -m -o -p)')
    print(font.bold + ' -a' + font.end + '   Remove applications')
    print(font.bold + ' -d' + font.end + '   Remove demos and coverdiscs')
    print(font.bold + ' -e' + font.end + '   Remove educational titles')
    print(font.bold + ' -l' + font.end + '   Remove titles with (Alt) tags')
    print(font.bold + ' -m' + font.end + '   Remove multimedia titles')
    print(font.bold + ' -o' + font.end + '   Set an output folder')
    print(font.bold + ' -p' + font.end + '   Remove betas and prototypes')
    print(font.bold + ' -r' + font.end + '   Split dat into regional dats')
    print(font.bold + ' -s' + font.end + '   Split dat into regional dats, include dupes\n')
    sys.exit()

# Check user input
def check_input(region_list_english, region_list_other):
    error_state = False

    # Handle optional flags
    flag_no_apps = True if len([x for x in sys.argv if x == '-a']) >= 1 else False
    flag_no_demos = True if len([x for x in sys.argv if x == '-d']) >= 1 else False
    flag_no_edu = True if len([x for x in sys.argv if x == '-e']) >= 1 else False
    flag_no_alts = True if len([x for x in sys.argv if x == '-l']) >= 1 else False
    flag_no_multi = True if len([x for x in sys.argv if x == '-m']) >= 1 else False
    flag_no_protos = True if len([x for x in sys.argv if x == '-p']) >= 1 else False
    flag_english_only = True if len([x for x in sys.argv if x == '-en']) >= 1 else False

    if len([x for x in sys.argv if '-s' in x]) > 0 and len([x for x in sys.argv if '-r' in x]) > 0:
        print(font.red + '* The -s and -r options can\'t be combined' + font.end)
        error_state = True
    if len([x for x in sys.argv if '-s' in x]) > 0 and len([x for x in sys.argv if '-en' in x]) > 0:
        print(font.red + '* The -s and -en options can\'t be combined' + font.end)
        error_state = True
    else:
        flag_split_regions_no_dupes = True if len([x for x in sys.argv if x == '-r']) >= 1 else False
        flag_split_regions = True if len([x for x in sys.argv if x == '-s']) >= 1 else False

    # If no flags provided, or if -i is missing
    if len(sys.argv) == 1:
        error_instruction()

    if len([x for x in sys.argv if '-i' in x]) == 0:
        if len([x for x in sys.argv if '-i' in x]) == 0:
            print(font.red + '* Missing -i, no input file specified' + font.end)

        error_state = True

    # Handle input, output, recursive, and invalid flags
    excess_i = False
    excess_o = False
    i_is_folder = False
    o_is_folder = False

    for i, x in enumerate(sys.argv):
        if x.startswith('-'):
            if not ((x == '-i') or (x == '-o') or (x == '-a') or (x == '-d') or (x == '-e') or (x == '-l') or (x == '-m') or (x == '-p') or (x == '-s') or (x == '-r') or (x == '-en')):
                print(font.red + '* Invalid option ' + sys.argv[i] + font.end)
                error_state = True
        if x == '-i':
            if i+1 == len(sys.argv) or bool(re.search('^-([ioademprs]|en]$)', sys.argv[i+1])):
                print(font.red + '* No input file specified' + font.end)
                error_state = True
            else:
                input_file_name = os.path.abspath(sys.argv[i+1])

                if not os.path.exists(input_file_name):
                    print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.red + '* Input file "' + font.bold + input_file_name + font.end + font.red + '" does not exist.' + font.end))
                    error_state = True

                if os.path.isdir(input_file_name):
                    i_is_folder = True

            if len([x for x in sys.argv if '-i' in x]) > 1:
                excess_i = True
                error_state = True

        if x == '-o':
                if i+1 == len(sys.argv) or bool(re.search('^-([ioademprs]|en]$)', sys.argv[i+1])):
                    print(font.red + '* No output folder specified' + font.end)
                    error_state = True
                else:
                    output_file_name = os.path.abspath(sys.argv[i+1])

                    # Check that output is a folder
                    if os.path.isdir(output_file_name) == False:
                        print(font.red + '* Output must be set to an existing folder' + font.end)
                        error_state = True

        if len([x for x in sys.argv if '-o' in x]) > 1:
                excess_o = True
                error_state = True

    if len([x for x in sys.argv if '-o' in x]) == 0 and i_is_folder == False:
        output_file_name = ''

    if len([x for x in sys.argv if '-o' in x]) == 0 and i_is_folder == True:
        output_file_name = os.path.abspath('.')

    if excess_i == True: print(font.red + '* Can\'t have more than one -i' + font.end)
    if excess_o == True: print(font.red + '* Can\'t have more than one -o' + font.end)

    # Exit if there was an error in user input
    if error_state == True:
        error_instruction()

    # Check if the user defined output file already exists
    overwrite_file = False

    english_status = ''
    if flag_english_only == True:
        english_status = ' (English)'

    return UserInput(input_file_name, output_file_name, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_alts, flag_no_multi, flag_no_edu, flag_split_regions, flag_split_regions_no_dupes, flag_english_only)

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
        name = '\n\t\t<name>' + dat_name + ' (' + region + ')' + english_status + dat_header_exclusion + ' (' + regional_title_count + ' of ' + new_title_count + ') (' + dat_version + ')' + '</name>'
        description = '\n\t\t<description>' + dat_name  + ' (' + region + ')' + english_status + dat_header_exclusion + ' (' + regional_title_count + ' of ' + new_title_count + ') (' + dat_version + ')' + '</description>'
    else:
        name = '\n\t\t<name>' + dat_name + english_status + dat_header_exclusion + ' (' + new_title_count + ') (' + dat_version + ')' + '</name>'
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

#Establish a class for user input
class UserInput:
    def __init__(self, file_input, file_output, no_demos, no_apps, no_protos, no_alts, no_multi, no_edu, split_regions, split_regions_no_dupes, english_only):
        self.file_input = file_input
        self.file_output = file_output
        self.no_demos = no_demos
        self.no_apps = no_apps
        self.no_alts = no_alts
        self.no_multi = no_multi
        self.no_protos = no_protos
        self.no_edu = no_edu
        self.split_regions = split_regions
        self.split_regions_no_dupes = split_regions_no_dupes
        self.english_only = english_only

# Establish a class for title data
class DatNode:
    def __init__(self, full_title, region, category, description, roms):
        self.full_title = full_title

        if re.findall(' \(' + region + '.*?\)', full_title) != []:
            remove_region = full_title.replace(re.findall(' \(' + region + '.*?\)', full_title)[0],'')
            remove_languages = re.findall('( (\(En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)(,.*?\)|\)))', remove_region)
            if len(remove_languages) > 0:
                try:
                    self.full_title_regionless = remove_region.replace(remove_languages[0][0], '')
                except:
                    self.full_title_regionless = ''
            else:
                try:
                    self.full_title_regionless = remove_region
                except:
                    self.full_title_regionless = ''
        else:
            self.full_title_regionless = ''

        self.category = category
        self.description = description
        self.roms = roms

class DatNodeRom:
    def __init__(self, rom, crc, md5, name, sha1, size):
        self.crc = crc
        self.md5 = md5
        self.name = name
        self.sha1 = sha1
        self.size = size

# Splits dat into regions
def localized_titles(region, native, soup, user_input):
    sys.stdout.write("\033[K")
    if native != 'Unknown':
        print('* Checking dat for regions... ' + region, sep='', end='\r', flush=True)
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
def add_titles(region_list, titles, unique_list, dupe_list, user_input, unique_regional_titles):
    if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
        title_xml = {}
    else:
        title_xml = ''

    for region in region_list:
        unique_regional_titles[region] = localized_titles_unique(region, titles[region], unique_list, dupe_list, user_input)

        if unique_regional_titles[region]['unique_titles'] != []:
            print('  * Adding titles from ' + region + '...', sep='', end='\r', flush=True)
            for title in unique_regional_titles[region]['unique_titles']:
                unique_list.append(title)

            # Add titles to XML
            if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
                title_xml[region] = convert_to_xml(region, unique_regional_titles, titles, user_input)
            else:
                title_xml += convert_to_xml(region, unique_regional_titles, titles, user_input)

            sys.stdout.write("\033[K")
            print('  * Adding titles from ' + region + '... done.')
    return title_xml

# Finds unique titles in regions, removes dupes
def localized_titles_unique (region, titles, unique_list, dupe_list, user_input):
    regional_titles = []
    regional_titles_data = {}

    # Extract each title name
    for title in titles:
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

        # Check that there aren't multiple discs or revisions
        if regional_titles_data.get(raw_title, -1) != -1:
            regional_titles_data[raw_title].append(DatNode(str(title.category.parent['name']), region, title.category.contents[0], title.description.contents[0], newroms))
        else:
            regional_titles_data[raw_title] = [DatNode(str(title.category.parent['name']), region, title.category.contents[0], title.description.contents[0], newroms)]

    # Find the uniques
    if user_input.split_regions == False:
        unique_regional_list = [x for x in regional_titles if x not in unique_list and x not in dupe_list]

        # Sort and dedupe unique_regional_list
        if len(unique_regional_list) > 1:
            unique_regional_list = sorted(unique_regional_list, key=str.lower)
            unique_regional_temp = []
            for i, x in enumerate(unique_regional_list):
                if  unique_regional_list[i] != unique_regional_list[i-1]:
                    unique_regional_temp.append(unique_regional_list[i])
            unique_regional_list = unique_regional_temp

        # Trim the dictionary so only unique titles are in there
        regional_titles_data_temp = {}

        for x in unique_regional_list:
            if x in regional_titles_data:
                regional_titles_data_temp[x] = regional_titles_data[x]

        regional_titles_data = regional_titles_data_temp

        # Remove titles that have dupes with additional regions
        for title in regional_titles_data:
            for subtitle in regional_titles_data[title]:
                for subtitle2 in regional_titles_data[title]:
                    if subtitle.full_title_regionless == subtitle2.full_title_regionless and subtitle.full_title != subtitle2.full_title:
                        if len(subtitle.full_title) < len(subtitle2.full_title):
                            regional_titles_data[title].remove(subtitle2)
                        else:
                            regional_titles_data[title].remove(subtitle)

        # Remove older versions and revisions of titles
        for title in regional_titles_data:
            # print('\n' + font.bold + '■  ' + title + font.end)
            highest_version = {}
            highest_revision = {}

            # First, get the highest version
            for subtitle in regional_titles_data[title]:
                # print('   └ ' + subtitle.full_title)

                # print('   └ ' + str(vars(subtitle)))
                # for i, rom in enumerate(subtitle.roms):
                #     if i == len(subtitle.roms) - 1:
                #         print('        └ ' + str(vars(rom)))
                #     else:
                #         print('        ├ ' + str(vars(rom)))

                if bool(re.match('.*?\(v[0-9].*?$', subtitle.full_title)):
                    ver_title = re.findall('.*?\(v[0-9]', subtitle.full_title_regionless)[0][:-4]

                    highest_version.setdefault(ver_title, [])

                    highest_version[ver_title].append(re.findall('\(v[0-9].*?\)', str(subtitle.full_title_regionless))[0][2:-1])

                    highest_version[ver_title].sort(reverse = True)

            if len(highest_version) > 0:
                ver_title_keep = []
                ver_title_delete = []

                for key, value in highest_version.items():
                    for subtitle in regional_titles_data[title]:
                        if key + ' (v' + str(value[0]) in subtitle.full_title_regionless:
                            ver_title_keep.append(subtitle.full_title)
                        # Delete original, unrevised title and its alts
                        if key == subtitle.full_title_regionless or bool(re.match(re.escape(key) + ' \(Alt.*?\)', subtitle.full_title_regionless)):
                            ver_title_delete.append(subtitle.full_title)
                    # Delete previous versions
                    for i, x in enumerate(highest_version[key]):
                        if i < len(highest_version[key]):
                            for subtitle in regional_titles_data[title]:
                                if key + ' (v' + str(x) in subtitle.full_title_regionless:
                                    ver_title_delete.append(subtitle.full_title)

                # Dedupe delete list. It's a hack, but a more elegant solution will have to come another time.
                ver_title_delete = [x for x in ver_title_delete if x not in ver_title_keep]
                ver_title_delete = merge_identical_list_items(ver_title_delete)

                if len(ver_title_delete) > 0:
                    for x in ver_title_delete:
                        for something in regional_titles_data[title]:
                            if something.full_title == x:
                                regional_titles_data[title].remove(something)

            # Then, get the highest revision
            for subtitle in regional_titles_data[title]:
                if '(Rev ' in str(subtitle.full_title):
                    # Get the base titles
                    rev_title = re.findall('.*?\(Rev ', subtitle.full_title_regionless)[0][:-6]

                    highest_revision.setdefault(rev_title, [])

                    try:
                        highest_revision[rev_title].append(int(re.findall('\(Rev [0-9]\)', str(subtitle.full_title_regionless))[0][4:-1]))
                    except:
                        highest_revision[rev_title].append(re.findall('\(Rev [A-Z]\)', str(subtitle.full_title_regionless))[0][5:-1])

                    highest_revision[rev_title].sort(reverse = True)

            if len(highest_revision) > 0:

                # print('\n---RAW-REVISION------')
                # print(highest_revision)

                # Delete older titles
                rev_title_keep = []
                rev_title_delete = []

                for key, value in highest_revision.items():
                    for subtitle in regional_titles_data[title]:
                        if key + ' (Rev ' + str(value[0]) in subtitle.full_title_regionless:
                            rev_title_keep.append(subtitle.full_title)
                        # Delete original, unrevised title and its alts
                        if key == subtitle.full_title_regionless or bool(re.match(re.escape(key) + ' \(Alt.*?\)', subtitle.full_title_regionless)):
                            rev_title_delete.append(subtitle.full_title)
                    # Delete previous versions
                    for i, x in enumerate(highest_revision[key]):
                        if i > 0 and i < len(highest_revision[key]) and value[0] != 1:
                            for subtitle in regional_titles_data[title]:
                                if key + ' (Rev ' + str(x) in subtitle.full_title_regionless:
                                    rev_title_delete.append(subtitle.full_title)

                # Dedupe delete list. It's a hack, but a more elegant solution will have to come another time.
                rev_title_delete = merge_identical_list_items(rev_title_delete)

                # print('\n---KEEP--------------')
                rev_title_keep.sort()
                # for x in rev_title_keep:
                #     print(x)

                if len(rev_title_delete) > 0:
                    # print('\n---DELETE--------------')

                    for x in rev_title_delete:
                        # print(x)
                        for something in regional_titles_data[title]:
                            if something.full_title == x:
                                regional_titles_data[title].remove(something)


                # print('\n---ALSO KEEP---------')

                # rev_title_remainder = []
                # for subtitle in regional_titles_data[title]:
                #     rev_title_remainder.append(subtitle.full_title)

                # rev_title_remainder = [x for x in rev_title_remainder if x not in rev_title_keep and x not in rev_title_delete]

                # for x in rev_title_remainder:
                #     print(x)

                # input('>')
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
            if list_dupes[i] != list_dupes[i-1]:
                list_dupes_temp.append(list_dupes[i])
        else:
            list_dupes_temp.append(list_dupes[i])

    list_dupes = list_dupes_temp
    return list_dupes

# Uses a title to create its original XML node, dedupe versions
def convert_to_xml(region, unique_regional_titles, titles, user_input):
    final_title_xml = ''
    if unique_regional_titles[region] != []:
            progress = 0
            progress_total = len(unique_regional_titles[region])

            for title in unique_regional_titles[region]:
                if title != 'unique_titles':
                    for subtitle in unique_regional_titles[region][title]:
                        final_title_xml += '\t<game name="' + html.escape(subtitle.full_title) + '">'
                        final_title_xml += '\n\t\t<category>' + html.escape(subtitle.category) + '</category>'
                        final_title_xml += '\n\t\t<description>' + html.escape(subtitle.description) + '</description>'
                        for rom in subtitle.roms:
                            final_title_xml += '\n\t\t<rom crc="' + rom.crc + '" md5="' + rom.md5 + '" name="' + html.escape(rom.name) + '" sha1="' + rom.sha1 + '" size="' + rom.size + '"/>'
                        final_title_xml += '\n\t</game>\n'

                progress += 1
                progress_percent = progress/progress_total*100
                sys.stdout.write("\033[K")
                print('  * Adding unique titles from ' + region + '... ' + str(int(progress_percent)) + '%', sep='', end='\r', flush=True)
    return final_title_xml

# The actual file operations on the dat files
def process_dats(user_input, region_list_english, region_list_other, is_folder):
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

            # Sanitize any info used for output file name
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

    # Store regions in a dictionary
    titles = {}
    unique_regional_titles = {}

    # First populate the regions that are natively in English
    for region in region_list_english:
        titles[region] = localized_titles(region, True, soup, user_input)

    # Now those that might have English versions
    for region in region_list_other:
        titles[region] = localized_titles(region, user_input.split_regions, soup, user_input)

    sys.stdout.write("\033[K")
    print('* Checking dat for regions... done.')

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
        else:
            print('* Looking for non-dupes...')

    # Set up dupe lists for titles that have the same content, but different names in different regions
    dupe_list = []

    if dat_name == 'Apple - Macintosh': dupe_list = _regional_renames.mac_rename_list()
    if dat_name == 'DVD-Video': dupe_list = _regional_renames.dvd_video_rename_list()
    if dat_name == 'Microsoft - Xbox': dupe_list = _regional_renames.xbox_rename_list()
    if dat_name == 'Microsoft - Xbox 360': dupe_list = _regional_renames.x360_rename_list()
    if dat_name == 'Microsoft - Xbox One': dupe_list = _regional_renames.xbone_rename_list()
    if dat_name == 'NEC - PC Engine CD & TurboGrafx CD': dupe_list = _regional_renames.pce_rename_list()
    if dat_name == 'Nintendo - GameCube' or dat_name == 'Nintendo - GameCube - NKit GCZ' or dat_name == 'Nintendo - GameCube - NKit ISO' or dat_name == 'Nintendo - GameCube - NASOS': dupe_list = _regional_renames.gamecube_rename_list()
    if dat_name == 'Nintendo - Wii' or dat_name =='Nintendo - Wii - NKit GCZ' or dat_name =='Nintendo - Wii - NKit ISO' or dat_name =='Nintendo - Wii - NASOS': dupe_list = _regional_renames.wii_rename_list()
    if dat_name == 'Nintendo - Wii U' or dat_name =='Nintendo - Wii U - WUX': dupe_list = _regional_renames.wii_u_rename_list()
    if dat_name == 'Panasonic - 3DO Interactive Multiplayer': dupe_list = _regional_renames.threedo_rename_list()
    if dat_name == 'Philips - CD-i': dupe_list = _regional_renames.cdi_rename_list()
    if dat_name == 'Sega - Dreamcast': dupe_list = _regional_renames.dreamcast_rename_list()
    if dat_name == 'Sega - Mega CD & Sega CD': dupe_list = _regional_renames.segacd_rename_list()
    if dat_name == 'Sega - Saturn': dupe_list = _regional_renames.saturn_rename_list()
    if dat_name == 'Sony - PlayStation': dupe_list = _regional_renames.psx_rename_list()
    if dat_name == 'Sony - PlayStation 2': dupe_list = _regional_renames.ps2_rename_list()
    if dat_name == 'Sony - PlayStation 3': dupe_list = _regional_renames.ps3_rename_list()
    if dat_name == 'Sony - PlayStation 4': dupe_list = _regional_renames.ps4_rename_list()
    if dat_name == 'Sony - PlayStation Portable': dupe_list = _regional_renames.psp_rename_list()

    # Find unique titles in each region and add their XML node
    final_title_xml = add_titles(region_list_english + region_list_other, titles, unique_list, dupe_list, user_input, unique_regional_titles)

    unique_regional_titles['Unknown'] = localized_titles_unique('Unknown', titles['Unknown'], unique_list, dupe_list, user_input)

    # Find titles without regions
    if len(unique_regional_titles['Unknown']) > 1:
        unknown_region_title_count = len(unique_regional_titles['Unknown']['unique_titles'])
        print('  * Adding titles without regions...', sep='', end='\r', flush=True)

        # Add titles to XML
        if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
            final_title_xml['Unknown'] = convert_to_xml('Unknown', unique_regional_titles, titles, user_input)
        else:
            final_title_xml += convert_to_xml('Unknown', unique_regional_titles, titles, user_input)

        sys.stdout.write("\033[K")
        print('  * Adding titles without regions... done.')
    else:
        unknown_region_title_count = 0

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
    alt_count = 0
    apps_count = 0
    demos_count = 0
    edu_count = 0
    multi_count = 0
    protos_count = 0

    if user_input.no_alts == True:
        alt_count = len(soup.find_all('game', {'name':re.compile('(\(Alt\)|\(Alt [0-9]\))')}))
        print('-  Alternate titles removed: ' + str('{:,}'.format(alt_count)))
    if user_input.no_apps == True:
        apps_count = len(soup.find_all('category', string='Applications'))
        print('-  Applications removed: ' + str('{:,}'.format(apps_count)))
    if user_input.no_demos == True:
        demos_count = len(soup.find_all('category', string='Demos')) + len(soup.find_all('category', string='Coverdiscs'))
        print('-  Demos removed: ' + str('{:,}'.format(demos_count)))
    if user_input.no_edu == True:
        edu_count = len(soup.find_all('category', string='Educational'))
        print('-  Educational titles removed: ' + str('{:,}'.format(edu_count)))
    if user_input.no_multi == True:
        multi_count = len(soup.find_all('category', string='Multimedia'))
        print('-  Multimedia titles removed: ' + str('{:,}'.format(multi_count)))
    if user_input.no_protos == True:
        protos_count = len(soup.find_all('category', string='Preproduction'))
        print('-  Prototypes and betas removed: ' + str('{:,}'.format(protos_count)))
    if len(unique_regional_titles['Unknown']) > 1:
        print('+  Titles without regions included (might not be English): ' + str('{:,}'.format(unknown_region_title_count)))

    dupe_count = original_title_count - new_title_count -alt_count -apps_count - demos_count - edu_count - multi_count - protos_count
    if dupe_count < 0: dupe_count = 0

    english_status = ''
    if user_input.english_only == True:
        english_status = ' (English)'
        print('-  Dupes and non-English titles removed: ' + str('{:,}'.format(dupe_count)))
    else:
        print('-  Dupes removed: ' + str('{:,}'.format(dupe_count)))

    print(font.bold + '---------------------------')
    print('=  New title count: ' + str('{:,}'.format(new_title_count)) + font.end + '\n')

    # Set up final output file name and dat header strings
    if user_input.file_output != '':
        output_folder = user_input.file_output
        user_input.file_output_final = os.path.join(output_folder, dat_name)
    else:
        user_input.file_output_final = dat_name

    dat_version_filename = ''
    if dat_version != '': dat_version_filename = ' (' + dat_version + ')'

    if user_input.no_apps == True or user_input.no_demos == True or user_input.no_edu == True or user_input.no_multi == True or user_input.no_protos == True or user_input.no_alts == True or user_input.split_regions == True or user_input.split_regions_no_dupes == True:
        dat_header_exclusion = ' (-'
        if user_input.no_apps == True: dat_header_exclusion += 'a'
        if user_input.no_demos == True: dat_header_exclusion += 'd'
        if user_input.no_edu == True: dat_header_exclusion += 'e'
        if user_input.no_alts == True: dat_header_exclusion += 'l'
        if user_input.no_multi == True: dat_header_exclusion += 'm'
        if user_input.no_protos == True: dat_header_exclusion += 'p'
        if user_input.split_regions_no_dupes == True: dat_header_exclusion += 'r'
        if user_input.split_regions == True: dat_header_exclusion += 's'
        dat_header_exclusion += ')'
    else:
        dat_header_exclusion = ''

    # Write the dat files
    try:
        file_name_title_count = {}
        if user_input.split_regions_no_dupes == True or user_input.split_regions == True:
            print('* Writing regional dat files...\n')
            for region in region_list_english + region_list_other:
                if final_title_xml.get(region, -1) != -1 and new_title_count_region[region] > 0:
                    with open(user_input.file_output_final + ' (' + region + ')' + english_status + dat_header_exclusion + ' (' + str('{:,}'.format(new_title_count_region[region])) + ' of ' + str('{:,}'.format(new_title_count)) + ')' + dat_version_filename + ' (Retool ' +  datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3] + ')' + '.dat', 'w') as output_file:
                        dat_header = header(dat_name, dat_version, dat_author, dat_url, dat_header_exclusion, new_title_count_region[region], new_title_count, region, user_input)
                        output_file.writelines(dat_header)
                        output_file.writelines(final_title_xml[region])
                        output_file.writelines('</datafile>')
                        output_file.close()

            if final_title_xml.get('Unknown', -1) != -1:
                with open(user_input.file_output_final + ' (Unknown)' + english_status + dat_header_exclusion + ' (' + str('{:,}'.format(unknown_region_title_count)) + ' of ' + str('{:,}'.format(new_title_count)) + ')' + dat_version_filename + ' (Retool ' +  datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3] + ')' + '.dat', 'w') as output_file:
                    dat_header = header(dat_name, dat_version, dat_author, dat_url, dat_header_exclusion, unknown_region_title_count, new_title_count, 'Unknown', user_input)
                    output_file.writelines(dat_header)
                    output_file.writelines(final_title_xml['Unknown'])
                    output_file.writelines('</datafile>')
                    output_file.close()
        else:
            print('* Writing dat file...\n')
            with open(user_input.file_output_final + english_status + dat_header_exclusion + ' (' + str('{:,}'.format(new_title_count)) + ')' + dat_version_filename + ' (Retool ' +  datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3] + ')' + '.dat', 'w') as output_file:
                dat_header = header(dat_name, dat_version, dat_author, dat_url, dat_header_exclusion, False, new_title_count, False, user_input)
                output_file.writelines(dat_header)
                output_file.writelines(final_title_xml)
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