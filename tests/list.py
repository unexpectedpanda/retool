#!/usr/bin/env python

"""Export list of names integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/systems/Microsoft - Xbox - Datfile.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    golden_comparison_folder = 'features/list'
    test_name = 'Export list of names'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --listnames',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
