#!/usr/bin/env python

"""Missing header data integration test."""

from tests.integration import integration_test


def main() -> None:

    input_dats: list[str]
    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Missing data LogiqX
    input_dats = ['tests/source/features/Retool - Missing header data.dat']

    golden_comparison_folder = 'features/missing-header-data-logiqx'
    test_name = 'Missing header data LogiqX'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Missing data CLRMAMEPro
    input_dats = ['tests/source/features/Retool - Missing header data (CMP).dat']

    golden_comparison_folder = 'features/missing-header-data-cmp'
    test_name = 'Missing header data CLRMAMEPro'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
