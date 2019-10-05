# Strips Redump dats to only have English titles, preferencing US titles.
#
# Dependencies:
# * lxml
# * bs4

import os
import sys
import re # For regular expressions
from xml.dom import minidom # For prettier XML than BeautifulSoup can create
from bs4 import BeautifulSoup, Doctype # For XML parsing
import datetime
from time import strftime
import importlib # For bringing in renamed lists
import _regional_renames # Duplicate image titles that have different names in different regions

version_number = '0.1'

# Set up some nice formatting
# https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
class font:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[37m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BLINK = '\033[5m'

# Generic error message
def error_instruction():
    print('\nUSAGE:\n' + font.BOLD + ' python ' + os.path.basename(__file__) + ' -i input.dat -o output.dat <options>' + font.END)
    print('\nOPTIONS:\n' + font.BOLD + ' -a' + font.END + '   Remove applications')
    print(font.BOLD + ' -d' + font.END + '   Remove demos and coverdiscs')
    print(font.BOLD + ' -e' + font.END + '   Remove educational')
    print(font.BOLD + ' -m' + font.END + '   Remove multimedia')
    print(font.BOLD + ' -p' + font.END + '   Remove betas and prototypes')
    print(font.BOLD + ' -ra' + font.END + '  Split into regions, all languages (not checked for dupes)')
    print(font.BOLD + ' -re' + font.END + '  Split into regions, English only (not checked for dupes)')
    sys.exit()
    return

# Check user input
def check_input():
    if len(sys.argv) == 1:
        error_instruction()

    if len([x for x in sys.argv if '-i' in x]) == 0:
        print(font.RED + '\nMissing -i argument, no input file specified.' + font.END)
        error_instruction()

    for i, x in enumerate(sys.argv):
        if x == '-i':
            if (len(sys.argv) == 2) or (sys.argv[i+1] == '-o') or (sys.argv[i+1] == '-d') or (sys.argv[i+1] == '-a') or (sys.argv[i+1] == '-p') or (sys.argv[i+1] == '-m') or (sys.argv[i+1] == '-e') or (sys.argv[i+1] == '-ra') or (sys.argv[i+1] == '-re'):
                print('\n' + font.RED + 'ERROR: No input file specified.' + font.END)
                error_instruction()

            input_file_name = sys.argv[i+1]

            if not os.path.exists(input_file_name):
                print('\n' + font.RED + 'ERROR: ' + input_file_name + ' does not exist.' + font.END)
                error_instruction()

            if not input_file_name.endswith('.dat'):
                print('\n' + font.RED + 'ERROR: Redump input file must have a .dat extension.' + font.END)
                error_instruction()

    if len([x for x in sys.argv if '-o' in x]) == 0:
        print(font.RED + '\nMissing -o argument, no output file specified.' + font.END)
        error_instruction()

    for i, x in enumerate(sys.argv):
        if x == '-o':
            if i+1 == len(sys.argv):
                print('\n' + font.RED + 'ERROR: No output file specified.' + font.END)
                error_instruction()
            else:
                output_file_name = sys.argv[i+1]
            if not output_file_name.endswith('.dat'):
                output_file_name = output_file_name + '.dat'

    for i, x in enumerate(sys.argv):
        if x.startswith('-'):
            if not ((x == '-a') or (x == '-d') or (x == '-i') or (x == '-o') or (x == '-p') or (x == '-m') or (x == '-e') or (x == '-ra') or (x == '-re')):
                print('\n' + font.RED + 'ERROR: Invalid option ' + sys.argv[i] + font.END)
                error_instruction()

    if len([x for x in sys.argv if '-d' in x]) > 0:
        no_demos = True
    else:
        no_demos = False

    if len([x for x in sys.argv if '-a' in x]) > 0:
        no_apps = True
    else:
        no_apps = False

    if len([x for x in sys.argv if '-p' in x]) > 0:
        no_protos = True
    else:
        no_protos = False

    if len([x for x in sys.argv if '-m' in x]) > 0:
        no_multi = True
    else:
        no_multi = False

    if len([x for x in sys.argv if '-e' in x]) > 0:
        no_edu = True
    else:
        no_edu = False

    if len([x for x in sys.argv if '-ra' in x]) > 0:
        if len([x for x in sys.argv if '-re' in x]) > 0:
            print('\n' + font.RED + 'ERROR: Can\'t combine -ra and -re options.' + font.END)
            error_instruction()
        else:
            regions = True
    else:
        regions = False

    if len([x for x in sys.argv if '-re' in x]) > 0:
        if len([x for x in sys.argv if '-ra' in x]) > 0:
            print('\n' + font.RED + 'ERROR: Can\'t combine -ra and -re options.' + font.END)
            error_instruction()
        else:
            regions_english = True
    else:
        regions_english = False

    return input_file_name, output_file_name, no_demos, no_apps, no_protos, no_multi, no_edu, regions, regions_english

def minidom_prettify(string, output_file):
    # Using minidom to prettify, because it can define indents and we need tabs
    doc = minidom.parseString(string)
    doc = doc.toprettyxml(newl='', encoding=None)[22:] + '\n'
    doc = doc.splitlines()

    for line in doc:
        output_file.write('\t' + line.rstrip() + '\n')
    return

def filter_flags(output_file, node, no_demos, no_apps, no_protos, no_multi, no_edu):
    if (no_demos == True) and (no_apps == False) and (no_protos == False) and (no_multi == False) and (no_edu == False):
        if str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == False) and (no_protos == False) and (no_multi == False) and (no_edu == True):
        if str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == False) and (no_protos == False) and (no_multi == True) and (no_edu == False):
        if str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == False) and (no_protos == False) and (no_multi == True) and (no_edu == True):
        if str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == True) and (no_protos == False) and (no_multi == False) and (no_edu == False):
        if str(node.category) != '<category>Applications</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == True) and (no_protos == False) and (no_multi == False) and (no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == True) and (no_protos == False) and (no_multi == True) and (no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Multimedia</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == True) and (no_protos == False) and (no_multi == True) and (no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == False) and (no_protos == True) and (no_multi == False) and (no_edu == False):
        if str(node.category) != '<category>Preproduction</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == False) and (no_protos == True) and (no_multi == False) and (no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == False) and (no_protos == True) and (no_multi == True) and (no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Multimedia</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == False) and (no_protos == True) and (no_multi == True) and (no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == True) and (no_protos == True) and (no_multi == False) and (no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Applications</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == True) and (no_protos == True) and (no_multi == False) and (no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == True) and (no_protos == True) and (no_multi == True) and (no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Multimedia</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == False) and (no_apps == True) and (no_protos == True) and (no_multi == True) and (no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == True) and (no_protos == False) and (no_multi == False) and (no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == True) and (no_protos == False) and (no_multi == False) and (no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == True) and (no_protos == False) and (no_multi == True) and (no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == True) and (no_protos == False) and (no_multi == True) and (no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == False) and (no_protos == True) and (no_multi == False) and (no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == False) and (no_protos == True) and (no_multi == False) and (no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == False) and (no_protos == True) and (no_multi == True) and (no_edu == False):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == False) and (no_protos == True) and (no_multi == True) and (no_edu == True):
        if str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == True) and (no_protos == True) and (no_multi == False) and (no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Preproduction</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == True) and (no_protos == True) and (no_multi == False) and (no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == True) and (no_protos == True) and (no_multi == True) and (no_edu == False):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Multimedia</category>':
            minidom_prettify(str(node.category.parent), output_file)
    elif (no_demos == True) and (no_apps == True) and (no_protos == True) and (no_multi == True) and (no_edu == True):
        if str(node.category) != '<category>Applications</category>' and str(node.category) != '<category>Demos</category>' and str(node.category) != '<category>Coverdiscs</category>' and str(node.category) != '<category>Preproduction</category>' and str(node.category) != '<category>Multimedia</category>' and str(node.category) != '<category>Educational</category>':
            minidom_prettify(str(node.category.parent), output_file)
    else:
        minidom_prettify(str(node.category.parent), output_file)
    return

def header(dat_name, dat_version, dat_author, dat_url, new_title_count, country, regions, regions_english):
    if new_title_count == False:
        new_title_count = ' '
    else:
        new_title_count = ' (' + str(new_title_count) + ') '

    if regions_english == True:
        description = '\n\t\t<description>' + dat_name  + new_title_count + '(' + dat_version + ') (' + country + ') (English)</description>'
    elif regions == True:
        description = '\n\t\t<description>' + dat_name  + new_title_count + '(' + dat_version + ') (' + country + ')</description>'
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

def filter_dat(input_file_name, output_file_name, no_demos, no_apps, no_protos, no_multi, no_edu, regions, regions_english):
    # Read in the dat file
    print('\n* Reading dat file: "' + font.BOLD + input_file_name + font.END + '"')
    with open(input_file_name, 'r') as input_file_read:
        soup = BeautifulSoup(input_file_read, "lxml-xml")
        print('* Validating dat file... ', sep=' ', end='', flush=True) # Continue printing to the same line

        for item in soup.contents:
            if isinstance(item, Doctype):
                if item == 'datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd"':
                    print('file is a CLRMAMEPro dat file.')
                    if soup.find('author').string == 'redump.org':
                        dat_name = soup.find('name').string
                        dat_description = soup.find('description').string
                        dat_author = soup.find('author').string
                        dat_url = soup.find('url').string
                        dat_version = soup.find('version').string

                        print('\n|  Description: ' + dat_description)
                        print('|  Author: ' + dat_author)
                        print('|  URL: ' + dat_url)
                        print('|  Version: ' + dat_version + '\n')

                        # Find out how many titles are in the dat file
                        original_title_count = len(soup.find_all('game'))

                        # Remove existing output file
                        if os.path.exists(output_file_name):
                            os.remove(output_file_name)

                        with open(output_file_name, 'a+') as output_file:
                            def localized_image_list(locale, native):
                                sys.stdout.write("\033[K")
                                print('* Splitting dat into regions... ' + locale, sep='', end='\r', flush=True)
                                if native == True:
                                    return soup.find_all('game', {'name':re.compile('(\(' + locale + '\))')}) + soup.find_all('game', {'name':re.compile('(\(' + locale + ',.*?\))')})
                                else:
                                    if locale == 'Europe':
                                        # Grab all European games that don't have languages listed, as well as those that specify English
                                        return soup.find_all('game', {'name':re.compile('^(?!.*(\(.*?(En|Fr|De|Es|It|Nl|Sv|No|Da|Fi|Pl|Ru)(,|\)))).*(\(.*?' + locale + '.*?\))')}) + soup.find_all('game', {'name':re.compile('(\(.*' + locale + '.*?\) \(En,)')})
                                    else:
                                        return soup.find_all('game', {'name':re.compile('(\(.*' + locale + '.*?\) \(.*?En(,|\)))')})

                            # First populate the regions that are natively in English
                            images = {}
                            images['usa'] = localized_image_list('USA', True)
                            images['world'] = localized_image_list('World', True)
                            images['uk'] = localized_image_list('UK', True)
                            images['ca'] = localized_image_list('Canada', True) # There's a chance this could be French Canadian. Keep an eye out.
                            images['au'] = localized_image_list('Australia', True)
                            images['br'] = localized_image_list('Brazil', True) # BR images may only be in Portugese these days... old console images were in English though

                            # Now those that may have English versions
                            images['eu'] = localized_image_list('Europe', regions)
                            images['asia'] = localized_image_list('Asia', regions)
                            images['scandi'] = localized_image_list('Scandinavia', regions)
                            images['at'] = localized_image_list('Austria', regions)
                            images['be'] = localized_image_list('Belgium', regions)
                            images['ch'] = localized_image_list('Switzerland', regions)
                            images['cn'] = localized_image_list('China', regions)
                            images['de'] = localized_image_list('Germany', regions)
                            images['dk'] = localized_image_list('Denmark', regions)
                            images['es'] = localized_image_list('Spain', regions)
                            images['fi'] = localized_image_list('Finland', regions)
                            images['fr'] = localized_image_list('France', regions)
                            images['gr'] = localized_image_list('Greece', regions)
                            images['hr'] = localized_image_list('Croatia', regions)
                            images['in'] = localized_image_list('India', regions)
                            images['it'] = localized_image_list('Italy', regions)
                            images['jp'] = localized_image_list('Japan', regions)
                            images['ko'] = localized_image_list('Korea', regions)
                            images['nl'] = localized_image_list('Netherlands', regions)
                            images['no'] = localized_image_list('Norway', regions)
                            images['pl'] = localized_image_list('Poland', regions)
                            images['pt'] = localized_image_list('Portugal', regions)
                            images['ru'] = localized_image_list('Russia', regions)
                            images['sa'] = localized_image_list('South Africa', regions)
                            images['se'] = localized_image_list('Sweden', regions)

                            sys.stdout.write("\033[K")
                            print('* Splitting dat into regions... done.')

                            if regions == True or regions_english == True:
                                print('* Adding titles from USA to "' + font.BOLD + output_file_name + font.END + '"...', sep='', end='\r', flush=True)
                                new_title_count = len(images['usa'])
                                dat_header = header(dat_name, dat_version, dat_author, dat_url, False, 'USA', True, False)
                                output_file.writelines(dat_header)
                            else:
                                print('* Finding USA titles and writing them to "' + font.BOLD + output_file_name + font.END + '"...')

                            for node in images['usa']:
                                filter_flags(output_file, node, no_demos, no_apps, no_protos, no_multi, no_edu)

                            def region_split(country, locale):
                                if images[locale] != []:
                                    if output_file_name.find('.dat', len(output_file_name) - 4, len(output_file_name)):
                                        output_file_name_split = output_file_name.strip('.dat')
                                    else:
                                        output_file_name_split = output_file_name

                                    print('* Adding titles from ' + country + ' to "'  + font.BOLD +  output_file_name_split +  ' (' + country + ').dat' + font.END + '"...', sep='', end='\r', flush=True)

                                    with open(output_file_name_split + ' (' + country + ').dat', 'w') as output_file_split:
                                        dat_header = header(dat_name, dat_version, dat_author, dat_url, False, country, regions, regions_english)
                                        output_file_split.writelines(dat_header)


                                        for node in images[locale]:
                                            filter_flags(output_file_split, node, no_demos, no_apps, no_protos, no_multi, no_edu)
                                        output_file_split.writelines('</datafile>')
                                    sys.stdout.write("\033[K")
                                    print('* Adding titles from ' + country + ' to "'  + font.BOLD +  output_file_name_split +  ' (' + country + ').dat' + font.END + '"... done.')
                                return

                            # Split into regional dats if -r* flag is present
                            if regions == True or regions_english == True:
                                output_file.writelines('</datafile>')
                                sys.stdout.write("\033[K")
                                print('* Adding titles from USA to "' + font.BOLD + output_file_name + font.END + '"...done.')

                                region_split('World', 'world')
                                region_split('UK', 'uk')
                                region_split('Canada', 'ca')
                                region_split('Australia', 'au')
                                region_split('Brazil', 'br')
                                region_split('Europe', 'eu')
                                region_split('Asia', 'asia')
                                region_split('Scandinavia', 'scandi')
                                region_split('Austria', 'at')
                                region_split('Belgium', 'be')
                                region_split('Switzerland', 'ch')
                                region_split('China', 'cn')
                                region_split('Germany', 'de')
                                region_split('Denmark', 'dk')
                                region_split('Spain', 'es')
                                region_split('Finland', 'fi')
                                region_split('France', 'fr')
                                region_split('Greece', 'gr')
                                region_split('Croatia', 'hr')
                                region_split('India', 'in')
                                region_split('Italy', 'it')
                                region_split('Switzerland', 'ch')
                                region_split('Japan', 'jp')
                                region_split('Korea', 'ko')
                                region_split('Netherlands', 'nl')
                                region_split('Norway', 'no')
                                region_split('Poland', 'pl')
                                region_split('Portugal', 'pt')
                                region_split('Russia', 'ru')
                                region_split('South Africa', 'sa')
                                region_split('Sweden', 'se')

                                print(font.GREEN + '\n* Finished splitting dat into regions.' + font.END)
                                sys.exit()

                            print('* Analyzing other regions, and adding English non-dupes to "' + font.BOLD + output_file_name + font.END + '"...')

                            # Get English non-dupe images
                            unique_list = []
                            dupe_list = []

                            # List of known titles that are dupes, but are named something different in other regions
                            if dat_name == 'Microsoft - Xbox':
                                dupe_list = _regional_renames.xbox_rename_list()
                            if dat_name == 'Microsoft - Xbox 360':
                                dupe_list = _regional_renames.x360_rename_list()
                            if dat_name == 'Microsoft - Xbox One':
                                dupe_list = _regional_renames.xbone_rename_list()
                            if dat_name == 'Nintendo - GameCube':
                                dupe_list = _regional_renames.gamecube_rename_list()
                            if dat_name == 'Nintendo - Wii':
                                dupe_list = _regional_renames.wii_rename_list()
                            if dat_name == 'Nintendo - Wii U':
                                dupe_list = _regional_renames.wii_u_rename_list()
                            if dat_name == 'Panasonic - 3DO Interactive Multiplayer':
                                dupe_list = _regional_renames.threedo_rename_list()
                            if dat_name == 'Sega - Dreamcast':
                                dupe_list = _regional_renames.dreamcast_rename_list()
                            if dat_name == 'Sega - Mega CD & Sega CD':
                                dupe_list = _regional_renames.segacd_rename_list()
                            if dat_name == 'Sega - Saturn':
                                dupe_list = _regional_renames.saturn_rename_list()
                            if dat_name == 'Sony - PlayStation':
                                dupe_list = _regional_renames.psx_rename_list()
                            if dat_name == 'Sony - PlayStation 2':
                                dupe_list = _regional_renames.ps2_rename_list()
                            if dat_name == 'Sony - PlayStation 3':
                                dupe_list = _regional_renames.ps3_rename_list()
                            if dat_name == 'Sony - PlayStation 4':
                                dupe_list = _regional_renames.ps4_rename_list()
                            if dat_name == 'Sony - PlayStation Portable':
                                dupe_list = _regional_renames.psp_rename_list()

                            # Add USA image names to unique_list
                            for item in images['usa']:
                                unique_list.append(item.category.parent['name'][:item.category.parent['name'].index('(USA') - 1])

                            # Sort and dedupe unique_list
                            unique_list = sorted(unique_list, key=str.lower)
                            unique_list_temp = []
                            for i, x in enumerate(unique_list):
                                if unique_list[i] != unique_list[i-1]:
                                    unique_list_temp.append(unique_list[i])
                            unique_list = unique_list_temp

                            def regional_unique_image_list(locale, country_code):
                                print('  - Adding unique titles from ' + locale + '...', sep='', end='\r', flush=True)
                                regional_images = []
                                for item in images[country_code]:
                                    locale_start = [m.span()[0] for m in re.finditer('(\(.*' + locale + '.*\))', item.category.parent['name'])][0]
                                    locale_end = [m.span()[1] for m in re.finditer('(\(.*' + locale + '.*\))', item.category.parent['name'])][0]
                                    regional_images.append(item.category.parent['name'][:locale_end - (locale_end - locale_start + 1)])

                                unique_images = [x for x in regional_images if x not in unique_list and x not in dupe_list]

                                # Sort and dedupe unique_images
                                unique_images = sorted(unique_images, key=str.lower)
                                unique_images_temp = []
                                for i, x in enumerate(unique_images):
                                    if unique_images[i] != unique_images[i-1]:
                                        unique_images_temp.append(unique_images[i])
                                unique_images = unique_images_temp

                                # Write regional images to dat file
                                if not unique_images == []:
                                    for image in unique_images:
                                        for node in images[country_code]:
                                            if bool(re.search('(^' + image + ' \()', node.category.parent['name'])):
                                                filter_flags(output_file, node, no_demos, no_apps, no_protos, no_multi, no_edu)

                                    sys.stdout.write("\033[K")
                                    print('  - Adding unique titles from ' + locale + '... done.')

                                    for item in unique_images:
                                        unique_list.append(item)
                                return

                            regional_unique_image_list('World', 'world')
                            regional_unique_image_list('Europe', 'eu')
                            regional_unique_image_list('UK', 'uk')
                            regional_unique_image_list('Australia', 'au')
                            regional_unique_image_list('Canada', 'ca')
                            regional_unique_image_list('Brazil', 'br')
                            regional_unique_image_list('Asia', 'asia')
                            regional_unique_image_list('Austria', 'at')
                            regional_unique_image_list('Belgium', 'be')
                            regional_unique_image_list('Switzerland', 'ch')
                            regional_unique_image_list('China', 'cn')
                            regional_unique_image_list('Germany', 'de')
                            regional_unique_image_list('Denmark', 'dk')
                            regional_unique_image_list('Spain', 'es')
                            regional_unique_image_list('Finland', 'fi')
                            regional_unique_image_list('France', 'fr')
                            regional_unique_image_list('Greece', 'gr')
                            regional_unique_image_list('Croatia', 'hr')
                            regional_unique_image_list('India', 'in')
                            regional_unique_image_list('Italy', 'it')
                            regional_unique_image_list('Japan', 'jp')
                            regional_unique_image_list('Korea', 'ko')
                            regional_unique_image_list('Netherlands', 'nl')
                            regional_unique_image_list('Norway', 'no')
                            regional_unique_image_list('Poland', 'pl')
                            regional_unique_image_list('Portugal', 'pt')
                            regional_unique_image_list('Russia', 'ru')
                            regional_unique_image_list('South Africa', 'sa')
                            regional_unique_image_list('Scandinavia', 'scandi')
                            regional_unique_image_list('Sweden', 'se')

                            sys.stdout.write("\033[K")

                            # Finish up the file
                            output_file.close()

                        with open(output_file_name, 'r') as output_file:
                            content = output_file.read()
                            output_file.close()

                        # Find out how many titles are in the new dat file
                        new_title_count = content.count('<game name=')

                        print('\n|  Original title count: ' + str('{:,}'.format(original_title_count)) + '\n|  Dupes and non-English titles: ' + str('{:,}'.format(original_title_count - new_title_count)) + '\n|  New title count: ' + str('{:,}'.format(new_title_count)))

                        # Dat file header
                        dat_header = header(dat_name, dat_version, dat_author, dat_url, new_title_count, False, False, False)

                        with open(output_file_name, 'w') as output_file:
                            output_file.writelines(dat_header)
                            output_file.close()
                        with open(output_file_name, 'a') as output_file:
                            output_file.write(content)
                            output_file.writelines('</datafile>')
                            output_file.close()

                        print(font.GREEN + '\n* Finished writing unique English titles to "' +  font.BOLD + output_file_name + font.END + font.GREEN + '".' + font.END)

                    else:
                        print('\nERROR: This dat file is not authored by Redump')

                else:
                    print('\n\nERROR: "' + input_file_name + '" is not a CLRMAMEPro dat file.')


# Initial splash screen
os.system('cls' if os.name == 'nt' else 'clear')
print(font.RED + '______   _____ _____ _____ _' +
    '\n| ___ \ |_   _|  _  |  _  | |' +
    '\n| |_/ /___| | | | | | | | | |' +
    '\n|    // _ \ | | | | | | | | |' +
    '\n| |\ \  __/ | \ \_/ | \_/ / |____' +
    '\n\_| \_\___\_/  \___/ \___/\_____/ '+ font.END + 'v' + version_number)
print('=======================================')
if len(sys.argv) == 1:
    print('\nStrips Redump (' + font.UNDERLINE + 'http://redump.org/' + font.END + ') dats to only include English titles from\nall regions, with no dupes. US titles are preferenced. This is not an\nofficial Redump project.')

# Check user input
user_input = check_input()
filter_dat(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4], user_input[5], user_input[6], user_input[7], user_input[8])