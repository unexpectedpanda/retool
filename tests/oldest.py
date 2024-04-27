#!/usr/bin/env python

"""Oldest production versions integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Oldest.dat',
    ]

    golden_comparison_folder: str = 'features'
    test_name: str = 'Oldest production versions'
    arguments_list: list[str] = [
        '--test --config tests/configs/user-config-regions-1.yaml -o',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
