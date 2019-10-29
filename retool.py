# Strips Redump dats to only include English titles, preferencing US titles.
# Also removes titles from other regions that have different names, but
# the same content.
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
from bs4 import BeautifulSoup, Doctype # For XML parsing
import _regional_renames # Duplicate image titles that have different names in different regions

version_number = '0.34'

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
        print(textwrap.fill('Strips Redump (' + font.underline + 'http://redump.org/' + font.end + ') dats to only include English titles, with no dupes. US titles are preferenced. This is not an official Redump project.', 80))

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
        'Brazil', # Classic console games were in English. Modern titles might only be in Portugese these days. Keep an eye out.
        'Latin America', # Generally Spanish, but seems to include English versions
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
        output_folder = user_input.file_output
        file_count = 0

        for file in os.listdir(input_folder):
            if file.endswith('.dat'):
                file_count += 1
                user_input.file_input = os.path.join(input_folder, file)
                user_input.file_output = os.path.join(output_folder, file[:-4] + ' (Retool ' +  datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3] + ')')
                process_dats(user_input, region_list_english, region_list_other, True)

        stop = time.time()

        if file_count == 1:
            file_plural_singular = 'file'
        else:
            file_plural_singular = 'files'

        if file_count != 0:
            if output_folder == '.': output_folder = os.getcwd()

            if user_input.regions_en == True:
                print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished processing ' + str('{:,}'.format(file_count)) + ' ' + file_plural_singular + ' in the "' + font.bold + input_folder + font.end + font.green + '" folder in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's. Unique English titles have been added to regional dats in the "' + font.bold + output_folder + font.end + font.green + '" folder.' + font.end) + '\n')
            elif user_input.regions_all == True:
                print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished processing ' + str('{:,}'.format(file_count)) + ' ' + file_plural_singular + ' in the "' + font.bold + input_folder + font.end + font.green + '" folder in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's. All dats have been split into regions in the "' + font.bold + output_folder + font.end + font.green + '" folder.' + font.end) + '\n')
            else:
                print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished processing ' + str('{:,}'.format(file_count)) + ' ' + file_plural_singular + ' in the "' + font.bold + input_folder + font.end + font.green + '" folder in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's. Unique English titles have been added to dats in the "' + font.bold + output_folder + font.end + font.green + '" folder.' + font.end) + '\n')
        else:
            print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.yellow + '* No files found to process in the "' + font.bold + input_folder + font.end + font.yellow + '" folder.' + font.end) + '\n')

        sys.exit()
    else:
        new_title_count = process_dats(user_input, region_list_english, region_list_other, False)

        stop = time.time()

        if user_input.regions_en == True:
            print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished adding unique English titles to regional dats in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's.' + font.end) + '\n')
        elif user_input.regions_all == True:
            print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished splitting "' + font.bold + user_input.file_input + font.end + font.green + '" into regional dats in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's.' + font.end) + '\n')
        else:
            print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.green + '* Finished adding ' + str('{:,}'.format(new_title_count)) + ' unique English titles to "' +  font.bold + user_input.file_output + '.dat' + font.end + font.green + '" in ' + str('{0:.2f}'.format(round(stop - start,2))) + 's.' + font.end) + '\n')
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
def error_instruction():
    print('\nUSAGE:\n' + font.bold + ' python ' + os.path.basename(__file__) + ' -i ' + font.end + '<input dat/folder>' + font.bold + ' -o ' + font.end + '<output dat/folder> <options>\n')
    print(textwrap.TextWrapper(width=70, subsequent_indent='   ').fill('\n\n Input and output must both be files, or both be folders. Not setting a folder output writes to the current folder.'))
    print('\nOPTIONS:\n' + font.bold + ' -a' + font.end + '   Remove applications')
    print(font.bold + ' -d' + font.end + '   Remove demos and coverdiscs')
    print(font.bold + ' -e' + font.end + '   Remove educational')
    print(font.bold + ' -m' + font.end + '   Remove multimedia')
    print(font.bold + ' -p' + font.end + '   Remove betas and prototypes')
    print(font.bold + ' -ra' + font.end + '  Split into regions, all languages (dupes are included)')
    print(font.bold + ' -re' + font.end + '  Split into regions, English only\n')
    sys.exit()

# Check user input
def check_input(region_list_english, region_list_other):
    error_state = False

    # Handle optional flags
    flag_no_apps = True if len([x for x in sys.argv if x == '-a']) >= 1 else False
    flag_no_demos = True if len([x for x in sys.argv if x == '-d']) >= 1 else False
    flag_no_edu = True if len([x for x in sys.argv if x == '-e']) >= 1 else False
    flag_no_multi = True if len([x for x in sys.argv if x == '-m']) >= 1 else False
    flag_no_protos = True if len([x for x in sys.argv if x == '-p']) >= 1 else False

    if len([x for x in sys.argv if '-ra' in x]) > 0 and len([x for x in sys.argv if '-re' in x]) > 0:
        print(font.red + '* The -ra and -re options can\'t be combined' + font.end)
        error_state = True
    else:
        flag_regions_en = True if len([x for x in sys.argv if x == '-re']) >= 1 else False
        flag_regions_all = True if len([x for x in sys.argv if x == '-ra']) >= 1 else False

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
            if not ((x == '-i') or (x == '-o') or (x == '-a') or (x == '-d') or (x == '-e') or (x == '-m') or (x == '-p') or (x == '-ra') or (x == '-re')):
                print(font.red + '* Invalid option ' + sys.argv[i] + font.end)
                error_state = True
        if x == '-i':
            if i+1 == len(sys.argv) or bool(re.search('-([ioademp]|re|ra])', sys.argv[i+1])):
                print(font.red + '* No input file specified' + font.end)
                error_state = True
            else:
                input_file_name = os.path.abspath(sys.argv[i+1].rstrip(os.sep))

                if not os.path.exists(input_file_name):
                    print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(font.red + '* Input file "' + font.bold + input_file_name + font.end + font.red + '" does not exist.' + font.end))
                    error_state = True

                if os.path.isdir(input_file_name):
                    i_is_folder = True

            if len([x for x in sys.argv if '-i' in x]) > 1:
                excess_i = True
                error_state = True

        if x == '-o':
                if i+1 == len(sys.argv) or bool(re.search('-([ioademp]|re|ra])', sys.argv[i+1])):
                    print(font.red + '* No output file specified' + font.end)
                    error_state = True
                else:
                    output_file_name = os.path.abspath(sys.argv[i+1].rstrip(os.sep))

                    # Check that both input/output are files, or that both are folders
                    if os.path.isdir(output_file_name) == False and i_is_folder == True:
                        print(font.red + '* Input is a folder, output must be set to an existing folder' + font.end)
                        sys.exit()
                    elif  os.path.isdir(output_file_name) == True and i_is_folder == False:
                        print(font.red + '* Input is a file, output must be set to a file' + font.end)
                        sys.exit()
                    else:
                        # Strip .dat from the end of the output file if it exists
                        if output_file_name.endswith('.dat'):
                            output_file_name = output_file_name[:-4]

        if len([x for x in sys.argv if '-o' in x]) > 1:
                excess_o = True
                error_state = True

    if len([x for x in sys.argv if '-o' in x]) == 0 and i_is_folder == False:
        print(font.red + '* Missing -o, no output file specified' + font.end)

        error_state = True

    if len([x for x in sys.argv if '-o' in x]) == 0 and i_is_folder == True:
        output_file_name = '.'

    if excess_i == True: print(font.red + '* Can\'t have more than one -i' + font.end)
    if excess_o == True: print(font.red + '* Can\'t have more than one -o' + font.end)

    # Exit if there was an error in user input
    if error_state == True:
        error_instruction()

    # Check if the user defined output file already exists
    overwrite_file = False


    if flag_regions_en == True or flag_regions_all == True:
        region_output_files = False
        for region in region_list_english + region_list_other:
            if os.path.isfile(output_file_name + ' (' + region + ').dat') == True:
                region_output_files += 1
        if region_output_files != False:
            while overwrite_file != 'y' and overwrite_file != 'n' and overwrite_file != '':
                if region_output_files > 1:
                    overwrite_file = input(textwrap.fill('There are ' + str(region_output_files) + ' dat files that already exist in the "' + font.bold + os.path.dirname(output_file_name) + font.end + '" folder with the format "' + font.bold + os.path.basename(output_file_name) + ' (<region name>).dat"' + font.end + '. Continuing might overwrite some or all of them.', 80) + '\n\nDo you want to continue? [y/N] > ').lower()
                else:
                    overwrite_file = input(textwrap.fill('A dat file with the format "' + font.bold + os.path.basename(output_file_name) + ' (<region name>).dat"' + font.end + ' already exists in the ' + font.bold + os.path.dirname(output_file_name) + font.end + ' folder. Continuing might overwrite this file.', 80) + '\n\nDo you want to continue? [y/N] > ').lower()

            if overwrite_file == 'n' or overwrite_file == '':
                print('\nExiting Retool...\n')
                sys.exit()
            elif overwrite_file == 'y':
                print()
    else:
        if os.path.isfile(output_file_name) == True or os.path.isfile(output_file_name + '.dat') == True:
            while overwrite_file != 'y' and overwrite_file != 'n' and overwrite_file != '':
                overwrite_file = input(textwrap.fill('The file ' + font.bold + output_file_name + '.dat' + font.end + ' already exists.', 80) + '\n\nDo you want to overwrite it? [y/N] > ').lower()

            if overwrite_file == 'n' or overwrite_file == '':
                print('\nExiting Retool...\n')
                sys.exit()
            elif overwrite_file == 'y':
                print('\n* Overwriting ' + font.bold + output_file_name + '.dat' + font.end)

    return UserInput(input_file_name, output_file_name, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_multi, flag_no_edu, flag_regions_all, flag_regions_en)

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
def header(dat_name, dat_version, dat_author, dat_url, new_title_count, region, user_input):
    if new_title_count == False:
        new_title_count = ' '
    else:
        new_title_count = ' (' + str('{:,}'.format(new_title_count)) + ') '

    if user_input.no_apps == True or user_input.no_demos == True or user_input.no_edu == True or user_input.no_multi == True or user_input.no_protos == True:
        dat_header_exclusion = ' (-'
        if user_input.no_apps == True: dat_header_exclusion += 'a'
        if user_input.no_demos == True: dat_header_exclusion += 'd'
        if user_input.no_edu == True: dat_header_exclusion += 'e'
        if user_input.no_multi == True: dat_header_exclusion += 'm'
        if user_input.no_protos == True: dat_header_exclusion += 'p'
        dat_header_exclusion += ')'
    else:
        dat_header_exclusion = ''

    if user_input.regions_en == True:
        name = '\n\t\t<name>' + dat_name  + new_title_count + '(' + dat_version + ') (' + region + ') (English)' + dat_header_exclusion + '</name>'
        description = '\n\t\t<description>' + dat_name  + new_title_count + '(' + dat_version + ') (' + region + ') (English)' + dat_header_exclusion + '</description>'
    elif user_input.regions_all == True:
        name = '\n\t\t<name>' + dat_name  + new_title_count + '(' + dat_version + ') (' + region + ')' + dat_header_exclusion + '</name>'
        description = '\n\t\t<description>' + dat_name  + new_title_count + '(' + dat_version + ') (' + region + ')' + dat_header_exclusion + '</description>'
    else:
        name = '\n\t\t<name>' + dat_name  + new_title_count + '(' + dat_version + ') (English)' + dat_header_exclusion + '</name>'
        description = '\n\t\t<description>' + dat_name  + new_title_count + '(' + dat_version + ') (English)' + dat_header_exclusion + '</description>'

    header = ['<?xml version="1.0"?>',
        '\n<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">',
        '\n<datafile>',
        '\n\t<header>',
        '\n\t\t<name>' + name + '</name>',
        description,
        '\n\t\t<version>' + dat_version + '</version>',
        '\n\t\t<date>' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '</date>',
        '\n\t\t<author>' + dat_author + ' & Retool</author>',
        '\n\t\t<homepage>redump.org</homepage>',
        '\n\t\t<url>' + dat_url + '</url>',
        '\n\t</header>\n']
    return header

#Establish a class for user input
class UserInput:
    def __init__(self, file_input, file_output, no_demos, no_apps, no_protos, no_multi, no_edu, regions_all, regions_en):
        self.file_input = file_input
        self.file_output = file_output
        self.no_demos = no_demos
        self.no_apps = no_apps
        self.no_protos = no_protos
        self.no_multi = no_multi
        self.no_edu = no_edu
        self.regions_all = regions_all
        self.regions_en = regions_en

# Establish a class for title data
class DatNode:
    def __init__(self, full_title, category, description, roms):
        self.full_title = full_title
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
def localized_titles(region, native, soup):
    sys.stdout.write("\033[K")
    if native != 'Unknown':
        print('* Checking dat for regions... ' + region, sep='', end='\r', flush=True)
    if native == True:
        return soup.find_all('game', {'name':re.compile('(\(' + region + '\))')}) + soup.find_all('game', {'name':re.compile('(\(' + region + ',.*?\))')})
    elif native == 'Unknown':
        return soup.find_all('game', {'name':re.compile('^(?!.*(\(.*?(' + region + ').*?\))).*(.*)')})
    else:
        if region == 'Europe':
            # Grab all European games that don't have languages listed, as well as those that specify English
            return soup.find_all('game', {'name':re.compile('^(?!.*(\(.*?(En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)(,|\)))).*(\(.*?' + region + '.*?\))')}) + soup.find_all('game', {'name':re.compile('(\(.*' + region + '.*?\) \(En,)')})
        else:
            return soup.find_all('game', {'name':re.compile('(\(.*' + region + '.*?\) \(.*?En(,|\)))')})

# Adds titles in Logiqx XML dat form
def add_titles(region_list, titles, unique_list, dupe_list, user_input, unique_regional_titles):
    if user_input.regions_en == True or user_input.regions_all == True:
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
            if user_input.regions_en == True or user_input.regions_all == True:
                title_xml[region] = convert_to_xml(region, unique_regional_titles, titles, user_input)
            else:
                title_xml += convert_to_xml(region, unique_regional_titles, titles, user_input)

            sys.stdout.write("\033[K")
            print('  * Adding titles from ' + region + '... done.')
    return title_xml

# Finds unique titles in regions
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
        if user_input.no_demos == True and (title.category.contents[0] == 'Demos' or title.category.contents[0] == 'Coverdiscs'): continue
        if user_input.no_apps == True and (title.category.contents[0] == 'Applications'): continue
        if user_input.no_protos == True and (title.category.contents[0] == 'Preproduction'): continue
        if user_input.no_multi == True and (title.category.contents[0] == 'Multimedia'): continue
        if user_input.no_edu == True and (title.category.contents[0] == 'Educational'): continue

        # Build a dictionary so we don't have to go searching the XML again later
        roms = title.findChildren('rom', recursive=False)
        newroms = []
        for rom in roms:
                newroms.append(DatNodeRom('rom', rom['crc'], rom['md5'], rom['name'], rom['sha1'], rom['size']))

        # Check that there isn't multiple discs or revisions
        if regional_titles_data.get(raw_title, -1) != -1:
            regional_titles_data[raw_title].append(DatNode(str(title.category.parent['name']), title.category.contents[0], title.description.contents[0], newroms))
        else:
            regional_titles_data[raw_title] = [DatNode(str(title.category.parent['name']), title.category.contents[0], title.description.contents[0], newroms)]

    # Find the uniques
    if user_input.regions_all == False:
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
    else:
        unique_regional_list = [x for x in regional_titles]

    # Add unique list to the dictionary
    regional_titles_data['unique_titles'] = unique_regional_list

    return regional_titles_data

# Uses a title to create its original XML node
def convert_to_xml(region, unique_regional_titles, titles, user_input):
    final_title_xml = ''
    if unique_regional_titles[region] != []:
            progress = 0
            progress_total = len(unique_regional_titles[region])

            for title in unique_regional_titles[region]:
                if title != 'unique_titles':
                    for subtitle in unique_regional_titles[region][title]:
                        final_title_xml += '\t<game name="' + subtitle.full_title + '">'
                        final_title_xml += '\n\t\t<category>' + subtitle.category + '</category>'
                        final_title_xml += '\n\t\t<description>' + subtitle.description + '</description>'
                        for rom in subtitle.roms:
                            final_title_xml += '\n\t\t<rom crc="' + rom.crc + '" md5="' + rom.md5 + '" name="' + rom.name + '" sha1="' + rom.sha1 + '" size="' + rom.size + '"/>'
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
        dat_version = 'Unknown'
        soup = BeautifulSoup(xml_convert, "lxml-xml")
    else:
        soup = BeautifulSoup(checkdat, "lxml-xml")
        # Check for a valid Redump XML dat, then grab the dat details
        for item in soup.contents:
            if isinstance(item, Doctype):
                if item == 'datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd"':
                    print('file is a Logiqx dat file.')
                    if soup.find('author').string == 'redump.org':
                        dat_name = soup.find('name').string
                        dat_description = soup.find('description').string
                        dat_author = soup.find('author').string
                        dat_url = soup.find('url').string
                        dat_version = soup.find('version').string
                    else:
                        print(font.red + '\n* This dat file isn\t authored by Redump' + font.end)
                        if is_folder == False:
                            sys.exit()
                        else:
                            return
                else:
                    print(font.red + '\n* "' + user_input.file_input + '" isn\'t a CLRMAMEPro dat file.' + font.end)
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
        titles[region] = localized_titles(region, True, soup)

    # Now those that might have English versions
    for region in region_list_other:
        titles[region] = localized_titles(region, user_input.regions_all, soup)

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

    titles['Unknown'] = localized_titles(region_list, 'Unknown', soup)

    if titles['Unknown'] == []:
        print('none found.')
    else:
        print('done.')

    # Variable that holds each title's XML. Titles get added one by one to be written to a file later
    final_title_xml= ''

    # Create a list to store unique titles
    unique_list = []

    # Start work on the other regions
    if user_input.regions_all == True:
        print('* Splitting regions...')
    else:
        print('* Looking for English non-dupes...')

    # Set up dupe lists for titles that have the same content, but different names in different regions
    dupe_list = []

    if dat_name == 'Microsoft - Xbox': dupe_list = _regional_renames.xbox_rename_list()
    if dat_name == 'Microsoft - Xbox 360': dupe_list = _regional_renames.x360_rename_list()
    if dat_name == 'Microsoft - Xbox One': dupe_list = _regional_renames.xbone_rename_list()
    if dat_name == 'Nintendo - GameCube': dupe_list = _regional_renames.gamecube_rename_list()
    if dat_name == 'Nintendo - Wii': dupe_list = _regional_renames.wii_rename_list()
    if dat_name == 'Nintendo - Wii U': dupe_list = _regional_renames.wii_u_rename_list()
    if dat_name == 'Panasonic - 3DO Interactive Multiplayer': dupe_list = _regional_renames.threedo_rename_list()
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
        if user_input.regions_en == True or user_input.regions_all == True:
            final_title_xml['Unknown'] = convert_to_xml('Unknown', unique_regional_titles, titles, user_input)
        else:
            final_title_xml += convert_to_xml('Unknown', unique_regional_titles, titles, user_input)

        sys.stdout.write("\033[K")
        print('  * Adding titles without regions... done.')
    else:
        unknown_region_title_count = 0

    # Stats so people can see something was done
    new_title_count = 0

    if user_input.regions_en == True or user_input.regions_all == True:
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
    apps_count = 0
    demos_count = 0
    edu_count = 0
    multi_count = 0
    protos_count = 0

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

    dupe_count = original_title_count - new_title_count -apps_count - demos_count - edu_count - multi_count - protos_count
    if dupe_count < 0: dupe_count = 0

    print('-  Dupes and non-English titles removed: ' + str('{:,}'.format(dupe_count)))

    print(font.bold + '---------------------------')
    print('=  New title count: ' + str('{:,}'.format(new_title_count)) + font.end + '\n')

    try:
        if user_input.regions_en == True or user_input.regions_all == True:
            print('* Writing regional dat files...\n')
            for region in region_list_english + region_list_other:
                if final_title_xml.get(region, -1) != -1 and new_title_count_region[region] > 0:
                    with open(user_input.file_output + ' (' + region + ').dat', 'w') as output_file:
                        dat_header = header(dat_name, dat_version, dat_author, dat_url, new_title_count_region[region], region, user_input)
                        output_file.writelines(dat_header)
                        output_file.writelines(final_title_xml[region])
                        output_file.writelines('</datafile>')
                        output_file.close()

            if final_title_xml.get('Unknown', -1) != -1:
                with open(user_input.file_output + ' (Unknown).dat', 'w') as output_file:
                    dat_header = header(dat_name, dat_version, dat_author, dat_url, unknown_region_title_count, 'Unknown', user_input)
                    output_file.writelines(dat_header)
                    output_file.writelines(final_title_xml['Unknown'])
                    output_file.writelines('</datafile>')
                    output_file.close()
        else:
            print('* Writing dat file...\n')
            with open(user_input.file_output + '.dat', 'w') as output_file:
                dat_header = header(dat_name, dat_version, dat_author, dat_url, new_title_count, False, user_input)
                output_file.writelines(dat_header)
                output_file.writelines(final_title_xml)
                output_file.writelines('</datafile>')
                output_file.close()
        return new_title_count
    except OSError as e:
        print('\n' + font.bold + font.red + '* Error: ' + font.end + str(e) + '\n')
        raise

if __name__ == '__main__':
    main()