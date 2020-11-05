import html
import os
import re
import sys

from modules.classes import Stats
from modules.utils import Font, natural_keys, printwrap
from modules.xml import header


def generate_config(languages, regions, gui_settings=False, overwrite=False, gui=False):
    if not os.path.isfile('user-config.yaml') or overwrite == True:
        try:
            with open('user-config.yaml', 'w') as output_file:
                output_file.writelines('---\n# If the -l option is used, only include titles with the following languages.')
                output_file.writelines('\n# Comment out languages you don\'t want.')
                output_file.writelines('\nlanguage filter:')

                def write_entry(string, comment=False):
                    if comment == True:
                        output_file.writelines(f'\n# - {string}')
                    else:
                        output_file.writelines(f'\n- {string}')

                if overwrite == False:
                    for language in languages:
                        write_entry(language, True)
                else:
                    for language in languages:
                        if 'True|' in language:
                            write_entry(language[5:], True)
                        else:
                            write_entry(language)

                output_file.writelines('\n\n# The region order Retool follows. Comment out the regions you don\'t want.')
                output_file.writelines('\nregion order:')

                for region in regions:
                    if overwrite == False:
                        write_entry(region)
                    else:
                        if 'True|' in region:
                            write_entry(region[5:], True)
                        else:
                            write_entry(region)

                output_file.writelines('\n\n# GUI settings only, not used by the CLI.')
                output_file.writelines('\ngui settings:')

                if gui_settings != False:
                    for setting in gui_settings:
                        write_entry(setting)

                if overwrite == False and gui==False:
                    printwrap(
                        f'{Font.warning}* The {Font.warning_bold}user-config.yaml '
                        f'{Font.warning}file was missing, so a new one has been generated. '
                        'You might want to edit it to define a custom region order, or to '
                        f'filter specific languages. You can now run Retool '
                        f'normally.{Font.end}', 'error')
                    sys.exit()

        except OSError as e:
            print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise


def write_dat_file(input_dat, user_input, output_file_name, stats, titles, dat_numbered, REGEX):
    """ Output the final dat file """

    dat_header = header(input_dat, stats.final_title_count, user_input)

    # Write the file
    try:
        if user_input.keep_remove == True:
            keep_remove_list = output_file_name[:-4] + ' auto keep-remove list.txt'
            user_remove_list = output_file_name[:-4] + ' user remove list.txt'

            with open(keep_remove_list, 'a') as list_output:
                list_output.writelines(f'This file shows which titles have been kept in the output dat with a `+`,\n')
                list_output.writelines(f'and which have been automatically removed by Retool with a `-`. If the\n')
                list_output.writelines(f'`-` is indented, then the title was removed because it was a clone of the\n')
                list_output.writelines(f'title above it with a `+`.\n\n')

                audit_list = {}

                list_output.close()

            if user_input.removed_titles != {}:
                with open(user_remove_list, 'a') as list_output:
                    list_output.writelines(f'This file shows which titles have been removed from the output dat\n')
                    list_output.writelines(f'due to the user setting an option.\n')

                audit_list = {}

                list_output.close()

        with open(output_file_name, 'w') as output_file:
            output_file.writelines(dat_header)
            progress = 0
            progress_old = 0
            if user_input.legacy == False:
                progress_total = stats.final_title_count + stats.clone_count
            else:
                progress_total = stats.final_title_count

            final_xml = {}

            for group in sorted(titles.all):
                for title in sorted(titles.all[group], key=lambda x: natural_keys(x.full_name)):

                    if dat_numbered == False:
                        final_name = title.full_name
                    else:
                        final_name = title.numbered_name

                    progress += 1
                    progress_percent = int(progress/progress_total*100)

                    if progress_old != progress_percent:
                        sys.stdout.write("\033[K")
                        print(f'* Writing dat file... [{str(progress_percent)}%]', sep='', end='\r', flush=True)

                    game_xml = ''

                    if title.cloneof == '':
                        game_xml = f'\t<game name="{html.escape(final_name, quote=False)}">'
                        if user_input.keep_remove == True:
                            if final_name not in audit_list:
                                audit_list[final_name] = []
                    else:
                        if user_input.keep_remove == True:
                            if title.cloneof not in audit_list:
                                audit_list[title.cloneof] = []
                            audit_list[title.cloneof].append(final_name)

                        if user_input.legacy == True:
                            game_xml = f'\t<game name="{html.escape(final_name, quote=False)}" cloneof="{html.escape(title.cloneof, quote=False)}">'

                    rom_xml = []

                    for rom in title.roms:
                        if rom.crc == '':
                            crc_string = ''
                        else:
                            crc_string = f'crc="{rom.crc}" '

                        if rom.md5 == '':
                            md5_string = ''
                        else:
                            md5_string = f'md5="{rom.md5}" '

                        if rom.sha1 == '':
                            sha1_string = ''
                        else:
                            sha1_string = f'sha1="{rom.sha1}" '
                        rom_xml.append(
                            f'\n\t\t<rom {crc_string}{md5_string}'
                            f'name="{html.escape(rom.name, quote=False)}" {sha1_string}'
                            f'size="{rom.size}"/>')

                    rom_xml = ''.join(rom_xml)

                    # Reverse engineer category for No-Intro
                    if title.category == '':
                        for program in REGEX.programs:
                            if re.search(program, final_name) != None:
                                title.category = "Applications"
                        for demo in REGEX.demos:
                            if re.search(demo, final_name) != None:
                                title.category = "Demos"
                        for preproduction in REGEX.preproduction:
                            if re.search(preproduction, final_name) != None:
                                title.category = "Preproduction"
                    if title.category == '':
                        title.category = "Games"

                    if game_xml != '':
                        final_xml[final_name] = (
                            f'{game_xml}\n\t\t'
                            f'<category>{html.escape(title.category, quote=False)}</category>\n\t\t'
                            f'<description>{html.escape(title.description, quote=False)}'
                            f'</description>\n\t\t'
                            f'<release name="{html.escape(title.description, quote=False)}"'
                            f' region="{title.primary_region}"/>{rom_xml}\n\t</game>\n'
                        )

                    progress_old = progress_percent

            final_xml_sort = sorted(final_xml)

            for key in final_xml_sort:
                    output_file.writelines(final_xml[key])

            if user_input.keep_remove == True:
                with open(user_remove_list, 'a') as list_output:
                    if user_input.removed_titles != {}:
                        temp_sort = sorted(user_input.removed_titles)
                        temp_removed_titles = {}

                        for key in temp_sort:
                            temp_removed_titles[key] = user_input.removed_titles[key]

                        user_input.removed_titles = temp_removed_titles

                        list_output.writelines(f'\nTITLE TYPES REMOVED\n')
                        list_output.writelines(f'===================\n')
                        for key, values in user_input.removed_titles.items():
                            list_output.writelines(f'* {key.upper().replace("_"," ")}\n')

                        list_output.writelines(f'\n')
                        for key, values in user_input.removed_titles.items():
                            list_output.writelines(f'\n# {key.upper().replace("_"," ")}\n')
                            underline = []
                            for i in range(0,len(key) + 2):
                                underline.append('=')
                            list_output.writelines(f'{"".join(underline)}\n')
                            for value in sorted(values, key=lambda x: natural_keys(x)):
                                list_output.writelines(f'- {value}\n')
                            list_output.writelines(f'\n')

                    list_output.close()


                with open(keep_remove_list, 'a') as list_output:
                    list_output.writelines(f'\n# STANDALONES\n')
                    list_output.writelines(f'==============\n')

                    final_keep_remove_sort = sorted(audit_list)

                    for key in final_keep_remove_sort:
                        if audit_list[key] == []:
                            list_output.writelines(f'+ {key}\n')

                    parents_clones = {}

                    for key, values in audit_list.items():
                        if values != []:
                            parents_clones[key] = []
                            for value in values:
                                parents_clones[key].append(f'\t- {value}\n')

                    if parents_clones != {}:
                        final_parents_clones_sort = sorted(parents_clones)

                        list_output.writelines(f'\n\n# PARENTS & CLONES\n')
                        list_output.writelines(f'===================\n')

                        for title in final_parents_clones_sort:
                            list_output.writelines(f'+ {title}\n')
                            for clone in parents_clones[title]:
                                list_output.writelines(clone)

                    list_output.close()

            output_file.writelines('</datafile>')
            output_file.close()

        sys.stdout.write("\033[K")
        print('* Writing dat file... done.')
    except OSError as e:
        print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
        raise