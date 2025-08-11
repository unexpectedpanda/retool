#!/usr/bin/env python

"""Report file integration test."""

from tests.integration import integration_test


def main() -> None:
    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    input_dats: list[str] = [
        'tests/source/systems/Sony - PlayStation - Datfile.dat',
    ]

    golden_comparison_folder = 'features/reports'
    test_name = 'Generate a report'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --report --exclude aAbBcdDefmMopPruv -q',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments, runs=1)


if __name__ == '__main__':
    main()
