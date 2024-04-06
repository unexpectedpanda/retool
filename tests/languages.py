#!/usr/bin/env python

"""Regions integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Languages.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Test English > German > French > Italian > Japanese
    golden_comparison_folder = 'features/languages-1'
    test_name = 'English > German > French > Italian > Japanese'
    arguments_list = ['--test --config tests/configs/user-config-languages-1.yaml -l']

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Test Spanish > Italian > German
    golden_comparison_folder = 'features/languages-2'
    test_name = 'Spanish > Italian > German'
    arguments_list = ['--test --config tests/configs/user-config-languages-2.yaml -l']

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Test Japanese > English
    golden_comparison_folder = 'features/languages-3'
    test_name = 'Japanese > English'
    arguments_list = ['--test --config tests/configs/user-config-languages-3.yaml -l']

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
