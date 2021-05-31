import os
import platform
import re
import sys
import textwrap

def enable_vt_mode():
    """ Turns on VT-100 emulation mode for Windows
    https://bugs.python.org/issue30075
    """

    import ctypes
    import msvcrt

    from ctypes import wintypes

    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

    ERROR_INVALID_PARAMETER = 0x0057
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

    def _check_bool(result, func, args):
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return args

    LPDWORD = ctypes.POINTER(wintypes.DWORD)
    kernel32.GetConsoleMode.errcheck = _check_bool
    kernel32.GetConsoleMode.argtypes = (wintypes.HANDLE, LPDWORD)
    kernel32.SetConsoleMode.errcheck = _check_bool
    kernel32.SetConsoleMode.argtypes = (wintypes.HANDLE, wintypes.DWORD)

    def set_conout_mode(new_mode, mask=0xffffffff):
        # Don't assume StandardOutput is a console.
        # Open CONOUT$ instead
        fdout = os.open('CONOUT$', os.O_RDWR)
        try:
            hout = msvcrt.get_osfhandle(fdout)
            old_mode = wintypes.DWORD()
            kernel32.GetConsoleMode(hout, ctypes.byref(old_mode))
            mode = (new_mode & mask) | (old_mode.value & ~mask)
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


def natural_keys(text):
    """ Sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    """

    def atoi(text):
        return int(text) if text.isdigit() else text

    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


def old_windows():
    if sys.platform.startswith('win'):
        if (float(platform.release()) < 10):
            return(True)

    return(False)


def printwrap(string, style=''):
    """ A wrapper for the textwrap function """

    if style == '':
        print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(f'' + string))

    if style == 'no_indent':
        print(textwrap.fill(string, 80))

    if style == 'error':
        print('\n' + textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(
            f'' + string))


def printverbose(verbose, string):
    """ A wrapper for the textwrap function

    Should only print if user_input.verbose == True
    """

    if verbose == True:
        print('\n' + textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(
                f'' + string))


def regex_test(list, list_name):
    """ Checks for valid regexes in a list """

    if type(list) is not str:
        list_temp = list.copy()

        for item in list_temp:
            if item.startswith('/'):
                try:
                    re.compile(item[1:])
                    regex_valid = True
                except:
                    regex_valid = False

                if regex_valid == False:
                    print(f'{Font.warning}* Invalid regex in {list_name} filters: "{item[1:]}". Ignoring.{Font.end}')
                    list.remove(item)
    return list


class Font:
    """ Console text formatting.

    This can't live in classes.py due to circular import
    """

    if old_windows() != True:
        success = '\033[0m\033[92m'
        success_bold = '\033[1m\033[92m'
        warning = '\033[0m\033[93m'
        warning_bold = '\033[1m\033[93m'
        error = '\033[0m\033[91m'
        error_bold = '\033[1m\033[91m'
        disabled = '\033[90m'
        bold = '\033[1m'
        underline = '\033[4m'
        end = '\033[0m'
    else:
        success = ''
        success_bold = ''
        warning = ''
        warning_bold = ''
        error = ''
        error_bold = ''
        disabled = ''
        bold = ''
        underline = ''
        end = ''