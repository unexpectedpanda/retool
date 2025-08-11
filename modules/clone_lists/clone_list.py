from __future__ import annotations

from typing import Any


class CloneList:
    def __init__(
        self,
        min_retool_version: str = '2.4',
        mias: list[dict[str, str]] | None = None,
        retroachievements: list[dict[str, str]] | None = None,
        variants: list[dict[str, Any]] | None = None,
    ):
        """
        Creates an object that contains data originally stored in a clone list.

        Args:
            min_retool_version (str, optional): The minimum Retool version required to
                process the imported clone list. Defaults to `2.00`.

            mias (list[dict[str, str]], optional): A list to store the `mias` array found
                in a related MIA file, if it exists. Defaults to `None`.

            retroachievements (list[dict[str, str]], optional): A list to store the
                `retroachievements` array found in a related retroachievements file, if it
                exists. Defaults to `None`.

            variants (dict[str, list[dict[str, Any]]], optional): A dictionary to store
                the `variants` object found in a related clone list, if it exists.
                Defaults to `None`.
        """
        self.min_retool_version: str = min_retool_version
        self.mias: list[dict[str, str]] = mias if mias is not None else []
        self.retroachievements: list[dict[str, str]] = (
            retroachievements if retroachievements is not None else []
        )
        self.variants: list[dict[str, Any]] = variants if variants is not None else []
