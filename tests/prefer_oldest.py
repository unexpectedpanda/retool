#!/usr/bin/env python

"""Prefer oldest production versions integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Prefer oldest.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Prefer licensed oldest on
    golden_comparison_folder = 'features/prefer-oldest-1'
    test_name = 'Prefer oldest production versions on'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml -o',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Prefer licensed oldest off
    golden_comparison_folder = 'features/prefer-oldest-2'
    test_name = 'Prefer oldest production versions off'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
