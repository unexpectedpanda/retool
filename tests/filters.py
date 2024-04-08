#!/usr/bin/env python

"""Filters integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Filters.dat',
    ]

    golden_comparison_folder: str = 'features/filters-1'
    test_name: str = 'Filters default (USA > Germany)'
    arguments_list: list[str] = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/filters-2'
    test_name = 'Filters limited regions'
    arguments_list = [
        '--test --config tests/configs/user-config-filters-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/filters-3'
    test_name = 'Filters reversed region priority (Germany > USA)'
    arguments_list = [
        '--test --config tests/configs/user-config-filters-2.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/filters-4'
    test_name = 'Filters reversed region priority (Japan > USA)'
    arguments_list = [
        '--test --config tests/configs/user-config-filters-3.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
