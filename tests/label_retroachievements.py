#!/usr/bin/env python

"""Label titles with RetroAchievements integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/features/Retool - RetroAchievements.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Prefer licensed oldest on
    golden_comparison_folder = 'features/label-retroachievements'
    test_name = 'Prefer RetroAchievements'
    arguments_list = [
        '--test --config tests/configs/user-config-regions-1.yaml --labelretro',
    ]

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
