#!/usr/bin/env python

"""MIAs integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - MIAs.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Test marking as MIA
    golden_comparison_folder = 'features/mia-1'
    test_name = 'Mark as MIA'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --labelmia',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Test removing MIA
    golden_comparison_folder = 'features/mia-2'
    test_name = 'Remove MIA'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --exclude k',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
