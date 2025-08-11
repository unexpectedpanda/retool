from __future__ import annotations

import argparse
import datetime
import os
import pathlib
import platform
import re
import sys
import textwrap
import time
import urllib.parse
import urllib.request
from re import Pattern
from typing import TYPE_CHECKING, Any
from urllib.error import HTTPError, URLError

if TYPE_CHECKING:
    from modules.input import UserInput

import modules.constants as const


def download(download_details: tuple[str, ...], report_download: bool = True) -> bool:
    """
    Downloads a file from a given URL.

    Args:
        download_details (tuple[str, ...]): A tuple of the URL to download the file from,
            and the location to write it to.

        report_download (bool): Whether to report the filename being downloaded. Defaults
            to `True`.

    Returns:
        bool: Whether the download has failed.
    """
    download_url: str = download_details[0]
    local_file_path: str = download_details[1]

    if report_download:
        eprint(
            f'• Downloading {Font.b}{pathlib.Path(download_details[1]).name}...{Font.be}',
            wrap=False,
            overwrite=True,
        )

    def get_file(req: urllib.request.Request) -> tuple[bytes, bool]:
        """Error handling for downloading a file."""
        downloaded_file: bytes = b''
        failed: bool = False
        retrieved: bool = False
        retry_count: int = 0

        while not retrieved:
            try:
                with urllib.request.urlopen(req) as response:
                    downloaded_file = response.read()
            except HTTPError as error:
                now = get_datetime()

                if error.code == 404:
                    eprint(
                        f'\n  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: 404, file not found: {Font.b}{download_url}',
                        level='warning',
                    )
                    eprint(
                        f'  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Skipping...\n',
                        level='warning',
                    )
                    retrieved = True
                else:
                    eprint(
                        f'\n  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Data not retrieved: {error}',
                        level='warning',
                    )
                    eprint(
                        f'  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Skipping...\n',
                        level='warning',
                    )
                    retrieved = True

                failed = True
            except URLError as error:
                if retry_count == 5:
                    break

                retry_count += 1
                now = get_datetime()
                eprint(
                    f'\n  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Something unexpected happened: {error}',
                    level='warning',
                )
                eprint(
                    f'  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Trying again in 5 seconds ({retry_count}/5)...'
                )
                time.sleep(5)
            except TimeoutError as error:
                if retry_count == 5:
                    break

                retry_count += 1
                now = get_datetime()
                eprint(
                    f'\n  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Socket timeout: {error}',
                    level='warning',
                )
                eprint(
                    f'  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Trying again in 5 seconds ({retry_count}/5)...'
                )
                time.sleep(5)
            except OSError as error:
                if retry_count == 5:
                    break

                retry_count += 1
                now = get_datetime()
                eprint(
                    f'\n  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Socket error: {error}',
                    level='warning',
                )
                eprint(
                    f'  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Trying again in 5 seconds ({retry_count}/5)...'
                )
                time.sleep(5)
            except Exception:
                if retry_count == 5:
                    break

                retry_count += 1
                now = get_datetime()
                eprint(
                    f'\n  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Something unexpected happened.',
                    level='warning',
                )
                eprint(
                    f'  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: Trying again in 5 seconds ({retry_count}/5)...'
                )
                time.sleep(5)
            else:
                retrieved = True

        if retry_count == 5:
            failed = True
            now = get_datetime()
            eprint(
                f'\n  • [{now.strftime("%Y/%m/%d, %H:%M:%S")}]: {local_file_path} failed to download.\n\n',
                level='warning',
            )

        # Delete any zero-sized files that have been created
        if failed:
            failed_file: pathlib.Path = pathlib.Path(local_file_path)

            if failed_file.exists() and failed_file.stat().st_size == 0:
                pathlib.Path.unlink(failed_file)

        return (downloaded_file, failed)

    headers: dict[str, str] = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }

    req: urllib.request.Request = urllib.request.Request(
        f'{os.path.dirname(download_url)}/{urllib.parse.quote(os.path.basename(download_url))}',
        None,
        headers,
    )

    downloaded_file: tuple[bytes, bool] = get_file(req)

    file_data: bytes = downloaded_file[0]
    failed: bool = downloaded_file[1]

    if not failed:
        pathlib.Path(local_file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(pathlib.Path(f'{local_file_path}').resolve(), 'wb') as output_file:
            output_file.write(file_data)

    if report_download:
        eprint(Font.overwrite)

    return failed


def enable_vt_mode() -> Any:
    """
    Turns on VT-100 emulation mode for Windows, allowing things like colors.

    From https://bugs.python.org/issue30075
    """
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

    def set_conout_mode(new_mode: int, mask: int = 0xFFFFFFFF) -> int:
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
    except OSError as e:
        if e.winerror == ERROR_INVALID_PARAMETER:
            raise NotImplementedError
        raise


def eprint(
    text: str = '',
    wrap: bool = True,
    level: str = '',
    indent: int = 2,
    section: bool = False,
    pause: bool = False,
    overwrite: bool = False,
    **kwargs: Any,
) -> None:
    """
    Prints to STDERR.

    Args:
        text (str, optional): The content to print. Defaults to `''`.

        wrap (bool, optional): Whether to wrap text. Defaults to `True`.

        level (str, optional): How the text is formatted. Valid values include `warning`,
            `error`, `success`, `disabled`, `heading`, `subheading`. Defaults to `''`.

        indent (int, optional): After the first line, how many spaces to indent whenever
            text wraps to a new line. Defaults to `2`.

        pause (bool, optional): Shows a `Press enter to continue` message and waits for
            user input. Defaults to `False`.

        overwrite (bool, optional): Delete the previous line and replace it with this one.
            Defaults to `False`.

        **kwargs (Any): Any other keyword arguments to pass to the `print` function.
    """
    indent_str: str = ''
    new_line: str = ''
    overwrite_str: str = ''
    section_indicator: str = ''

    if text:
        indent_str = ' '

    if overwrite:
        overwrite_str = '\033M\033[2K'

    if section:
        section_indicator = '│  '

    if level == 'warning':
        color = Font.warning
    elif level == 'error':
        color = Font.error
        new_line = '\n'
    elif level == 'success':
        color = Font.success
    elif level == 'disabled':
        color = Font.disabled
    elif level == 'heading':
        color = Font.heading_bold
    elif level == 'subheading':
        color = Font.subheading
    else:
        color = Font.end

    message: str = f"{overwrite_str}{color}{text}{Font.end}"

    if wrap:
        if level == 'heading':
            print(f'\n\n{Font.heading_bold}{"─"*95}{Font.end}', file=sys.stderr)  # noqa: T201
        if level == 'subheading':
            print(f'\n{Font.subheading}{"─"*60}{Font.end}', file=sys.stderr)  # noqa: T201
        print(  # noqa: T201
            f'{new_line}{section_indicator}{textwrap.TextWrapper(width=95, subsequent_indent=section_indicator + indent_str*indent, replace_whitespace=False, break_long_words=False, break_on_hyphens=False).fill(message)}',
            file=sys.stderr,
            **kwargs,
        )
        if level == 'heading':
            print('\n')  # noqa: T201
    else:
        print(f'{section_indicator}{message}', file=sys.stderr, **kwargs)  # noqa: T201

    if pause:
        empty_lines: str = '\n'

        if not text:
            empty_lines = ''

        print(  # noqa: T201
            f'{empty_lines}{Font.d}Press enter to continue{Font.end}', file=sys.stderr
        )
        input()


def format_value(value: Any) -> str:
    """
    Formats a string-convertible value based on whether it is empty.

    Args:
        value (Any): The value.

    Returns:
        str: A string that either indicates there's no value, or the original value
        converted to a string.
    """
    if not value:
        return_value: str = f'{Font.d}None{Font.end}'
    else:
        return_value = f'{value}'

    return return_value


def get_datetime() -> datetime.datetime:
    """Gets the current datetime and time zone."""
    return (
        datetime.datetime.now(tz=datetime.timezone.utc)
        .replace(tzinfo=datetime.timezone.utc)
        .astimezone(tz=None)
    )


def minimum_version(min_version: str, file_name: str, gui_input: UserInput | None) -> None:
    """
    Figures out if a file requires a higher version of Retool.

    Args:
        min_version (str): The minimum file version to compare against the Retool version.

        file_name (str): The filename of a clone list, or internal config file.

        gui_input (UserInput): Used to determine if the function is being called from the
            GUI.
    """
    # Convert old versions to new versioning system
    if len(re.findall('\\.', min_version)) < 2:
        min_version = f'{min_version}.0'

    # Make sure current Retool version is new enough to handle internal-config.json
    out_of_date: bool = False

    input_file_version_major: int = int(min_version.split('.')[0])
    input_file_version_minor: int = int(min_version.split('.')[1])
    input_file_version_patch: int = int(min_version.split(".")[2])

    retool_version_major: int = int(const.__version__.split(".")[0])
    retool_version_minor: int = int(const.__version__.split('.')[1])
    retool_version_patch: int = int(const.__version__.split('.')[2])

    if input_file_version_major > retool_version_major:
        out_of_date = True
    elif input_file_version_major == retool_version_major:
        if input_file_version_minor > retool_version_minor:
            out_of_date = True
        elif input_file_version_minor == retool_version_minor:
            if input_file_version_patch > retool_version_patch:
                out_of_date = True

    if out_of_date:
        out_of_date_response: str = ''

        def query_user(out_of_date_response: str) -> None:
            eprint(f'{Font.overwrite*3}')
            while not (out_of_date_response == 'y' or out_of_date_response == 'n'):
                eprint(
                    f'• The clone list {Font.b}{file_name}{Font.be} requires Retool '
                    f'{min_version!s} or higher. Behavior might be unpredictable. '
                    'Update Retool to fix this.',
                    level='error',
                )

                eprint('  Continue? (y/n)', level='error')

                out_of_date_response = input()

            if out_of_date_response == 'n':
                if gui_input:
                    raise ExitRetool
                else:
                    sys.exit(1)
            else:
                eprint('')

        query_user(out_of_date_response)


def old_windows() -> bool:
    """
    Figures out if Retool is running on a version of Windows earlier than Windows 10 or
    Windows Server 2019.
    """
    windows_version: str = platform.release()

    if sys.platform.startswith('win'):
        # Catch Windows Server
        if re.search('[A-Za-z]', windows_version):
            if int(re.sub('[A-Za-z]', '', windows_version)) < 2019:
                return True
        # Catch consumer versions of Windows
        elif float(windows_version) < 10:
            return True
    return False


def pattern2string(regex: Pattern[str], search_str: str, group_number: int = 0) -> str:
    """
    Takes a regex pattern, searches in a string, then returns the result. Exists only so
    MyPy doesn't complain about `None` grouping.

    Args:
        regex (Pattern[str]): The regex pattern.

        search_str (str): The string to search in.

        group_number (int): The regex group to return.

    Returns:
        str: A regex group if found.
    """
    regex_search_str: str = ''

    regex_search = re.search(regex, search_str)
    if regex_search:
        regex_search_str = regex_search.group(group_number)

    return regex_search_str


def regex_test(regex_list: list[str], regex_origin: str, type: str) -> list[str]:
    """
    Checks for valid regexes.

    Args:
        regex_list (list[str]): A list of regex patterns in string form.

        regex_origin (str): The origin of the regex filters, included in messages to the
            user when a regex is found to be invalid. Usually `categories`, `overrides`,
            `variants`, `global exclude`, `global include`, `system exclude`,
            `system include`, `global post filter`, `system post filter`.

        type (str): Whether the regex comes from an `user filter` (both overrides and post
            filters), `clone list`, or `trace`. Behavior of the regex test changes based
            on this.

    Returns:
        list[str]: The remaining valid regexes as strings.
    """
    list_temp: list[str] = regex_list.copy()

    for item in list_temp:
        if item.startswith('/') or type != 'user filter':
            try:
                if item.startswith('/'):
                    re.compile(item[1:])
                else:
                    re.compile(item)
                regex_valid: bool = True
            except Exception:
                regex_valid = False

            if not regex_valid:
                regex_list.remove(item)

    if list_temp != regex_list:
        if type == 'user filter':
            eprint(
                f'• The following {regex_origin} regexes are invalid and will be skipped:\n',
                level='warning',
            )
        elif type == 'clone list':
            eprint(
                f'• The following regex in the clone list\'s {regex_origin} object is invalid and will be skipped:\n',
                level='warning',
            )
        elif type == 'trace':
            eprint('• The following regex in the requested trace is invalid:\n', level='warning')

        for invalid_regex in [x for x in list_temp if x not in regex_list]:
            eprint(f'  • {invalid_regex}', level='warning')

        if type == 'trace':
            eprint('\nExiting...\n')
            sys.exit(1)

        eprint(f'{Font.end}')

    return regex_list


class Font:
    """Console text formatting."""

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
        bold_end: str = '\033[22m'
        italic = '\033[3m'
        italic_end = '\033[23m'
        underline: str = '\033[4m'
        underline_end = '\033[24m'
        plain = '\033[22m\033[23m\033[24m'
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
        bold_end = ''
        italic = ''
        italic_end = ''
        underline = ''
        underline_end = ''
        plain = ''
        end = ''

    b: str = bold
    be: str = bold_end
    d: str = disabled
    i: str = italic
    ie: str = italic_end
    u: str = underline
    ue: str = underline_end
    overwrite: str = '\033M\033[2K'


class ExitRetool(Exception):
    """Cleanly exits Retool when it's run from the GUI."""


class SmartFormatter(argparse.HelpFormatter):
    """
    Text formatter for argparse that respects new lines.

    From https://stackoverflow.com/questions/3853722/how-to-insert-newlines-on-argparse-help-text
    """

    def _split_lines(self, text: str, width: int) -> list[Any]:
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)
