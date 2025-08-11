#!/usr/bin/env python

"""Missing title data integration test."""

from tests.integration import integration_test


def main() -> None:

    input_dats: list[str]
    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Missing title data LogiqX
    input_dats = [
        'tests/source/features/Retool - Missing title data.dat',
    ]

    golden_comparison_folder = 'features/missing-title-data-1'
    test_name = 'Missing title data LogiqX'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Missing title data CLRMAMEPro
    input_dats = [
        'tests/source/features/Retool - Missing title data (CMP).dat',
    ]

    golden_comparison_folder = 'features/missing-title-data-2'
    test_name = 'Missing title data CLRMAMEPro'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
