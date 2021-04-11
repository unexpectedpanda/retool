import platform
import re
import sys
import textwrap


def natural_keys(text):
    """ Sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    """

    def atoi(text):
        return int(text) if text.isdigit() else text

    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


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


def old_windows():
    if sys.platform.startswith('win'):
        if (float(platform.release()) < 10):
            return(True)

    return(False)


<<<<<<< HEAD
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


=======
>>>>>>> 093831f44d214dee317ebfb6b7c9aa74466b70ad
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