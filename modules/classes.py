import argparse
import re

from modules.titleutils import get_languages, get_raw_title, remove_languages,\
    remove_regions, remove_tags
from modules.utils import Font

class CloneList:
    """ Returns a formatted clone list """

    def __init__(self, compilations, overrides, conditional_overrides, renames):
        self.compilations = compilations
        self.renames = renames
        self.overrides = overrides
        self.conditional_overrides = conditional_overrides


class Dat:
    """ Returns an object that contains the input dat's details """

    def __init__(self, contents='', name='Unknown', description='Unknown', version='Unknown', author='Unknown', url='Unknown', user_options=[]):
        self.name = name
        self.description = description
        self.version = version
        self.author = author
        self.url = url
        self.contents = contents
        self.user_options = user_options


class DatNode:
    """ Returns an object that contains all of a title's properties """

    def __init__(self, node, region, region_data, user_input, input_dat, dat_numbered, REGEX):
        if dat_numbered == False:
            self.full_name = str(node.description.parent['name'])
            self.numbered_name = ''
        else:
            self.full_name = str(node.description.parent['name'])[7:]
            self.numbered_name = str(node.description.parent['name'])

        metadata = input_dat.metadata

        if self.full_name in metadata:
            self.online_languages = metadata[self.full_name]['languages']
        else:
            self.online_languages = ''


        # Set title with minimal tags, starting with normalizing disc names
        tag_free_name = self.full_name

        for key, value in user_input.tag_strings.disc_rename.items():
            if key in tag_free_name:
                tag_free_name = tag_free_name.replace(key, value)

        # Strip out other tags found in tags.json
        self.tag_free_name = remove_tags(tag_free_name, user_input, REGEX)

        # Set region free, language free title
        if re.search(' \((.*?,){0,} {0,}' + region + '(,.*?){0,}\)', self.full_name) != None:
            self.region_free_name = remove_regions(remove_languages(self.full_name, REGEX.languages), region_data)

            # Now set regionless title with minimal tags
            self.short_name = remove_regions(remove_languages(self.tag_free_name, REGEX.languages), region_data)
        else:
            self.region_free_name = self.full_name
            self.short_name = self.tag_free_name

        self.title_languages = get_languages(self.full_name, REGEX.languages)
        self.group = get_raw_title(self.full_name)

        # Set implied language for the region
        if region != 'Unknown':
            self.implied_language = region_data.implied_language[region]

            self.regions = re.search('\((.*?,){0,} {0,}' + region + '(,.*?){0,}\)', self.full_name)[0][1:-1]

            region_list = self.regions.split(', ')
            region_reorder = []

            for another_region in region_data.all:
                if another_region in region_list:
                    region_reorder.append(another_region)

            self.regions = ', '.join(region_reorder)

            for another_region in region_data.all:
                if re.search(another_region + '(,.*?){0,}', self.regions) != None:
                    self.primary_region = another_region
                    break

            for i, x in enumerate(region_data.all):
                if self.primary_region == x:
                    self.region_priority = i
        else:
            self.implied_language = ''
            self.regions = 'Unknown'
            self.primary_region = 'Unknown'
            self.region_priority = 100

        if ',' in self.regions:
            self.secondary_region = self.regions.replace(self.primary_region + ', ', '')
        else:
            self.secondary_region = ''

        # Reverse engineer category for No-Intro
        if node.category is None:
            self.category = ''
            for program in REGEX.programs:
                if re.search(program, self.full_name) != None:
                    self.category = 'Applications'
            for demo in REGEX.demos:
                if re.search(demo, self.full_name) != None:
                    self.category = 'Demos'
            for preproduction in REGEX.preproduction:
                if re.search(preproduction, self.full_name) != None:
                    self.category = 'Preproduction'
        else:
            self.category = node.category.contents[0]

        # Some further category assignments
        if (
            self.category == 'Console'
            or '[BIOS]' in self.full_name):
                self.category = 'BIOS'
        elif self.category == '':
            self.category = 'Games'

        self.description = node.description.contents[0]
        self.cloneof = ''
        self.cloneof_group = ''

        # From multiple sources, set the canonical supported languages for the title
        if self.online_languages != '':
            self.languages = self.online_languages
        elif self.online_languages == '' and self.title_languages == '':
            self.languages = self.implied_language
        elif self.online_languages == '' and self.title_languages != '':
            if '+' in self.title_languages:
                self.title_languages = self.title_languages.replace('+', ',')
                new_title_languages = self.title_languages.split(',')
                new_title_languages = set(new_title_languages)
                self.title_languages = ','.join(new_title_languages)

            self.languages = self.title_languages

        # Compensate for poor language formatting
        self.languages = re.sub(',([\S])', r', \1', self.languages)

        # Convert the <rom> lines for the current node
        node_roms = node.findChildren('rom', recursive=False)
        roms = []
        for rom in node_roms:
            if 'crc' not in (str(rom)):
                crc_string = ''
            else:
                crc_string = rom['crc']

            if 'md5' not in (str(rom)):
                md5_string = ''
            else:
                md5_string = rom['md5']

            if 'sha1' not in (str(rom)):
                sha1_string = ''
            else:
                sha1_string = rom['sha1']

            roms.append(DatNodeRom('rom', crc_string, md5_string, rom['name'], sha1_string, rom['size']))

        self.roms = roms

        # Check if the (Demo) tag is missing, and add it if so
        if self.category == 'Demos' and '(Demo' not in self.full_name:
            self.short_name = self.short_name + ' (Demo)'
            self.region_free_name = self.region_free_name + ' (Demo)'
            self.tag_free_name = self.tag_free_name + ' (Demo)'


    def __str__(self):
        ret_str = []


        def format_property(property, string, tabs):
            """ Formats a string properly based on whether a property has a value
            or not """

            none_str = f'{Font.disabled}None{Font.end}'
            if property == '':
                ret_str.append(f'  ├ {string}:{tabs}{none_str}\n')
            else:
                ret_str.append(f'  ├ {string}:{tabs}{property}\n')


        ret_str.append(f'  ○ full_name:\t\t{self.full_name}\n')
        ret_str.append(f'  ├ numbered_name:\t{self.numbered_name}\n')
        ret_str.append(f'  ├ description:\t{self.description}\n')
        ret_str.append(f'  ├ region_free_name:\t{self.region_free_name}\n')
        ret_str.append(f'  ├ tag_free_name:\t{self.tag_free_name}\n')
        ret_str.append(f'  ├ short_name:\t\t{self.short_name}\n')
        ret_str.append(f'  ├ group:\t\t{self.group}\n')
        ret_str.append(f'  ├ regions:\t\t{self.regions}\n')
        ret_str.append(f'  ├ primary_region:\t{self.primary_region}\n')
        format_property(self.secondary_region, 'secondary_region', '\t')
        ret_str.append(f'  ├ region_priority:\t{str(self.region_priority)}\n')
        format_property(self.title_languages, 'title_languages', '\t')
        format_property(self.implied_language, 'implied_language', '\t')
        format_property(self.online_languages, 'online_languages', '\t')
        format_property(self.languages, 'languages', '\t\t')
        format_property(self.cloneof, 'cloneof', '\t\t')
        format_property(self.cloneof_group, 'cloneof_group', '\t')
        ret_str.append(f'  ├ category:\t\t{self.category}\n')
        ret_str.append(f'  └ roms ┐\n')
        for i, rom in enumerate(self.roms):
            if i == len(self.roms) - 1:
                ret_str.append(f'         └ name: {rom.name} | crc: {rom.crc} | md5: {rom.md5} | sha1: {rom.sha1} | size: {rom.size}\n\n')
            else:
                ret_str.append(f'         ├ name: {rom.name} | crc: {rom.crc} | md5: {rom.md5} | sha1: {rom.sha1} | size: {rom.size}\n')

        ret_str = ''.join(ret_str)

        return ret_str


class DatNodeRom:
    """ Returns an object that contains a title's rom properties """

    def __init__(self, rom, crc, md5, name, sha1, size):
        self.crc = crc.lower()
        self.md5 = md5.lower()
        self.name = name
        self.sha1 = sha1.lower()
        self.size = size


class Filters:
    """ Filters constructor """

    def __init__(self):
        self.global_exclude = []
        self.global_include = []
        self.system_exclude = []
        self.system_include = []
        self.system_file = ''


class Regex:
    """ Regex constructor """

    def __init__(self, LANGUAGES):
        # Preproduction
        self.alpha = re.compile('\((?:(?!\(|Alpha( [0-9]{,2}){,1})[\s\S])*Alpha( [0-9]{,2}){,1}\)')
        self.beta = re.compile('\((?:(?!\(|Beta( [0-9]{,2}){,1})[\s\S])*Beta( [0-9]{,2}){,1}\)')
        self.proto = re.compile('\((?:(?!\(|Proto( [0-9]{,2}){,1})[\s\S])*Proto( [0-9]{,2}){,1}\)')
        self.preprod = re.compile('\(Pre-production\)')
        self.review = re.compile('\(Review Code\)')

        # Tags
        self.alt = re.compile('\(Alt.*?\)')
        self.bad = re.compile('\[b\]')
        self.bios = re.compile('(\[BIOS\])|(\(Enhancement Chip\))')
        self.covermount = re.compile('\(Covermount\)')
        self.dates = re.compile('\((\d{8}|\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4}|\d{2}-\d{2}-\d{2}|(January|February|March|April|May|June|July|August|September|October|November|December), \d{4})\)')
        self.dates_whitespace = re.compile('\s?\((\d{8}|\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4}|\d{2}-\d{2}-\d{2}|(January|February|March|April|May|June|July|August|September|October|November|December), \d{4})\)\s?')
        self.edc = re.compile('\(EDC\)')
        self.languages = re.compile('( (\((' + LANGUAGES + ')\.*?)(,.*?\)|\)))')
        self.oem = re.compile('\((?:(?!\(|OEM.*?)[\s\S])*OEM.*?\)')
        self.hibaihin = re.compile('\(Hibaihin.*?\)')
        self.pirate = re.compile('\(Pirate\)')
        self.rerelease = re.compile('\(Rerelease\)')

        # Exclude filters
        self.demos = [
            re.compile('\(Demo( [1-9])*\)'),
            re.compile('\(Demo-CD\)'),
            re.compile('Taikenban'),
            re.compile('\(@barai\)'),
            re.compile('\(GameCube Preview\)'),
            re.compile('\(Preview\)'),
            re.compile('\(Sample( [1-9])*\)'),
            re.compile('Trial Edition')
            ]
        self.manuals = re.compile('\(Manual\)'),
        self.preproduction = [
            self.alpha,
            self.beta,
            self.proto,
            self.preprod,
            self.review,
            ]
        self.preproduction_bad = '\((?:(?!\(|(Alpha|Beta|Pre-production|Proto|Review Code)( [0-9]{,2}){,1})[\s\S])*(Alpha|Beta|Pre-production|Proto|Review Code)( [0-9]{,2}){,1}\)|(\[b\])'
        self.programs = [
            re.compile('\(Program\)'),
            re.compile('\(Test Program\)'),
            re.compile('Check Program'),
            re.compile('Sample Program')
        ]
        self.promotional = [
            re.compile('EPK'),
            re.compile('Press Kit'),
            re.compile('\(Promo\)')
        ]
        self.unlicensed = [
            re.compile('\(Unl\)')
        ]

        # Versions
        self.version = re.compile('\(v[0-9].*?\)')
        self.long_version = re.compile('Version [+-]?([0-9]+([.][0-9]*)?|[.][0-9]+).*?[ \)]')
        self.revision = re.compile('\(Rev [0-9A-Z].*?\)')
        self.sega_ring_code = re.compile('\(([0-9]{1,2}[A-Z]([ ,].[0-9]{1,2}[A-Z])*|R[E]{,1}[-]{,1}[0-9]{0,})\)')
        self.sega_ring_code_re = re.compile('R[E]{,1}[-]{,1}[0-9]{0,}')
        self.fds_version = re.compile('\(DV [0-9].*?\)')


class RegionKeys():
    """ Region keys constructor """

    def __init__(self):
        self.filename = 'internal-config.json'
        self.region_order = 'default_region_order'
        self.languages = 'languages'


class Regions():
    """ Regions constructor """

    def __init__(self):
        self.all = []
        self.region_order = []
        self.implied_language = []
        self.languages_filter = []
        self.languages_long = []
        self.languages_short = []
        self.languages_key = {}

    def __str__(self):
        ret_str = []
        replace_str = ',\n    '

        ret_str.append(
            f'  ○ all:\n    [  \n     '
            f'{str(self.all)[1:-1].replace(",", replace_str)}\n    ]\n')
        ret_str.append(
            f'  ○ region_order:\n    [  \n     '
            f'{str(self.region_order)[1:-1].replace(",", replace_str)}\n    ]\n')
        ret_str.append(
            f'  ○ implied_language:\n    [  \n     '
            f'{str(self.implied_language)[1:-1].replace(",", replace_str)}\n    ]\n')

        ret_str = ''.join(ret_str)

        return ret_str


class SmartFormatter(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        # This is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)


class Stats():
    """ Stores stats before processing the dat """

    def __init__(self, original_title_count, user_input=False, final_title_count=0, clone_count=0):

        self.original_title_count = original_title_count
        self.final_title_count = final_title_count
        self.clone_count = clone_count

        if user_input != False:
            def get_count(exclusion):
                """ Returns how many titles were excluded for a given category """

                if exclusion in user_input.removed_titles:
                    return len(user_input.removed_titles[exclusion])
                else:
                    return 0

            self.applications_count = get_count('Applications')
            self.audio_count = get_count('Audio')
            self.bad_dump_count = get_count('Bad_dumps')
            self.bios_count = get_count('Console')
            self.compilations_count = get_count('Compilations')
            self.coverdiscs_count = get_count('Coverdiscs')
            self.demos_count = get_count('Demos')
            self.educational_count = get_count('Educational')
            self.manuals_count = get_count('Manuals')
            self.multimedia_count = get_count('Multimedia')
            self.pirate_count = get_count('Pirate')
            self.preproduction_count = get_count('Preproduction')
            self.promotional_count = get_count('Promotional')
            self.unlicensed_count = get_count('Unlicensed')
            self.video_count = get_count('Video')

            self.custom_system_filter_count = len(user_input.removed_titles['Custom system filter excludes'])
            self.custom_global_filter_count = len(user_input.removed_titles['Custom global filter excludes'])


class TagKeys:
    """ Tag keys constructor """

    def __init__(self):
        self.filename = 'internal-config.json'
        self.demote_editions = 'demote_editions'
        self.disc_rename = 'disc_rename'
        self.ignore = 'ignore_tags'
        self.modern_editions = 'modern_editions'
        self.promote_editions = 'promote_editions'


class Tags:
    """ Tags constructor """

    def __init__(self):
        self.demote_editions = set()
        self.disc_rename = {}
        self.ignore = set()
        self.modern_editions = set()
        self.promote_editions = set()

    def __str__(self):
        ret_str = []
        replace_str = ',\n    '

        ret_str.append(
            f'  ○ demote_editions:\n    [  \n     '
            f'{str(self.demote_editions)[1:-1].replace(",", replace_str)}\n    ]\n')
        ret_str.append(
            f'  ○ disc_rename:\n    {{  \n     '
            f'{str(self.disc_rename)[1:-1].replace(",", replace_str)}\n    }}\n')
        ret_str.append(
            f'  ○ ignore:\n    [  \n     '
            f'{str(self.ignore)[1:-1].replace(",", replace_str)}\n    ]\n')
        ret_str.append(
            f'  ○ modern_editions:\n    [  \n     '
            f'{str(self.modern_editions)[1:-1].replace(",", replace_str)}\n    ]\n')
        ret_str.append(
            f'  ○ promote_editions:\n    [  \n     '
            f'{str(self.promote_editions)[1:-1].replace(",", replace_str)}\n    ]\n')

        ret_str = ''.join(ret_str)

        return ret_str


class Titles:
    """ Tag keys constructor """

    def __init__(self):
        self.all = {}
        self.regions = {}


class UserInput:
    """ Stores user input values, including what types of titles to exclude """

    def __init__(self, input_file_name='', output_folder_name='',
                 no_applications='', no_audio='', no_bad_dumps='',
                 no_bios='', no_compilations='', no_coverdiscs='',
                 no_demos='', no_educational='', no_manuals='',
                 no_multimedia='', no_pirate='', no_preproduction='',
                 no_promotional='', no_unlicensed='', no_video='',
                 modern='', supersets='', filter_languages='',
                 legacy='', user_options='', verbose='',
                 no_filters='', keep_remove='', list=''):

        self.input_file_name = input_file_name
        self.output_folder_name = output_folder_name

        self.no_applications = no_applications
        self.no_bad_dumps = no_bad_dumps
        self.no_compilations = no_compilations
        self.no_demos = no_demos
        self.no_educational = no_educational
        self.no_coverdiscs = no_coverdiscs
        self.no_audio = no_audio
        self.no_video = no_video
        self.no_bios = no_bios
        self.no_console = no_bios
        self.no_multimedia = no_multimedia
        self.no_pirate = no_pirate
        self.no_manuals = no_manuals
        self.no_preproduction = no_preproduction
        self.no_promotional = no_promotional
        self.no_unlicensed = no_unlicensed
        self.modern = modern
        self.supersets = supersets
        self.filter_languages = filter_languages
        self.legacy = legacy
        self.user_options = user_options
        self.verbose = verbose
        self.no_filters = no_filters
        self.keep_remove = keep_remove
        self.list = list

        self.global_exclude = []
        self.global_include = []
        self.system_exclude = []
        self.system_include = []