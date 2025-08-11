#!/usr/bin/env python

"""Removes DAT file integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/systems/Sega - Master System - Mark III.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    golden_comparison_folder = 'features/removes'
    test_name = 'Generate removes DAT file'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --removesdat -q',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments, runs=1)


if __name__ == '__main__':
    main()
