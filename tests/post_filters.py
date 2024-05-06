#!/usr/bin/env python

"""Post filters integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - Post filters.dat',
    ]

    golden_comparison_folder: str = 'features'
    test_name: str = 'Post filters'
    arguments_list: list[str] = [
        '--test --config tests/configs/user-config-post-filters.yaml',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
