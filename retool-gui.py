#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" retool-gui.py: GUI version of Retool for Windows.

https://github.com/unexpectedpanda/retool
"""

import os
import platform
import PySimpleGUIQt as sg
import retool
import sys
import updateclonelists
import webbrowser

from modules.classes import Filters, RegionKeys, UserInput
from modules.importdata import build_regions
from modules.output import generate_config
from modules.userinput import import_user_config, import_user_filters
from modules.xml import process_input_dat

# Generate regions and languages from internal-config.json
region_data = build_regions(RegionKeys())

# Platform-specific setup
font = 'Any'
scale_multiplier = 1

if sys.platform.startswith('win'):
    import ctypes

    # Fix the taskbar icon not loading on Windows
    if sys.argv[0].endswith('.exe') == False:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'retool.retool.retool.retool')

    # Fonts
    font = 'Segoe UI, Tahoma, Arial'

    # Get the scale factor
    if float(platform.release()) > 9:
        scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
        os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

        if scale_factor >= 1.5:
            os.environ['QT_SCALE_FACTOR'] = '0.8'
        elif scale_factor == 1.25 or scale_factor == 2.25:
            os.environ['QT_SCALE_FACTOR'] = '1'
            scale_multiplier = 1.3
    elif float(platform.release()) == 8.1:
            ctypes.windll.shcore.SetProcessDpiAwareness(0)

elif 'linux' in sys.platform:
    font = 'Ubuntu, DejVu Sans, FreeSans'
    scale_multiplier = 1.1

# Set defaults
sg.theme('SystemDefaultForReal')
sg.SetOptions(font=(font, 10))


def main():
    __version__ = '0.12'

    # Generate user config file if it's missing
    generate_config(region_data.languages_long, region_data.region_order, False, False, True)

    # Menu
    menu = [
        ['&File', ['&Check for clone list updates', '&Exit']],
        ['&Help', ['&Wiki', '&Github', '&About...']]]

    # Exclusions
    tab_exclusions = [
        [sg.Text('Title types to exclude from the output dat',
                 font=(font, 9, 'bold'),
                 pad=(30,30))],

        [sg.HorizontalSeparator()],

        generate_checkbox(['Add-ons', 'Educational'], 30*scale_multiplier, ['Exclude titles with the dat category "Add-Ons" -- these\ninclude expansion packs and additional materials for titles', 'Exclude titles with the dat category "Educational"']),
        generate_checkbox(['Applications', 'Manuals'], 30*scale_multiplier, ['Exclude titles with the dat category "Applications"\nor with the following text in the name:\n\n* (Program)\n* (Test Program)\n* Check Program\n* Sample Program', 'Exclude titles with the "(Manual)" in the name']),
        generate_checkbox(['Audio', 'Multimedia'], 30*scale_multiplier, ['Exclude titles with the dat category "Audio"\n-- these might be used as soundtracks by games', 'Exclude titles with the dat category "Multimedia"\n-- these might include games']),
        generate_checkbox(['Bad dumps', 'Pirate'], 30*scale_multiplier, ['Exclude titles with "[b]" in the name', 'Exclude titles with "(Pirate)" in the name']),
        generate_checkbox(['BIOS and other chips', 'Preproduction'], 30*scale_multiplier, ['Exclude titles with the dat category "Console"\nor with the following text in the name:\n\n* [BIOS]\n* (Enhancement Chip)', 'Exclude titles with the dat category "Preproduction" or with the\nfollowing text in the name:\n\n* (Alpha [0-99])\n* (Beta [0-99])\n* (Pre-Production)\n* (Possible Proto)\n* (Proto [0-99])\n* (Review Code)']),
        generate_checkbox(['Bonus discs', 'Promotional'], 30*scale_multiplier, ['Exclude titles with the dat category "Bonus Discs" -- these\ncould be anything other than the main title content,\nlike patches, manuals, collector discs, or otherwise', 'Exclude titles with the dat category "Promotional" or with the\nfollowing text in the name:\n\n* (Promo)\n* EPK\n* Press Kit']),
        generate_checkbox(['Coverdiscs', 'Unlicensed'], 30*scale_multiplier, ['Exclude titles with the dat category "Coverdiscs" -- these\nwere discs that were attached to the front of magazines', 'Exclude titles with "(Unl), (Aftermarket), or (Homebrew) in the name']),
        generate_checkbox(['Demos, kiosks, and samples', 'Video'], 30*scale_multiplier, ['Exclude titles with the dat category "Demos" or with the\nfollowing text in the name:\n\n* @barai\n* (Demo [1-9])\n* (Demo-CD)\n* (GameCube Preview\n* (Kiosk *|* Kiosk)\n* (Preview)\n* Kiosk Demo Disc\n* PS2 Kiosk\n* PSP System Kiosk\n* Sample\n* Taikenban\n* Trial Edition', 'Exclude titles with the dat category "Video"']),
    ]

    # Modes
    tab_modes = [
        [sg.Text('Modes to enable',
                 font=(font, 9, 'bold'),
                 pad=(30,30))],

        [sg.HorizontalSeparator()],

        generate_checkbox(['Include titles that don\'t have hashes, ROMs, or disks specified'], 50*scale_multiplier, ['Not recommended\n\nBy default, Retool removes these titles from the output dat']),
        generate_checkbox(['Don\'t replace Unl/Aftermarket/Homebrew titles if a production version is in another region'], 60*scale_multiplier, ['By default, Retool prefers production titles from lower regions over\n(Unl) and (Aftermarket) titles from higher regions']),
        generate_checkbox(['Titles ripped from modern platform rereleases replace standard editions'], 50*scale_multiplier, ['Not recommended\n\nThese titles are ripped from modern platforms like Virtual Console,\nand might not work with emulators']),
        generate_checkbox(['Output dat in legacy parent/clone format'], 50*scale_multiplier, ['Not recommended for use with dat managers\n\nUse for the following things:\n\n* CloneRel\n* Manually analyzing parent/clone relationships created by Retool\n* Diffing outputs in order to update clone lists']),
        generate_checkbox(['Disable custom global and system filters'], 50*scale_multiplier, ['User-defined strings that include or exclude\ntitles Retool ordinarily wouldn\'t']),
        generate_checkbox(['Also output lists of what titles have been kept and removed'], 50*scale_multiplier, ['In addition to the output dat, two text files will be\nproduced that detail the changes Retool has made,\nseparated by the types of changes']),
        generate_checkbox(['Also output a list of just the 1G1R title names'], 50*scale_multiplier, ['In addition to the output dat, generate a list with each\n1G1R title name taking a new line, and no extra formatting']),

        [sg.Text('')],

        [
            sg.Text('', size=(20,15)),
            sg.Text('Add this text to the start of each title (start with http://, https://, or ftp:// to URL encode each line)', key='prefix-label', visible=False)],

        [
            sg.Text('', size=(20,15)),
            sg.Input(enable_events=True, key='prefix-input', size=(300*scale_multiplier, 35*scale_multiplier), visible=False)],

        [sg.Text('')],

        [
            sg.Text('', size=(20,15)),
            sg.Text('Add this text to the end of each title', key='suffix-label', visible=False)],

        [
            sg.Text('', size=(20,15)),
            sg.Input(enable_events=True, key='suffix-input', size=(300*scale_multiplier, 35*scale_multiplier), visible=False)]
    ]

    # User filters
    tab_global_filters = [
        [sg.Text('Custom global filters (all dats)',
                 font=(font, 9, 'bold'),
                 pad=(30,30))],

        [sg.HorizontalSeparator()],

        [sg.Text('Exclude or include specific titles by adding your own text '
                 'strings to match against. Each string should\nbe on its own '
                 'line, and is case sensitive. See the wiki for more '
                 'information.\n'
                 '\n• Plain text indicates a partial string match.'
                 '\n• A prefix of / indicates a regular expression match.'
                 '\n• A prefix of | indicates a full string match.\n',
                 font=(font, 9),
                 pad=(30,30))],

        [
            sg.Text('Exclude'),
            sg.Text('Include')
        ],
        [
            sg.Multiline(key='global-filters-exclude', enable_events=True),
            sg.Multiline(key='global-filters-include', enable_events=True)
        ]
    ]

    tab_system_filters = [
        [sg.Text('Custom system filters',
                 key='custom-system-filters-heading',
                 font=(font, 9, 'bold'),
                 pad=(30,30))],

        [sg.HorizontalSeparator()],

        [sg.Text(
            'You must open a single dat file before you can set its custom system filters.',
            key='system-filters-text',
            font=(font, 9),
            pad=(30,30))],

        [
            sg.Text('Exclude', key='system-filters-label-exclude', visible=False),
            sg.Text('Include', key='system-filters-label-include', visible=False)
        ],
        [
            sg.Multiline(key='system-filters-exclude', enable_events=True, visible=False),
            sg.Multiline(key='system-filters-include', enable_events=True, visible=False)
        ]
    ]

    # Region selection
    tab_regions = [
        [sg.Text('Filter by regions (must add at least one)',
                 font=(font, 9, 'bold'))],

        [sg.HorizontalSeparator()],

        [
            sg.Text('Available regions'),
            sg.Text('Filter by these regions (order is important)')
        ],

        [
            sg.Listbox(
                enable_events=True,
                key='available-regions',
                select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
                size=(220*scale_multiplier,200*scale_multiplier),
                values=sorted(region_data.all)),

            sg.Column(
                layout=[
                    [sg.Button(
                        '»',
                        enable_events=True,
                        font=(f'Arial, Verdana', 10),
                        key='button-region-move-remainder-right',
                        size=(50,40),
                        tooltip='Add the remaining available regions to the\nend of the filtered list')],
                    [sg.Button(
                        '►',
                        enable_events=True,
                        font=(f'Arial, Verdana', 10),
                        key='button-region-move-right',
                        size=(50,40),
                        tooltip='Move the selected regions to the filtered list')],
                    [sg.Button(
                        '◄',
                        enable_events=True,
                        font=(f'Arial, Verdana', 10),
                        key='button-region-move-left',
                        size=(50,40),
                        tooltip='Move the selected regions to the available list')],
                    [sg.Button(
                        '«',
                        enable_events=True,
                        font=(f'Arial, Verdana', 10),
                        key='button-region-move-all-left',
                        size=(50,40),
                        tooltip='Move all regions to the available list')]
                ]
            ),

            sg.Listbox(
                values='',
                size=(220*scale_multiplier,200*scale_multiplier),
                key='filtered-regions',
                enable_events=True,
                select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED),

            sg.Column(
                layout=[
                [sg.Text('', font=('Arial, Verdana', 10), size=(50,20))],
                [sg.Button(
                    '▲',
                    enable_events=True,
                    font=(f'Arial, Verdana', 10),
                    key='button-region-move-up',
                    size=(50,40),
                    tooltip='Move the selected regions up the order')],
                [sg.Button(
                    '▼',
                    enable_events=True,
                    font=(f'Arial, Verdana', 10),
                    key='button-region-move-down',
                    size=(50,40),
                    tooltip='Move the selected regions down the order')]
                ]
            )
        ],

        [sg.Text('', font=('Arial, Verdana', 9), size=(30,15))],

        [
            sg.Button(
                'Use suggested region order for English speakers',
                enable_events=True,
                key='button-default-region-order',
                size=(350*scale_multiplier,45*scale_multiplier),
                target=(555666777,-1),
                tooltip='Set a region order that prioritizes English and 60Hz regions.\nAdd only English in the Languages tab to restrict the output to English titles.')
        ],

        [sg.Text('', font=('Arial, Verdana', 9), size=(30,55))],
    ]

    # Language selection
    tab_languages = [
        [sg.Text('Filter by language (leave filter list empty to include all languages)', font=(font, 9, 'bold'))],

        [sg.HorizontalSeparator()],

        [
            sg.Text('Available languages'),
            sg.Text('Filter by these languages (order doesn\'t matter)')
        ],

        [
            sg.Listbox(
                enable_events=True,
                key='available-languages',
                select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
                size=(220*scale_multiplier,200*scale_multiplier),
                values=sorted(region_data.languages_long)),
            sg.Column(
                layout=[
                    [sg.Button(
                        '»',
                        enable_events=True,
                        font=(f'Arial, Verdana', 10),
                        key='button-language-move-remainder-right',
                        size=(50,40),
                        tooltip='Add the remaining available languages to the\nend of the filtered list')],
                    [sg.Button(
                        '►',
                        enable_events=True,
                        font=(f'Arial, Verdana', 10),
                        key='button-language-move-right',
                        size=(50,40),
                        tooltip='Move the selected languages to the filtered list')],
                    [sg.Button(
                        '◄',
                        enable_events=True,
                        font=(f'Arial, Verdana', 10),
                        key='button-language-move-left',
                        size=(50,40),
                        tooltip='Move the selected regions to the available list')],
                    [sg.Button(
                        '«',
                        enable_events=True,
                        font=(f'Arial, Verdana', 10),
                        key='button-language-move-all-left',
                        size=(50,40),
                        tooltip='Move all regions to the available list')],
                ]),

            sg.Listbox(
                enable_events=True,
                key='filtered-languages',
                select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
                size=(220*scale_multiplier,200*scale_multiplier),
                values=''),

            sg.Column(
                layout=[
                    [sg.Text('', font=(f'Arial, Verdana', 10), size=(50,40))]
                ]),
        ],

        [sg.Text('', font=('Arial, Verdana', 9), size=(30,15))],

        [sg.Text('', size=(350*scale_multiplier,45*scale_multiplier))],

        [sg.Text('', font=('Arial, Verdana', 9), size=(30,55))],
    ]

    # The actual GUI layout
    layout = [
        [sg.Menu(menu, key='menu')],

        # File/folder selection
        [sg.Text('Select the dat/s to convert', font=(font, 9, 'bold'))],

        [
            sg.Input(visible=False, enable_events=True, key='button-single-dat'),
            sg.FileBrowse(
                'Choose single dat',
                file_types=(('Dat files', '*.dat'),('All files', '*.*')),
                initial_folder=None,
                size=(170*scale_multiplier,45*scale_multiplier),
                target=(555666777,-1)),
            sg.Input(visible=False, enable_events=True, key='button-folder-dat'),
            sg.FolderBrowse(
                'Choose folder of dats',
                initial_folder=None,
                size=(170*scale_multiplier,45*scale_multiplier),
                target=(555666777,-1)),
        ],

        [sg.Text('Nothing selected yet', size=(500*scale_multiplier,20*scale_multiplier), text_color='#777', key='filename', font=(f'{font}', 9))],

        [sg.Text('_'*125, text_color='#CCC')],

        [sg.Text('', font=(f'{font}', 6, 'bold'))],
        [sg.Text('Select an output folder', font=(font, 9, 'bold'))],

        [
            sg.Input(visible=False, enable_events=True, key='button-output-folder'),
            sg.FolderBrowse(
                'Choose output folder',
                initial_folder=None,
                size=(170*scale_multiplier,45*scale_multiplier),
                target=(555666777,-1))
        ],

        [sg.Text('Nothing selected yet', size=(500*scale_multiplier,20*scale_multiplier), text_color='#777', key='output-folder', font=(f'{font}', 9))],

        [sg.Text('', font=(f'{font}', 10, 'bold'))],

        # Tabs

        [
            sg.TabGroup(
                [
                    [
                        sg.Tab('Regions', tab_regions, background_color='white'),
                        sg.Tab('Languages', tab_languages, background_color='white'),
                        sg.Tab('Exclusions', tab_exclusions, background_color='white'),
                        sg.Tab('Modes', tab_modes, background_color='white'),
                        sg.Tab('Custom global filters', tab_global_filters, background_color='white'),
                        sg.Tab('Custom system filters', tab_system_filters, background_color='white')
                    ],
                ],
                key='tab-group'
            )
        ],

        [sg.Text('', font=(f'{font}', 6, 'bold'))],

        # CTAs
        [
            sg.Text('Your settings are saved automatically for future use', size=(500*scale_multiplier,30), text_color='#777'),
            sg.Button('Go!', size=(130*scale_multiplier,45*scale_multiplier), key='button-go', bind_return_key=True, tooltip='Process the input dat/s')]
        ]

    window = sg.Window('Retool - convert Redump and No-Intro dats to 1G1R!',
                       layout,
                       icon='retool.ico',
                       resizable=False,
                       finalize=True)

    # Customize styles
    checkbox_style = (
    'QCheckBox {font-size: 10pt;}'
    + 'QCheckBox::indicator {margin: 4px 4px 2px 0;}'
    + 'QCheckBox::indicator {width: 14px; height: 14px;}'
    + 'QCheckBox::indicator:unchecked {image: url(images/checkbox.svg);}'
    + 'QCheckBox::indicator:unchecked:hover {image: url(images/checkbox-hover.svg);}'
    + 'QCheckBox::indicator:unchecked:pressed {image: url(images/checkbox-pressed.svg);}'
    + 'QCheckBox::indicator:checked {image: url(images/checkbox-checked.svg);}'
    + 'QCheckBox::indicator:checked:hover {image: url(images/checkbox-checked-hover.svg);}'
    + 'QCheckBox::indicator:checked:pressed {image: url(images/checkbox-checked-pressed.svg);}'
    )

    tab_style = (
        f'QTabBar {{font-size: 9pt; font-family: {font}}}'
    )

    for key in window.AllKeysDict:
        if 'checkbox-' in key:
            window[key].QT_Checkbox.setStyleSheet(checkbox_style)
        if 'tab-group' in key:
            window[key].Widget.setStyleSheet(tab_style)


    input_file = ''
    output_folder = ''

    # Reset listboxes for predictable results
    window['filtered-regions'].update([])
    window['filtered-languages'].update([])

    # Import settings from user-config.yaml
    gui_settings = []
    settings = import_user_config(region_data, UserInput())

    if settings.user_config.data['language filter'] != '':
        window['filtered-languages'].update(sorted(settings.user_config.data['language filter']))
        window['available-languages'].update([language for language in getattr(window['available-languages'], 'Values') if language not in settings.user_config.data['language filter']])

    if settings.user_config.data['region order'] != '':
        window['filtered-regions'].update(settings.user_config.data['region order'])
        window['available-regions'].update([language for language in getattr(window['available-regions'], 'Values') if language not in settings.user_config.data['region order']])

    for setting in settings.user_config.data['gui settings']:
        if 'exclude' in str(setting):
            for key, value in dict(setting).items():
                if value != '':
                    if 'a' in value: window['checkbox-applications'].update(True)
                    if 'A' in value: window['checkbox-audio'].update(True)
                    if 'b' in value: window['checkbox-bad-dumps'].update(True)
                    if 'B' in value: window['checkbox-bios-and-other-chips'].update(True)
                    if 'c' in value: window['checkbox-coverdiscs'].update(True)
                    if 'd' in value: window['checkbox-demos-kiosks-and-samples'].update(True)
                    if 'D' in value: window['checkbox-add-ons'].update(True)
                    if 'e' in value: window['checkbox-educational'].update(True)
                    if 'm' in value: window['checkbox-manuals'].update(True)
                    if 'M' in value: window['checkbox-multimedia'].update(True)
                    if 'o' in value: window['checkbox-bonus-discs'].update(True)
                    if 'p' in value: window['checkbox-pirate'].update(True)
                    if 'P' in value: window['checkbox-preproduction'].update(True)
                    if 'r' in value: window['checkbox-promotional'].update(True)
                    if 'u' in value: window['checkbox-unlicensed'].update(True)
                    if 'v' in value: window['checkbox-video'].update(True)
        if 'output' in str(setting):
            window['button-output-folder'].update(os.path.abspath(dict(setting)['output']))
            window['output-folder'].update(os.path.abspath(dict(setting)['output']))
            output_folder = os.path.abspath(dict(setting)['output'])

    if 'emptytitles' in settings.user_config.data['gui settings']: window['checkbox-include-titles-that-dont-have-hashes-roms-or-disks-specified']
    if 'z' in settings.user_config.data['gui settings']: window['checkbox-titles-ripped-from-modern-platform-rereleases-replace-standard-editions'].update(True)
    if 'y' in settings.user_config.data['gui settings']: window['checkbox-dont-replace-unl-aftermarket-homebrew-titles-if-a-production-version-is-in-another-region'].update(True)
    if 'x' in settings.user_config.data['gui settings']: window['checkbox-output-dat-in-legacy-parent-clone-format'].update(True)
    if 'log' in settings.user_config.data['gui settings']: window['checkbox-also-output-lists-of-what-titles-have-been-kept-and-removed'].update(True)
    if 'list' in settings.user_config.data['gui settings']:
        window['checkbox-also-output-a-list-of-just-the-1g1r-title-names'].update(True)
        window['prefix-label'].update(visible=True)
        window['prefix-input'].update(visible=True)
        window['suffix-label'].update(visible=True)
        window['suffix-input'].update(visible=True)
    if 'nofilters' in settings.user_config.data['gui settings']: window['checkbox-disable-custom-global-and-system-filters'].update(True)

    # Import list prefix and suffixes
    if settings.user_config.data['list prefix'] != '':
        window['prefix-input'].update(settings.user_config.data['list prefix'][0])

    if settings.user_config.data['list suffix'] != '':
        window['suffix-input'].update(settings.user_config.data['list suffix'][0])

    # Import settings from user-filters/global.yaml
    user_filters = import_user_filters('global', 'global')

    window['global-filters-exclude'].update('\n'.join(user_filters.data['exclude']))
    window['global-filters-include'].update('\n'.join(user_filters.data['include']))

    # Check for clone lists
    if os.path.exists('./clonelists'):
        if len(os.listdir('./clonelists')) == 0:
            gate(
                window,
                'Update clone lists?',
                'You don\'t have any clone lists. Clone lists help Retool to match\ntitles with different names in different regions.\n\nDownload them now?','Download','No thanks')
    else:
        gate(
                window,
                'Update clone lists?',
                'You don\'t have any clone lists. Clone lists help Retool to match\ntitles with different names in different regions.\n\nDownload them now?','Download','No thanks')


    # Instantiate filters and other things
    filters = Filters()

    # The main loop
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Check for clone list updates':
            updateclonelists.main()

        if event =='Wiki':
            webbrowser.open('https://github.com/unexpectedpanda/retool/wiki', new=2)

        if event =='Github':
            webbrowser.open('https://github.com/unexpectedpanda/retool/', new=2)

        if event == 'About...':
            retool_version = retool.retool_version()
            gate(
                window,
                'Retool GUI',
                f'Retool converts Redump and No-Intro dats to 1G1R.\n\nVersions:\n\n • Retool GUI:\t{__version__}\n • Retool CLI:\t{retool_version}')

        if event == 'button-go':
            # Make sure the required settings are available
            error_list = []

            if input_file == '':
                error_list.append('Choose a dat file or folder of dats')
            if output_folder == '':
                error_list.append('Choose an output folder')
            if getattr(window['filtered-regions'], 'Values') == []:
                error_list.append('Choose at least one region to filter by')

            error_list_string = '\n  • '.join(error_list)

            if error_list != []:
                gate(window, 'Missing details required', f'You must do the following before you can process a dat: \n\n  • {error_list_string}')
            else:
                if getattr(window['filtered-languages'], 'Values') != []:
                    filter_by_languages = True
                else:
                    filter_by_languages = False

                if gui_settings == []:
                    gui_output_settings = ''
                else:
                    hidden_options = ['Input', 'g', 'l', 'output', 'q', 'errors', 'log', 'nofilters', 'list']
                    gui_output_settings = [setting for setting in gui_settings if ('output' not in setting and 'exclude' not in setting)]

                    exclude_settings = [setting for setting in gui_settings if 'exclude' in setting]
                    exclude_settings = str(exclude_settings).replace('exclude: ','')

                    if exclude_settings != '':
                        gui_output_settings.append(exclude_settings.replace('[','').replace(']','').replace('\'',''))

                    gui_output_settings = f' (-{"".join(sorted([setting for setting in gui_output_settings if setting not in hidden_options], key=str.casefold))})'

                gui_input = UserInput(
                    input_file,
                    output_folder,
                    values['checkbox-applications'],
                    values['checkbox-audio'],
                    values['checkbox-bad-dumps'],
                    values['checkbox-bios-and-other-chips'],
                    values['checkbox-coverdiscs'],
                    values['checkbox-demos-kiosks-and-samples'],
                    values['checkbox-add-ons'],
                    values['checkbox-educational'],
                    values['checkbox-manuals'],
                    values['checkbox-multimedia'],
                    values['checkbox-bonus-discs'],
                    values['checkbox-pirate'],
                    values['checkbox-preproduction'],
                    values['checkbox-promotional'],
                    values['checkbox-unlicensed'],
                    values['checkbox-video'],
                    values['checkbox-titles-ripped-from-modern-platform-rereleases-replace-standard-editions'],
                    values['checkbox-dont-replace-unl-aftermarket-homebrew-titles-if-a-production-version-is-in-another-region'],
                    filter_by_languages, # languages
                    values['checkbox-output-dat-in-legacy-parent-clone-format'],
                    gui_output_settings, # user options
                    False,
                    values['checkbox-disable-custom-global-and-system-filters'],
                    values['checkbox-also-output-lists-of-what-titles-have-been-kept-and-removed'],
                    values['checkbox-also-output-a-list-of-just-the-1g1r-title-names'],
                    values['checkbox-include-titles-that-dont-have-hashes-roms-or-disks-specified'],
                    False)
                retool.main(gui_input)

        if event == 'checkbox-also-output-a-list-of-just-the-1g1r-title-names':
            if values['checkbox-also-output-a-list-of-just-the-1g1r-title-names'] == True:
                window['prefix-label'].update(visible=True)
                window['prefix-input'].update(visible=True)
                window['suffix-label'].update(visible=True)
                window['suffix-input'].update(visible=True)
            else:
                window['prefix-label'].update(visible=False)
                window['prefix-input'].update(visible=False)
                window['suffix-label'].update(visible=False)
                window['suffix-input'].update(visible=False)

        if event == 'button-single-dat':
            if values['button-single-dat'] != '':
                window['filename'].update(os.path.basename(values['button-single-dat']))
                input_file = values['button-single-dat']

                # Get the dat name
                dat_read = process_input_dat(input_file, False, True)

                if 'PlayStation Portable' in dat_read.name:
                    if 'no-intro' in dat_read.url:
                        filters.system_file = 'Sony - PlayStation Portable (No-Intro)'
                    elif 'redump' in dat_read.url:
                        filters.system_file = 'Sony - PlayStation Portable (Redump)'
                else:
                    filters.system_file = dat_read.name

                # Clear the custom system filters
                window['system-filters-exclude'].update('')
                window['system-filters-include'].update('')

                # Import settings from user-filters/dat-name.yaml if it exists
                if os.path.isfile(f'user-filters/{filters.system_file}.yaml'):
                    custom_system_filters = import_user_filters(filters.system_file, 'system')
                    window['system-filters-exclude'].update('\n'.join(custom_system_filters.data['exclude']))
                    window['system-filters-include'].update('\n'.join(custom_system_filters.data['include']))

                # Show the custom system filters
                system_filters_text = (
                    'Exclude or include specific titles by adding your own text '
                    'strings to match against. Each string should\nbe on its own '
                    'line, and is case sensitive. See the wiki for more '
                    'information.\n'
                    '\n• Plain text indicates a partial string match.'
                    '\n• A prefix of / indicates a regular expression match.'
                    '\n• A prefix of | indicates a full string match.\n'
                )
                window['custom-system-filters-heading'].update(f'Custom system filters ({filters.system_file})')
                window['system-filters-text'].update(system_filters_text)
                window['system-filters-label-exclude'].update(visible=True)
                window['system-filters-label-include'].update(visible=True)
                window['system-filters-exclude'].update(visible=True)
                window['system-filters-include'].update(visible=True)


        if event == 'button-folder-dat':
            if values['button-folder-dat'] != '':
                window['filename'].update(os.path.abspath(values['button-folder-dat']))
                input_file = values['button-folder-dat']

        if event == 'button-output-folder':
            if values['button-output-folder'] != '':
                window['output-folder'].update(os.path.abspath(values['button-output-folder']))
                output_folder = values['button-output-folder']

        if event == 'button-region-move-right':
            move_listbox_item_right(window, 'available-regions', 'filtered-regions', values)

        if event == 'button-region-move-left':
            move_listbox_item_left(window, 'available-regions', 'filtered-regions', values)

        if event == 'button-region-move-remainder-right':
            move_listbox_remainder_right(window, 'available-regions', 'filtered-regions')

        if event == 'button-region-move-all-left':
            move_listbox_all_left(window, 'available-regions', 'filtered-regions')

        if event == 'button-region-move-up' or event == 'button-region-move-down':
            # Get the values from the filtered regions listbox
            if type(getattr(window['filtered-regions'], 'Values')) is not str:
                filtered_region_list = getattr(window['filtered-regions'], 'Values')
            else:
                filtered_region_list = []

            #  Get the indexes of everything selected, and figure out the items required
            #  to calculate the move
            if filtered_region_list != []:
                all_regions = getattr(window['filtered-regions'], 'Values')
                selected_regions = values['filtered-regions']
                selected_indexes = []

                for i, value in enumerate(all_regions):
                    if value in values['filtered-regions']:
                        selected_indexes.append(i)

                if selected_indexes != []:
                    filtered_regions_remainder = [region for region in all_regions if region not in selected_regions]

                    # Shuffle the items up or down
                    if event == 'button-region-move-up':
                        if selected_indexes[0] <= 1:
                            all_regions = selected_regions + filtered_regions_remainder
                        else:
                            all_regions = filtered_regions_remainder[:selected_indexes[0] - 1] + selected_regions + filtered_regions_remainder[selected_indexes[0]-1:]

                        # Change the position of the list box when moving items
                        window['filtered-regions'].update(all_regions)
                        window['filtered-regions'].set_value(selected_regions)
                        window['filtered-regions'].Widget.scrollToItem(window['filtered-regions'].Widget.item(selected_indexes[0] - 2))

                    if event == 'button-region-move-down':
                        if selected_indexes[-1] >= len(all_regions) - 2:
                            all_regions = filtered_regions_remainder + selected_regions
                        else:
                            all_regions = (
                                filtered_regions_remainder[:-len(all_regions[selected_indexes[-1] + 2:])]
                                + selected_regions
                                + all_regions[selected_indexes[-1] + 2:]
                            )

                        # Change the position of the list box when moving items
                        window['filtered-regions'].update(all_regions)
                        window['filtered-regions'].set_value(selected_regions)
                        window['filtered-regions'].Widget.scrollToItem(window['filtered-regions'].Widget.item(selected_indexes[-1] + 2))

        if event == 'button-default-region-order':
            window['available-regions'].update([])
            window['filtered-regions'].update(region_data.region_order)

        if event == 'button-language-move-right':
            move_listbox_item_right(window, 'available-languages', 'filtered-languages', values, True)

        if event == 'button-language-move-left':
            move_listbox_item_left(window, 'available-languages', 'filtered-languages', values)

        if event == 'button-language-move-remainder-right':
            move_listbox_remainder_right(window, 'available-languages', 'filtered-languages', True)

        if event == 'button-language-move-all-left':
            move_listbox_all_left(window, 'available-languages', 'filtered-languages')

        #  Write settings any time the user interacts with the appropriate widgets
        if event:
            gui_settings = []
            excludes = []

            if values['checkbox-applications'] == True:
                excludes.append('a')
            if values['checkbox-audio'] == True:
                excludes.append('A')
            if values['checkbox-bad-dumps'] == True:
                excludes.append('b')
            if values['checkbox-bios-and-other-chips'] == True:
                excludes.append('B')
            if values['checkbox-coverdiscs'] == True:
                excludes.append('c')
            if values['checkbox-demos-kiosks-and-samples'] == True:
                excludes.append('d')
            if values['checkbox-add-ons'] == True:
                excludes.append('D')
            if values['checkbox-educational'] == True:
                excludes.append('e')
            if values['checkbox-manuals'] == True:
                excludes.append('m')
            if values['checkbox-multimedia'] == True:
                excludes.append('M')
            if values['checkbox-bonus-discs'] == True:
                excludes.append('o')
            if values['checkbox-pirate'] == True:
                excludes.append('p')
            if values['checkbox-preproduction'] == True:
                excludes.append('P')
            if values['checkbox-promotional'] == True:
                excludes.append('r')
            if values['checkbox-unlicensed'] == True:
                excludes.append('u')
            if values['checkbox-video'] == True:
                excludes.append('v')
            if values['checkbox-include-titles-that-dont-have-hashes-roms-or-disks-specified'] == True:
                gui_settings.append('emptytitles')
            if values['checkbox-titles-ripped-from-modern-platform-rereleases-replace-standard-editions'] == True:
                gui_settings.append('z')
            if values['checkbox-dont-replace-unl-aftermarket-homebrew-titles-if-a-production-version-is-in-another-region'] == True:
                gui_settings.append('y')
            if values['checkbox-output-dat-in-legacy-parent-clone-format'] == True:
                gui_settings.append('x')
            if values['checkbox-also-output-lists-of-what-titles-have-been-kept-and-removed'] == True:
                gui_settings.append('log')
            if values['checkbox-also-output-a-list-of-just-the-1g1r-title-names'] == True:
                gui_settings.append('list')
            if values['checkbox-disable-custom-global-and-system-filters'] == True:
                gui_settings.append('nofilters')
            if values['button-output-folder'] != '':
                gui_settings.append(f'output: {os.path.abspath(values["button-output-folder"])}')

            gui_settings.append(f'exclude: {"".join(excludes)}')

            if values['global-filters-exclude'] != '':
                filters.global_exclude = []
                for filter_text in values['global-filters-exclude'].splitlines():
                    if filter_text != '': filters.global_exclude.append(filter_text.replace('\\', '\\\\').replace('"', '\\"'))
            if values['global-filters-include'] != '':
                filters.global_include = []
                for filter_text in values['global-filters-include'].splitlines():
                    if filter_text != '': filters.global_include.append(filter_text.replace('\\', '\\\\').replace('"', '\\"'))
            if values['system-filters-exclude'] != '':
                filters.system_exclude = []
                for filter_text in values['system-filters-exclude'].splitlines():
                    if filter_text != '': filters.system_exclude.append(filter_text.replace('\\', '\\\\').replace('"', '\\"'))
            if values['system-filters-include'] != '':
                filters.system_include = []
                for filter_text in values['system-filters-include'].splitlines():
                    if filter_text != '': filters.system_include.append(filter_text.replace('\\', '\\\\').replace('"', '\\"'))

            if values['prefix-input'] != '':
                list_prefix = values['prefix-input'].replace('\\', '\\\\').replace('"', '\\"')
            else:
                list_prefix = False

            if values['suffix-input'] != '':
                list_suffix = values['suffix-input'].replace('\\', '\\\\').replace('"', '\\"')
            else:
                list_suffix = False

            # Write the user-config.yaml file
            region_settings = getattr(window['filtered-regions'], 'Values').copy()

            for region in getattr(window['available-regions'], 'Values'):
                region_settings.append(f'True|{region}')

            if getattr(window['filtered-languages'], 'Values') != []:
                language_settings = getattr(window['filtered-languages'], 'Values').copy()
            else:
                language_settings = []

            for language in getattr(window['available-languages'], 'Values'):
                language_settings.append(f'True|{language}')

            if values['global-filters-exclude'] == '': filters.global_exclude = []
            if values['global-filters-include'] == '': filters.global_include = []
            if values['system-filters-exclude'] == '': filters.system_exclude = []
            if values['system-filters-include'] == '': filters.system_include = []

            generate_config(language_settings, region_settings, list_prefix, list_suffix, True, filters, gui_settings, True)

    window.close()


def move_listbox_item_right(window, left_key, right_key, values, sort=False):
    # Get the values that should remain in the left listbox
    left_listbox = [item for item in getattr(window[left_key], 'Values') if item not in values[left_key]]

    # Get the values in the right listbox, and add the new items
    if type(getattr(window[right_key], 'Values')) is not str:
        right_listbox = getattr(window[right_key], 'Values')
    else:
        right_listbox = []

    window[left_key].update(left_listbox)

    if sort == False:
        window[right_key].update(right_listbox + values[left_key])
    else:
        window[right_key].update(sorted(right_listbox + values[left_key]))


def move_listbox_item_left(window, left_key, right_key, values):
    # Get the values that should remain in the right listbox
    right_listbox = [item for item in getattr(window[right_key], 'Values') if item not in values[right_key]]

    # Get the values in the left listbox, and add the new items
    if type(getattr(window[left_key], 'Values')) is not str:
        left_listbox = getattr(window[left_key], 'Values')
    else:
        left_listbox = []

    window[right_key].update(right_listbox)
    window[left_key].update(sorted(left_listbox + values[right_key]))


def move_listbox_remainder_right(window, left_key, right_key, sort=False):
    # Get the values in the right listbox, and add the remaining items from the left listbox
    if type(getattr(window[right_key], 'Values')) is not str:
        right_listbox = getattr(window[right_key], 'Values')
    else:
        right_listbox = []

    if sort == False:
        window[right_key].update(right_listbox + getattr(window[left_key], 'Values'))
    else:
        window[right_key].update(sorted(right_listbox + getattr(window[left_key], 'Values')))

    window[left_key].update([])


def move_listbox_all_left(window, left_key, right_key):
    # Get the values in the right listbox, and move them all to the left listbox
    if type(getattr(window[right_key], 'Values')) is not str:
        right_listbox = getattr(window[right_key], 'Values')
    else:
        right_listbox = []

    window[left_key].update(sorted(right_listbox + getattr(window[left_key], 'Values')))
    window[right_key].update([])


def generate_checkbox(labels, width, tips=None):
        checkboxes = []
        single_quote = '\''

        for i, label in enumerate(labels):
            if tips == None:
                checkboxes.append(sg.Checkbox(
                    enable_events=True,
                    key=f'checkbox-{label.lower().replace(" ", "-").replace("/", "-").replace(",","").replace(single_quote,"").replace("(","").replace(")","")}',
                    font=(font, 9),
                    pad=(0,0),
                    size=(width,0.6),
                    text=label))
            else:
                checkboxes.append(sg.Checkbox(
                    enable_events=True,
                    key=f'checkbox-{label.lower().replace(" ", "-").replace("/", "-").replace(",","").replace(single_quote,"").replace("(","").replace(")","")}',
                    font=(font, 9),
                    pad=(0,0),
                    size=(width,0.6),
                    text=label,
                    tooltip=tips[i]))

        return checkboxes


def gate(window, notification_title, notification_message, button_name='Got it', secondary_button_name=False):

    if secondary_button_name == False:
        dialog_layout = [
            [sg.Text('', font=(f'{font}', 6, 'bold'))],
            [sg.Text(notification_message)],
            [sg.Text('', font=(f'{font}', 10, 'bold'))],
            [sg.Button(button_name,
                bind_return_key=True,
                enable_events=True,
                key='button-no-file-got-it',
                size=(100,50))]]
    else:
        dialog_layout = [
            [sg.Text('', font=(f'{font}', 6, 'bold'))],
            [sg.Text(notification_message)],
            [sg.Text('', font=(f'{font}', 10, 'bold'))],
            [
                sg.Button(button_name,
                    bind_return_key=True,
                    enable_events=True,
                    key='button-download',
                    size=(100,50)),
                sg.Button(secondary_button_name,
                    bind_return_key=True,
                    enable_events=True,
                    key='button-no-file-got-it',
                    size=(100,50))]
            ]

    no_file_window = sg.Window(
        notification_title,
        layout= dialog_layout,
        background_color='#aaa',
        icon='retool.ico',
        keep_on_top=True,
        no_titlebar=True,
        resizable=False,
        size=(200,100),
        finalize=True)

    window.Disable()

    while True:
        popup_event, popup_values = no_file_window.read()

        if popup_event in (sg.WIN_CLOSED, 'Exit'):
            window.Enable()
            no_file_window.close()
            break

        if popup_event == 'button-no-file-got-it':
            window.Enable()
            no_file_window.close()
            break

        if popup_event == 'button-download':
            window.Enable()
            no_file_window.close()
            updateclonelists.main()
            break

if __name__ == '__main__':
    main()