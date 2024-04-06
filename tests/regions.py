#!/usr/bin/env python

"""Regions integration test."""

from tests.integration import integration_test


def main() -> None:
    input_dats: list[str] = [
        'tests/source/systems/Apple - Macintosh - Datfile.dat',
        'tests/source/systems/Microsoft - Xbox - Datfile.dat',
        'tests/source/systems/Microsoft - Xbox - BIOS Datfile.dat',
        'tests/source/systems/Microsoft - Xbox 360 - Datfile.dat',
        'tests/source/systems/Nintendo - Game Boy Advance (Private).dat',
        'tests/source/systems/Nintendo - Game Boy Color (Private).dat',
        'tests/source/systems/Nintendo - GameCube - Datfile.dat',
        'tests/source/systems/Nintendo - Nintendo 3DS (Encrypted).dat',
        'tests/source/systems/Nintendo - Nintendo 64 (BigEndian) (Private).dat',
        'tests/source/systems/Nintendo - Nintendo DS (Decrypted) (Private).dat',
        'tests/source/systems/Nintendo - Nintendo Entertainment System (Headered) (Private).dat',
        'tests/source/systems/Nintendo - Super Nintendo Entertainment System (Private).dat',
        'tests/source/systems/Nintendo - Wii - Datfile.dat',
        'tests/source/systems/Nintendo - Wii U - Datfile.dat',
        'tests/source/systems/Sega - Dreamcast - Datfile.dat',
        'tests/source/systems/Sega - Game Gear.dat',
        'tests/source/systems/Sega - Master System - Mark III.dat',
        'tests/source/systems/Sega - Mega Drive - Genesis (Private).dat',
        'tests/source/systems/Sony - PlayStation - Datfile.dat',
        'tests/source/systems/Sony - PlayStation 2 - Datfile.dat',
        'tests/source/systems/Sony - PlayStation 3 - Datfile.dat',
    ]

    golden_comparison_folder: str
    test_name: str
    arguments_list: list[str]

    # Test USA as top priority
    golden_comparison_folder = 'usa-remainder'
    test_name = 'USA > remainder'
    arguments_list = ['--test --config tests/configs/user-config-regions-1.yaml']

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Test Europe > Spain > Portugal > France > Italy > Germany
    golden_comparison_folder = 'europe-spain-portugal-france-italy-germany-remainder'
    test_name = 'Europe combo #1: Europe > Spain > Portugal > France > Italy > Germany > remainder'
    arguments_list = ['--test --config tests/configs/user-config-regions-2.yaml']

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Test Europe > Germany > France > Italy > Spain > Portugal
    golden_comparison_folder = 'europe-germany-france-italy-spain-portugal-remainder'
    test_name = 'Europe combo #2: Europe > Germany > France > Italy > Spain > Portugal > remainder'
    arguments_list = ['--test --config tests/configs/user-config-regions-3.yaml']

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)

    # Test Japan > World > Asia > USA
    golden_comparison_folder = 'japan-world-asia-usa-remainder'
    test_name = 'Japan > World > Asia > USA > remainder'
    arguments_list = ['--test --config tests/configs/user-config-regions-4.yaml']

    for arguments in arguments_list:
        integration_test(input_dats, golden_comparison_folder, test_name, arguments)


if __name__ == '__main__':
    main()
