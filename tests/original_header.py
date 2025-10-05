#!/usr/bin/env python

"""Original header integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str]
    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Original header CRLF
    input_dats = [
        'tests/source/features/Retool - Original header CRLF.dat',
    ]

    golden_comparison_folder = 'features/original-header-1'
    test_name = 'Original header CRLF'
    arguments_list = [
        '--test --originalheader --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Original header LF
    input_dats = [
        'tests/source/features/Retool - Original header LF.dat',
    ]

    golden_comparison_folder = 'features/original-header-2'
    test_name = 'Original header LF'
    arguments_list = [
        '--test --originalheader --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
