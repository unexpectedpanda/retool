#!/usr/bin/env python

"""Exclusions integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Exclusions.dat',
    ]

    golden_comparison_folder: str = 'features'
    test_name: str = 'Exclusions'
    arguments_list: list[str] = [
        '--test --exclude aAbBcdDefkmMopPruv --config tests/configs/user-config-regions-1.yaml'
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
