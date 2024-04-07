#!/usr/bin/env python

"""Integration test functions for Retool."""

import difflib
import os
import pathlib
import subprocess
import sys

from modules.utils import Font, eprint

# Set the VS Code path here
vscode_path = pathlib.Path('C:/Users/lister/AppData/Local/Programs/Microsoft VS Code/Code.exe')


def integration_test(
    input_dats: list[str],
    golden_comparison_folder: str,
    test_name: str,
    arguments: str,
    runs: int = 1,
) -> None:
    """
    Manages running Retool for integration tests.

    Args:
        input_dats (list[str]): A list of DAT files to process.

        golden_comparison_folder (str): Where the golden output files are stored for
        comparison against the test output.

        test_name (str): The name of the test.

        arguments (str): The arguments to pass to Retool.

        runs (int, optional): How many runs to perform a test for. Defaults to 1.
    """
    # Remove existing files from the comparison folder
    files: list[pathlib.Path] = list(pathlib.Path('tests/comparison').glob('**/*'))
    delete_files(files)

    # Add the virtualenv site-packages to the path
    os.environ['PYTHONPATH'] = rf'{os.environ.get("VIRTUAL_ENV")}\Lib\site-packages'

    # Test deterministic output
    for i in range(1, runs + 1, 1):
        run_number = 0

        if runs != 1:
            run_number = i
            eprint(f'\n{Font.heading}Run {i} of {runs}{Font.end}')

        for dat in input_dats:
            subprocess.run(
                f'python retool.py "{pathlib.Path(dat)}" {arguments}', cwd='.', shell=True
            )

        compare_files(golden_comparison_folder, test_name, run_number)

        # Tests passed
        files = list(pathlib.Path('tests/comparison').glob('**/*'))
        delete_files(files)

    eprint(f'{Font.success}\nPASSED: {test_name}{Font.end}\n')


def compare_files(golden_folder: str, test_name: str, run: int = 0) -> None:
    """
    Compare the test output files against golden results.

    Args:
        golden_folder (str): Where the golden result to compare against is found.
        test_name (str): The name of the test.
        run (int, optional): Which run of the test is being executed. Defaults to 0.
    """
    eprint(f'\n{Font.subheading}Comparing files...{Font.end}\n')

    tests: list[pathlib.Path] = list(pathlib.Path('tests/comparison').glob('**/*'))
    test_failed: bool = False

    for test in tests:
        source_file: pathlib.Path = test
        golden_file: pathlib.Path = pathlib.Path(
            f'tests/goldens/{golden_folder}/{pathlib.Path(test).name}'
        )

        if not golden_file.is_file():
            eprint(f'{Font.error}{Font.bold}Golden file is missing:\n{golden_file}{Font.end}\n')
            sys.exit(1)

        if not source_file.is_file():
            eprint(f'{Font.error}{Font.bold}Test file is missing:\n{source_file}{Font.end}\n')
            sys.exit(1)

        if golden_file and source_file:
            with open(source_file) as file_1, open(golden_file) as file_2:
                diff = difflib.context_diff(file_2.readlines(), file_1.readlines(), n=0)

                delta = ''.join(diff)

                if delta:
                    eprint(f'{Font.error}{Font.bold}Difference found{Font.end}\n')
                    eprint(
                        f'[{pathlib.Path(test).name}]\n\nThe golden lines are listed first, then the test output lines:\n\n'
                    )
                    eprint(delta)
                    eprint(f'\n[{pathlib.Path(test).name}]\n')
                    test_failed = True
                    golden_link = pathlib.Path(
                        f'tests/goldens/{golden_folder}/{pathlib.Path(test).name}'
                    ).resolve()
                    test_link = pathlib.Path(test).resolve()

                    # Automatically open the differing files.
                    eprint('Opening file comparison...')

                    subprocess.run(
                        f'{vscode_path} -d "{golden_link}" "{test_link}"', shell=False, env=None
                    )

    eprint(f'{Font.subheading}Done.{Font.end}\n')

    if test_failed:
        if run:
            eprint(f'{Font.error}FAILED: {test_name}, run {run}\n\nExiting...{Font.end}')
            sys.exit(1)
        else:
            eprint(f'{Font.error}FAILED: {test_name}\n\nExiting...{Font.end}')
            sys.exit(1)


def delete_files(file_list: list[pathlib.Path]) -> None:
    """
    Deletes test output files.

    Args:
        file_list (list[pathlib.Path]): A list of files to delete.
    """
    for file in file_list:
        try:
            pathlib.Path.unlink(pathlib.Path(file).resolve())
        except Exception:
            eprint(f'Can\'t remove {pathlib.Path(file).resolve()}')
