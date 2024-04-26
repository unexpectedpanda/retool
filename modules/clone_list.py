from __future__ import annotations

from typing import Any


class CloneList:
    def __init__(
        self,
        min_retool_version: str = '2.02',
        mias: list[str] = [],
        variants: list[dict[str, Any]] = [],
    ):
        """
        Creates an object that contains data originally stored in a clone list.

        Args:
            min_retool_version (str, optional): The minimum Retool version required to
            process the imported clone list. Defaults to `2.00`.

            mias (list[str], optional): A list to store the `mias` array found in a
            related clone list, if it exists. Defaults to `[]`.

            variants (dict[str, list[dict[str, Any]]], optional): A dictionary to store
            the `variants` object found in a related clone list, if it exists. Defaults to
            `{}`.
        """
        self.min_retool_version: str = min_retool_version
        self.mias: list[str] = mias
        self.variants: list[dict[str, Any]] = variants
