from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import DatNode

from modules.title_selection.choose_string import choose_string


def choose_video_standard(
    standard: str, title_set: set[DatNode], config: Config, report_on_match: bool
) -> set[DatNode]:
    """
    Compares any two titles from a set of DatNodes to see which one has the highest
    priority video standard.

    Args:
        standard (str): The video standard. MPAL, NTSC, PAL, PAL 60Hz, SECAM.

        title_set (set[DatNode]): A set of titles as DatNode instances.

        config (Config): The Retool config object.

        report_on_match (bool): Whether Retool needs to report any titles being traced.

    Returns:
        set[DatNode]: A set of DatNodes filtered by video standard.
    """
    standard = standard.replace(' ', '_')

    for pattern in config.regex[standard]:
        title_set = choose_string(
            pattern, title_set, report_on_match, choose_title_with_string=True
        )

    return title_set
