#!/usr/bin/env python

"""Prefer regions integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Prefer regions.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Prefer regions on
    golden_comparison_folder = 'features/prefer-regions-1'
    test_name = 'Prefer regions on'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml -r',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Prefer regions off
    golden_comparison_folder = 'features/prefer-regions-2'
    test_name = 'Prefer regions off'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
