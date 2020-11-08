#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" retool-gui.py: GUI version of Retool for Windows.

https://github.com/unexpectedpanda/retool
"""


import os
import PySimpleGUIQt as sg
import retool
import updateclonelists
import webbrowser

from datetime import datetime
from typing import OrderedDict
from urllib.error import HTTPError, URLError

from modules.classes import RegionKeys, UserInput
from modules.importdata import build_regions
from modules.output import generate_config
from modules.userinput import import_user_config

# Generate regions and languages from internal-config.json
region_data = build_regions(RegionKeys())

sg.theme('SystemDefaultForReal')

sg.SetOptions(font=('Segoe UI', 10))


def main():
    __version__ = 0.03

    # Generate user config file if it's missing
    generate_config(region_data.languages_long, region_data.region_order, [], False, True)

    # Menu
    menu = [
        ['&File', ['&Check for clone list updates', '&Exit']],
        ['&Help', ['&Wiki', '&Github', '&About...']]]

    # Exclusions
    tab_exclusions = [
        [sg.Text('Title types to exclude from the output dat',
                 font=('Segoe UI', 9, 'bold'),
                 pad=(30,30))],

        [sg.HorizontalSeparator()],

        generate_checkbox(['Applications', 'Multimedia'], 30, ['Exclude titles with the dat category "Applications"\nor with "(Program)" in the name', 'Exclude titles with the dat category "Multimedia"\n-- these might include games']),
        generate_checkbox(['Audio', 'Pirate'], 30, ['Exclude titles with the dat category "Audio"\n-- these might be used in games as soundtracks', 'Exclude titles with "(Pirate)" in the name']),
        generate_checkbox(['Bad dumps', 'Preproduction'], 30, ['Exclude titles with "[b]" in the name', 'Exclude titles with the dat category "Preproduction" or with the\nfollowing text in the name:\n\n* (Alpha [0-99])\n* (Beta [0-99])\n* (Pre-Production)\n* (Proto [0-99])\n* (Review Code)']),
        generate_checkbox(['Compilations with no unique titles', 'Promotional'], 30, ['Exclude compilations where the titles already\nexist in the dat as single titles', 'Exclude titles with the dat category "Promotional" or with the\nfollowing text in the name:\n\n* (Promo)\n* EPK\n* Press Kit']),
        generate_checkbox(['Coverdiscs', 'Unlicensed'], 30, ['Exclude titles with the dat category "Coverdiscs" -- these\nare discs that were included on the front of magazines', 'Exclude titles with "(Unl)" in the name']),
        generate_checkbox(['Demos and samples', 'Video'], 30, ['Exclude titles with the dat category "Demos" or with the\nfollowing text in the name:\n\n* @barai\n* (Demo [1-9])\n* (Demo-CD)\n* (GameCube Preview)\n* (Preview)\n* Sample\n* Taikenban\n* Trial Edition', 'Exclude titles with the dat category "Video"']),
        generate_checkbox(['Educational'], 30, ['Exclude titles with the dat category "Educational"']),
    ]

    # Modes
    tab_modes = [
        [sg.Text('Modes to enable',
                 font=('Segoe UI', 9, 'bold'),
                 pad=(30,30))],

        [sg.HorizontalSeparator()],

        generate_checkbox(['Supersets replace standard editions'], 30, ['Special editions, game of the year editions, and collections\nreplace standard editions (if left unchecked, all editions\nare included in the output dat)']),
        generate_checkbox(['Export dat in legacy parent/clone format'], 30, ['Use for the following things:\n\n* CloneRel\n* Manually analyzing parent/clone relationships created by Retool\n* Diffing outputs in order to update clone lists\n\nNot recommended for use with dat managers']),
    ]

    # Region selection
    tab_regions = [
        [sg.Text('Filter by regions (must add at least one)',
                 font=('Segoe UI', 9, 'bold'))],

        [sg.HorizontalSeparator()],

        [
            sg.Text('Available regions'),
            sg.Text('Filter by these regions (order is important)')
        ],

        [sg.Listbox(
            enable_events=True,
            key='available-regions',
            select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
            size=(220,200),
            values=sorted(region_data.all)),

            sg.Column(
                layout=[
                    [sg.Button(
                        '»',
                        enable_events=True,
                        font=('any', 10),
                        key='button-region-move-remainder-right',
                        size=(50,40),
                        tooltip='Add the remaining available regions to the\nend of the filtered list')],
                    [sg.Button(
                        '►',
                        enable_events=True,
                        font=('any', 10),
                        key='button-region-move-right',
                        size=(50,40),
                        tooltip='Move the selected regions to the filtered list')],
                    [sg.Button(
                        '◄',
                        enable_events=True,
                        font=('any', 10),
                        key='button-region-move-left',
                        size=(50,40),
                        tooltip='Move the selected regions to the available list')],
                    [sg.Button(
                        '«',
                        enable_events=True,
                        font=('any', 10),
                        key='button-region-move-all-left',
                        size=(50,40),
                        tooltip='Move all regions to the available list')]
                ]
            ),

            sg.Listbox(
                values='',
                size=(220,200),
                key='filtered-regions',
                enable_events=True,
                select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED),

            sg.Column(
                layout=[
                [sg.Button(
                    '▲',
                    enable_events=True,
                    font=('any', 10),
                    key='button-region-move-up',
                    size=(50,40),
                    tooltip='Move the selected regions up the order')],
                [sg.Button(
                    '▼',
                    enable_events=True,
                    font=('any', 10),
                    key='button-region-move-down',
                    size=(50,40),
                    tooltip='Move the selected regions down the order')]
                ]
            )
        ],

        [sg.Text('', size=(30,15))],

        [
            sg.Button(
                'Use suggested region order for English speakers',
                enable_events=True,
                key='button-default-region-order',
                size=(320,40),
                target=(555666777,-1),
                tooltip='Set a region order that prioritizes English and 60Hz regions.\nAdd only English in the Languages tab to restrict the output to English titles.')
            ],

        [sg.Column(
                layout=[
                    [sg.Text('', size=(30,15))]
                ])]
    ]

    # Language selection
    tab_languages = [
        [sg.Text('Filter by language (leave filter list empty to include all languages)', font=('Segoe UI', 9, 'bold'))],

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
                size=(220,200),
                values=sorted(region_data.languages_long)),
            sg.Column(
                layout=[
                    [sg.Button(
                        '»',
                        enable_events=True,
                        font=('any', 10),
                        key='button-language-move-remainder-right',
                        size=(50,40),
                        tooltip='Add the remaining available languages to the\nend of the filtered list')],
                    [sg.Button(
                        '►',
                        enable_events=True,
                        font=('any', 10),
                        key='button-language-move-right',
                        size=(50,40),
                        tooltip='Move the selected languages to the filtered list')],
                    [sg.Button(
                        '◄',
                        enable_events=True,
                        font=('any', 10),
                        key='button-language-move-left',
                        size=(50,40),
                        tooltip='Move the selected regions to the available list')],
                    [sg.Button(
                        '«',
                        enable_events=True,
                        font=('any', 10),
                        key='button-language-move-all-left',
                        size=(50,40),
                        tooltip='Move all regions to the available list')],
                ]),
            sg.Listbox(
                enable_events=True,
                key='filtered-languages',
                select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
                size=(220,200),
                values=''),
            sg.Column(
                layout=[
                    # Empty so the QT layout behaves better
                ]),
        ],

        [sg.Column(
                layout=[
                    [sg.Text('', size=(30,75))]
                ])]
    ]

    # The actual GUI layout
    layout = [
        [sg.Menu(menu, key='menu')],

        # File/folder selection
        [sg.Text('Select the dat/s to convert', font=('Segoe UI', 9, 'bold'))],

        [
            sg.Input(visible=False, enable_events=True, key='button-single-dat'),
            sg.FileBrowse(
                'Choose single dat',
                file_types=(('Dat files', '*.dat'),('All files', '*.*')),
                initial_folder=None,
                size=(170,45),
                target=(555666777,-1)),
            sg.Input(visible=False, enable_events=True, key='button-folder-dat'),
            sg.FolderBrowse(
                'Choose folder of dats',
                initial_folder=None,
                size=(170,45),
                target=(555666777,-1)),
        ],

        [sg.Text('Nothing selected yet', size=(600,20), text_color='#777', key='filename')],

        [sg.Text('_'*125, text_color='#CCC')],

        [sg.Text('', font=('any', 6, 'bold'))],
        [sg.Text('Select an output folder', font=('Segoe UI', 9, 'bold'))],

        [
            sg.Input(visible=False, enable_events=True, key='button-output-folder'),
            sg.FolderBrowse(
                'Choose output folder',
                initial_folder=None,
                size=(170,45),
                target=(555666777,-1))
        ],

        [sg.Text('Nothing selected yet', size=(600,20), text_color='#777', key='output-folder')],

        [sg.Text('', font=('any', 10, 'bold'))],

        # Tabs

        [
            sg.TabGroup(
                [
                    [
                        sg.Tab('Regions', tab_regions, background_color='white'),
                        sg.Tab('Languages', tab_languages, background_color='white'),
                        sg.Tab('Exclusions', tab_exclusions, background_color='white'),
                        sg.Tab('Modes', tab_modes, background_color='white')
                    ]
                ]
            )
        ],

        [sg.Text('', font=('any', 6, 'bold'))],

        # CTAs
        [
            sg.Text('Your settings are saved automatically for future use', size=(500,30), text_color='#777'),
            sg.Button('Go!', size=(130,45), key='button-go', bind_return_key=True, tooltip='Process the input dat/s')]
        ]

    window = sg.Window('Retool - convert Redump and No-Intro dats to 1G1R!',
                       layout,
                       icon='retool.ico',
                       resizable=False,
                       finalize=True)

    # Event loop
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

    if 'a' in settings.user_config.data['gui settings']: window['checkbox-applications'].update(True)
    if 'b' in settings.user_config.data['gui settings']: window['checkbox-bad-dumps'].update(True)
    if 'c' in settings.user_config.data['gui settings']: window['checkbox-compilations-with-no-unique-titles'].update(True)
    if 'd' in settings.user_config.data['gui settings']: window['checkbox-demos-and-samples'].update(True)
    if 'e' in settings.user_config.data['gui settings']: window['checkbox-educational'].update(True)
    if 'f' in settings.user_config.data['gui settings']: window['checkbox-coverdiscs'].update(True)
    if 'i' in settings.user_config.data['gui settings']: window['checkbox-audio'].update(True)
    if 'j' in settings.user_config.data['gui settings']: window['checkbox-video'].update(True)
    if 'm' in settings.user_config.data['gui settings']: window['checkbox-multimedia'].update(True)
    if 'n' in settings.user_config.data['gui settings']: window['checkbox-pirate'].update(True)
    if 'p' in settings.user_config.data['gui settings']: window['checkbox-preproduction'].update(True)
    if 'r' in settings.user_config.data['gui settings']: window['checkbox-promotional'].update(True)
    if 'u' in settings.user_config.data['gui settings']: window['checkbox-unlicensed'].update(True)
    if 's' in settings.user_config.data['gui settings']: window['checkbox-supersets-replace-standard-editions'].update(True)
    if 'x' in settings.user_config.data['gui settings']: window['checkbox-export-dat-in-legacy-parent-clone-format'].update(True)

    for setting in settings.user_config.data['gui settings']:
        if isinstance (setting, OrderedDict):
            window['button-output-folder'].update(os.path.abspath(dict(setting)['output']))

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

            error_list_string = "\n  • ".join(error_list)

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
                    gui_output_settings = f' (-{"".join(sorted([setting for setting in gui_settings if "output" not in setting]))})'

                gui_input = UserInput(
                    input_file,
                    output_folder,
                    values['checkbox-applications'],
                    values['checkbox-bad-dumps'],
                    values['checkbox-compilations-with-no-unique-titles'],
                    values['checkbox-demos-and-samples'],
                    values['checkbox-educational'],
                    values['checkbox-coverdiscs'],
                    values['checkbox-audio'],
                    values['checkbox-video'],
                    values['checkbox-multimedia'],
                    values['checkbox-pirate'],
                    values['checkbox-preproduction'],
                    values['checkbox-promotional'],
                    values['checkbox-unlicensed'],
                    values['checkbox-supersets-replace-standard-editions'],
                    filter_by_languages, # languages
                    values['checkbox-export-dat-in-legacy-parent-clone-format'],
                    gui_output_settings, # user options
                    False,
                    False)
                retool.main(gui_input)

        if event == 'button-single-dat':
            if values['button-single-dat'] != '':
                window['filename'].update(os.path.basename(values['button-single-dat']))
                input_file = values['button-single-dat']

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

            if values['checkbox-applications'] == True:
                gui_settings.append('a')
            if values['checkbox-bad-dumps'] == True:
                gui_settings.append('b')
            if values['checkbox-compilations-with-no-unique-titles'] == True:
                gui_settings.append('c')
            if values['checkbox-demos-and-samples'] == True:
                gui_settings.append('d')
            if values['checkbox-educational'] == True:
                gui_settings.append('e')
            if values['checkbox-coverdiscs'] == True:
                gui_settings.append('f')
            if values['checkbox-audio'] == True:
                gui_settings.append('i')
            if values['checkbox-video'] == True:
                gui_settings.append('j')
            if values['checkbox-multimedia'] == True:
                gui_settings.append('m')
            if values['checkbox-pirate'] == True:
                gui_settings.append('n')
            if values['checkbox-preproduction'] == True:
                gui_settings.append('p')
            if values['checkbox-promotional'] == True:
                gui_settings.append('r')
            if values['checkbox-unlicensed'] == True:
                gui_settings.append('u')
            if values['checkbox-supersets-replace-standard-editions'] == True:
                gui_settings.append('s')
            if values['checkbox-export-dat-in-legacy-parent-clone-format'] == True:
                gui_settings.append('x')
            if values['button-output-folder'] != '':
                gui_settings.append(f'output: {os.path.abspath(values["button-output-folder"])}')

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

            generate_config(language_settings, region_settings, gui_settings, True)

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

        for i, label in enumerate(labels):
            if tips == None:
                checkboxes.append(sg.Checkbox(
                    enable_events=True,
                    key=f'checkbox-{label.lower().replace(" ", "-").replace("/", "-")}',
                    pad=(0,0),
                    size=(width,0.6),
                    text=label))
            else:
                checkboxes.append(sg.Checkbox(
                    enable_events=True,
                    key=f'checkbox-{label.lower().replace(" ", "-").replace("/", "-")}',
                    pad=(0,0),
                    size=(width,0.6),
                    text=label,
                    tooltip=tips[i]))

        return checkboxes


def gate(window, notification_title, notification_message):
    no_file_window = sg.Window(
        notification_title,
        layout=[
            [sg.Text('', font=('any', 6, 'bold'))],
            [sg.Text(notification_message)],
            [sg.Text('', font=('any', 10, 'bold'))],
            [sg.Button('Got it',
                bind_return_key=True,
                enable_events=True,
                key='button-no-file-got-it',
                size=(100,50))],
        ],
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

if __name__ == '__main__':
    main()