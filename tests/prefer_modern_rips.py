#!/usr/bin/env python

"""Prefer modern rips integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Prefer modern rips.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Prefer modern rips on
    golden_comparison_folder = 'features/prefer-modern-1'
    test_name = 'Prefer modern rips on'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml -z',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Prefer modern rips off
    golden_comparison_folder = 'features/prefer-modern-2'
    test_name = 'Prefer modern rips off'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
