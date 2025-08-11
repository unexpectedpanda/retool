#!/usr/bin/env python

"""Overrides integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/systems/Microsoft - Xbox - Datfile.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    golden_comparison_folder = 'features/overrides'
    test_name = 'Overrides'
    arguments_list = [
        '--test --config tests/configs/user-config-overrides.yaml -q',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
