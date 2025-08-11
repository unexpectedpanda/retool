from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hashlib import _Hash
    from modules.config.config import Config
    from modules.input import UserInput

from modules.utils import ExitRetool, Font, download, eprint


def get_updates(
    local_path: str | pathlib.Path,
    update_name: str,
    download_url: str,
    update_files: set[tuple[str, ...]],
) -> set[tuple[str, ...]]:
    """
    Figures out what clone lists and metadata files need to be updated. First downloads
    the relevant `hash.json` file, which contains names and digests for a set of files.
    Then compares these details with the digests of local files found in `local_path`, and
    returns whatever files have a digest mismatch and therefore need to be updated.

    Args:
        local_path (str): The directory that contains the files that need hashing.

        update_name (str): The name of the update being performed, to report to the user.

        download_url (str): The download directory where the online version of the file is
            found.

        update_files (set[tuple[str,...]]): A set of tuples to store the URLs to the files
            which need updating, and where to write them to disk.

    Returns:
        set[str]: A set of files to be updated.
    """
    # Create folders if they're missing
    pathlib.Path(local_path).mkdir(parents=True, exist_ok=True)

    # Get the hash.json
    eprint(f'• Checking for updated {update_name}...')
    download((f'{download_url}/hash.json', str(pathlib.Path(f'{local_path}/hash.json'))), False)

    if pathlib.Path(f'{local_path}/hash.json').exists():
        try:
            with open(pathlib.Path(f'{local_path}/hash.json'), encoding='utf-8') as file_hash:
                file_hash_str: str = file_hash.read()
        except OSError as e:
            eprint(f'* Error: {Font.end}{e!s}\n', level='error')
            raise

        # Use the filenames and digest values in hash.json to determine if updates
        # need to be downloaded
        pathlib.Path(local_path).mkdir(parents=True, exist_ok=True)

        for file_name, hash_value in json.loads(file_hash_str).items():
            if pathlib.Path(f'{local_path}/{file_name}').resolve().exists():
                hash_sha256: _Hash = hashlib.sha256()

                # Convert files from CRLF to LF to verify if they need updating
                try:
                    with open(
                        pathlib.Path(f'{local_path}/{file_name}'),
                        'r+',
                        newline='\n',
                        encoding='utf-8',
                    ) as file:
                        contents: str = file.read()

                        file.seek(0)
                        file.write(contents)
                        file.truncate()
                except OSError as e:
                    eprint(f'* Error: {Font.end}{e!s}\n', level='error')
                    raise

                # Get the hash of the new file
                try:
                    with open(pathlib.Path(f'{local_path}/{file_name}').resolve(), 'rb') as file:
                        for chunk in iter(lambda: file.read(4096), b''):
                            hash_sha256.update(chunk)
                except OSError as e:
                    eprint(f'* Error: {Font.end}{e!s}\n', level='error')
                    raise

                if hash_sha256.hexdigest() != hash_value:
                    update_files.add(
                        (
                            f'{download_url}/{file_name}',
                            str(pathlib.Path(f'{local_path}/{file_name}')),
                        )
                    )
            else:
                update_files.add(
                    (
                        f'{download_url}/{file_name}',
                        str(pathlib.Path(f'{local_path}/{file_name}')),
                    )
                )
    else:
        hash_json_path: str = str(pathlib.Path(local_path).joinpath('hash.json'))
        eprint(
            f'{hash_json_path} doesn\'t exist, can\'t update {update_name}.',
            level='warning',
        )

    eprint(f'• Checking for updated {update_name}... done.', overwrite=True)
    return update_files


def update_clonelists_metadata(
    config: Config, gui_input: UserInput | None, no_exit: bool = False
) -> None:
    """
    Downloads the latest clone lists and metadata files.

    Args:
        config (Config): The Retool config object.

        gui_input (UserInput): Used to determine if the update is being run from the GUI.
            If so, check if a custom download location has been set in `user-config.yaml`.

        no_exit (bool): Whether to exit the Retool process after the update has run.

    Raises:
        ExitRetool: Silently exit if run from the GUI, so UI elements can re-enable.
    """
    total_downloads: int = 0
    successful_downloads: int = 0

    # Download the latest internal-config.json
    download_location: str = config.clone_list_metadata_download_location

    if config.user_input.dev_mode:
        download_location = (
            'https://raw.githubusercontent.com/unexpectedpanda/retool-clonelists-metadata/dev'
        )

    if gui_input:
        download_location = config.user_input.user_clone_list_metadata_download_location

    failed: bool = False

    eprint(f'• Downloading {Font.b}config/{config.config_file.name}{Font.be}... ')

    total_downloads += 1

    failed = download(
        (
            f'{download_location}/config/{config.config_file.name}',
            str(pathlib.Path(f'{config.config_file}')),
        ),
        False,
    )

    if not failed:
        eprint(
            f'• Downloading {Font.b}config/{config.config_file.name}{Font.be}... done.',
            overwrite=True,
        )
        successful_downloads += 1

    # Get which clone lists and metadata files need to be updated
    update_files: set[tuple[str, ...]] = set()

    update_files = get_updates(
        config.path_clone_list, 'clone lists', f'{download_location}/clonelists', update_files
    )
    update_files = get_updates(
        config.path_metadata, 'metadata files', f'{download_location}/metadata', update_files
    )
    update_files = get_updates(
        config.path_mia, 'MIA files', f'{download_location}/mias', update_files
    )
    update_files = get_updates(
        config.path_ra,
        'RetroAchievements files',
        f'{download_location}/retroachievements',
        update_files,
    )

    # Download the clone lists and metadata files
    total_downloads += len(update_files)

    if update_files:
        eprint(f'• Downloading {total_downloads} files...')
        with ThreadPoolExecutor(max_workers=10) as executor:
            failure = executor.map(download, update_files)

            successful_downloads += list(failure).count(False)

    if total_downloads == 0:
        eprint('\n• Done. No new updates are available.', level='success')
    elif total_downloads == 1:
        eprint('\n• Done. Downloaded 1 file.', level='success')
    else:
        eprint(
            f'\n• Done. Downloaded {successful_downloads}/{total_downloads} files.', level='success'
        )

    if total_downloads != 0 and successful_downloads != total_downloads:
        eprint('• Some files failed to download.', level='error', overwrite=True)

    eprint()

    if not no_exit:
        if gui_input:
            raise ExitRetool
        else:
            sys.exit(0)
