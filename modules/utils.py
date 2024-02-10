from __future__ import annotations

import argparse
import os
import pathlib
import platform
import re
import socket
import sys
import textwrap
import time
import urllib.parse
import urllib.request

from datetime import datetime
from typing import Any, Pattern, TYPE_CHECKING
from urllib.error import HTTPError, URLError

if TYPE_CHECKING:
    from modules.config import Config
    from modules.input import UserInput


def download(download_url: str, local_file_path: str) -> bool:
    """ Downloads a file from a given URL.

    Args:
        - `download_url (str)` The URL to download the file from.
        - `local_file_path (str)` Where to save the file on the local drive.

    Returns:
        `bool` Whether or not the download has failed
    """

    def get_file(req: urllib.request.Request) -> tuple[bytes, bool]:
        """ Error handling for downloading a file """

        downloaded_file: bytes = b''
        failed: bool = False
        retrieved: bool = False
        retry_count: int = 0

        while not retrieved:
            try:
                with urllib.request.urlopen(req) as response:
                    downloaded_file = response.read()
            except HTTPError as error:
                now = datetime.now()

                if error.code == 404:
                    eprint(f'{Font.warning}\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: 404, file not found: {Font.bold}{download_url}')
                    eprint(f'  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Skipping...{Font.end}\n')
                    retrieved = True
                else:
                    eprint(f'{Font.warning}\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Data not retrieved: {error}', req)
                    eprint(f'  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Skipping...{Font.end}\n')
                    retrieved = True

                failed = True
            except URLError as error:
                if retry_count == 5: break

                retry_count += 1
                now = datetime.now()
                eprint(f'{Font.warning}\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Something unexpected happened: {error}')
                eprint(f'  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds ({retry_count}/5)...')
                time.sleep(5)
            except socket.timeout as error:
                if retry_count == 5: break

                retry_count += 1
                now = datetime.now()
                eprint(f'{Font.warning}\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Socket timeout: {error}{Font.end}')
                eprint(f'  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds ({retry_count}/5)...')
                time.sleep(5)
            except socket.error as error:
                if retry_count == 5: break

                retry_count += 1
                now = datetime.now()
                eprint(f'{Font.warning}\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Socket error: {error}{Font.end}')
                eprint(f'  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds ({retry_count}/5)...')
                time.sleep(5)
            except:
                if retry_count == 5: break

                retry_count += 1
                now = datetime.now()
                eprint(f'{Font.warning}\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Something unexpected happened.{Font.end}')
                eprint(f'  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds ({retry_count}/5)...')
                time.sleep(5)
            else:
                retrieved = True

        if retry_count == 5:
            failed = True
            now = datetime.now()
            eprint(f'{Font.warning}\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: {local_file_path} failed to download.{Font.end}\n\n')

        # Delete any zero-sized files that have been created
        if failed:
            failed_file: pathlib.Path = pathlib.Path(local_file_path)

            if (
                failed_file.exists()
                and failed_file.stat().st_size == 0):
                    pathlib.Path.unlink(failed_file)

        return (downloaded_file, failed)

    headers: dict[str, str] = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    req: urllib.request.Request = urllib.request.Request(f'{os.path.dirname(download_url)}/{urllib.parse.quote(os.path.basename(download_url))}', None, headers)

    downloaded_file: tuple[bytes, bool] = get_file(req)

    file_data: bytes = downloaded_file[0]
    failed: bool = downloaded_file[1]

    if not failed:
        pathlib.Path(local_file_path).parent.mkdir(parents=True, exist_ok=True)
        with open (pathlib.Path(f'{local_file_path}').resolve(), 'wb') as output_file:
            output_file.write(file_data)

    return failed


def enable_vt_mode() -> Any:
    """ Turns on VT-100 emulation mode for Windows, allowing things like colors.
    https://bugs.python.org/issue30075 """

    import ctypes
    import msvcrt

    from ctypes import wintypes

    kernel32: ctypes.WinDLL = ctypes.WinDLL('kernel32', use_last_error=True)

    ERROR_INVALID_PARAMETER: int = 0x0057
    ENABLE_VIRTUAL_TERMINAL_PROCESSING: int = 0x0004

    def _check_bool(result: int, func: Any, args: tuple[int, Any]) -> tuple[int, Any]:
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return args

    LPDWORD = ctypes.POINTER(wintypes.DWORD)
    setattr(kernel32.GetConsoleMode, 'errcheck', _check_bool)
    setattr(kernel32.GetConsoleMode, 'argtypes', (wintypes.HANDLE, LPDWORD))
    setattr(kernel32.GetConsoleMode, 'errcheck', _check_bool)
    setattr(kernel32.SetConsoleMode, 'argtypes', (wintypes.HANDLE, wintypes.DWORD))

    def set_conout_mode(new_mode: int, mask: int = 0xffffffff) -> int:
        # Don't assume STDOUT is a console, open CONOUT$ instead
        fdout: int = os.open('CONOUT$', os.O_RDWR)
        try:
            hout: int = msvcrt.get_osfhandle(fdout)
            old_mode: ctypes.c_ulong = wintypes.DWORD()
            kernel32.GetConsoleMode(hout, ctypes.byref(old_mode))
            mode: int = (new_mode & mask) | (old_mode.value & ~mask)
            kernel32.SetConsoleMode(hout, mode)
            return old_mode.value
        finally:
            os.close(fdout)

    mode = mask = ENABLE_VIRTUAL_TERMINAL_PROCESSING

    try:
        return set_conout_mode(mode, mask)
    except WindowsError as e:
        if e.winerror == ERROR_INVALID_PARAMETER:
            raise NotImplementedError
        raise


def eprint(*args: Any, **kwargs: Any) -> None:
    """ Prints to STDERR """
    print(*args, file=sys.stderr, **kwargs)


def format_value(value: Any) -> str:
    """ Formats a string-convertible value based on whether or not it is empty.

    Args:
        - `value (Any)` The value.

    Returns:
        `str` A string that either indicates there's no value, or the original
        value converted to a string.
    """

    if not value:
        return_value: str = f'{Font.disabled}None{Font.end}'
    else:
        return_value = f'{value}'

    return return_value


def minimum_version(min_version: str, file_name: str, gui_input: UserInput|None, config: Config) -> None:
    """ Figures out if a file requires a higher version of Retool

    Args:
        - `min_version`: The minimum file version to compare against the Retool version.

        - `gui_input (UserInput)` Used to determine whether or not the function is being
          called from the GUI.

        - `config (Config)` The Retool config object.
    """

    # Convert old versions to new versioning system
    if len(re.findall('\\.', min_version)) < 2:
        min_version = f'{min_version}.0'

    # Make sure current Retool version is new enough to handle internal-config.json
    out_of_date: bool = False

    clone_list_version_major = f'{min_version.split(".")[0]}.{min_version.split(".")[1]}'
    clone_list_version_minor = f'{min_version.split(".")[2]}'
    if clone_list_version_major > config.version_major:
        out_of_date = True
    elif clone_list_version_major == config.version_major:
        if clone_list_version_minor > config.version_minor:
            out_of_date = True

    if out_of_date:
        out_of_date_response: str = ''

        while not (out_of_date_response == 'y' or out_of_date_response == 'n'):
            printwrap(
                f'{Font.warning_bold}* {file_name} requires Retool '
                f'{str(min_version)} or higher. Behaviour might be unpredictable. '
                'Please update Retool to fix this.',
                'error'
            )

            eprint(f'\n  Continue? (y/n) {Font.end}')
            out_of_date_response = input()

        if out_of_date_response == 'n':
            if gui_input:
                raise ExitRetool
            else:
                sys.exit()
        else:
            eprint('')


def old_windows() -> bool:
    """ Figures out if Retool is running on a version of Windows earlier than Windows 10.
    """

    if (
        sys.platform.startswith('win')
        and (float(platform.release()) < 10)):
            return True
    return False


def pattern2string(regex: Pattern[str], search_str: str, group_number: int = 0) -> str:
    """ Takes a regex pattern, searches in a string, then returns the result. Exists only
    so MyPy doesn't complain about `None` grouping.

    Args:
        - `regex (Pattern[str])` The regex pattern.

        - `search_str (str)` The string to search in.

        - `group_number (int)` The regex group to return.

    Returns:
        `str` A regex group if found.
    """
    regex_search_str: str = ''

    regex_search = re.search(regex, search_str)
    if regex_search: regex_search_str = regex_search.group(group_number)

    return regex_search_str


def printwrap(string: str, style: str = '') -> None:
    """ Ensures long print messages wrap at a certain column count, and controls text
    indenting.

    Args:
        - `string (str)` The input string.

        - `style (str, optional)` Which message style to use. Valid choices are
          `no_indent`, `error`, `dat_details`, or `''`. Defaults to `''`.
    """

    if not style:
        eprint(textwrap.TextWrapper(width=95, subsequent_indent='  ').fill(f'' + string))

    if style == 'no_indent':
        eprint(textwrap.fill(string, 80))

    if style == 'error':
        eprint('\n' + textwrap.TextWrapper(width=95, subsequent_indent='  ').fill(
            f'' + string))

    if style == 'dat_details':
        eprint(textwrap.TextWrapper(width=95, subsequent_indent='   ').fill(
            f'' + string))


def regex_test(regex_list: list[str], regex_origin: str, type: str) -> list[str]:
    """ Checks for valid regexes.

    Args:
        - `regex_list (list[str])` A list of regex patterns in string form.

        - `regex_origin (str)` The origin of the regex filters, included in messages to the
          user when a regex is found to be invalid. Usually `categories`, `overrides`,
          `variants`, `global exclude`, `global include`, `system exclude`, `system include`,
          `global post filter`, `system post filter`.

        - `type (str)` Whether the regex comes from an `user filter` (both overrides and
          post filters), `clone list`, or `trace`. Behavior of the regex test changes based
          on this.

    Returns:
        `list[str]` The remaining valid regexes as strings.
    """

    list_temp: list[str] = regex_list.copy()

    for item in list_temp:
        if (
            item.startswith('/')
            or type != 'user filter'):
                try:
                    if item.startswith('/'):
                        re.compile(item[1:])
                    else:
                        re.compile(item)
                    regex_valid: bool = True
                except:
                    regex_valid = False

                if not regex_valid:
                    regex_list.remove(item)

    if list_temp != regex_list:
        if type == 'user filter':
            eprint(f'{Font.warning}\n* The following {regex_origin} regexes are invalid and will be skipped:\n')
        elif type == 'clone list':
            eprint(f'{Font.warning}\n* The following regex in the clone list\'s {regex_origin} object is invalid and will be skipped:\n')
        elif type == 'trace':
            eprint(f'{Font.warning}\n* The following regex in the requested trace is invalid:\n')

        for invalid_regex in [x for x in list_temp if x not in regex_list]:
            eprint(f'  * {invalid_regex}')

        if type == 'trace':
            eprint(f'\n{Font.end}Exiting...\n')
            sys.exit()

        eprint(f'{Font.end}')

    return regex_list


class Font:
    """
    Console text formatting
    """

    if not old_windows():
        success: str = '\033[0m\033[92m'
        success_bold: str = '\033[1m\033[92m'
        warning: str = '\033[0m\033[93m'
        warning_bold: str = '\033[1m\033[93m'
        error: str = '\033[0m\033[91m'
        error_bold: str = '\033[1m\033[91m'
        heading: str = '\033[0m\033[36m'
        heading_bold: str = '\033[1m\033[36m'
        subheading: str = '\033[0m\033[35m'
        subheading_bold: str = '\033[1m\033[35m'
        disabled: str = '\033[90m'
        bold: str = '\033[1m'
        italic = '\033[3m'
        underline: str = '\033[4m'
        end: str = '\033[0m'
    else:
        success = ''
        success_bold = ''
        warning = ''
        warning_bold = ''
        error = ''
        error_bold = ''
        disabled = ''
        bold = ''
        italic = ''
        underline = ''
        end = ''


class ExitRetool(Exception):
    """ Cleanly exits Retool when it's run from the GUI """
    pass


class SmartFormatter(argparse.HelpFormatter):
    """
    Text formatter for argparse that respects new lines.
    https://stackoverflow.com/questions/3853722/how-to-insert-newlines-on-argparse-help-text
    """

    def _split_lines(self, text: str, width: int) -> list[Any]:
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)
