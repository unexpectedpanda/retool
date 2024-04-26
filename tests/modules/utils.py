import argparse
import datetime
import os
import platform
import re
import sys
import textwrap
import time
import urllib.parse
import urllib.request
from re import Pattern
from typing import Any
from urllib.error import HTTPError, URLError


def download(download_url: str, local_file_path: str = '') -> Any:
    """Downloads a file from a given URL."""

    def get_file(req: urllib.request.Request) -> bytes:
        """Error handling for downloading a file."""
        retrieved: bool = False
        downloaded_file: bytes = b''

        while not retrieved:
            try:
                with urllib.request.urlopen(req) as response:
                    downloaded_file = response.read()
            except HTTPError as error:
                now = get_datetime()
                eprint(
                    f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Data not retrieved', error, req
                )
                eprint(f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Skipping...')
                retrieved = True
            except URLError as error:
                now = get_datetime()
                eprint(
                    f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Something unexpected happened: {error}'
                )
                eprint(
                    f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds...'
                )
                time.sleep(5)
            except TimeoutError as error:
                now = get_datetime()
                eprint(f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Socket timeout: {error}')
                eprint(
                    f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds...'
                )
                time.sleep(5)
            except OSError as error:
                now = get_datetime()
                eprint(f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Socket error: {error}')
                eprint(
                    f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds...'
                )
                time.sleep(5)
            except Exception:
                now = get_datetime()
                eprint(
                    f'\n  * [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Something unexpected happened.'
                )
                eprint('\n  Trying again in 5 seconds...')
                time.sleep(5)
            else:
                retrieved = True

        return downloaded_file

    HEADERS: dict[str, str] = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }

    req: urllib.request.Request = urllib.request.Request(
        f'{os.path.dirname(download_url)}/{urllib.parse.quote(os.path.basename(download_url), safe="=?")}',
        None,
        HEADERS,
    )

    if local_file_path:
        downloaded_file: bytes = get_file(req)

        with open(os.path.abspath(f'{local_file_path}'), 'wb') as output_file:
            output_file.write(downloaded_file)

    return get_file(req)


def enable_vt_mode() -> Any:
    """
    Turns on VT-100 emulation mode for Windows.

    https://bugs.python.org/issue30075
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
        # Don't assume StandardOutput is a console, open CONOUT$ instead
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


def eprint(*args: Any, **kwargs: Any) -> None:
    """Prints to STDERR."""
    print(*args, file=sys.stderr, **kwargs)  # noqa: T201


def format_value(value: Any) -> str:
    """Formats a string value based on whether or not it is empty."""
    if not value:
        return_value: str = f'{Font.disabled}None{Font.end}'
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


def old_windows() -> bool:
    """Figures out if the script is running on a version of Windows earlier than Windows 10."""
    if sys.platform.startswith('win') and (float(platform.release()) < 10):
        return True
    return False


def pattern2string(regex: Pattern[str], search_str: str) -> str:
    """
    Takes a regex pattern, searches in a string, then returns the result. Exists
    only so MyPy doesn't complain about None grouping.
    """
    regex_search_str: str = ''

    regex_search = re.search(regex, search_str)

    if regex_search:
        regex_search_str = regex_search.group()

    return regex_search_str


def printwrap(string: str, style: str = '') -> None:
    """A wrapper for the textwrap function."""
    if not style:
        eprint(textwrap.TextWrapper(width=95, subsequent_indent='  ').fill('' + string))

    if style == 'no_indent':
        eprint(textwrap.fill(string, 80))

    if style == 'error':
        eprint('\n' + textwrap.TextWrapper(width=95, subsequent_indent='  ').fill('' + string))

    if style == 'dat_details':
        eprint(textwrap.TextWrapper(width=95, subsequent_indent='   ').fill('' + string))


def regex_test(regex_list: list[str], list_name: str) -> list[str]:
    """Checks for valid regexes in a list."""
    list_temp: list[str] = regex_list.copy()

    for item in list_temp:
        if item.startswith('/'):
            try:
                re.compile(item[1:])
                regex_valid: bool = True
            except Exception:
                regex_valid = False

            if not regex_valid:
                regex_list.remove(item)

    if list_temp != regex_list:
        eprint(
            f'{Font.warning}\n• The following {list_name} regex filters are invalid and will be skipped:\n'
        )

        for invalid_regex in [x for x in list_temp if x not in regex_list]:
            eprint(f'  • {invalid_regex}')

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


class SmartFormatter(argparse.HelpFormatter):
    """
    Text formatter for argparse that respects new lines.

    https://stackoverflow.com/questions/3853722/how-to-insert-newlines-on-argparse-help-text
    """

    def _split_lines(self, text: str, width: int) -> list[Any]:
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)
