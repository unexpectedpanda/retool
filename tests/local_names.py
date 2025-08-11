#!/usr/bin/env python

"""Local names integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Local names.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    golden_comparison_folder = 'features/local-names'
    test_name = 'Local names'
    arguments_list = [
        '--test --config tests/configs/user-config-local-names.yaml -n',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
