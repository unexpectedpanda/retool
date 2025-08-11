#!/usr/bin/env python

"""Exclusions integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Exclusions.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    golden_comparison_folder = 'features/exclusions'
    test_name = 'Exclusions'
    arguments_list = [
        '--test --exclude aAbBcdDefkmMopPruv --config tests/configs/user-config-regions-1.yaml'
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
