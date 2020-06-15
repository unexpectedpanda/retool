import datetime
import html
import json
import os
import re
import sys

from lxml import etree
from bs4 import BeautifulSoup

from modules.classes import Dat, DatNode, DatNodeRom
from modules.titleutils import choose_parent, get_raw_title
from modules.utils import Font, printverbose, printwrap


def convert_clrmame_dat(clrmame_header, input_dat, is_folder):
    """ Converts CLRMAMEPro dat format to LogiqX dat format """

    def header_details(find_string, replace_string):
        """ Gets values for CLRMAMEPro dat header details """

        search_string = re.search(find_string, clrmame_header[0])

        if search_string != None:
            return re.sub(
                replace_string,
                '',
                search_string.group(0)).strip()
        else:
            return ''

    dat_name = header_details(re.compile('.*?name.*'), 'name |(\")')
    dat_description = header_details(
        re.compile('.*?description.*'), 'description |(\")')
    dat_category = header_details(re.compile('.*?category.*'), 'category |(\")')
    dat_version = header_details(re.compile('.*?version.*'), 'version |(\")')
    dat_author = header_details(re.compile('.*?author.*'), 'author |(\")')

    convert_dat = []

    convert_dat.append(
        '<?xml version="1.0"?>\n\
        <!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" \
            "http://www.logiqx.com/Dats/datafile.dtd"><datafile>\n\t<header>')
    convert_dat.append(f'\t\t<name>{dat_name}</name>')
    convert_dat.append(f'\t\t<description>{dat_description}</description>')
    convert_dat.append(f'\t\t<version>{dat_version}</version>')
    convert_dat.append(f'\t\t<author>{dat_author}</author>\n\t</header>')

    # Now work through each of the title details
    dat_contents = re.findall('^game \($.*?^\)$', input_dat, re.M|re.S)
    if dat_contents:
        for item in dat_contents:
            xml_node = re.split('\n', item)
            regex = re.sub('name |(\")', '', xml_node[1].strip())
            convert_dat.append(
                f'\t<game name="{regex}">'
                f'\n\t\t<category>{dat_category}</category>\n\t\t<description>'
                f'{regex}</description>')
            for node in xml_node:
                if node.strip().startswith('rom'):
                    node = node
                    node = re.sub('^rom \( name ', '<rom name="', node.strip())
                    node = re.sub(' size ', '" size="', node.strip())
                    node = re.sub(' crc ', '" crc="', node.strip())
                    node = re.sub(' md5 ', '" md5="', node.strip())
                    node = re.sub(' sha1 ', '" sha1="', node.strip())
                    node = re.sub(' \)$', '" />', node.strip())
                    convert_dat.append('\t\t' + node)
            convert_dat.append('\t</game>')
        convert_dat.append('</datafile>')

        convert_dat = '\n'.join(convert_dat)
    else:
        printwrap(
            f'{Font.error_bold} * Error: {Font.error}file isn\'t Logiqx XML or '
            f'CLRMAMEPro dat.{Font.end}', 'error')
        if is_folder == False:
            sys.exit()
        else:
            return 'end_batch'
    return Dat(convert_dat, dat_name, dat_description, dat_version, dat_author)


def dat_to_dict(region, region_data, input_dat, user_input, compilations_found, REGEX):
    """ Converts an input dat file to a dict """

    # Find all titles in the soup object that belong to the current region
    if region == 'Unknown':
        refined_region_xml = input_dat.soup.find_all(
            'game', {'name': re.compile(
                '^(?!.*(\(.*?(' + '|'.join(region_data.all).replace(
                    '|Unknown','') + ').*?\))).*(.*)')})
    else:
        # Rough region selection first, as this speeds up processing larger files.
        region_xml = input_dat.soup.find_all(
            'game', {'name': lambda x: x and region in x})

        # Now refine the region selection
        refined_region_xml = []
        for node in region_xml:
            if re.search('game.*?name=.*?\((.*?,){0,} {0,}' + region + '(,.*?){0,}\)', str(node)) != None:
                refined_region_xml.append(node)
        region_xml = None

    progress = 0
    progress_old = 0
    progress_total = len(refined_region_xml)

    # Create a dict to store groups of related titles in
    groups = {}

    # Convert the XML to dict
    for node in refined_region_xml:
        progress += 1
        progress_percent = int(progress/progress_total*100)

        if progress_old != progress_percent:
            sys.stdout.write("\033[K")
            print(
                    f'* Checking dat for titles in provided regions... {region} [{progress_percent}%]',
                    sep='', end='\r', flush=True
                )

        # Drop xml nodes with categories the user has chosen to exclude
        def exclude_categories(category, regexes=[]):
            if hasattr(user_input, 'no_' + category.lower()):
                if getattr(user_input, 'no_' + category.lower()) == True:
                    if node.category.contents[0] == category:
                        return True
                    if regexes != []:
                        for regex in regexes:
                            if re.search(regex, node.category.parent['name']) != None:
                                return True

        if exclude_categories('Applications') == True: continue
        if exclude_categories('Demos', [
            re.compile('\(Demo( [1-9])*\)'),
            re.compile('\(Demo-CD\)'),
            re.compile('\(.*?Taikenban.*?\)'),
            re.compile('\(@barai\)'),
            re.compile('\(Sample\)'),
            re.compile('Trial Edition')]) == True: continue
        if exclude_categories('Coverdiscs') == True: continue
        if exclude_categories('Educational') == True: continue
        if exclude_categories('Multimedia') == True: continue
        if exclude_categories('Preproduction', [
            re.compile('\(Alpha( [1-9])*\)'),
            re.compile('\(Beta( [1-9])*\)'),
            re.compile('\(Prototype\)'),
            ]) == True: continue
        if exclude_categories('Unlicensed', [
            re.compile('\(Unl\)')
        ]) == True: continue

        if input_dat.clone_lists != None:
            if user_input.no_compilations == True:
                compilation_check = False

                for compilation in input_dat.clone_lists.compilations:
                    if compilation == node.category.parent['name']:
                        compilation_check = True
                        compilations_found.update([compilation])

                if compilation_check == True:
                    continue

        # Get the group name for the current node, then add it to the groups list
        group_name = get_raw_title(node.category.parent['name'])

        if group_name not in groups:
            groups[group_name] = []

        groups[group_name].append(
            DatNode(node, region, region_data, user_input, input_dat, REGEX))

        # Filter languages, if the option has been turned on
        if user_input.filter_languages == True:
            for disc_title in groups[group_name]:
                language_found = False
                for language in user_input.user_languages:
                    if language in disc_title.languages:
                        language_found = True
                if language_found == False and disc_title.languages != '':
                    if disc_title in groups[group_name]: groups[group_name].remove(disc_title)

        progress_old = progress_percent

    # Remove the nodes from the soup object so processing other regions is quicker.
    print(
            f'* Checking dat for titles in provided regions... {region} [Finishing up...]',
            sep='', end='\r', flush=True
        )
    for node in refined_region_xml:
        node.decompose()

    # Process the overrides, which take them out of existing groups, put them into
    # others, and set fake shortnames
    if input_dat.clone_lists != None:
        if input_dat.clone_lists.overrides != None:
            for key, value in input_dat.clone_lists.overrides.items():
                if region in key:
                    try:
                        titles_temp = groups[get_raw_title(key)].copy()

                        # If value[1] = False, match against the tag_free_name
                        # If value[1] = True, match against the full_name
                        for title in titles_temp:
                            if value[1] == False:
                                if title.tag_free_name == key:
                                    title.short_name = value[0]
                                    if value[0] not in groups:
                                        groups[value[0]] = []
                                    groups[value[0]].append(title)
                                    groups[get_raw_title(key)].remove(title)
                            elif value[1] == True:
                                if title.full_name == key:
                                    title.short_name = value[0]
                                    if value[0] not in groups:
                                        groups[value[0]] = []
                                    groups[value[0]].append(title)
                                    groups[get_raw_title(key)].remove(title)
                    except:
                        printverbose(
                            user_input.verbose,
                            f'{Font.warning}* Override title not found in dat or current region: '
                            f'{Font.warning_bold}{key}{Font.end}')

        # Conditional overrides for when renames get funky depending on region ordering
        # For example, Bishi Bashi Special (Europe) contains Bishi Bashi Special (Japan)
        # and Bishi Bashi Special 2 (Japan). The fact that the first two titles have the
        # same name but different content means a conditional override is required.
        if input_dat.clone_lists.conditional_overrides != None:
            for key, value in input_dat.clone_lists.conditional_overrides.items():
                if region in key:
                    region_one = []
                    region_two = []

                    for i, another_region in enumerate(user_input.user_region_order):
                        for check_region in value['condition']['region']:
                            if another_region == check_region:
                                region_one.append(i)
                        for higher_than_region in value['condition']['higher_than']:
                            if another_region == higher_than_region:
                                region_two.append(i)

                    if region_one != []:
                        conditional_override = ''

                        # Check if the title region is higher priority than any of the
                        # other supplied regions
                        for i in range(0, len(region_one)):
                            for priority in region_two:
                                if region_one[i] < priority:
                                    conditional_override = True
                                    break
                                else:
                                    conditional_override = False
                                    break
                            if conditional_override != '': break

                        # If the region is higher, reassign the group and short_name
                        if conditional_override == True:
                            try:
                                titles_temp = groups[get_raw_title(key)].copy()

                                for title in titles_temp:
                                    if title.tag_free_name == key:
                                        title.short_name = value['new_group']
                                        title.group = value['new_group']
                                        if value['new_group'] not in groups:
                                            groups[value['new_group']] = []
                                        groups[value['new_group']].append(title)
                                        groups[get_raw_title(key)].remove(title)
                            except:
                                printverbose(
                                    user_input.verbose,
                                    f'{Font.warning}* Conditional override title not found in dat or current region: '
                                    f'{Font.warning_bold}{key}{Font.end}')
                        # If the region is lower and there's an "else_group" property,
                        # file the title into that group with the same short_name
                        elif 'else_group' in value['condition']:
                            try:
                                titles_temp = groups[get_raw_title(key)].copy()

                                for title in titles_temp:
                                    if title.tag_free_name == key:
                                        title.short_name = value['condition']['else_group']
                                        title.group = value['condition']['else_group']
                                        if value['condition']['else_group'] not in groups:
                                            groups[value['condition']['else_group']] = []
                                        groups[value['condition']['else_group']].append(title)
                                        groups[get_raw_title(key)].remove(title)
                            except:
                                printverbose(
                                    user_input.verbose,
                                    f'{Font.warning}* Conditional override title not found in dat or current region: '
                                    f'{Font.warning_bold}{key}{Font.end}')

    # Identify the parents for the region
    for group, titles in groups.items():
        if (
            'Saturn' in input_dat.name
            or 'Sega CD' in input_dat.name
            or 'Panasonic - 3DO' in input_dat.name):
            ring_code = True
        else:
            ring_code = False

        titles = choose_parent(titles, region_data, user_input, REGEX, ring_code)

    return groups


def process_input_dat(dat_file, is_folder):
    """ Prepares input dat file and converts to an object

    Returns a Dat object with the following populated:

    .name
    .description
    .version
    .author
    .url
    .soup

    Removes the following from a Dat object:

    .contents
    """

    if is_folder == True:
        next_status = ' Skipping file...'
    else:
        next_status = ''

    printwrap(f'* Reading dat file: "{Font.bold}{dat_file}{Font.end}"')
    try:
        with open(dat_file, 'r') as input_file:
            print('* Validating dat file... ', sep=' ', end='', flush=True)
            input_dat = input_file.read()
    except OSError as e:
        printwrap(
            f'{Font.error_bold}* Error: {Font.error}{str(e)}.{Font.end}{next_status}',
            'error')
        if is_folder == False:
            raise
        else:
            return

    # Check the dat file format -- if it's CLRMAMEPro format, convert it to LogiqX
    clrmame_header = re.search('^clrmamepro \($.*?^\)$', input_dat, re.M|re.S)

    if clrmame_header:
        print('file is a CLRMAMEPro dat file.')
        input_dat = convert_clrmame_dat(clrmame_header, input_dat, is_folder)

        # Go to the next file in a batch operation if something went wrong.
        if input_dat == 'end_batch': return
    else:
        input_dat = Dat(input_dat)

        # Exit if there are entity or element tags to avoid abuse
        if '<!ENTITY' in input_dat.contents or '<!ELEMENT' in input_dat.contents:
            print('failed.')
            printwrap(
                f'{Font.error_bold} Error: {Font.error}Entity and element tags '
                f'aren\'t supported in dat files.{Font.end}{next_status}', 'error')
            sys.exit()

        # Check for a valid Redump XML dat that follows the Logiqx dtd
        valid_dat_file = False

        if ('<datafile>' in input_dat.contents and '<?xml' in input_dat.contents and '<game' in input_dat.contents):
            # Remove unexpected XML declarations from the file so we can check validity
            try:
                input_dat.contents = input_dat.contents.replace(re.search('<\?xml.*?>', input_dat.contents)[0], '<?xml version="1.0"?>')
            except:
                print('failed.')
                printwrap(
                    f'{Font.error_bold}* Error: {Font.error}File is missing an XML '
                    f'declaration. It\'s probably not a dat file.'
                    f'{next_status}{Font.end}', 'error')
                if is_folder == False:
                    sys.exit()
                else:
                    return
            try:
                with open('datafile.dtd') as dtdfile:
                    dtd = etree.DTD(dtdfile)
                    try:
                        root = etree.XML(input_dat.contents)

                        if dtd.validate(root) == False:
                            print('failed.')
                            printwrap(
                                f'{Font.error_bold}* Error: {Font.error}XML file'
                                f'doesn\'t conform to Logiqx dtd. '
                                f'{dtd.error_log.last_error}.'
                                f'{next_status}{Font.end}', 'error')
                            if is_folder == False:
                                sys.exit()
                            else:
                                return
                    except etree.XMLSyntaxError as e:
                        print('failed.')
                        printwrap(
                            f'{Font.error_bold}* Error: {Font.error}XML file is '
                            f'malformed. {e}.{next_status}{Font.end}', 'error')
                        if is_folder == False:
                            sys.exit()
                        else:
                            return
                    else:
                        print('file is a Logiqx dat file.')

            except OSError as e:
                printwrap(f'{Font.error_bold}* Error: {str(e)}{next_status}{Font.end}',
                          'error')
                if is_folder == False:
                    raise
                else:
                    return
        else:
            print('failed.')
            printwrap(
                f'{Font.error_bold}* Error: "{dat_file}"{Font.error} '
                f'isn\'t a compatible dat file.{next_status}{Font.end}', 'error')
            if is_folder == False:
                sys.exit()
            else:
                return

    # Convert contents to BeautifulSoup object, remove original contents attribute
    print('* Converting dat file to a searchable format... ', sep=' ', end='', flush=True)
    input_dat.soup = BeautifulSoup(input_dat.contents, "lxml-xml")
    del input_dat.contents
    print('done.')

    # Set input dat header details
    if input_dat.soup.find('header') != None:
        for key, value in input_dat.__dict__.items():
            if (
                key != 'soup'
                and key != 'user_options'
                and value == 'Unknown'
                and input_dat.soup.find(key) != None):
                setattr(input_dat, key, input_dat.soup.find(key).string)
            elif value == '':
                setattr(input_dat, key, 'Unknown')

    # Remove Retool tag from name if it exists
    input_dat.name = input_dat.name.replace(' (Retool)', '')

    # Sanitize some header details which are used in the output filename
    characters = [':', '\\', '/', '<', '>', '"', '|', '?', '*']
    reserved_filenames = ['con', 'prn', 'aux', 'nul', 'com[1-9]', 'lpt[1-9]']

    for character in characters:
        if character in input_dat.name:
            input_dat.name = input_dat.name.replace(character, '-')
        if character in input_dat.version:
            input_dat.version = input_dat.version.replace(character, '-')

    for filename in reserved_filenames:
        if re.search('^' + filename + '$', input_dat.name) != None:
            input_dat.name = 'Unknown'
        if re.search('^' + filename + '$', input_dat.version) != None:
            input_dat.version = 'Unknown'

    return input_dat


def header(input_dat, new_title_count, user_input):
    """ Creates a header for the output dat file """

    new_title_count = str('{:,}'.format(new_title_count))

    name = f'\n\t\t<name>{html.escape(input_dat.name, quote=False)} (Retool)</name>'
    description = (
        f'\n\t\t<description>{html.escape(input_dat.name, quote=False)}{user_input.user_options}'
        f' ({new_title_count}) ({input_dat.version})</description>')

    if input_dat.author != '' and input_dat.author != None:
        input_dat.author = f'{html.escape(input_dat.author, quote=False)} &amp; Retool'
    else:
        input_dat.author = 'Unknown &amp; Retool'

    header = [
        '<?xml version="1.0"?>',
        '\n<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" '
        '"http://www.logiqx.com/Dats/datafile.dtd">',
        '\n<datafile>',
        '\n\t<header>',
        name,
        description,
        f'\n\t\t<version>{html.escape(input_dat.version, quote=False)}</version>',
        f'\n\t\t<date>{datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}</date>',
        f'\n\t\t<author>{input_dat.author}</author>',
        '\n\t\t<homepage>redump.org</homepage>',
        f'\n\t\t<url>{html.escape(input_dat.url, quote=False)}</url>',
        '\n\t</header>\n']
    return header