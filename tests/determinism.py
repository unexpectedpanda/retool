#!/usr/bin/env python

"""Determinism integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/systems/Microsoft - Xbox - BIOS Datfile.dat',
        'tests/source/systems/Nintendo - Game Boy Advance (Private).dat',
        'tests/source/systems/Nintendo - Nintendo DS (Decrypted) (Private).dat',
        'tests/source/systems/Nintendo - Nintendo Entertainment System (Headered) (Private).dat',
        'tests/source/systems/Sega - Master System - Mark III.dat',
        'tests/source/systems/Sony - PlayStation - Datfile.dat',
        'tests/source/systems/Sony - PlayStation 2 - Datfile.dat',
    ]

    golden_comparison_folder: str = 'usa-remainder'
    test_name: str = 'Determinism'
    arguments_list: list[str] = ['--test --config tests/configs/user-config-regions-1.yaml']

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments, runs=5)


if __name__ == '__main__':
    main()
