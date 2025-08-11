#!/usr/bin/env python

"""Compilations integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Compilations.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    golden_comparison_folder = 'features/compilations-1'
    test_name = 'Compilations default'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/compilations-2'
    test_name = 'Compilations prefer indivdual titles'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --compilations i',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/compilations-3'
    test_name = 'Compilations keep individual titles and compilations'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --compilations k',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/compilations-4'
    test_name = 'Compilations optimize for least duplicates'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --compilations o',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
