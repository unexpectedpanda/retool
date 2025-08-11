#!/usr/bin/env python

"""Clone list filters integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Clone list filters.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    golden_comparison_folder = 'features/clone-list-filters-1'
    test_name = 'Clone list filters default (USA > Germany)'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/clone-list-filters-2'
    test_name = 'Clone list filters limited regions'
    arguments_list = [
        '--test --config tests/configs/user-config-clone-list-filters-1.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/clone-list-filters-3'
    test_name = 'Clone list filters reversed region priority (Germany > USA)'
    arguments_list = [
        '--test --config tests/configs/user-config-clone-list-filters-2.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    golden_comparison_folder = 'features/clone-list-filters-4'
    test_name = 'Clone list filters reversed region priority (Japan > USA)'
    arguments_list = [
        '--test --config tests/configs/user-config-clone-list-filters-3.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
