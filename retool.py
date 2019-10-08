# Strips Redump dats to only have English titles, preferencing US titles.
# Also removes titles from other regions that have different names, but
# the same content.
#
# Dependencies:
# * bs4
# * lxml

import os
import sys
import re # For regular expressions
from xml.dom import minidom # For prettier XML than BeautifulSoup can create
from bs4 import BeautifulSoup, Doctype # For XML parsing
import datetime
from time import strftime
import importlib # For bringing in renamed lists
import _regional_renames # Duplicate image titles that have different names in different regions

version_number = '0.2'

def main():
    # Initial splash screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(font.red + '______   _____ _____ _____ _' +
        '\n| ___ \ |_   _|  _  |  _  | |' +
        '\n| |_/ /___| | | | | | | | | |' +
        '\n|    // _ \ | | | | | | | | |' +
        '\n| |\ \  __/ | \ \_/ | \_/ / |____' +
        '\n\_| \_\___\_/  \___/ \___/\_____/ '+ font.end + 'v' + version_number)
    print('=======================================\n')
    if len(sys.argv) == 1:
        print('Strips Redump (' + font.underline + 'http://redump.org/' + font.end + ') dats to only include English titles from\nall regions, with no dupes. US titles are preferenced. This is not an\nofficial Redump project.')

    # Check user input
    user_input = check_input()

    input_file_name = user_input[0]
    output_file_name = user_input[1]
    flag_no_demos = user_input[2]
    flag_no_apps = user_input[3]
    flag_no_protos = user_input[4]
    flag_no_multi = user_input[5]
    flag_no_edu = user_input[6]
    flag_regions_all = user_input[7]
    flag_regions_en = user_input[8]

    # Check if the output file already exists
    if os.path.isfile(output_file_name) == True:
        overwrite_file = ''
        while overwrite_file != 'y' and overwrite_file != 'n':
            overwrite_file = input('The file ' + font.bold + output_file_name + font.end + ' already exists. Do you want to overwrite it? [y/n] > ').lower()

        if overwrite_file == 'n':
            print('\nExiting Retool')
            sys.exit()
        elif overwrite_file == 'y':
            print('\nOverwriting ' + font.bold + output_file_name + font.end)

    # Regions where English is a primary language
    region_list_english = [
        'USA',
        'World',
        'UK',
        'Canada',
        'Australia',
        'Brazil' # Classic console games were in English. Modern titles might only be in Portugese these days. Keep an eye out.
    ]

    # Regions where titles may have an English version
    region_list_other = [
        'Europe',
        'Asia',
        'Scandinavia',
        'Japan',
        'Austria',
        'Belgium',
        'China',
        'Croatia',
        'Denmark',
        'Finland',
        'France',
        'Greece',
        'India',
        'Italy',
        'Korea',
        'Netherlands',
        'Norway',
        'Poland',
        'Portugal',
        'Russia',
        'South Africa',
        'Spain',
        'Sweden',
        'Switzerland'
    ]

    # Read in the dat file
    print('* Reading dat file: "' + font.bold + input_file_name + font.end + '"')
    with open(input_file_name, 'r') as input_file_read:
        print('* Validating dat file... ', sep=' ', end='', flush=True)
        checkdat = input_file_read.read()
        input_file_read.seek(0)

        # Make sure the dat file isn't a CLRMAMEPro dat, if it is, check it's valid and convert it
        clrmame_header = re.findall('^clrmamepro \($.*?^\)$', checkdat, re.M|re.S)
        if clrmame_header:
            print('file is a CLRMAMEPro dat file.')
            converted_dat = convert_clr_logiqx(clrmame_header, checkdat)
            xml_convert = converted_dat[0]
            dat_name = converted_dat[1]
            dat_description = converted_dat[2]
            dat_author = converted_dat[3]
            dat_url = 'Unknown'
            dat_version = 'Unknown'
            soup = BeautifulSoup(xml_convert, "lxml-xml")
        else:
            soup = BeautifulSoup(input_file_read, "lxml-xml")
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
                            sys.exit()
                    else:
                        print(font.red + '\n* "' + input_file_name + '" isn\'t a CLRMAMEPro dat file.' + font.end)
                        sys.exit()

        print('\n|  Description: ' + dat_description)
        print('|  Author: ' + dat_author)
        print('|  URL: ' + dat_url)
        print('|  Version: ' + dat_version + '\n')

        # Find out how many titles are in the dat file
        original_title_count = len(soup.find_all('game'))

    # Store regions in an object
    titles = {}
    unique_regional_titles = {}

    # First populate the regions that are natively in English
    for region in region_list_english:
        titles[region] = localized_titles(region, True, soup)

    # Now those that may have English versions
    for region in region_list_other:
        titles[region] = localized_titles(region, flag_regions_all, soup)

    sys.stdout.write("\033[K")
    print('* Checking dat for regions... done.')

    # Variable that holds each title's XML. Titles get added one by one to be written to file later.
    final_title_xml=''

    # Create a list to store unique titles
    unique_list = []

    if titles['USA'] == []:
        print('* No USA titles found...')
    else:
        print('* Adding titles from USA...', sep='', end='', flush=True)

        # Sort USA titles
        usa_titles = []
        for title in titles['USA']:
            usa_titles.append(str(title.category.parent['name']))
        usa_titles = sorted(usa_titles, key=str.lower)

        # Add USA titles to unique_list
        for title in usa_titles:
            unique_list.append(title[:title.index('(USA') - 1])

        # Dedupe unique_list
        unique_regional_titles['USA'] = []

        for i, x in enumerate(unique_list):
            if unique_list[i] != unique_list[i-1]:
                unique_regional_titles['USA'].append(x)
        unique_list = unique_regional_titles['USA']

        # Add the USA titles XML
        for node in titles['USA']:
            final_title_xml += filter_flags(node, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_multi, flag_no_edu)

        print(' done.')

    # Start work on the other regions
    print('* Looking for English non-dupes in other regions...')

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

    # Find unique titles in each region
    for i, locale in enumerate(region_list_english):
        if i > 0:
            unique_regional_titles[locale] = localized_titles_unique(locale, titles[locale], unique_list, dupe_list)

            if unique_regional_titles[locale] != []:
                print('  - Adding unique titles from ' + locale + '...', sep='', end='\r', flush=True)
                for title in unique_regional_titles[locale]:
                    unique_list.append(title)

                 # Add titles to XML
                final_title_xml = convert_to_xml(locale, unique_regional_titles, titles, final_title_xml, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_multi, flag_no_edu)
                sys.stdout.write("\033[K")
                print('  - Adding unique titles from ' + locale + '... done.')

    for i, locale in enumerate(region_list_other):
            unique_regional_titles[locale] = localized_titles_unique(locale, titles[locale], unique_list, dupe_list)

            if unique_regional_titles[locale] != []:
                print('  - Adding unique titles from ' + locale + '...', sep='', end='\r', flush=True)
                for title in unique_regional_titles[locale]:
                    unique_list.append(title)

                 # Add titles to XML
                final_title_xml = convert_to_xml(locale, unique_regional_titles, titles, final_title_xml, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_multi, flag_no_edu)
                sys.stdout.write("\033[K")
                print('  - Adding unique titles from ' + locale + '... done.')

    # Stats so people can see something was done
    new_title_count = final_title_xml.count('<game name=')

    if new_title_count == 0:
        print(font.yellow + '\n* No English titles found, no dat file created.' + font.end)
        sys.exit()

    print('\n|  Original title count: ' + str('{:,}'.format(original_title_count)) + '\n|  Dupes and non-English titles: ' + str('{:,}'.format(original_title_count - new_title_count)) + '\n|  New title count: ' + str('{:,}'.format(new_title_count)))

    # Write the dat file
    with open(output_file_name, 'w') as output_file:
        dat_header = header(dat_name, dat_version, dat_author, dat_url, new_title_count, False, False, False)
        output_file.writelines(dat_header)
        output_file.writelines(final_title_xml)
        output_file.writelines('</datafile>')
        output_file.close()

    print(font.green + '\n* Finished writing unique English titles to "' +  font.bold + output_file_name + font.end + font.green + '".' + font.end)
    return
###############################################################################

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
    print('\nUSAGE:\n' + font.bold + ' python ' + os.path.basename(__file__) + ' -i input.dat -o output.dat <options>' + font.end)
    print('\nOPTIONS:\n' + font.bold + ' -a' + font.end + '   Remove applications')
    print(font.bold + ' -d' + font.end + '   Remove demos and coverdiscs')
    print(font.bold + ' -e' + font.end + '   Remove educational')
    print(font.bold + ' -m' + font.end + '   Remove multimedia')
    print(font.bold + ' -p' + font.end + '   Remove betas and prototypes')
    print(font.bold + ' -ra' + font.end + '  Split into regions, all languages (not checked for dupes)')
    print(font.bold + ' -re' + font.end + '  Split into regions, English only (not checked for dupes)')
    sys.exit()

# Check user input
def check_input():
    error_state = False

    # If no flags provided, or if -i or -o are missing
    if len(sys.argv) == 1:
        error_instruction()

    if len([x for x in sys.argv if '-i' in x]) == 0 or len([x for x in sys.argv if '-o' in x]) == 0:

        if len([x for x in sys.argv if '-i' in x]) == 0:
            print(font.red + '* Missing -i, no input file specified' + font.end)

        if len([x for x in sys.argv if '-o' in x]) == 0:
            print(font.red + '* Missing -o, no output file specified' + font.end)

        error_state = True

    # Handle input, output, and invalid flags
    excess_i = False
    excess_o = False

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
                input_file_name = sys.argv[i+1]

                if not os.path.exists(input_file_name):
                    print(font.red + '* Input file "' + font.bold + input_file_name + font.end + font.red + '" does not exist.' + font.end)
                    error_state = True

                if not input_file_name.endswith('.dat'):
                    print(font.red + '* Input file must have a .dat extension' + font.end)
                    error_state = True

            if len([x for x in sys.argv if '-i' in x]) > 1:
                excess_i = True
                error_state = True

        if x == '-o':
            if i+1 == len(sys.argv) or bool(re.search('-([ioademp]|re|ra])', sys.argv[i+1])):
                print(font.red + '* No output file specified' + font.end)
                error_state = True
            else:
                output_file_name = sys.argv[i+1]

                if not output_file_name.endswith('.dat'):
                    output_file_name += '.dat'

            if len([x for x in sys.argv if '-o' in x]) > 1:
                excess_o = True
                error_state = True

    if excess_i == True: print(font.red + '* Can\'t have more than one -i' + font.end)
    if excess_o == True: print(font.red + '* Can\'t have more than one -o' + font.end)

    # Handle optional flags
    flag_no_apps = True if len([x for x in sys.argv if '-a' in x]) >= 1 else False
    flag_no_demos = True if len([x for x in sys.argv if '-d' in x]) >= 1 else False
    flag_no_edu = True if len([x for x in sys.argv if '-e' in x]) >= 1 else False
    flag_no_multi = True if len([x for x in sys.argv if '-m' in x]) >= 1 else False
    flag_no_protos = True if len([x for x in sys.argv if '-p' in x]) >= 1 else False

    if len([x for x in sys.argv if '-ra' in x]) > 0 and len([x for x in sys.argv if '-re' in x]) > 0:
        print(font.red + '* The -ra and -re options can\'t be combined' + font.end)
        error_state = True
    else:
        flag_regions_en = True if len([x for x in sys.argv if '-re' in x]) == 1 else False
        flag_regions_all = True if len([x for x in sys.argv if '-ra' in x]) == 1 else False

    # Exit if there was an error in user input
    if error_state == True:
        error_instruction()

    return input_file_name, output_file_name, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_multi, flag_no_edu, flag_regions_all, flag_regions_en

# Converts CLRMAMEPro format to XML
def convert_clr_logiqx(clrmame_header, checkdat):
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
                    node = re.sub('^rom \( name ', '<rom name="', node.strip())
                    node = re.sub(' size ', '" size="', node.strip())
                    node = re.sub(' crc ', '" crc="', node.strip())
                    node = re.sub(' md5 ', '" md5="', node.strip())
                    node = re.sub(' sha1 ', '" sha1="', node.strip())
                    node = re.sub(' md5 ', '" md5="', node.strip())
                    node = re.sub(' \)$', '">', node.strip())
                    xml_convert += '\t\t' + node + '\n'
            xml_convert += '\t</game>\n'
        xml_convert += '</datafile>'
    else:
        print(font.red + 'file isn\'t Logiqx XML or CLRMAMEPro dat.' + font.end)
        sys.exit()
    return xml_convert, dat_name, dat_description, dat_author

# Creates a header for dat files
def header(dat_name, dat_version, dat_author, dat_url, new_title_count, locale, flag_regions_all, flag_regions_en):
    if new_title_count == False:
        new_title_count = ' '
    else:
        new_title_count = ' (' + str(new_title_count) + ') '

    if flag_regions_en == True:
        description = '\n\t\t<description>' + dat_name  + new_title_count + '(' + dat_version + ') (' + locale + ') (English)</description>'
    elif flag_regions_all == True:
        description = '\n\t\t<description>' + dat_name  + new_title_count + '(' + dat_version + ') (' + locale + ')</description>'
    else:
        description = '\n\t\t<description>' + dat_name  + new_title_count + '(' + dat_version + ') (English)</description>'

    header = ['<?xml version="1.0"?>',
        '\n<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">',
        '\n<datafile>',
        '\n\t<header>',
        '\n\t\t<name>' + dat_name + '</name>',
        description,
        '\n\t\t<version>' + dat_version + '</version>',
        '\n\t\t<date>' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '</date>',
        '\n\t\t<author>' + dat_author + ' & NI+ROE</author>',
        '\n\t\t<homepage>redump.org</homepage>',
        '\n\t\t<url>' + dat_url + '</url>',
        '\n\t</header>\n']
    return header

# Splits dat into regions
def localized_titles(locale, native, soup):
    sys.stdout.write("\033[K")
    print('* Checking dat for regions... ' + locale, sep='', end='\r', flush=True)
    if native == True:
        return soup.find_all('game', {'name':re.compile('(\(' + locale + '\))')}) + soup.find_all('game', {'name':re.compile('(\(' + locale + ',.*?\))')})
    else:
        if locale == 'Europe':
            # Grab all European games that don't have languages listed, as well as those that specify English
            return soup.find_all('game', {'name':re.compile('^(?!.*(\(.*?(En|Ar|At|Be|Ch|Da|De|Es|Fi|Fr|Gr|Hr|It|Ja|Ko|Nl|No|Pl|Pt|Ru|Sv)(,|\)))).*(\(.*?' + locale + '.*?\))')}) + soup.find_all('game', {'name':re.compile('(\(.*' + locale + '.*?\) \(En,)')})
        else:
            return soup.find_all('game', {'name':re.compile('(\(.*' + locale + '.*?\) \(.*?En(,|\)))')})

# Finds unique titles in regions
def localized_titles_unique (locale, titles, unique_list, dupe_list):
    regional_titles = []
    # Extract each title name
    for title in titles:
        locale_start = [m.span()[0] for m in re.finditer('(\(.*' + locale + '.*\))', title.category.parent['name'])][0]
        locale_end = [m.span()[1] for m in re.finditer('(\(.*' + locale + '.*\))', title.category.parent['name'])][0]
        regional_titles.append(title.category.parent['name'][:locale_end - (locale_end - locale_start + 1)])

    # Find the uniques
    unique_regional_list = [x for x in regional_titles if x not in unique_list and x not in dupe_list]

    # Sort and dedupe unique_regional_list
    if len(unique_regional_list) > 1:
        unique_regional_list = sorted(unique_regional_list, key=str.lower)
        unique_regional_temp = []
        for i, x in enumerate(unique_regional_list):
            if  unique_regional_list[i] != unique_regional_list[i-1]:
                unique_regional_temp.append(unique_regional_list[i])
        unique_regional_list = unique_regional_temp

    return unique_regional_list

# Uses a title to match to its original XML node
def convert_to_xml(locale, unique_regional_titles, titles, final_title_xml, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_multi, flag_no_edu):
    if unique_regional_titles[locale] != []:
            progress = 0
            progress_total = len(unique_regional_titles[locale])

            for title in unique_regional_titles[locale]:
                for node in titles[locale]:
                    if bool(re.search('(^' + title + ' \()', node.category.parent['name'])):
                        final_title_xml += filter_flags(node, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_multi, flag_no_edu)
                progress += 1
                progress_percent = progress/progress_total*100
                sys.stdout.write("\033[K")
                print('  - Adding unique titles from ' + locale + '... ' + str(int(progress_percent)) + '%', sep='', end='\r', flush=True)
    return final_title_xml

# Selects what titles to output based on user selected flags
def filter_flags(node, flag_no_demos, flag_no_apps, flag_no_protos, flag_no_multi, flag_no_edu):
    formatted_node =''
    if (flag_no_demos == True) and (flag_no_apps == False) and (flag_no_protos == False) and (flag_no_multi == False) and (flag_no_edu == False):
        if str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == False) and (flag_no_protos == False) and (flag_no_multi == False) and (flag_no_edu == True):
        if str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == False) and (flag_no_protos == False) and (flag_no_multi == True) and (flag_no_edu == False):
        if str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == False) and (flag_no_protos == False) and (flag_no_multi == True) and (flag_no_edu == True):
        if str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == True) and (flag_no_protos == False) and (flag_no_multi == False) and (flag_no_edu == False):
        if str(node.category) != '<category>Applications</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == True) and (flag_no_protos == False) and (flag_no_multi == False) and (flag_no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == True) and (flag_no_protos == False) and (flag_no_multi == True) and (flag_no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Multimedia</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == True) and (flag_no_protos == False) and (flag_no_multi == True) and (flag_no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == False) and (flag_no_protos == True) and (flag_no_multi == False) and (flag_no_edu == False):
        if str(node.category) != '<category>Preproduction</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == False) and (flag_no_protos == True) and (flag_no_multi == False) and (flag_no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == False) and (flag_no_protos == True) and (flag_no_multi == True) and (flag_no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Multimedia</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == False) and (flag_no_protos == True) and (flag_no_multi == True) and (flag_no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == True) and (flag_no_protos == True) and (flag_no_multi == False) and (flag_no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Applications</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == True) and (flag_no_protos == True) and (flag_no_multi == False) and (flag_no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == True) and (flag_no_protos == True) and (flag_no_multi == True) and (flag_no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Multimedia</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == False) and (flag_no_apps == True) and (flag_no_protos == True) and (flag_no_multi == True) and (flag_no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == True) and (flag_no_protos == False) and (flag_no_multi == False) and (flag_no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == True) and (flag_no_protos == False) and (flag_no_multi == False) and (flag_no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == True) and (flag_no_protos == False) and (flag_no_multi == True) and (flag_no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == True) and (flag_no_protos == False) and (flag_no_multi == True) and (flag_no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == False) and (flag_no_protos == True) and (flag_no_multi == False) and (flag_no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == False) and (flag_no_protos == True) and (flag_no_multi == False) and (flag_no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == False) and (flag_no_protos == True) and (flag_no_multi == True) and (flag_no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == False) and (flag_no_protos == True) and (flag_no_multi == True) and (flag_no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == True) and (flag_no_protos == True) and (flag_no_multi == False) and (flag_no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Preproduction</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == True) and (flag_no_protos == True) and (flag_no_multi == False) and (flag_no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == True) and (flag_no_protos == True) and (flag_no_multi == True) and (flag_no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Multimedia</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    elif (flag_no_demos == True) and (flag_no_apps == True) and (flag_no_protos == True) and (flag_no_multi == True) and (flag_no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            formatted_node = minidom_prettify(str(node.category.parent))
    else:
        formatted_node = minidom_prettify(str(node.category.parent))
    return formatted_node

# Use minidom to prettify XML for each node, because it can define indents and we need tabs
def minidom_prettify(string):
    doc = minidom.parseString(string)
    doc = doc.toprettyxml(newl='', encoding=None)[22:] + '\n'
    doc = doc.splitlines()

    formatted_node=''

    for line in doc:
        formatted_node += '\t' + line.rstrip() + '\n'
    return formatted_node

if __name__ == '__main__':
    main()