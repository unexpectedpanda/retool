#!/usr/bin/env python

"""Prefer licensed titles integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Prefer licensed.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Prefer licensed titles on
    golden_comparison_folder = 'features/prefer-licensed-1'
    test_name = 'Prefer licensed titles on'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml -y',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Prefer licensed titles off
    golden_comparison_folder = 'features/prefer-licensed-2'
    test_name = 'Prefer licensed titles off'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
