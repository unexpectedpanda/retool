import linecache
import os
import timeit
import tracemalloc
from tracemalloc import Frame, Snapshot, Statistic
from typing import Any

from .utils import eprint

# Mostly cribbed from https://stackoverflow.com/questions/552744/how-do-i-profile-memory-usage-in-python


def display_top(snapshot: Snapshot, key_type: str = 'lineno', limit: int = 3) -> None:
    """Lists the top three lines in terms of memory usage."""
    snapshot = snapshot.filter_traces(
        (
            tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
            tracemalloc.Filter(False, "<unknown>"),
        )
    )
    top_stats: list[Statistic] = snapshot.statistics(key_type)

    eprint(f'\n\nMEMORY USAGE\n============\nTop {limit} lines', wrap=False)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame: Frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename: str = os.sep.join(frame.filename.split(os.sep)[-2:])
        eprint(f'#{index}: {filename}:{frame.lineno}: {(stat.size/1024):.1f} KiB', wrap=False)
        line: str = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            eprint(f'    {line}', wrap=False)

    other = top_stats[limit:]
    if other:
        size: float = sum(stat.size for stat in other)
        eprint(f'{len(other)} other: {(size/1024):.1f} KiB', wrap=False)
    total: float = sum(stat.size for stat in top_stats)
    eprint(f'Total allocated size: {(total / 1024):.1f} KiB', wrap=False)


def perf_test(func: Any) -> Any:
    """Runs a memory and time test for the decorated function."""

    def inner(*args: str, **kwargs: str) -> Any:
        tracemalloc.start()
        result: Any = func(*args, **kwargs)

        snapshot: Snapshot = tracemalloc.take_snapshot()
        display_top(snapshot)

        runs: int = 500
        eprint(f'\nPress any key to time {runs} runs\n', wrap=False)
        input()

        eprint(f'\nTIME: {runs} RUNS\n=================', wrap=False)
        eprint(
            f'\n{timeit.timeit(lambda: func(*args, **kwargs), number = runs)/runs}s per run',
            wrap=False,
        )

        return result

    return inner
