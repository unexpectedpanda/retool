#!/usr/bin/env python

"""Original header integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Original header.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    golden_comparison_folder = 'features/original-header'
    test_name = 'Original header'
    arguments_list = [
        '--test --originalheader --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
