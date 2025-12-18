# Retool changelog

## 2.4.6 (2025-18-11)

-  **_Change_**: Excluding Add-ons now also excludes titles with `(DLC)`, `(Addon)`, and
   `(Addon for XBLA)` tags (issue #359). Thanks
   [steven-sheehy](https://github.com/steven-sheehy)!

-  **_Fix_**: Running tests through Hatch doesn't rely on there being a `.dev` file in
   Retool's root folder any more.

-  **_Fix_**: Fixed missing grip handle graphic between the DAT files list and the rest of
   the app.

-  **_Fix_**: If a user cancels out of adding DAT files, and there's no DAT files in the
   list, Retool now returns the placeholder text to "No DAT files added yet".

-  **_Fix_**: If you select **Override global settings** in the system **Options** tab,
   but nothing else in the options tab, Retool no longer outputs an empty options string
   (`(-)`) in the filename.

-  **_Fix_**: I bought myself a Mac, and so the following things have been fixed in the
   GUI on macOS:

   - The **Settings** and **About** options are now in the proper menus, and not moved by
     macOS heuristics into different places.

   - The delete key now works for removing items from list boxes.

   - The minimum width and height of the Retool GUI has been increased to accommodate
     better widget rendering on macOS.

   - Fonts are no longer statically set in the QT design file. Instead they're assigned
     on an OS-basis in Python, which avoids font loading miss penalties and wrong font
     sizes being assigned.

   - Many buttons now have a fixed size with explicitly set minimum and maximum sizes to
     prevent deformation into odd aspect ratios.

   - Custom checkboxes have been replaced with native checkboxes.

   - An outline has been removed from the status bar.

   - Tab contents have had their layouts reworked for consistent item placement.

   - Tabs labels now elide to the right to overcome tab width issues.


## 2.4.5 (2025-11-05)

-  **_Feature_**: Added some Nintendo mastering codes.

-  **_Change_**: Category matching is no longer case-sensitive (issue #357).


## 2.4.4 (2025-10-26)

-  **_Fix_**: Prevents stacking of RetroAchievements tags if a DAT file is processed more
   than once.

-  **_Fix_**: Fixed a type warning when dragging and dropping files using Retool with
   PySide6 6.10.0.0.


## 2.4.3 (2025-10-20)

-  **_Change_**: Titles with the `(Video)` tag are now categorized as Videos.

-  **_Fix_**: Updated QT version bundled with the compiled Windows version to correct
   issue #354.


## 2.4.2 (2025-10-06)

-  **_Change_**: The `<rom>` elements in output DAT files are now listed in alphabetical
   order based on file name. This makes it easier to find problems when analyzing DAT
   files.

-  **_Fix_**: Removed video regular expressions from the tags Retool ignores when grouping
   titles together. These were added accidentally in 2.4.0.

-  **_Fix_**: Original header output now works again for custom No-Intro DAT files (for
   example, RVZ and WUX versions of Redump DAT files). Turns out reading the file in as
   bytes required extra work to deal with LF line endings.

-  **_Fix_**: The data source that provided RetroAchievement hashes has switched from
   providing ISO, BIN, and CHD hashes to CHD and RVZ hashes. As such, Retool can now add
   RetroAchievements labels to
   [MAME Redump DAT files](https://github.com/MetalSlug/MAMERedump).


## 2.4.1 (2025-08-13)

- **_Fix_**: Turns out pathing in QT is case sensitive, and a path rename broke wherever
  there were arrow icons on buttons. This has now been fixed.

- **_Fix_**: The `<retool>` element is now added to output DAT file headers again in all
  circumstances. This enables the skipping of files that have already been processed.

-  **_Fix_**: Added a Benesse ID regex to version detection.


## 2.4.0 (2025-08-11)

Consider this update a bonus, as I wanted to correct a few things. It isn't a sign of
future updates to come.

Redump clone lists have been updated. No-Intro clone lists... maybe, maybe not. Pulling
No-Intro data is just as arduous as it's ever been, its bot protection and missing
downloads frustrating automating the process.

The primary focus of this update is fixing coding sins of the past, while making memory
and speed improvements.

Benchmarking platform:

- CPU: Intel Core i7 14700K (28 threads across 8 P-Cores and 12 E-cores)

- RAM: 64GB DDR DD5-6400

- Disk: Samsung SSD 990 Pro 2TB

Windows 10, Python 3.13.3 results:

<style>
    td {
        --better-than-10: #0cbf9bdd;
        --better-than-5: #1ac914b0;
        --better-than-3: #1ac914a0;
        --better-than-2: #1ac91480;
        --better-than-1: #1ac91460;
    }
</style>

<table>
    <thead>
        <tr>
            <th rowspan="3">DAT file</th>
            <th rowspan="3">Number of titles</th>
            <th rowspan="3">Options</th>
            <th colspan="3">
                <p>DAT processing time</p>
                <p style="font-size:0.8em;line-height:0.8em">(seconds, averaged over five runs)</p>
            </th>
            <th colspan="3">
                <p>Peak memory usage</p>
                <p style="font-size:0.8em;line-height:0.8em">(Resident size, MB)<p>
                <p style="font-size:0.8em;line-height:0.8em"><em>Measured by <a href="https://pypi.org/project/memory-profiler/">memory-profiler</a></em></p>
            </th>
        </tr>
        <tr>
            <th>v2.3.9</th>
            <th>v2.4.0</th>
            <th>Improvement</th>
            <th>v2.3.9</th>
            <th>v2.4.0</th>
            <th>Improvement</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Commodore - Amiga CD</td>
            <td>567</td>
            <td>Default</td>
            <td>1.45</td>
            <td>0.35</td>
            <td style="background-color:var(--better-than-3);">4.14x</td>
            <td>54.70</td>
            <td>47.60</td>
            <td style="background-color:var(--better-than-1);">1.15x</td>
        </tr>
        <tr>
            <td>Nintendo - Nintendo 3DS (Digital) (CDN)</td>
            <td>10,152</td>
            <td>Default</td>
            <td>66.51</td>
            <td>4.67</td>
            <td style="background-color:var(--better-than-10);">14.24x</td>
            <td>298.10</td>
            <td>197.80</td>
            <td style="background-color:var(--better-than-1);">1.51x</td>
        </tr>
        <tr>
            <td>Nintendo - Nintendo Entertainment System</td>
            <td>6,965</td>
            <td>Default</td>
            <td>3.71</td>
            <td>2.68</td>
            <td style="background-color:var(--better-than-1);">1.38x</td>
            <td>143.00</td>
            <td>120.20</td>
            <td style="background-color:var(--better-than-1);">1.19x</td>
        </tr>
        <tr>
            <td>Sony - PlayStation</td>
            <td>10,776</td>
            <td>Default</td>
            <td>4.88</td>
            <td>2.83</td>
            <td style="background-color:var(--better-than-1);">1.72x</td>
            <td>286.50</td>
            <td>207.70</td>
            <td style="background-color:var(--better-than-1);">1.38x</td>
        </tr>
        <tr>
            <td>Sony - PlayStation</td>
            <td>10,776</td>
            <td>Exclude <code>aABcdDefmMopPruv</code></td>
            <td>10.58</td>
            <td>3.04</td>
            <td style="background-color:var(--better-than-3);">3.48x</td>
            <td>271.20</td>
            <td>192.50</td>
            <td style="background-color:var(--better-than-1);">1.41x</td>
        </tr>
    </tbody>
</table>

Ubuntu 24.04.2 LTS on [WSL](https://github.com/microsoft/WSL), Python 3.12.3 results:

<table>
    <thead>
        <tr>
            <th rowspan="3">DAT file</th>
            <th rowspan="3">Number of titles</th>
            <th rowspan="3">Options</th>
            <th colspan="3">
                <p>DAT processing time</p>
                <p style="font-size:0.8em;line-height:0.8em">(seconds, averaged over five runs)</p>
            </th>
            <th colspan="3">
                <p>Peak memory usage</p>
                <p style="font-size:0.8em;line-height:0.8em">(Heap size, MB)</p>
                <p style="font-size:0.8em;line-height:0.8em"><em>Measured by <a href="https://github.com/bloomberg/memray">Memray</a></em></p>
            </th>
            <th colspan="3">
                <p>Peak memory usage</p>
                <p style="font-size:0.8em;line-height:0.8em">(Resident size, MB)</p>
                <p style="font-size:0.8em;line-height:0.8em"><em>Measured by <a href="https://github.com/bloomberg/memray">Memray</a></em></
            </th>
        </tr>
        <tr>
            <th>v2.3.9</th>
            <th>v2.4.0</th>
            <th>Improvement</th>
            <th>v2.3.9</th>
            <th>v2.4.0</th>
            <th>Improvement</th>
            <th>v2.3.9</th>
            <th>v2.4.0</th>
            <th>Improvement</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Commodore - Amiga CD</td>
            <td>567</td>
            <td>Default</td>
            <td>0.35</td>
            <td>0.34</td>
            <td style="background-color:var(--better-than-1);">1.03x</td>
            <td>15.47</td>
            <td>12.64</td>
            <td style="background-color:var(--better-than-1);">1.22x</td>
            <td>67.13</td>
            <td>62.92</td>
            <td style="background-color:var(--better-than-1);">1.07x</td>
        </tr>
        <tr>
            <td>Nintendo - Nintendo 3DS (Digital) (CDN)</td>
            <td>10,152</td>
            <td>Default</td>
            <td>63.75</td>
            <td>3.70</td>
            <td style="background-color:var(--better-than-10);">17.23x</td>
            <td>235.40</td>
            <td>70.96</td>
            <td style="background-color:var(--better-than-3);">3.32x</td>
            <td>336.40</td>
            <td>126.10</td>
            <td style="background-color:var(--better-than-2);">2.67x</td>
        </tr>
        <tr>
            <td>Nintendo - Nintendo Entertainment System</td>
            <td>6,965</td>
            <td>Default</td>
            <td>5.93</td>
            <td>1.56</td>
            <td style="background-color:var(--better-than-3);">3.80x</td>
            <td>52.50</td>
            <td>28.01</td>
            <td style="background-color:var(--better-than-1);">1.87x</td>
            <td>113.30</td>
            <td>79.79</td>
            <td style="background-color:var(--better-than-1);">1.42x</td>
        </tr>
        <tr>
            <td>Sony - PlayStation</td>
            <td>10,776</td>
            <td>Default</td>
            <td>3.63</td>
            <td>2.24</td>
            <td style="background-color:var(--better-than-1);">1.62x</td>
            <td>181.20</td>
            <td>65.76</td>
            <td style="background-color:var(--better-than-2);">2.76x</td>
            <td>255.80</td>
            <td>118.10</td>
            <td style="background-color:var(--better-than-2);">2.17x</td>
        </tr>
        <tr>
            <td>Sony - PlayStation</td>
            <td>10,776</td>
            <td>Exclude <code>aABcdDefmMopPruv</code></td>
            <td>8.27</td>
            <td>2.31</td>
            <td style="background-color:var(--better-than-3);">3.58x</td>
            <td>182.10</td>
            <td>66.83</td>
            <td style="background-color:var(--better-than-2);">2.72x</td>
            <td>257.60</td>
            <td>118.80</td>
            <td style="background-color:var(--better-than-2);">2.17x</td>
        </tr>
    </tbody>
</table>

While I've done my best to equalize performance between Windows and Linux, the Python
interpreter on Linux is much better than on Windows for multiprocessing,
_even when Linux is running under Windows_. Mostly this is because of
[the different ways Python starts a process on different operating systems](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods).
Perhaps by the time the thread-free model becomes the default in Python and has been
optimized things will change a little &mdash; but that's not going to happen for at least
another year or more.

For curiosity, I ran the same Sony - PlayStation DAT file on Retool 0.53, which dates back
to 2020. It took 2m, 10.51s to complete. Now it's down to 2.83s, a 46x speed improvement
in five years. Knowledge is a crazy thing. At this point in time there probably isn't
many big performance wins left to squeeze out, just a collection of infinite tiny tweaks
of diminishing returns that are likely not worth making.

Here are the changes for 2.4.0:

-  **_Feature_**: Retool can now assign titles as RetroAchievements compatible by adding a
    `retroachievements="yes"` attribute on `game` or `machine` tags. You can also set your
    1G1R title selection to prefer RetroAchievement titles. RetroAchievements data is
    retrieved from an external source. If the source stops updating or becomes
    unavailable, using RetroAchievements features won't be effective.

-   **_Feature_**: Unrecognized attributes in `game` and `machine` elements are now passed
    through to the output DAT file.

-   **_Feature_**: Unrecognized child elements in the `game` and `machine` elements are
    now passed through to the output DAT file.

-   **_Change_**: There's now a `versionIgnore` array in `internal-config.json`, which
    details the titles that shouldn't be picked up by automatic version detection.
    Retool's version detection originally caused confusion in creating clone lists, where
    you'd have to get tricky with workarounds for titles like _Pokemon - Black Version 2_,
    as Retool would see it as version 2.0 of _Pokemon - Black_ &mdash; not its own game.

    Now, so long as those problem titles are in the `versionIgnore` array, you can refer
    to them directly in the clone lists instead of using workarounds.

-   **_Change_**: Windows no longer uses the maximum amount of CPU cores available to it
    in all scenarios. The cost of spinning up a process in Python under Windows is very
    high, meaning that using more cores can mean less performance than fewer cores in
    many cases. Instead, Retool makes a ballpark guess at the best number of processes to
    use for best performance. While there is a penalty for adding processes in Linux as
    well, the total processing time is still so small you may as well just use all cores
    anyway. MacOS likely suffers the same fate as Windows as it also uses the `spawn`
    method instead of `fork` to create a process, but I don't have the hardware to test,
    so no changes have been made there.

-   **_Change_**: Removed the **Include titles without hashes or sizes** option, as it was
    tied to old code that was no longer used.

-   **_Change_**: CLRMAMEPro DAT files are no longer converted to LogiqX before
    processing. Instead, data gets ingested directly.

-   **_Change_**: Retool no longer checks for XML external entity attacks, as its DAT file
    parsing doesn't resolve these entities anyway.

-   **_Change_**: DTD validation is no longer performed against a LogiqX DAT file. It's
    clear people aren't really following the DTD, and the validation just takes up
    processing time.

-   **_Change_**: Output files now terminate with an empty line for easier diff
    comparisons.

-   **_Change_**: MIAs are no longer labelled by default. The `--nolabelmia` flag has been
    inverted to be `--labelmia`.

-   **_Change_**: MIA data is now downloaded from an external source. If the source stops
    updating or becomes unavailable, marking MIAs won't be effective.

-   **_Change_**: The option to remove MIAs now removes the entire title if it's missing a
    file, not just the individual file from the title.

-   **_Change_**: Numbered DAT files are now output sorted according to their number, not
    their name without the number.

-   **_Change_**: Since Retool's code base has matured enough, and there are now enough
    tests to find problems, Retool no longer checks for clones that are also assigned as
    parents. Files should process faster as a result.

-   **_Fix_**: Redump now uses two sets of language tags for some titles. For example,
    _Gears of War 2 (Europe) (En,Fr,De,Es,It,Zh,Ko,Pl,Ru,Cs,Hu) **(En,Es,It)**_ and
    _Ultimate Action Triple Pack (Europe) (En,Fr,De,Es,It,Nl,Pt) **(En,Fr,De)**_. The
    second set of languages unfortunately is used to mean more than one thing, so is not
    useful for filtering based on the filename alone. For example, in
    _Gears of War 2 (Europe) (En,Fr,De,Es,It,Zh,Ko,Pl,Ru,Cs,Hu) (En,Es,It)_, English,
    Spanish, and Italian are the spoken languages available for the title. For
    _Ultimate Action Triple Pack (Europe) (En,Fr,De,Es,It,Nl,Pt) (En,Fr,De)_ however,
    the second set of languages represents the common languages found in each of the games
    in the compilation:

    * _Deus Ex: Human Revolution (BLES-01151) (v01.00) (Fr,De,Es,It)_

    * _Hitman: Absolution (BLES-01403) (v01.00) (En,Fr,Es)_

    * _Thief (BLES-01982) (v01.01) (En,Fr,De,Es,It,Pl,Ru)_

    In the compilation's case, the second language block is being used as a marker of
    where the title was intended to be distributed, since Redump is unable to add new
    regions to their system.

    Since this data is not presented in a syntax that's useful for filtering, the second
    language tag is now stripped by Retool, and only the first is used to determine
    language.

-   **_Fix_**: You could turn on a system setting override in the GUI, but turning it off
    again wouldn't save the off state in the config. This has been fixed.

-   **_Fix_**: When you enabled **Prefer titles ripped from modern rereleases**, the
    output file name added a code of `-r`, which is actually for
    **Prefer licensed over unlicensed titles**. A code of `-z` is now used, as intended.
    The content of the output DAT file was always correct, so no fix was required there.

-   **_Fix_**: Fixed a crash when using include overrides.

-   **_Fix_**: If one line was marked in the include or exclude overrides to remove
    related titles, Retool removed the related titles for _all_ lines in the include or
    exclude overrides. This has been fixed.

-   **_Fix_**: If titles can be removed due to more than one exclusion setting, they now
    always show up in the same exclusion category in the report.

-   **_Fix_**: Fixed a stat counting bug to do with supersets.

-   **_Fix_**: Fixed the `cloneof` property in legacy mode being set as a non-numbered
    name in numbered DAT files.

-   **_Fix_**: Fixed CLRMAMEPro BIOS DAT files from Redump exporting with a category of
    `Console` instead of `BIOS`.

-   **_Fix_**: Fixed the exclude and include options comment in system config files, so
    it now correctly says "SYSTEM" instead of "GLOBAL".

-   **_Fix_**: Some version comparison bugs were squashed.

-   **_Chore_**: Created custom checkboxes as SVGs, as QT's default checkboxes don't scale
    properly. Amusingly I'd done this before for Retool's first GUI, so was able to take
    some of that work as a starting point. Also fixed the down arrow on dropdown boxes, as
    the default moves weirdly on 4k monitors when you mouse over it.

-   **_Chore_**: Retool now more aggressively skips some title comparisons to avoid doing
    work it doesn't have to, improving performance for large groups. This was put in place
    due to _Doko Demo Honya-san_ in the Nintendo 3DS CDN DAT file, which has 1,519 titles
    bundled into the one group with no clones, and dramatically slowed down processing.

-   **_Chore_**: Multiprocessing performance improvements. When each new process is
    spawned/forked, Python does a bunch of serializing of data for each process. The more
    data that goes in, the more performance tax there is for starting a process. As such,
    things have been refactored to push as little as possible into each process.

-   **_Chore_**: Memory usage improvements.

    - Entire DAT files are no longer loaded into memory to read them. Instead, one `game`,
      `set`, or `machine` element is ingested at a time.

    - A full copy of the original data read in from the DAT file is no longer kept to
      makes override includes work.

    - Metadata and clone list content are discarded when they're no longer used.

-   **_Chore_**: The progress bar now increments per title during the
    _Selecting 1G1R titles_ stage, instead of incrementing milestone style after each
    sub-stage completes.

-   **_Chore_**: Deduped search strings found in both `internal-config.json` and Retool's
    code.

-   **_Chore_**: Moved most of the version normalization code out of the comparison loop,
    so it's only performed once per title instead of for every comparison.

-   **_Chore_**: Overhauled how Retool handles exclusions and stats, and got a nice speed
    boost out of it.

-   **_Chore_**: Overhauled how Retool handles config file incompatibilities between
    versions.

-   **_Chore_**: Fixed doc strings so they format properly in Visual Studio code when
    hovering over the function name.

-   **_Chore_**: Corrected multiple typing hints.

-   **_Chore_**: Added multiple tests.

-   **_Chore_**: Did some profiling between [Austin](https://github.com/P403n1x87/austin),
    [Memray](https://github.com/bloomberg/memray), and
    [memory-profiler](https://pypi.org/project/memory-profiler/) to reduce performance
    issues.

-   **_Chore_**: Updated dependencies. Unpinned QT version, as the bug that interfered
    with testing was fixed.

-   **_Chore_**: Almost six years into Python and apparently I missed the basics of
    setting defaults in a function. Check out this function:

    ```py
    def message(
        message_add: str = '',
        message_list: list[str] = []
        ) -> list[str]:
            message_list.append(message_add)

            return message_list

    a: list[str] = message('Hello')
    b: list[str] = message('Goodbye')
    ```

    What is the value of `a` going to be?

    ```py
    >>> print(a)
    ['Hello', 'Goodbye']
    ```

    Huh, that's weird. What about `b`?

    ```py
    >>> print(b)
    ['Hello', 'Goodbye']
    ```

    The same?!

    It turns out that when you set a default for a function argument to an empty value of
    a mutable type, that value only gets used the _first_ time the function runs as part
    of constructing and assigning that variable.

    So the first time `message` is called without specifying `message_list`, it creates
    the empty list, `[]`... but every _subsequent_ time the function is called, it says
    "oh hey, I've already got a reference to this variable... I'm going to use that
    instead!"

    So when `a = message('Hello')` is called, `message_list` starts as `[]`, and then
    `Hello` is added to it. When `b = message('Goodbye')` is called... as far as Python is
    concerned, the value for `message_list` already exists, and it's `['Hello']`... so it
    appends `'Goodbye'` to it. _And_ because that value is just a reference, and both `a`
    and `b` are pointing to that reference... they now both equal `['Hello', 'Goodbye']`.

    To work around this, we need some Python boilerplate that's apparently well known...
    that somehow I missed.

    ```py
    def message(
        message_add: str = '',
        message_list: list[str] | None = None
        ) -> list[str]:
            message_list = message_list if message_list is not None else []

            message_list.append(message_add)

            return message_list

    a: list[str] = message('Hello')
    b: list[str] = message('Goodbye')
    ```

    Now let's see how things go:

    ```py
    >>> print(a)
    ['Hello']

    >>> print(b)
    ['Goodbye']
    ```

    Much better, much more predictable, and this is now fixed in Retool's code.


## 2.3.9 (2025-03-09)

-   **_Fix_**: Retool now handles empty description fields.


## 2.3.8 (2024-05-06)

-   **_Fix_**: Fixed post filters not working.


## 2.3.7 (2024-04-28)

-   **_Fix_**: Fixed clone list and `internal-config.json` minimum version detection.


## 2.3.6 (2024-04-27)

-   **_Feature_**: You can now choose to prefer the oldest production version of a title
    instead of the newest.

-   **_Fix_**: Budget rereleases are now promoted above original titles with high
    revisions. For example, `Example Title (USA) (PlayStation the Best)` is now chosen
    over `Example Title (USA) (Rev 3)`. This is on the assumption that budget rereleases
    most likely contain the latest revisions. This was also necessary to implement the
    oldest version feature properly.

-   **_Fix_**: Fixed the flags in the output DAT file filename to reflect system settings
    when system settings are in use, instead of reflecting global settings.


## 2.3.5 (2024-04-27)

-   **_Fix_**: Fixed Retool crashing when **Prefer titles ripped from modern rereleases**
    was enabled.

-   **_Change_**: Because case can change frequently between DAT file revisions, overrides
    and post filters are no longer case sensitive. This increases convenience, but also
    means you're more likely to shoot your own foot off with partial and regex matches, so
    caveat utilitor.

-   **_Change_**: The way the version is reported has changed to accommodate dynamic
    versioning in Hatch. Instead of 2.03.5, Retool now shows 2.3.5.

-   **_Chore_**: Lately Windows Defender has been finding false positives on the compiled
    Windows version of Retool. While there's not much that can be done about this other
    than marking an exception in Defender on your machine, Python, PyInstaller, and UPX
    have all been updated in the hope that enough changes have occured to prevent the
    incorrect alert from happening.

-   **_Chore_**: Cleaned up how Retool outputs to screen. Made more use of code page 437
    characters to freshen up the look.

-   **_Chore_**: Started reorganizing where functions live for future clean up and
    optimizations. While I don't really expect anyone will go code diving, those who do
    will find things are stored in an inconsistent fashion until this task is complete.


## 2.03.4 (2024-04-08)

-   **_Change_**: When you specify `--output` in a non-interactive terminal, the output
    is now written to a file, not `STDOUT`.

-   **_Fix_**: If you didn't populate your region priority list with all the regions in
    a clone list filter, the condition would fail to `true`, causing odd title selection.
    This has now been fixed.


## 2.03.3 (2024-04-07)

-   **_Feature_**: Clone list and metadata updates now use threaded downloads to reduce
    wait times.


## 2.03.2 (2024-04-06)

-   **_Fix_**: Fixed Retool falsely thinking CLRMAMEPro DAT files have already been
    processed.

-   **_Chore_**: Updated dependencies. Locked down PySide6 version due to a
    [bug](https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-2665?filter=allopenissues)
    that interferes with testing.


## 2.03.1 (2024-04-06)

-   **_Change_**: The **Prefer regions over languages** setting now also overrides
    superset selection.

-   **_Fix_**: DTD file detection wasn't updated to take into account the new entry point
    paths. This didn't matter on Windows, but did affect Linux and MacOS.


## 2.03.0 (2024-04-06)

-   **_Feature_**: Some changes aimed at ROMVault and DATVault users:

    -   You can now choose not to add MIA attributes to titles and ROMs from clone lists.
        This is mainly useful if you're a DATVault subscriber.

    -   You can now add a quick import folder through **File > Settings**. When you click
        the **Add DAT files recursively from your quick import folder** button, all DAT
        files in that folder and its subfolders are loaded into Retool.

    -   You can now replace your input DAT files with the Retool version instead of
        creating new files. Make sure you've backed up your original DAT files first.

    -   By default, Retool no longer processes files it has already processed. You can
        bypass this by going to the **Options** tab and enabling
        **Allow processing of already processed files**.

-   **_Feature_**: Thanks to a rewrite of the compilations code and Retool's new testing
    framework, you can now choose how to handle compilations. There are four modes:

    -   **Default**: Chooses individual titles most of the time. Only chooses compilations
        when they have a higher region, language, or clone list priority, or contain
        unique titles. When choosing a compilation for unique titles, if other titles in
        the compilation have individual equivalents, the individual titles are also
        included, leading to some title duplication.

    -   **Prefer individual titles**: Chooses individual titles regardless of region,
        language, and clone list priorities, and discards compilations unless they contain
        unique games. You're likely to prefer this mode if you use ROM hacks or Retro
        Achievements. When choosing a compilation for unique titles, if other titles in
        the compilation have individual equivalents, the individual titles are also
        included, leading to some title duplication.

    -   **Keep individual titles and compilations**: Ignores the relationship between
        individual titles and compilations, meaning individual titles are only compared
        against other individual titles, and compilations against other compilations. This
        option has the most title duplication.

    -   **Optimize for least possible title duplication**: Beta, not recommended. Prefers
        compilations to minimize file count. While this mode can save disk space, it can
        be hard to tell what compilations contain based on their filename. This mode might
        not choose the most optimal solution when supersets or clone list priorities are
        involved.

-   **_Change_**: In Retool GUI you now set the global output path in the **Paths** tab.

-   **_Change_**: The **Unlicensed** exclude settings are now more intuitively laid out in
    Retool GUI, which allows for more granular choices.

-   **_Change_**: The `u` exclude option in Retool CLI no longer includes aftermarket and
    pirate titles. Instead, set the flags separately for each unlicensed title type: `u`
    for `(unl)`, `f` for `(Aftermarket)`, `p` for `(Pirate)`.

-   **_Change_**: A separator has been placed between the add and remove buttons in
    Retool GUI, to reduce accidental clicks and to more cleanly separate functions.

-   **_Change_**: A majority of the Retool GUI interface is now disabled during processing
    to prevent settings changes while the program is working.

-   **_Change_**: The open file dialog box now opens at the currently set folder for the
    specific Retool option you're changing. This reduces needless navigation.

-   **_Change_**: Output DAT file headers have been tweaked a little to make replacing and
    splitting DAT files easier.

-   **_Change_**: Thanks to [@thiagokokada](https://github.com/thiagokokada), entry points
    have been set up properly for Retool. Additionally, Retool now treats the folder where
    it lives as the root folder for its relative paths, no matter the current working
    directory.

    This isn't consequential for Windows users running the EXE file, but to those running
    the Python scripts directly and launching from the command line, it means instead of
    navigating to the Retool folder and running `python retool.py` or
    `python retoolgui.py`, if you have your environment set up correctly you can just run
    `retool` or `retoolgui` from anywhere.

    Want to try it out?
    [Clone Retool from the GitHub repo](https://unexpectedpanda.github.io/retool/download/#git-and-python-gui-and-cli),
    navigate to the folder it was cloned to, then install it as a package with
    `pip install .`. Retool is then installed to your Python scripts folder, and your
    config files, clone lists, and metadata files are also kept there. Providing that
    folder is added to your system path, you can now run `retool` or `retoolgui` from any
    folder on the command line.

    There's a caveat: if you do things this way, every time you update Retool you need to
    run `pip install --upgrade .` to update the package version too, or you'll see the old
    version of Retool when you run `retool` or `retoolgui`.

-   **_Change_**: `config/systems/template.yaml` is no longer needed, as Retool now
    generates system config files from scratch.

-   **_Fix_**: Compensated for yet another of No-Intro's inconsistent date formats, this
    time in the (~YYYY-XX-XX) format.

-   **_Fix_**: Retool used to try to make another decision if it ultimately chose a bad
    dump, a preproduction title, or a pirate title. If the user didn't prefer modern
    titles or preferred licensed titles over unlicensed, it would also try again if it
    selected a title the user didn't want. This was causing selection errors, particularly
    when it came to preferring regions over languages. This is now treated as a filter
    instead of a recovery process and happens earlier, resulting in better title
    selection.

-   **_Fix_**: Fixed the incorrect default region order for system configs, which placed
    Europe lower than the global default region order.

-   **_Fix_**: Fixed user override titles not being excluded from the output DAT file when
    they had already been reassigned groups by a clone list.

-   **_Fix_**: Fixed the **Process DAT files** button not enabling if you clicked a button
    to add DAT files, cancelled, then actually added DAT files.

-   **_Fix_**: Retool now works on Windows Server 2019+.

-   **_Chore_**: Removed the `(Homebrew)` tag from Retool's processing, as No-Intro
    doesn't use it anymore.


## 2.02.2 (2024-03-08)

-   **_Fix_**: Ensured MAME Redump DAT files have unique config settings, but
    load Redump clone lists and metadata.

-   **_Fix_**: Fixed titles without regions being assigned a blank set of regions
    instead of being set to `(Unknown)`. This was most obvious when converting
    Redump BIOS DAT files.

-   **_Fix_**: When outputting a DAT file of removed titles while using legacy
    parent/clone format, the removes DAT file no longer contains clones found in the
    legacy parent/clone DAT file.

-   **_Fix_**: More reliable sorting of exclusions and user option tags in
    filenames and descriptions.

-   **_Fix_**: If a title is in a `<game>` or `<machine>` node, that node is used in the
    output DAT file.

-   **_Chore_**: Style fixes and reduction of unnecessary work across the code
    base in preparation for building out more comprehensive tests.


## 2.02.1 (2024-02-18)

-   **_Feature_**: Retool now supports
    [MAME Redump](https://github.com/MetalSlug/MAMERedump/tree/main) sets. These DATs
    match against Redump clone lists.

-   **_Feature_**: You can now choose to use `<machine>` for your title nodes in
    the output DAT file instead of `<game>`.

-   **_Change_**: `<rom>` and `<disk>` nodes in an input DAT file no longer need
    a size assigned for Retool to process them. This is because CHDs are often
    defined with only a hash.

-   **_Fix_**: If you run Retool CLI on a folder with only one DAT file, and no
    titles are in that DAT file that match your preferences, Retool no longer
    ends the task with a crash.


## 2.02.0 (2024-02-08)

-   **_Breaking change_**: The clone list format has changed. Update to 2.02.0
    to avoid issues.

-   **_Feature_**: You can now output a DAT using the local name of a title in
    unicode, if it's available in the metadata scraped from Redump and No-Intro,
    or included in a clone list. For example, instead of
    `Shining Force II - Inishie no Fuuin (Japan)`, you can output
    `シャイニング·フォースII 『古の封印』 (Japan)`. Tags like `(Japan)` and
    `(Disc 1)` remain in English.

    Open the **Local names** tab to choose which languages to enable local
    names for, and to set language priorities for titles with multiple local
    names.

    This is very much a work in progress. Both No-Intro and Redump aren't
    consistent about recording local names, so there are plenty missing. Retool
    community contributions are needed to fill the gaps. Find something you
    think should have a local name? Create an issue or pull request, provide
    the correct name, and post a screenshot of the title screen or box image for
    validation.

-   **_Feature_**: You can now add `filters` to a title entry in clone lists.
    Think of the `filters` parameter as an easy way to isolate specific titles
    in a search result, and apply changes to them based on conditions.

    For example:

    ```json
    {
        "group": "Bomberman GB 2",
        "titles": [
            {
                "searchTerm": "Bomberman GB 2",
                "filters": [
                    {
                        "conditions": {"matchRegions": ["Japan"]},
                        "results": {"group": "Bomberman GB"}
                    }
                ]
            }
        ]
    }
    ```

    In the previous example the `searchTerm` of `Bomberman GB2` finds all titles
    with the short name `Bomberman GB2`, and gathers them in the `Bomberman GB2`
    group. If the region of a title happens to include `Japan`, then that title
    is moved to the group `Bomberman GB` instead.

    Conditions include:

    - **`matchRegions`**: `array[string]`. Regions a title must have for the
      condition to be true.

    - **`matchLanguages`**: `array[string]`. Languages a title must have for the
      condition to be true.

    - **`matchString`**: `regex string`. A regex string that must find a match
      in a title's full name for the condition to be true.

    - **`regionOrder`**: `object[string, array[string]]`. The user region order
      that must be fulfilled for the condition to be true.

    All conditions in a filter must be true for the `result` to be executed.

    Results include:

    - **`categories`**: `array[string]`. A list of categories to assign to the
      title.

    - **`englishFriendly`**: `bool`: Whether a title is English friendly.

    - **`group`**: `string`. The group to assign the title to.

    - **`localNames`**: `object[string, string]`: Local names to assign to the
      title.

    - **`priority`**: `integer`. The clone list priority to assign to the title.

    - **`superset`**: `bool`. Elevate the title to a superset.

-   **_Feature_**: You can now mark titles as "English friendly" in clone lists.
    For example, the Japanese version of _Enduro Racer_ on the Sega Master
    System has twice as many levels as the USA version. Of what little text
    there is, it's in English, but the No-Intro database lists its language as
    Japanese. To make sure the Japanese version is selected even when USA is
    higher in the region order, we can construct a clone list entry as follows:

    ```json
    {
        "group": "Enduro Racer",
        "titles": [
            {
                "searchTerm": "Enduro Racer",
                "filters": [
                    {
                        "conditions": {
                            "matchRegions": ["Japan"]
                        },
                        "results": {
                            "englishFriendly": true,
                            "superset": true
                        }
                    }
                ]
            }
        ]
    }
    ```

    You don't always need a filter to apply the `englishFriendly` tag &mdash; it's
    available at the `searchTerm` level as well.

-   **_Change_**: To better support regional language variants, the following
    languages have been split:

    - Chinese is now available as Chinese (Simplified) and Chinese
      (Traditional). They detect `Zh-Hans` and `Zh-Hant` respectively, but
      also the generic Chinese code of `Zh`. When faced with just `Zh`, Retool
      attempts to infer which written language is used based on region. This won't
      be perfect &mdash; if a mismatch is found in No-Intro, get them to use the
      more accurate language code. If a mismatch is found in Redump, all you can
      do is request that they adopt the more accurate language codes in the
      first place.

    - Portuguese is now available as Portuguese and Portuguese (Brazilian).
      Brazilian titles with no language set are now set to `Pt-BR` instead of
      `Pt`.

    - Spanish is now available as Spanish, Spanish (Latin American), and Spanish
      (Mexican). Mexican titles with no language set are now set to `Es-MX`
      instead of `Es.` Latin American titles with no languages set are now set to
      `Es-XL`.

    - French is now available as French and French (Canadian).

-   **_Change_**: The `Asia` region no longer has an implied language of
    English. At the time this was implemented, the majority of `Asia` titles
    supported English, but those days are definitely gone and there's no way
    to tell language support for a title programmatically. If you find an `Asia`
    title with no languages listed, get No-Intro or Redump to fix it.

-   **_Change_**: There's now a check if a DAT file starts a filename with
    `.`. In these circumstances, it's replaced with the fixed-width version,
    `．`.

-   **_Change_**: Clone lists have been refactored for greater flexibility and
    to make contributing easier.

    -   Group names in clone lists are now used verbatim, instead of being
        converted to a sanitized equivalent. This means you can include
        parentheses and version-like strings such as "v2" and they won't get
        stripped, reducing potential confusion for contributors.

    -   The `overrides` array is no longer supported in clone lists. Instead,
        use the `filters` parameter in the same object as a `searchTerm` in
        the `variants` array.

        For example, take the _King's Field_ problem.

        | Japanese title   | Equivalent USA title |
        |------------------|----------------------|
        | King's Field     | None                 |
        | King's Field II  | King's Field         |
        | King's Field III | King's Field II      |

        How do we deal with _King's Field (Japan)_ not getting mixed up with
        _King's Field (USA)_, or _King's Field II (Japan)_ getting mixed up
        with _King's Field II (USA)_?

        This is how you'd do it with old school overrides:

        ```json
        "overrides": [
            {
			"searchTerm": "King's Field II (Japan)",
			"newGroup": "King's Field"
            },
            {
                "searchTerm": "King's Field (Japan)",
                "newGroup": "King's Field Japan"
            }
        ]
        ```

        Now it's all done with `filters` in the `variants` array:

        ```json
        "variants": [
            {
                "group": "King's Field",
                "titles": [
                    {
                        "searchTerm": "King's Field",
                        "filters": [
                            {
                                "conditions": {"matchRegions": ["Japan"]},
                                "results": {"group": "King's Field (Japan)"}
                            }
                        ]
                    }
                ]
            },
            {
                "group": "King's Field II",
                "titles": [
                    {
                        "searchTerm": "King's Field II",
                        "filters": [
                            {
                                "conditions": {"matchRegions": ["Japan"]},
                                "results": {"group": "King's Field"}
                            }
                        ]
                    }
                ]
            }
        ]
        ```

        In the previous example:

        -   The group `King's Field` collects all titles that match the short
            name `King's Field`. When Retool finds a `King's Field` title with
            a region of `Japan`, it's moved to the group `King's Field (Japan)`.

        -   The group `King's Field II` collects all titles that match the short
            name `King's Field II`. When Retool finds a `King's Field II` title
            with a region of `Japan`, it's moved to the group `King's Field`.

        It's ultimately more code, but it allows greater flexibility when
        combined with the rest of the `filters` options, not to mention
        everything now lives in the `variants` array so you don't have to look
        in two places. Additionally, Retool should be a bit more performant as
        a result of this change.

    -   The `categories` array is no longer supported in clone lists. Instead,
        add a `categories` key in the same object as a `searchTerm` in the
        `variants` array:

        ```json
        {"searchTerm": "Cite des Enfants Perdus, La", "categories": ["Games", "Demos"]}
        ```

        You can also set `categories` at the top level to apply categories to
        every title in the group (unless categories have been set at the individual
        title or `filters` level). In the following example, everything in the
        `titles` array now has the categories of `Games` and `Demos`:

        ```json
        {
            "group": "City of Lost Children, The",
            "categories": ["Games", "Demos"],
            "titles": [
                {"searchTerm": "Cite des Enfants Perdus, La"},
                {"searchTerm": "City of Lost Children, The"},
                {"searchTerm": "Ciudad de los Ninos Perdidos, La"},
                {"searchTerm": "Lost Children - The City of Lost Children"},
                {"searchTerm": "Stadt der verlorenen Kinder, Die"}
            ]
        }
        ```

    -   The `removes` array is no longer supported in clone lists. Instead, set
        a property of `"ignore": true` in the same object as a `searchTerm` in
        the `variants` array:

        ```json
        {"searchTerm": "Cite des Enfants Perdus, La", "ignore": true}
        ```

        You can also set an `ignore` at the top level to ignore every title in
        the group. In the following example, everything in the `titles` array is
        now ignored by Retool:

        ```json
        {
            "group": "City of Lost Children, The",
            "ignore": true,
            "titles": [
                {"searchTerm": "Cite des Enfants Perdus, La"},
                {"searchTerm": "City of Lost Children, The"},
                {"searchTerm": "Ciudad de los Ninos Perdidos, La"},
                {"searchTerm": "Lost Children - The City of Lost Children"},
                {"searchTerm": "Stadt der verlorenen Kinder, Die"}
            ]
        }
        ```

        As with the `removes` array, an `ignore` completely removes a title from
        Retool's consideration. You should only use `ignore` if you can't
        achieve what you want using other clone list methods.

    -  The `tagFree` name type is no longer supported in clone lists. Clone list
       capability has been improved enough that it's no longer required.

-   **_Change_**: DAT filename tags have been externalized into
    `internal-config.json` so the Retool application doesn't have to be updated
    when No-Intro makes a change.

-   **_Change_**: Closing the main Retool GUI now force closes the title tool
    if it's open, so the app quits as expected.

-   **_Change_**: Shifted some search terms from regex to strings for a small
    speed boost.

-   **_Fix_**: Depending on region settings, sometimes a superset could be
    assigned as both a parent and clone. Retool used to remove clone
    relationships in this instance to resolve conflicts, but this resulted in
    unwanted supersets being in the output DAT. It now assigns titles with the
    superset as a parent to the superset's parent instead.

-   **_Fix_**: Windows: Fixed checkboxes flickering on hover on 4k monitors.

-   **_Fix_**: Ubuntu: link colors are now more readable in dark mode, and title
    tool fields are no longer white text on a white background.


## 2.01.9 (2024-01-02)

- Added a few extra No-Intro DAT formats to take into account recent Lynx
  changes.


## 2.01.8 (2023-12-10)

-   Retool now makes better selection choices when a multi-region title is
    involved. Mostly this affects users that place Europe higher than USA in
    their region priority, however USA users might notice improvements in some
    places too, particularly when selecting single titles in preference of
    compilations.

      For example, if a DAT file contains the following titles:

      ```
      Example title (USA)
      Example title (USA, Europe) (Rev 1)
      Example title (Europe) (Rev 2)
      ```

      And you put Europe above USA in your region order, Retool used to choose
      `Example title (USA, Europe) (Rev 1)`, as it had multiple regions. Now, it
      chooses `Example title (Europe) (Rev 2)`, giving you the higher revision.

      Additionally, language selection is now weighted higher than multi-region
      selection during in-region comparison (for example, Europe versus Europe
      titles, USA versus USA titles). This results in smarter selection choices,
      particularly where European titles are involved.

      For example, if a DAT file contains the following titles:

      ```
      Example Title (Europe, Australia) (En,It)
      Example Title (Europe) (En,De)
      ```

      And your region order begins with Europe > Germany, Retool used to select
      `Example Title (Europe, Australia) (En,It)` as it had multiple regions,
      even though the title that supports German is clearly the better choice
      for the user. It now selects `Example Title (Europe) (En,De)` instead, as
      it should.

- If there are duplicate `game` nodes in an input DAT, they are now removed.


## 2.01.7 (2023-12-03)

-   Fixed a bug that would crash the clone list updater when it found unicode
    characters.

-   Fixed a bug that would crash Retool if you used an override to include some
    compilations.


## 2.01.6 (2023-12-03)

-   Added an extra code to the PlayStation 1 / 2 disc ID regex.

-   Fixed a bug where Retool wouldn't choose between two competing supersets,
    and clones wouldn't be assigned.

-   Fixed an uncommon bug that crashed Retool when the user preferred regions
    over languages.

-   Fixed some button tooltips in the GUI that incorrectly mentioned "regions"
    instead of "languages".


## 2.01.5 (2023-08-05)

-   Prevented preproduction titles being selected over modern edition titles.


## 2.01.4 (2023-07-25)

-   Actually fixed the bug where the system language list fell back to the
    global language list when empty.


## 2.01.3 (2023-07-23)

-   You can now press the `Del` key on your keyboard in the DAT, region, and
    language lists to remove the selected entry.

-   The title tool now decodes HTML entities like `&amp;` in title names.

-   The Fujitsu version code regex was modified to take into account a new
    variation.


## 2.01.2 (2023-07-22)

-   Fixed a bug where an empty system language list fell back to a global
    language list instead of using all languages.

-   Fixed a bug that crashed Retool when a trace string was entered in the
    global settings, the **Options** tab was set to override in the system
    settings, and no system-level trace string was entered.

-   Added a PlayStation Vita disc ID regex to automate one stage of choosing
    between Vita titles.

-   Added a few more demo regexes to identify different demo types.

-   When Redump or No-Intro forgot to add the `(Demo)` tag to a title's full
    name but added a category of `Demos`, Retool would append `(Demo)` to the
    full, short, tag-free, and region-free names to avoid confusion with the
    full version of the title.

    This lead to strange situations in clone lists where a title like `Example
    Title (USA) (Trial)` had a short name of `Example Title (Trial) (Demo)`.
    This behavior also wasn't taken into account for Retool GUI's title tools,
    making clone list updating harder than it needed to be for contributors.

    Now a `(Demo)` tag is only added if a title doesn't contain any of a
    collection of demo regexes, making short names more predictable to deal
    with.

-   The title tool now has a checkbox for when a title has a DAT category of
    `Demos`, which can affect how a title's names are generated.


## 2.01.1 (2023-07-16)

Looks like post filters needed a little more testing before release. The feature
now works properly.

-   Post filters now work if you don't have a system settings file for the DAT
    you're processing.

-   Post filters now remove superset titles that exist across multiple groups.

-   Post filters now remove titles that are related to compilations. Previously,
    even if a such a title was meant to be filtered out, it could randomly turn
    up in the output DAT due to the way compilations work.


## 2.01.0 (2023-07-16)

-   The **Games** title type is now an option for exclusion. Retool assume
    titles without categories assigned in the input DAT are games. For those who
    click **Select all** in the **Exclusions** tab, make sure to deselect
    **Games** if you want to keep them.

-   User filters have been renamed to overrides, since that's what they actually
    do.

-   Added post filters. After Retool has finished its processing, any title
    matches it finds in the post filter list are kept, and everything else is
    discarded. This is for those who only keep a short list of titles, but want
    to make sure they're getting the latest versions via Retool's processing
    first.

-   You can now use the original input DAT header in the output DAT. This is
    useful if you already have original Redump and No-Intro DATs in CLRMAMEPro,
    and want to treat the Retool DAT as an update.

-   Made several small tweaks to improve results for those who rank Europe
    higher than USA in their region order. This mainly results in European
    titles with languages reflecting user preferences being chosen over `(USA,
    Europe)` titles that don't specify languages.

-   During compilation comparisons, the _World_, _Europe_, and _Japan_ regions
    are considered equivalent. This was already the case for _USA_ and _World_.
    This means that individual _World_ titles can be chosen in place of _USA_,
    _Europe_, or _Japan_ compilations (and vice versa).

-   Exclusions are now much faster.

-   Fixed a bug on exclusions that caused Retool to crash.

-   Fixed a bug where Retool included more titles than it should when
    considering multi-region titles For example,
    _Bonanza Bros. (USA, Europe, Korea) (En) (Rev B)_ and
    _Bonanza Bros. (Japan, Europe) (En) (Rev A)_ were both being kept in the
    Genesis DAT. Now Retool correctly chooses only one.

-   Fixed a bug introduced in 2.00.4 where superset titles with more languages
    would be selected over higher region priority titles.

-   Fixed a bug where setting a legacy export in the system options didn't work.

-   Fixed a bug where some compilation titles weren't set to clones.

-   Made some tweaks to the GUI so the interface is more solid on Windows for
    4k, 150% scaled screens.

-   An internal automated test framework is now used when making changes to
    Retool. It checks the output of multiple different configurations, verifies
    the output is consistent, and makes it easier to pick up errors as a result
    of code changes.


## 2.00.5 (2023-05-21)

-   Fixed handling of No-Intro's quasi-RFC 3339 date format.


## 2.00.4 (2023-05-20)

-   Added another level of language selection fallback if you have a language
    order specified. If Retool finds none of the languages it's looking for in
    your language order when it compares titles, its next step is to check the
    language order derived from your region order.

    This is most beneficial for European titles when you're filtering by a
    language, and want to _preference_ but not _filter_ by other languages. You
    might want to do this when you want a title that was released in a specific
    country, but due to No-Intro and Redump naming rules gets assigned to the
    Europe region.

    For example, if a DAT file has the following titles:

    - _Example Title (Europe) (En,Fr,De,It)_

    - _Example Title (Europe) (En,Es,Pt)_

    And you have the following region order:

    1. Europe

    1. Spain

    1. Portugal

    1. France

    And you filter by English and no other language, Retool used to choose
    _Example Title (Europe) (En,Fr,De,It)_, as it contains English (the only
    language you specified in your language priority) and has the most
    languages.

    But given your region order, you've expressed a clear preference for Spanish
    and Portuguese above French.

    Now because of the new region order language fallback, the language order
    effectively becomes:

    1. English (explicitly in the language filter, and also the implied language
       for Europe)

    1. Spanish

    1. Portuguese

    1. French

    You still only get titles that support English because of the filter,
    however this means that Retool now selects _Example Title (Europe)
    (En,Es,Pt)_ instead of _Example Title (Europe) (En,Fr,De,It)_.

-   Added granularity back to the kept/removed list. Instead of filing every
    user exclusion under "category removes", Retool now categorizes under
    individual exclusions like "application", "audio", "bad dump" and so on.

-   Made heading underlines in the kept/removed list variable depending on
    heading length.

-   Fixed an index heading in the kept/removed list that incorrectly had "system
    excludes" instead of "global excludes".

-   Made some minor GUI tweaks for consistency.


## 2.00.3 (2023-05-07)

-   Due to the influx of pirate ROMs in the No-Intro NES DAT, pirate ROMs are
    now treated like bad dumps. That is, they are demoted below licensed
    variations of games, even if the pirate ROM is in a preferred language and
    the licensed version isn't.


## 2.00.2 (2023-04-30)

-   Expanded support for some newer No-Intro DATs.


## 2.00.1 (2023-04-24)

-   Expanded the demo regex to incorporate a set of Genesis demos.


## 2.00.0 (2023-04-10)

-   Fixed grouping of titles with oddly-named video standards in the filename.


## 2.00.0 Beta 9 (2023-04-07)

-   Fixed conditional override priorities not working.


## 2.00.0 Beta 8 (2023-04-07)

-   You can now drag and drop DAT files into the file list.

-   Retool now understands preproduction compilations when comparing against
    individual titles.

-   When considering compilations, individual titles are now preferred over
    compilations except in the following scenarios:

    - The compilation has a higher priority primary region than the individual
      title (during compilation comparisons, the _World_ and _USA_ regions are
      considered equivalent).

    - The compilation has a higher priority primary language than the individual
      title.

    - The individual title is set as lower priority than the compilation in the
      related clone list.

    Compilations are otherwise only included if they feature unique titles. This
    increases duplicates in the output DAT, but is much better for patches,
    retro achievements, and actually knowing which individual titles you have.

-   Compilation selection has been dramatically sped up.

-   If you overrode global settings for system languages but didn't specify any
    languages, Retool used to fall back to the global language order and disable
    the system languages override. This isn't what the label says: "an empty
    filter list includes all languages". This behavior has been changed to match
    the label &mdash; when you override system languages and leave an empty
    filter list, it first uses the implied language order from the system
    regions, and if they're not available, the implied language order from the
    global regions. In both cases, this is makes sure all languages are
    included.

-   The Python version check is now done earlier, and explains to the user the
    minimum version required.

-   The CLI progress bar no longer shows if multiprocessing is disabled, to make
    debugging with print and input statements easier.

-   Fixed a bug where compilations specified in a clone list broke user filter
    includes.

-   Fixed a bug where clone list priorities could be misassigned.

-   Fixed a bug where user-supplied regexes weren't validated for some patterns.

-   Fixed a bug where regex escapes for a title trace that were set in the GUI
    weren't interpreted properly.

-   Polished up some rough areas of code, made some minor GUI tweaks.


## 2.00.0 Beta 7 (2023-03-21)

-   System languages are now filtering correctly again.


## 2.00.0 Beta 6 (2023-03-18)

-   Fixed a compilations bug introduced with the last version that added extra
    titles to the output DAT.

-   Another fix for the parent/clone warning message.


## 2.00.0 Beta 5 (2023-03-17)

-  The GUI is now resizable.

-  GUI optimizations have been made. It's unlikely you'll notice a difference
   using it, but it's easier to maintain now.

-  Europe has been moved further up the default English region order, as
   Retool's new language prioritization bypasses any particular issues there.

-  Added an extra filter stage for compilations, checking for which title has
   more of the user's languages.

-  Fixed titles with multiple regions not being categorized into the correct
   primary region. For example, `(Europe, Australia)` titles were being filtered
   into the `Australia` region instead of `Europe`, which caused some duplicates
   to sneak through to the final output DAT.

-  The [`Export`](http://redump.org/discs/region/Ex/) region for Redump titles
   is now treated as equivalent to `World`.

-  Fixed a problem where a new system config would populate selected languages
   from the global config.

-  Fixed the log not outputting in the correct folder when a system output was
   selected.

-  Fixed the parent/clone clash warning message so it displayed the correct
   clone title.


## 2.00.0 Beta 4 (2023-03-12)

-   Pirate and unlicensed exclusions work again. Pirate titles have been added
    to the unlicensed exclude option.

-   The GUI documentation link now goes to the right place.


## 2.00.0 Beta 3 (2023-03-11)

-   Fixed user filter excludes not removing some excludes.

-   Fixed system name formatting in the GUI, so the right system settings file
    is referenced.

-   Unified CLI and GUI versions, as splitting them was no longer useful.


## 2.00.0 Beta 2 (2023-03-10)

A minor update to fix system user filters for No-Intro's _Redump Custom DATs_.


## 2.00.0 Beta 1 (2023-03-05)

Retool 2.0 is here in beta form. Ten months in the making, it'll be in beta for
a few more months to get feedback and fix bugs found by users. Retool 1.x is
still available from the [v1 branch](https://github.com/unexpectedpanda/retool/tree/v1),
although it won't receive clone list updates from this point, and issues will
only be fixed for v2.

Retool 2.0 is a hefty rewrite with a focus on static typing, better code
practices, maintainability, and making things go _faster_.

Check out how much things have improved over time, despite a huge increase in
Retool's capability (measurements taken on a Core i7-8700K, Python 3.10):

**Redump: Sony PlayStation (10628) (2021-12-29 02-47-27)**

| Retool version | DAT process time | Speed vs previous |
|----------------|------------------|-------------------|
| 0.53           | 3m, 44s          | N/A               |
| 0.62           | 28.23s           | 7.93x             |
| 1.17           | 27.15s           | 1.04x             |
| 2.00.0         | 7.76s            | 3.50x             |

Improvement 0.53 > 2.00.0: 29x speed increase

**Redump: IBM - PC Compatible (28316) (2021-07-23 22-27-03)**

| Retool version | DAT process time | Speed vs previous |
|----------------|------------------|-------------------|
| 0.53           | 20m, 56s         | N/A               |
| 0.62           | 2m, 4s           | 10.13x            |
| 1.17           | 1m, 27s          | 1.43x             |
| 2.00.0         | 14.88s           | 5.85x             |

Improvement 0.53 > 2.00.0: 84x speed increase

**No-Intro: Sony - PlayStation 3 (PSN) (Updates) (20211224-182932)**

| Retool version | DAT process time | Speed vs previous |
|----------------|------------------|-------------------|
| 0.53           | (Unsupported)    | N/A               |
| 0.62           | (Unsupported)    | N/A               |
| 1.17           | 5m, 45s          | N/A               |
| 2.00.0         | 21.72s           | 15.88x            |

Additionally, large and complex DATs like _Nintendo 3DS (Digital) (CDN)_ now
actually finish processing in a reasonable time. A Retool user [timed that DAT](https://github.com/unexpectedpanda/retool/issues/224)
to take 72,776 seconds on an Intel Core i7 8700K, which equates to 20 hours, 13
minutes. Retool v2 finishes it on the same processor in 245 seconds, which is
297x faster.

There's no doubt code in there that would still make more experienced developers
shudder, but it's nice to see things get better 😁

It's not all benefits though &mdash; Retool's increase in complexity means that
some DATs that were previously ultra-fast in v1 are slower to complete in v2:

**No-Intro: Atari - Lynx - (20220513-205052)**

| Retool version | DAT process time | Speed vs previous |
|----------------|------------------|-------------------|
| 0.53           | (Unsupported)    | N/A               |
| 0.62           | (Unsupported)    | N/A               |
| 1.17           | 0.39s            | N/A               |
| 2.00.0         | 1.83s            | 0.21x             |

The total time spent is still quite brief, and is worth the price of admission
for the very slow DATs to be faster and the increase in accuracy.

Check out the following list for other changes that have come in v2.

<h3>Accuracy</h3>

-   Language order is now taken into account. If you don't filter by languages,
    the language order will be inferred from your region order. This mostly
    impacts European titles, where compared to previous versions of Retool
    another title might be selected to better reflect your language choices. For
    example, take these titles in Redump's PlayStation DAT:

    - _Hugo (Europe)_

    - _Hugo (Europe) (Nl,Pt) (Rev 1)_

    - _Hugo (Europe) (Nl,Pt)_

    - _Hugo (France)_

    - _Hugo (Germany)_

    - _Hugo (Italy)_

    - _Hugo (Scandinavia) (Da,Fi)_

    - _Hugo (Scandinavia) (Sv,No)_

    - _Hugo (Spain)_

    If you have USA as your top region, followed by Europe, Retool 1.x selects
    _Hugo (Europe) (Nl,Pt) (Rev 1)_ as the 1G1R title, because it's the highest
    revision in Europe. Retool 2.0 realizes that because USA is your highest
    region, that it's looking for English titles as a priority, and selects
    _Hugo (Europe)_ instead.

    This also applies to say, Japanese titles that are only in English, and a
    special edition is available in English in another region. For example, take
    these titles, again in Redump's PlayStation DAT:

    - _Car and Driver Presents - Grand Tour Racing '98 (USA)_

    - _Gekisou!! Grand Racing - Total Drivin' (Japan)_

    - _M6 Turbo Racing (France)_

    - _Total Drivin (Europe) (En,Fr,De,Es,It,Pt)_

    If you have Japan as your top region, Retool 1.x selects
    _Gekisou!! Grand Racing - Total Drivin' (Japan)_ as the top title. Retool
    2.0 recognizes that the Japanese title is only in English, sees that the USA
    title is a special edition, and selects
    _Car and Driver Presents - Grand Tour Racing '98 (USA)_ instead. You may as
    well get more content if the title's going to be in the same language
    anyway.

    If you don't like this style of selection, you can turn on strict region
    filtering with `-r`.

-   Compilations are now automatically handled by adding them to a system's
    clone list with the correct syntax. Retool figures out the most optimal
    combination of titles, taking your language and region preferences into
    account. Sometimes it might look like Retool hasn't chosen the optimal
    combination, but this is usually due to user region preferences and titles
    being available in both the Europe region _and_ specific European countries.
    For example, take the following titles, and assume Italy is higher than
    Europe in the user's region order:

    - _2 Games in 1 - Disney Principesse + Il Re Leone (Italy) (It+En,Fr,De,Es,It,Nl,Sv,Da)_

    - _2 Games in 1 - Disney Principesse + Koda, Fratello Orso (Italy) (It+En,Fr,De,Es,It,Nl,Sv,Da)_

    - _Brother Bear (Europe) (Fr,De,Es,It,Nl,Sv,Da)_

    For those who don't speak Italian, _Fratello Orso_ is the Italian version of
    Brother Bear. Therefore, the most optimal solution for disk space and minimal
    redundancy is:

    - _2 Games in 1 - Disney Principesse + Il Re Leone (Italy) (It+En,Fr,De,Es,It,Nl,Sv,Da)_

    - _Brother Bear (Europe) (Fr,De,Es,It,Nl,Sv,Da)_

    This works, as both titles support Italian. However, because Italy is
    prioritized as a region, Retool selects the Italian release of _Brother Bear_
    instead, meaning you end up with:

    - _2 Games in 1 - Disney Principesse + Il Re Leone (Italy) (It+En,Fr,De,Es,It,Nl,Sv,Da)_

    - _2 Games in 1 - Disney Principesse + Koda, Fratello Orso (Italy) (It+En,Fr,De,Es,It,Nl,Sv,Da)_

    Although you get two versions of _Disney Princess_, this choice is by design.
    The assumption is that the region-specific version of the game should enable
    that region's language by default, instead of requiring a language switch
    after boot up.

-   Priority level 0 is now gone, replaced by a `supersets` array. It functions in
    almost the same way, preferring language over region, except that order in the
    clone lists doesn't determine superset priority any more. For example, here's
    how things used to look for _Persona 3_ in Redump's PlayStation 2 DAT:

    ```json
    "Shin Megami Tensei - Persona 3": [
      ["Shin Megami Tensei - Persona 3 FES", 0],
      ["Persona 3 FES", 0],
      ["Yeosin Jeonsaeng Persona 3 FES", 0],
      ["P3 - Persona 3", 1],
      ["Persona 3", 1]
    ]
    ```

    Retool used to assume the top 0 priority title had higher priority than the
    0 priority title after it, and so on. Unfortunately in this scenario, we
    have two titles that should be the same rank:
    _Shin Megami Tensei - Persona 3 FES_, the USA version, and _Persona 3 FES_,
    the European version. In Retool v1, if someone put Europe above USA in their
    region order and specified English as their highest language, they would get
    the USA title instead of the European title that they wanted, as internally
    the first 0 priority title was ranked above the second.

    With the introduction of the `supersets` array, things change a little:

    ```json
    {
      "group": "Shin Megami Tensei - Persona 3",
      "titles": [
        {"searchTerm": "P3 - Persona 3"},
        {"searchTerm": "Persona 3"},
        {"searchTerm": "Shin Megami Tensei - Persona 3"}
      ],
      "supersets": [
        {"searchTerm": "Shin Megami Tensei - Persona 3 FES"},
        {"searchTerm": "Persona 3 FES"}
      ]
    }
    ```

    Retool v2 now chooses the correct superset for the selected region, You can
    still specify a `priority` on supersets, just in case there are multiple
    supersets of varying amounts of content. That priority is _only_ respected
    between supersets, and isn't related to the priority set on a `title`.

-   You can now use regex in the `categories`, `overrides` and `variants`
    objects in clone lists. Just set the `nameType` value to `regex`. The
    `removes` object does not support regex.

-   Overrides now support a `priority` key within a `regionOrder` condition.
    This means a title's clone list priority can be set from within a condition
    if that condition is true, not just its group and short name.

-   You can now define clones in the `variants` object not just by short name,
    but full name, region-free name, tag-free name, or regex on the full name.
    While mostly you should stick to short names, this extra flexibilty can
    solve some complex problems. For example
    _Silent Hill 2 (USA) (En,Ja,Fr,De,Es,It) (v2.01)_ is the USA version of
    _Silent Hill 2 - Director's Cut_. Unfortunately, due to its title the short
    name for
    _Silent Hill 2 (USA) (En,Ja,Fr,De,Es,It) (v2.01)_ is just _Silent Hill 2_
    &mdash; exactly the same as the standard version of the game. Historically
    with Retool this would mean we couldn't set unique priorities for both
    titles, and would have to figure out an esoteric workaround. Now, however,
    there's another way:

    ```json
    {
      "group": "Silent Hill 2",
      "titles": [
        {"searchTerm": "Silent Hill 2 (?:(?!USA.*v2.01).)*$", "nameType": "regex"},
      ],
      "supersets": [
        {"searchTerm": "Silent Hill 2 (USA) (En,Ja,Fr,De,Es,It) (v2.01)", "nameType": "full"},
        {"searchTerm": "Silent Hill 2 - Director's Cut"},
        {"searchTerm": "Silent Hill 2 - Saigo no Uta"}
      ]
    }
    ```

    The first entry effectively says "Match every Silent Hill title except the
    one with USA and v2.01 in it". We then specifically call out the v2.01 title
    as a superset afterward. Mind you, this is overkill. The following example
    works just fine:

    ```json
    {
      "group": "Silent Hill 2",
      "titles": [
        {"searchTerm": "Silent Hill 2"},
      ],
      "supersets": [
        {"searchTerm": "Silent Hill 2 (USA) (En,Ja,Fr,De,Es,It) (v2.01)", "nameType": "full"},
        {"searchTerm": "Silent Hill 2 - Director's Cut"},
        {"searchTerm": "Silent Hill 2 - Saigo no Uta"}
      ]
    }
    ```

    There's also the situation where the Japanese version of _Sonic the
    Hedgehog_ is in English, _and_ features extra parallax effects the USA
    version doesn't, making it the more desirable version. Even if the user
    preferences USA above Japan, we can still select the Japanese one:

    ```json
    {
      "group": "Sonic The Hedgehog",
      "titles": [
        {"searchTerm": "Sonic The Hedgehog"},
      ],
      "supersets": [
        {"searchTerm": "Sonic The Hedgehog \\(Japan.*", "nameType": "regex"}
      ]
    }
    ```

-   Hong Kong's implied language is now Chinese. This is because the available
    titles in No-Intro are solely in Chinese.

-   India's implied language is now set to English, since all Indian Redump
    titles feature English, and there are many English-only titles.

-   Thailand's implied language is now set to nothing, as a number of Thai-only
    titles have been dumped.

-   Scandinavia's implied language is now set to nothing.

-   Iceland and Icelandic have been added to the regions and languages.

-   Retool now handles No-Intro's (Language+Language+Language) format more
    efficiently, which is used exclusively in its GBA DAT.

-   Retool now supports mastering codes for FM Towns, Nintendo, and NEC
    consoles, and uses them as a versioning system.

-   Retool now supports disc IDs of some more modern consoles and uses them as a
    versioning system.

-   Added yet another No-Intro date format, YYYY-MM-DDTHHMMSS.

-   If there are duplicate title names in a DAT, Retool renames the dupes. As a
    result, they aren't considered when selecting 1G1R titles and remain in the
    DAT. Contact the DAT author to get the title renamed, as all title names
    should be unique.

-   The Redump website scraper has been majorly overhauled, which means metadata
    is now more up to date. This tool is kept internal to prevent people from
    spamming the Redump site.

<h3>New features</h3>

-   System settings. You can now override global settings on a per-system basis.
    For example, you can set global settings that affect all of the DATs you
    process, but set unique options for Sony PlayStation that override the global
    settings when Retool processes that DAT.

-   You can now disable 1G1R mode with `-d`. This is useful if you only want to
    filter the input DAT by region, language, or excludes, and ignore all the
    parent/clone relationships. It's also useful to use with the new
    `--regionsplit` feature, which outputs multiple DATs based on the regions
    you've selected.

-   You can now prioritize titles based on their video standard, including MPAL,
    NTSC, PAL, and SECAM. This only works on titles explicitly tagged with a video
    standard in their name (for example, `(NTSC)`), and is processed _after_
    languages and regions are processed. It is mainly used as a tie breaker for
    titles that were released in the same region with multiple video standards.

-   You can now additionally output a DAT file featuring all the removed titles
    with the `--removesdat` argument.

-   You can now exclude known MIA titles and individual MIA ROMs from both
    No-Intro and Redump DATs by using `k` with the `--exclude` option.

-   You can now update clone lists directly with Retool using `--update`. The DTD
    file is now included as part of this bundle.

-   You can now specify a custom clone list to load with `--clonelist`, and a
    custom metadata file with `--metadata`. This is mostly useful if:

    - Redump or No-Intro changes their DAT names, and the clone lists/metadata
      files are no longer automatically detected.

    - You're building your own clone lists, and want to compare the output
      versus the original.

-   You can now specify a custom local path where your clone lists and metadata
    live. You can change this path in `internal-config.json` &mdash; check out
    the `localDir` subkey under `clonelists` and `metadata`.

-   You can use a different user config file than the default with the
    `--config` argument.

-   You can wrap custom exclude and include strings in `<>` to also remove all
    titles related to a match. For example, `</Fah..nheit.*>` would match
    _Fahrenheit (Europe) (En,Fr,De,Es,It)_, but also _Indigo Prophecy (USA)_ as
    they're linked together by clone lists.

-   Retool GUI now lets you to add multiple DATs, or DATs recursively in a
    folder.

-   Retool GUI now lets you drag and drop regions and languages, not just use
    the position buttons.

<h3>Quality of life updates</h3>

-   There's a [brand new Retool website and documentation](https://unexpectedpanda.github.io/retool).

-   Retool can now cope with a user entering a trailing backslash in a path in
    Windows.

-   Retool CLI now supports the * wildcard for filenames and folders.

-   You can now download `internal-config.json` if it's missing.

-   The help text in the CLI version of Retool has been reorganized to make
    things easier to parse.

-   A DTD check failure now only gives a warning, it doesn't exit Retool.
    No-Intro introduces new violations to the schema with enough frequency that
    it's not worth enforcing too strictly any more.

-   Global user filters are now located in `user-config.yaml`.

-   The Windows binary now has several files UPX packed. This means on disk the
    size of Retool is now ~30MB smaller. The compressed archive that users
    initially download has also reduced to a total of ~24MB, down from ~32MB for
    Retool v1. I suspect as a result of the UPX packing some overzealous
    anti-virus tools might raise a false positive for Retool. There's nothing I
    can do about this, the issue is with the anti-virus suite, not Retool --
    you'll just have to clear Retool to run.

-   The GUI is now written directly in QT6 instead of using the PySimpleGUI
    middleware. A lot of changes have been made, including the following
    upgrades:

    - The GUI no longer crashes if the console portion of Retool crashes. It
      simply fails to process the current DAT.

    - The issue with the layout getting messed up when the UI was dragged
      between screens of different scaling factors should be addressed. This
      mostly impacted users with both 4k and HD screens.

    - The GUI is now more horizontally rectangular, to avoid elements going
      offscreen if people have set their scaling high on low resolution monitors.

    - You now add DATs to a list to process, not just open a single file or
      folder at a time. This means you can add multiple sets of individual DATs,
      multiple folders, or multiple folders recursively to the list, in any
      combination.

    - You can now drag and drop between region and language lists, and reorder
      items in the selected region and language lists.

    - A title tool is accessible from the **File** menu. If you enter a title's
      full name from the DAT, it shows you the other names Retool assigns to it
      to work its magic. This tool is only useful if you intend to contribute to
      clone lists or Retool itself.

    - You can now change some default file locations in **Settings**, also found
      in the **File** menu.

    - **Select all** and **Deselect all** buttons have been added to the
      exclusions tab.

<h3>Performance and maintenance</h3>

-   Improved conversion of CLRMAMEPro formatted DATs to Logiqx XML, which should
    avoid some crashes and handle larger files.

-   Removed BeautifulSoup for increased performance.

-   Changed some functions to use multiple processors.

-   More accurate and readable regular expressions for tag selection.

-   Removed regex queries where not necessary, concatenated them where possible.

-   A lot of code is now statically typed for better predictability.

-   Extra data validation is now performed on clone lists. The upshot is: you
    get a warning if things aren't formatted correctly, and even if they are,
    they shouldn't crash Retool &mdash; just that clone list entry is skipped.

<h3>Developer updates</h3>

-   New clone list format. This is for consistency and to explicitly name
    features, so newcomers have a better chance of understanding what's
    going on and contributing.

    **Old style categories**

    ```json
    "categories": {
      "BASIC Programming": {
        "match": "short",
        "categories": ["Applications"]
      },
      "Color Bar Generator": {
        "match": "short",
        "categories": ["Applications"]
      }
    }
    ```

    **New style categories**

    ```json
    "categories": [
      {
        "searchTerm": "BASIC Programming",
        "nameType": "short",
        "categories": ["Applications"]
      },
      {
        "searchTerm": "Color Bar Generator",
        "nameType": "short",
        "categories": ["Applications"]
      }
    ]
    ```

    The biggest thing to call out here is that the search term is now explicitly
    named, instead of being an undefined object key. Additionally, keys now us
    camel case. Overrides have had much the same makeover:

    **Old style overrides**

    ```json
    "overrides": {
      "CD-Action 03-1997 (10B) (Poland)": {
        "new group": "CD-Action 03-1997 (10B) (Poland)",
        "match": "full"
      },
      "CD-Action 06-1997 (13B) (Poland)": {
        "new group": "CD-Action 06-1997 (13B) (Poland)",
        "match": "full"
      }
    }
    ```

    **New style overrides**

    ```json
    "overrides": [
      {
        "searchTerm": "CD-Action 03-1997 (10B) (Poland)",
        "nameType": "full",
        "newGroup": "CD-Action 03-1997 10B Poland"
      },
      {
        "searchTerm": "CD-Action 06-1997 (13B) (Poland)",
        "nameType": "full",
        "newGroup": "CD-Action 06-1997 13B Poland"
      }
    ]
    ```

    Renames have had the biggest rework. They have been renamed to _variants_, and
    are significantly more verbose. Supersets and compilations have now been split
    out into their own arrays, as they are treated differently by Retool. Most
    notably, the confusing priority `0` is no longer a thing, with that work now
    done by either the `compilations` or `supersets` array.

    **Old style renames**
    ```json
    "renames": {
      "3-D Ultra Pinball": [
        ["3-D Ultra Pinball"]
        ["3-D Ultra Pinball & Trophy Bass", "title_position", 0]
      ],
      "Black & White (Data Disc)": [
        ["Black & White - Platinum Pack", 0]
      ],
    }
    ```

    **New style variants (formerly renames)**
    ```json
    "variants": [
      {
          "group": "3-D Ultra Pinball",
          "titles": [
            {"searchTerm": "3-D Ultra Pinball"}
          ],
          "compilations": [
            {"searchTerm": "3-D Ultra Pinball & Trophy Bass", "titlePosition": 1}
          ]
        },
        {
          "group": "Black & White (Data Disc)",
          "titles": [
            {"searchTerm": "Black & White (Data Disc)"}
          ],
          "supersets": [
            {"searchTerm": "Black & White - Platinum Pack"}
          ]
        },
        {
          "group": "Trophy Bass",
          "compilations": [
            {"searchTerm": "3-D Ultra Pinball & Trophy Bass", "titlePosition": 2}
          ]
        }
    ]
    ```

    Not seen here: you can add `priority` and `nameType` keys to each object in
    the `titles`, `compilations`, and `supersets` arrays. See the documentation
    for more information.

-   All user messages now go to STDERR instead of STDOUT. If you redirect the
    STDOUT with >, <, or >>, the only output is now the data of the final
    filtered DAT. This is most useful for those who build their own scripts and
    want to chain tools together.

-   There's a new `--trace` argument that you can use to trace a title's journey
    through Retool. It's useful when you're trying to figure out where something
    unexpected happens, and don't want to insert a bunch of print and input
    statements. It works on regex matches and is very verbose, so be careful
    with precision. Running a trace disables file output and multiprocessor
    operation in some places, as it's intended for testing only.

-   There's a new `--singlecpu` argument that you can use to run Retool on just
    one CPU. Python doesn't like `input` statements when it's running things
    across multiple processors, so use this argument if you're debugging
    multiprocessing parts of the code.

-   There's a new `--nodtd` argument that bypasses Logiqx's DTD validation.
    Despite quoting it in their DATs, No-Intro and Redump don't validate against
    the DTD schema. This effectively hides the warning that the input DAT isn't
    compliant.

-   All classes and functions now have consistent docstrings so people
    (including myself) have a chance to figure out what's going on.

-   You can add the `@perf_test` decorator to any function to run memory and
    time tests.

-   There's a new `config` object that gets passed around a lot, which contains
    almost all the settings Retool needs to operate. Because it's quite large,
    it can be browsed interactively by running `print(config)` where the
    `config` instance is available. This should help those new to the codebase,
    or myself when I'm trying to track down bugs or haven't looked at the code
    in a while.

-   The `input_dat` object can now be browsed interactively just like the
    `config` object. It contains all the information about the DAT the user has
    fed into Retool.

-   Incidentally, the objects that contain the titles (DatNode objects) can also
    be printed to show the title's information in a tree-like fashion.


## 1.18 (2022-08-27)

-   A small change to handle a new versioning system in No-Intro.


## 1.17 (2022-08-05)

-   Retool can now handle No-Intro DATs that reference an XSD file.


## 1.16 (2022-07-14)

-   The `<name>` tag in the output DAT header has been changed so CLRMAMEPro
    recognizes DAT updates between Retool versions.

-   The order of `<rom>` attributes has been changed in the output DAT to match
    that of the in-progress Retool v2. This is mainly to help with internal
    testing.

-   A message has been improved that tells a user when Retool can't find titles
    that match their preferences.


## 1.15 (2022-07-09)

-   Titles that have invalid filename characters
    (`:`, `\`, `/`, `<`, `>`, `"`, `|`, `?`, `*`) in DATs now have those
    characters removed or replaced with valid ones. No-Intro metadata is
    also checked for invalid filename characters.


## 1.14 (2022-07-01)

-   Ring code version checking is now turned on for FM-Towns.

-   The `(Homebrew)` tag is now recognized.

-   When you exclude unlicensed titles, that now includes aftermarket and
    homebrew titles.

-   Unlicensed titles now get demoted if there's a production title in the same
    region.

-   Clone lists and metadata have been moved to their own [repository](https://github.com/unexpectedpanda/retool-clonelists-metadata).
    This is in preparation for the shift to Retool v2.

-   Retool CLI now prompts you to download clone lists and metadata if it finds
    the `clonelists` or `metadata` folders missing.


## 1.13 (2022-05-22)

-   The `(Headered)` and `(Headerless)` tags No-Intro were adding to the new NES
    DATs caused Retool to not associate them with the NES clone list. This has
    now been fixed.


## 1.12 (2022-05-21)

-   Retool now brings over ROM manager directives in headers, including header
    skippers. This should resolve issues around things like headered DATs.


## 1.11 (2022-05-21)

-   Fixed how Retool searches for `rom` attributes to avoid incorrect substring
    matches. Retool should no longer crash on game names that contain `mia`.


## 1.10 (2022-05-20)

-   Updated Retool to support `mia` attributes on `rom` elements.


## 1.09 (2022-05-17)

-   Updated Retool to support `header` attributes on `rom` elements.


## 1.08 (2022-05-12)

-   Updated Retool to support SHA256 hashes.


## 1.07 (2022-04-23)

-   Changed the way Retool handles versions to deal with more complex version
    systems introduced in recent No-Intro DATs. Some version selections are now
    more accurate as a result.

-   Retool can now handle empty `<url>` tags in DAT headers.


## 1.06 (2022-03-24)

-   The `release` tag now copies the `game name` attribute, instead of the
    `description` tag. This is because No-Intro started using descriptions in
    the GBA DAT that were different from the name.

-   The `(Deprecated)` tag is now ignored in DAT file names when matching to
    clone lists and metadata.


## 1.05 (2022-02-24)

-   Fixed a region selection regex bug which caused Retool to crash when
    including files with specific regex custom filters.

-   Added a more specific error message for DATs with no games.

-   The DTD was updated to make `size` an optional attribute of `rom`.


## 1.04 (2022-01-09)

-   Fixed a bug where _(United Kingdom)_ titles in No-Intro DATs were being
    recognized as _(Unknown)_ titles as well.


## 1.03 (2022-01-02)

-   The Satellaview-specific `(Magazine)` tag has been added to the multimedia
    filter.

-   The `(DEBUG)` tag has been added to the preproduction filter.


## 1.02 (2022-01-02)

-   Fixed a Sega ring code version comparison bug.

-   The N-Gage-specific tag `(Full Trial)` has been added to the demos filter.

-   The N-Gage-specific tag `(Review Kit ##)` has been added to the
    preproduction filter.

-   Fixed errors in the Redump scraper that stopped Croatian and Slovakian being
    added as a language to the metadata.

-   Added new languages: Albanian, Indonesian, Latvian, Macedonian, Serbian.

-   Added metadata languages: Catalan, Estonian, Gaelic, Hindi, Lithuanian,
    Punjabi, Tamil, Ukranian.


## 1.01 (2021-10-28)

-   Fixed an issue where titles assigned to `BIOS` in a clone list weren't
    removed if a user had selected to remove BIOSes.


## 1.00 (2021-10-19)

-   Fixed an issue where multiple regions caused a crash when determining the
    implied language of a title.


## 0.99 (2021-09-10)

-   Fixed an issue where titles on the system include list wouldn't be
    recovered.


## 0.98 (2021-09-04)

-   Fixed an issue where if a title was reassigned to the `Demos` category, and
    was also featured in the `renames` object of a clone list, the clone
    wouldn't be assigned.


## 0.97 (2021-07-08)

-   Fixed titles with manually set categories in clone lists being erroneously
    added to remove lists when the `--log` option was set.


## 0.96 (2021-07-04)

-   Fixed DATs with an empty author field causing a crash.


## 0.95 (2021-06-28)

-   Fixed a bug where a combination of modern editions and the `(Unl)` tag
    caused the wrong 1G1R title to be selected when the user preferred modern
    ripped titles over the original.

-   Added an option to not replace `(Unl)` or `(Aftermarket)` titles if a
    production version is found in another region.

-   The Retool version used to create a DAT is now recorded in the DAT header to
    assist with troubleshooting.

-   Fixed a bug where "&amp; Retool" was added multiple times to the author
    field of a DAT previously processed by Retool.

-   Fixed a QT issue where the Retool icon wouldn't load properly on Windows.


## 0.93 (2021-06-01)

-   Fixed a crash for Linux users by adding conditionals to the new Windows CLI
    code.

-   Removed Colorama import accidentally left in when fixing Windows formatting.


## 0.92 (2021-05-31)

-   Retool CLI no longer clears the screen on start. Turns out this was also
    accidentally enabling VT-100 mode in Windows 10 (which allows ANSI codes
    like color formatting and bold to work), so there's now some new code to
    manually enable it instead.

-   You can now manually assign categories to titles in clone lists using the
    `categories` key. This is a highly manual task, and will only be maintained
    through user submissions.

-   You can now include titles that don't have hashes, ROMs, or disks specified.
    This might allow the conversion of DATs from parties other than No-Intro or
    Redump &mdash; these DATs aren't officially supported.

-   Files now write in UTF-8 to avoid characters causing crashes.

-   Enhancement chips are now set to the category `BIOS` in the output DAT.

-   Added some new modern edition tags.

-   Titles with the `(Aftermarket)` tags are now demoted below official ones
    within the same region.
-   Titles with the `(Prerelease)` tag are now treated as preproduction.

-   The regex for capturing demo titles is now more comprehensive.

-   Added Estonia & Lithuania as regions, along with their languages.


## 0.91 (2021-04-19)

-   Fixed a crash when processing the Mega CD/Sega CD DAT, and Europe or USA was
    not included in the region order.

-   Specified in the GUI that custom filters are case sensitive.


## 0.90 (2021-04-15)

-   Excluding demos now also excludes kiosk titles, and matches some extra
    strings for trial versions.

-   Excluding videos now excludes trailers as well.


## 0.89 (2021-04-12)

Things of note for this release:

-   The way supersets and compilations are handled has changed. Supersets are
    now default 1G1R titles. Compilations sometimes get removed, sometimes
    become 1G1R titles depending on region order/situation. Right now you won't
    see much difference outside of Master System &mdash; the point of this
    version was to get the functionality out, then the clone lists can be
    updated later.

-   Custom global/system includes now recover files from
    countries/languages/type exclusions. Grab that one title you want from
    Japan, or save that one demo while excluding the rest.

<h3>New features</h3>

-   Custom global or system filter includes can now force inclusion of titles
    that have been removed due to:

    - Region exclusions.

    - Language exclusions.

    - Any of the exclusion options being set in Retool.

-   Stat calculation now reports removals due to country and language filters.

-   Titles with the string "Game Boy Advance Video" are now removed when videos
    are excluded.

-   You can now set a custom URL to update from in `internal-config.json`. This
    means should the clone lists stop being updated at the main Git repository,
    someone else can more easily take over.
-   Titles with the category "Add-Ons" and "Bonus Discs" can now be excluded.
-   Clone lists now have Retool minimum version requirements. The user will be
    prompted in the command line output whether to continue or not if Retool is
    out of date compared to what the clone list requires.

<h3>Bug fixes</h3>

-   Stat calculation of custom global/system filters would crash Retool when
    `--nofilters` was set. This has been fixed.

-   Stat calculation of the dat's final title count has been fixed to include
    custom global/system includes.

-   Fixed a potential problem when outputting a 1G1R list with a web/ftp
    protocol prefix.

-   Fixed Retool GUI not remembering output folders or exclusion settings.

-   Updated a few dependencies.

<h3>Behavior changes</h3>

-   Tried to capture general crashes in order to give feedback to Retool GUI
    users, to help diagnose future issues.

-   Overrides and conditional overrides in clone lists are now merged into just
    overrides. They can also now match on full or tag free names. Note that some
    key names have changed &mdash; anything with an underscore in the name has
    been replaced by a space.

-   For the longest time, I kept matches as case sensitive just in case there
    was an oddity along the way. Turns out for the sake of Windows users not
    having problems this isn't the case, so all titles now get lowercase
    matched. This should help with clone list resilience as naming standards
    change over time.

-   Things started getting confusing with compilations and supersets when it
    came to choosing a 1G1R title. This was always an incredibly grey and fuzzy
    area, was a pain to maintain, and it became apparent over time that things
    needed to change for the sake of clarity. The upshot of all this? You get a
    better 1G1R selection without having to select the right options.

    Things that have changed:

    - Mega-CD 32x now gets hoisted above Sega CD 32x if you have Europe above
      USA in your region order.

    - A `removes` key is now available to use in clone lists to remove specific
      titles from a DAT. It works with full, tag free, or short names. This is
      mostly useful to take out titles that don't quite match anything, but
      should still be removed &mdash; for example, compilations whose titles are
      covered by other compilations, or individual titles in the same region.

    - The supersets option has been removed. It was nice to have in theory, but
      in practice, game of the year editions, special editions, and so on are
      mostly just the latest versions of games with bonus content and/or DLC
      included.

      There are incredibly rare exceptions &mdash; such as _Ninja Gaiden_ vs
      _Ninja Gaiden Black_, where dramatic rebalancing was done in addition to
      the extra content, along with new enemies and weapons &mdash; but for the
      most part, this isn't the case. If you care enough about an older version
      of a game, you can always add it to a custom system filter.

      Supersets are now often assigned a 1 or 0 priority, depending on the
      situation.

    - The exclude compilations option has been removed, and compilations are now
      usually treated in one of two ways:

      - As a remove; that is, the compilation is removed entirely from the DAT
        as it's covered by other titles or compilations.

      - As the 1G1R title for a set, depending on the region.

    - The guidelines for when to use a 0 priority in clone lists have changed
      because of this. You can use a 0 for:

      - Compilations that include multiple titles.

      - DVD releases of titles that are distributed as multiple CDs for other
        releases.

      - World releases that should be elevated above USA (as a World release
        includes USA).

      - A superset (gold edition, game of the year edition, etc) version of a
        title available in one region, but not in another.

      - A title in one region that definitely has more content than another
        region. For example, a release in Europe that's uncensored compared to
        the US release.


## 0.88 (2021-03-01)

Things of note for this release:

-   A key bug fix for clone list resilience.

-   A lot of command line options have changed.

-   Windows binaries no longer live in the `/dist/` folder, as it was becoming a
    download burden to those cloning the repo.

<h3>New features</h3>

-   You can now exclude Manuals.

-   Excluding BIOSes now also excludes enhancement chips.

-   Excluding applications now excludes titles with "Check Program" and "Sample
    Program" in their name.

-   A lot has shifted around in terms of Retool CLI arguments, so Retool can
    continue to grow:

      - The `-o` option is now `--output`.

      - The `-g` option has been removed to bring things in line with Retool
        GUI.

      - A new `--exclude` option that takes arguments is now used in place of a
        lot of the old filter options. Check `-h` for the full list.

-   Output file names are now a tiny bit smaller in length. User options and
    title counts are now at the end of the file name too, so sorting by alpha
    doesn't get confusing.

-   Added yet another beta tag variation.

-   In Retool GUI, the user is now prompted to download clone lists if they
    don't have any.

<h3>Bug fixes</h3>

-   If a key title in a clone list didn't exist in an input DAT (or had been
    removed by a Retool option), then all other titles in that array would
    become unlinked from one another. This has been fixed.

-   Fixed inaccurate and missing removal stats.

-   Fixed the program crashing if a prefix or suffix wasn't supplied when
    exporting a 1G1R list.

-   In Retool GUI, the up/down region priority buttons no longer crash the
    program if a region hasn't been selected.

-   Made sure release tags output consistently in legacy mode.

<h3>Behavior changes</h3>

-   The demotion of modern ripped titles (for example, Virtual Console) is now
    working cross-region. You'll still get them if the modern edition is the
    only one available with a language associated with a higher region priority.
    For example, sometimes English versions of games were only released much
    later on modern platforms, whereas previously they had exclusive Japanese
    releases. In this case, if you have an implied English speaking region high
    up in your region order, the modern edition will remain.


## 0.87 (2021-01-24)

Some big changes this time around, including some requested features.

<h3>New features</h3>

-   There are now user-customizable exclude and include filters, so you can keep
    or remove specific titles regardless of what Retool thinks should be done
    with them. You can set filters as partial strings, full strings, or regex.
    It's fairly advanced, so read the documentation to see how it works.

-   You can now output lists of what titles have been kept, removed, and set as
    clones by Retool GUI, just like Retool CLI. Check the **Modes** tab for the
    option.

-   You can now output a list of just the 1G1R title names, and optionally add
    your own prefix or suffix to each line. Starting a prefix with http://,
    https://, or ftp:// will URL encode each line.

-   The binary version for Windows now opens a heck of a lot faster, at the cost
    of having a much messier folder structure. Formerly everything was packed
    into a single executable, which meant the operating system had to extract
    all the dependencies before it could even think about launching the program,
    slowing things down.

<h3>Bug fixes</h3>

-   Rewrote the parent assignment code to correct misassignment issues in the
    NES DAT. It turns out this results in fixes for other sets too, requiring
    clone list changes. For accurate matches, you must update to Retool 0.87 to
    use the latest clone lists.

-   Fixed a bug that removed titles from the United Kingdom from No-Intro DATs.

-   Can now handle the new (DV #, #) versioning in No-Intro's FDS DAT without
    crashing.

-   Fixed the clone list/metadata update thinking that there was a new file if
    the original had been converted from CRLF to LF. Made sure all new clone
    lists and metadata are converted to LF before uploading to the repo.

-   The PlayStation Portable No-Intro and Redump DATs now refer to separate
    metadata from their respective databases.

-   Numbered samples are now removed when excluding demos and samples, for
    example `(Sample 1)`, `(Sample 2)` and so on.

-   Those using font scaling > 100% in Windows 10 should no longer have Retool
    GUI's layout be thrown all over the place, so long as they stick to the
    provided scaling levels. Note that Retool GUI on Windows 7 and 8 isn't
    supported.

-   Ubuntu users now get the Ubuntu font in Retool GUI. The UI is also slightly
    scaled to avoid text inside buttons being cut off.

-   Removed font colors, styles and fancy terminal things when running Retool
    CLI on Windows 7 and 8, as those versions of Command Prompt don't support
    them. Things still look shiny on Windows 10 and modern Linux terminals.

-   Stopped the command line instructions showing when Retool GUI was processing
    a DAT.

-   The lxml module has been updated, as GitHub advised of a security flaw with
    the previously used version.

-   Fixed dependency problems when running `updateclonelists.py` from the
    command line.

<h3>Behavior changes</h3>

-   More titles ripped from modern platform rereleases (such as Virtual Console
    titles in the SNES DAT, for example) have been demoted by default, as they
    don't necessarily play well (or at all) in emulators. You can make these
    titles the preferred 1G1R title instead with the `-v` option, or by
    selecting the
    **Titles ripped from modern platform rereleases replace retro editions**
    checkbox in Retool GUI.

-   Good titles are now preferred over bad (`[b]`) ones.

-   No-Intro pre-production titles are now categorized properly in the output
    DAT.

-   Updating clone lists now downloads `internal-config.json` as well, as
    updates to this file affect 1G1R title selection.

-   Retool now identifies Redump BIOS titles by the category `Console`, and
    they'll be removed if you excluded BIOSes. BIOS titles are also now assigned
    the category of `BIOS` in the output DAT.

-   Release tags are now only output in legacy mode. They also generate for
    every region and language of a title, not just the primary region. This is
    just tying a bow on Logiqx-style 1G1R parent/clone DAT files, 1G1R modes in
    DAT managers still aren't very useful.

<h3>Internal changes</h3>

-   `user-config.yaml` is no longer stored in the GitHub repo. It's also been
    removed from Windows ZIP file. This is to prevent users accidentally
    overwriting their own `user-config.yaml` when updating Retool. Both Retool
    CLI and GUI auto-generate the file if it's missing.

-   Metadata is now in alphabetical order.


## 0.86 (2020-12-21)

-   Modern rereleases like Virtual Console titles have been demoted in priority,
    as quite often emulators won't play them.

-   Now includes scraped language data from No-Intro for more accurate language
    filtering.

-   You can now exclude titles that contain the string `[BIOS]`. This should
    only apply to No-Intro DATs.

-   Excluding applications now additionally excludes titles with the string
    `(Test Program)`.

-   Removed a few unused properties from metadata files, which greatly reduced
    file sizes.

-   `-i` removed from `-g` option as some titles are used for soundtracks in
    games.


## 0.85 (2020-11-18)

-   Updated the date sorting to take into account another of No-Intro's
    inconsistent date formats `(Month name, YYYY)`.

-   Another tweak to the ordering of the output DAT.


## 0.84 (2020-11-14)

-   Updated the Sega ring code regex so more ring codes are captured.


## 0.83 (2020-11-09)

-   Accidentally uploaded the wrong `user-config.yaml`, where all regions were
    commented out. This resulted in the CLI version of Retool finding no clones
    unless manually edited by the user. This has now been fixed.

-   Some code clean up and extra explanation for some options.


## 0.82 (2020-11-08)

-   (Unl) titles in a higher region are now demoted below equivalent production
    titles in other regions.

-   You can now exclude by the "Audio" and "Video" categories.

-   Removed Multimedia from the `-g` option as the category might contain games.

-   Made clear that the Multimedia category might include games in the GUI.

-   Explained what a coverdisc is in the GUI.

-   Fixed a natural sort bug in the alphabetical ordering of output DATs.


## 0.81 (2020-11-06)

-   Fixed a bug in `retool-gui.py` where the output DAT file had ` (-)` in its
    file name if no options were set.

-   Fixed a bug where clone lists and metadata wouldn't download if their
    respective folders didn't exist.


## 0.80 (2020-11-05)

-   Retool can now handle No-Intro numbered DATs.

-   Output DATs used to do alphabetical order based on group, which could look
    like things were out of order if you didn't know what was happening behind
    the scenes. Output DATs are now ordered based on title.

-   Updated wording around enabling the supersets option, so it was clear that
    if you turned it on, supersets would replace standard editions in the output
    DAT.

-   Added some extra tooltips to the exclusion options in the GUI, so users have
    more information to work with.


## 0.79 (2020-10-19)

-   Fixed the online updating of clone lists to include Redump metadata.


## 0.78 (2020-10-1)

-   Implemented a GUI. You'll need to install `pysimpleguiqt` with pip, and
    after that you can run it with `retool-gui.py`. It's not as tight and
    consistent as it could be due to limitations with PySimpleGUIQt, but given
    PySimpleGUI's rapid, active development this should improve over time. Right
    now it looks best on Windows. Ubuntu has been tested, and looks a little
    janky, but is functional. MacOS hasn't been tested.

-   You can now run `updateclonelists.py` to download the latest clone lists.
    There's also an option available in the GUI under the File menu.

-   Reformatted `user-config.yaml` so strictyaml liked it a bit more, and things
    played well with the GUI. Improved YAML handling at the same time. Make sure
    to backup your current `user-config.yaml` before grabbing this version, so
    you can port your region order/language settings over.

-   Moved to argparse to handle user input in the CLI. It's less pretty, but
    it's more robust and scalable. This also means that the `-i` option is no
    longer a thing when specifying your input dat/folder &mdash; instead,
    specify it immediately after `retool.py`:

    `retool.py <input dat/folder> <options>`

-   Stopped misassignment in clone lists if Redump left off the `(Demo)` tag
    from a title.

-   Fixed an exit bug when the user would select only regions and/or languages
    that didn't exist in the input DAT.

-   Added a few promote tags.

-   Cleaned up some unused variables and imports.

-   Lots of code tweaks to better suit GUI interaction.

-   The `-g` option now keeps applications, as they are useful for computer
    platforms like the Atari ST and Commodore Amiga.

-   The new `-y` option outputs a list of what titles have been kept and removed
    in the output DAT.

-   Refactored how Retool options get listed in the output name.

-   Removed requirement for the !DOCTYPE element to exist that quotes the Logiqx
    DTD, so Retool can work with files from sites.dat. The DAT is still
    validated against the DTD, however.

-   Dealt with an edge case in selecting the right title if somehow there was
    both a version _and_ a revision of a title.

-   Hid displaying options behind the `-?` option.


## 0.76 (2020-08-03)

-   Fixed filtering by language. This was broken due to a last minute change
    from a string to regex in the 0.75 release.

-   Fixed folders not being processed to completion when filter by language was
    selected, and no valid titles were found in the current DAT.

-   Added `Ukranian` as a language.

-   When filtering by language, if titles in the following regions don't have
    languages specified, they will be included if you select any of their
    respective languages:

      - Asia &mdash; English, Chinese, Japanese.

      - Hong Kong, Taiwan &mdash; Chinese, English.

      - Latin America &mdash; Spanish, Portuguese

      - South Africa &mdash; Afrikaans, English

      - Switzerland &mdash; German, French, Italian

      - Ukraine &mdash; Ukranian, Russian.

-   Retool can now handle `rom` entries with no CRC specified. A `rom` entry
    must have at least a CRC, MD5, or SHA1, otherwise the title is dropped.

-   The `-g` option now keeps preproduction titles, as they're treated as
    versions of titles instead of a separate thing, and many will be removed
    automatically on account of production versions existing. You will need to
    specify `-p` if you want to remove all preproduction titles.


## 0.75 (2020-28-07)

-   Now handles No-Intro DATs. Note that Retool grouping follows different rules
    to No-Intro. For example, in the Atari 2600 DAT, a compilation is listed as
    a clone of a single title, despite featuring unique games. No-Intro also
    tends to include demos as clones of production titles. Retool also doesn't
    set clones for BIOSes, as you might need a different BIOS version in
    different situations. Retool also ignores titles that don't have `rom` or
    `disk` entries, which happens quite a bit in No-Intro's parent/clone sets.

-   Added `Mexico` and `Hong Kong` as regions.

-   Added `Zh-Hant` and `Zh-Hans` as languages.

-   Alphas, betas, and prototypes are now treated as versions of titles. This
    way you get the highest version of a title available, and less noise without
    stripping everything away with the `-p` tag. Retool prefers production
    versions of titles, even if there is a preproduction title in a higher
    priority region. Priority is as follows:

      - Production with highest version

      - Production with highest revision

      - Production with no version/revision

      - Highest beta revision

      - Highest alpha revision

      - Highest prototype revision

-   The exclude coverdiscs flag is now `-f`.

-   You can now exclude bad dumps, pirate titles, promotional titles (titles
    that contain `(Promo)`, `EPK`, and `Press Kit`), and samples.

-   Retool can now deal with DATs that fail DTD validation due to `<clrmamepro>`
    and `<romcenter>` tags being in an unexpected order in the header.

-   The DTD file has been updated to take into account that even though people
    include it in their XML files, their XML files don't actually validate
    against it.

-   Retool can now deal with DATs that don't include MD5 or SHA-1 hashes.

-   Windows and MacOS binaries have been removed. The Windows binary had
    performance issues due to the Python environment needing significant start
    up time, and I can no longer build the MacOS binary after the virtual
    machine stopped working.

-   Some crash fixes and message format tweaking.

-   Moved internal-config.json to the clonelists + metadata file so new releases
    of Retool aren't required each time the file is updated.


## 0.70 (2020-06-15)

Oof, this is a big update, with feature and performance improvements all over
the place.

<h3>Code readability and performance</h3>

Retool has been largely rewritten for readability, performance, security, and
to make forward momentum easier. This means a few breaking changes:

-   A new format for clone lists, so you need to update them. Retool is now
    better at automatically detecting different types of clones, so some titles
    no longer need to be listed in the clone lists.

-   The selected 1G1R titles might change compared to previous versions of
    Retool, due to a major audit of clone lists, tags, and increases in parent
    detection accuracy.

-   Retool no longer exports parent/clone DATs by default. Turns out the format
    can't really do the job properly, as it has no concept of priority within
    individual regions (and dealing with languages is a misery). As such, using
    DAT managers like CLRMAMEPro or Romcenter to manage 1G1R can lead to
    unexpected outcomes. Instead, you now use Retool to produce the 1G1R DAT you
    want, and only use the DAT manager to manage your files.

-   Retool now has a minimum requirement of Python 3.8.

Processing DATs is now also much faster as a result of better coding practices.
While this is nice for all DATs, you'll mostly feel it on the big ones.
The PlayStation and IBM DATs, for example, are now 2x faster.

<h3>Custom region orders, filter by language</h3>

Custom region orders are now supported &mdash; even for supersets. You can
also filter by languages. Make your choices by editing the `region order` and
`filter languages` sections in `user-config.yaml`. You can use the `-l` option
to filter by language, or leave it off to include all languages.

<h3>Other language and region stuff</h3>

Retool's a lot smarter with languages now.

For a start, implied languages are now enabled for most regions, and language
data for titles has been scraped from Redump's site. Redump doesn't always
include language data in the filename of their titles, so this assists in more
accurately selecting parent titles. For example, say your region priority is
USA, Europe. The USA title has CDs, but the European title has a DVD version
that we now know for sure supports English. Retool can now choose the European
DVD version over the USA CD version, depending on how clone lists are set up.

The following things have also changed:

-   A bunch of languages (`Af`, `Ca`, `Gd`, `Hr`, `Pa`, `Sk`, `Sl`, `Ta`) have
    been added.

-   Slovenia has been added as a region.

-   The incorrect `Gr` language code has been changed to `El`.

-   Multi-region titles are now handled more elegantly.

-   Fixed tags with regions in them causing a title to be filtered into the
    wrong region. For example, _Virtua Fighter 2 (Europe) (Rev A) (Made in USA)_
    used to be categorized as a USA title &mdash; it's now correctly identified
    as a European title.

<h3>Other updates</h3>

-   You can now exclude unlicensed titles.

-   Sega ring codes are now mostly handled automatically for assigning clones.
    This has greatly reduced the size of some clone lists.

-   Retool can now deal with "cloneof" tags in input DATs, as Redump has started
    adding a few.

-   Retool now handles Genteiban, Fukyuuban, and many other editions
    automatically.

-   If the user specifies an output folder that doesn't exist, that folder is
    now created.

-   Fixed problems that previously required overrides in clone lists.

-   Added basic failure states for not finding required data in JSON config
    files.

-   DAT header details are now escaped for valid XML, and XML file error
    handling is better.

-   A bug in CLRMAMEPro DAT conversions has been fixed.

-   DAT file output is now naturally sorted instead of lexicographically.

-   The decision to include the version of a title on the newest operating
    system has been reversed. For the sake of compatibility, if there are
    multiple OS versions for a title, all are included.


## 0.60 (2020-04-19)

-   Removed pointless milliseconds from output file name.

-   Added "Scholastic" to the publisher/distributor list.

-   Added more disc synonyms.

-   Automated handling PlayStation EDC titles.

-   Language codes removed: `At`, `Be`, `Ch`, `Hr`.

-   Languages codes added: `Bg`, `Cs`, `He`, `Ro`, `Tr`.

-   Regions added: Bulgaria, Romania. There are no games yet from these regions,

    but there are games with their languages.

-   Extracted configuration data from the main Python script, and moved it into
    an external JSON file. This can potentially lead to greater user
    customization later.


## 0.59 (2020-03-30)

-   Added "Best of the Best" and "Best Hit Selection" as
    publishers/distributors.

-   Added another disc synonym.


## 0.58 (2020-03-30)

-   Added yet another disc synonym.

-   Added "Hitsquad - Regenerator" as a publisher/distributor.

-   Removed `_version.py`.


## 0.57 (2020-03-25)

-   Separated removing coverdiscs from demos (`-d`), making it its own option
    (`-b`). Turns out plenty of full version games were given away as
    coverdiscs.

-   Made handling the XML definition in a DAT a bit more robust.

-   Fixed importing of CLRMAMEPro DAT files.

-   When a parent or clone of a superset, override, or compilation title is not
    found, it no longer crashes Retool or silently fails, but tells you what's
    missing.

-   Added "Teil" as a synonym for "Disc", to automatically pick up some German
    titles.

-   Added a `-g` option, which is shorthand for all options (-abcdemps).

-   Added Th as a language.

-   Converted clone lists to JSON so they're more portable, and binaries don't
    require an update every time the clones update.

-   Fixed a bug in selecting supersets.

-   Noted that supersets only currently really work if you follow Retool region
    order. Otherwise current limitations in DAT format and DAT managers get in
    the way.


## 0.56 (2020-03-06)

-   Messed with the region order a little to be more fair to more popular
    languages, taking in mind how many titles were actually released for those
    languages.

-   Bumped Portuguese up the priority list when deciding between two identical
    titles that support different languages.

-   Moved stuff out of `readme.md` to make it more readable, and created a
    GitHub wiki for more detailed information.


## 0.55 (2020-03-05)

- Code changes to support a build pipeline.


## 0.54 (2020-03-04)

-   Greatly sped up parent/clone processing, and removed XML conversion in favor
    of writing directly to the output DAT. This will be mostly noticeable for
    large DATs. The IBM and PlayStation Redump DATs, for example, now process
    around 10x faster, cutting a minutes long process for each into seconds on
    an i7 8700K.

-   Added another distributor/publisher to check for when scanning for clones.

-   Removed the option to remove titles with Alt tags, as it was a leftover from
    when Retool didn't do 1G1R properly.

-   Added a counter for how many compilations were removed, if the option is
    enabled.


## 0.53 (2020-02-24)

-   Fixed a bug where if a region name was in a title, it caused clones to be
    assigned to the wrong parents. For example,
    _Daytona **USA** Deluxe Edition (Taiwan)_,
    _Cossacks II - Battle for **Europe** (Germany)_ would confuse the logic in
    Retool as to what region the title belonged to.

-   Fixed a normalization bug when converting _Disc III_ into _Disc 3_ for title
    matching.


## 0.52 (2020-02-22)

Added better parent selection for the following:

-   Titles with multiple date versions.

-   Titles with distributor/publisher, OEM, and covermount tags.

-   Budget titles vs the originals.


## 0.51 (2020-02-16)

-   Added Zh as a language.

-   Fixed a crash if a DAT had no titles, and Retool was trying to process
    supersets.


## 0.50 (2019-11-26)

-   A huge architectural shift to move Retool to a 1G1R DAT generator. Due to
    this, the `_regional_renames.py` file has been renamed to `_renames.py` and
    massively expanded to take into account local title dupes. The file has
    also been reorganized to make future dupe additions easier.

-   The `-re`, `-ra`, and `-en` options have been removed.

-   The `-o` flag is no longer mandatory, and now defines an output folder.
    Output files are automatically named.

-   You can now remove alternate (Alt) titles with the `-l` option.

-   You can now promote supersets (for example, Game of the Year editions) to
    parents with the `-s` option.

-   Expanded demo removal criteria, as Redump does not always put demos in the
    "Demos" category.

-   Region processing is now much faster.

-   OEM and Hibaihin titles that have a matching commercial title with the same
    name are now marked as clones.

-   Titles that aren't the latest revisions or versions are now marked as
    clones. This doesn't support release versioning, like 0.100 being larger
    than 0.99, however there's not much evidence of that style of versioning
    being used across Redump titles.

-   Titles that include multiple regions are now deduped, preferencing titles
    with more regions. For example, out of _Grim Fandango (USA)_ and
    _Grim Fandango (USA, Europe)_, the former is marked as a clone.

-   Titles with the same name from the same region that include different
    language sets are now handled. The rules are quite complex:

    - If one title is in English, but the other isn't, mark the English title as
      the parent.

    - If one title from Europe has no languages listed, and the other has
      languages listed but English isn't one of them, mark the title with no
      languages listed as the parent (on the assumption that English may be in
      there).

    - If English is listed for both titles, and one title has more languages,
      mark the title with more languages as the parent.

    - If English is listed for both titles, and both titles have the same number
      of languages, check for preferred languages one by one, in the order
      listed below. The first title that doesn't support a preferred language is
      marked as a clone.

        1. Spanish

        1. French

        1. Japanese

        1. Portuguese

        1. German

        1. Italian

        1. Swedish

        1. Danish

        1. Norwegian

        1. Polish

        1. Greek

        1. Dutch

        1. Finnish

        1. Swiss

        1. Hungarian

        1. Russian

-   Brazil and Latin America have been moved off the native English list. Modern
    games from these regions aren't guaranteed to have English translations.

-   Japan has been moved up to second highest priority for non-native English
    regions, after Europe. The Asia region being higher priority than Japan was
    stealing titles that should have had Japanese parents.

-   The requirement for the Logiqx doctype string in input files has been
    removed, as some non-Redump DATs didn't have the string and were erroring.

-   DTD validation has been added for Logiqx-style DAT files. Redump DAT files
    are invalid by default, as the category tag isn't in the spec. A modified
    DTD file has been included in the release with the category tag added, so
    Redump DATs should pass.

-   When you add a newer version of a DAT to CLRMAMEPro that has been generated
    by Retool, it now triggers an update prompt where appropriate.

-   Redump is no longer required to be the DAT author.

-   Characters that aren't valid in XML (<, >, &) have been escaped in generated
    DAT files.

-   Empty name, description, author, url, and version fields in DATs are now
    handled, instead of crashing the program.

-   Several bugs involving options flags were fixed.

-   The title count was missing when DATs were split into regions. This is now
    fixed.

-   Bye bye ASCII logo. Vertical screen real estate is now more important.

-   Added CloneRel tool, that exports an Excel file from a DAT to better display
    existing parent/clone relationships.

-   Dealt with the "_King's Field_ problem". _King's Field (Japan)_ didn't get a
    Western release. _King's Field_ in the USA is known as _King's Field II_ in
    Japan. _King's Field II_ in the USA is _King's Field III_ in Japan. Without
    extra logic, the program would mark all _King's Field II_ titles as clones,
    which is not what we want.


## 0.34 (2019-10-29)

-   Added textwrap module for better readability on MacOS/Linux.

-   Bundled MacOS and Windows binaries.


## 0.33 (2019-10-27)

-   Added ability to operate on folders.

-   Fixed output file naming bugs.

-   Fixed some user input issues.

-   Tidied up some output for increased readability.

-   Added the following regions: Argentina, Czech, Hungary, Singapore, Slovakia,
    Thailand, Turkey, Ukraine, United Arab Emirates.


## 0.32 (2019-10-24)

-   Reimplemented `-re` and `-ra` flags.

-   Fixed header so the user wasn't prompted with false update warnings when the
    DAT was loaded in CLRMAMEPro.


## 0.31 (2019-10-22)

-   Used dictionaries and classes to greatly increase performance and improve
    code readability.

-   Removed minidom dependency.

-   Removed unused importlib dependency.

-   Usability tweaks.


## 0.20 (2019-10-06)

-   Refactored for performance, code readability, and usability.

-   Can handle CLRMAMEPro DAT files now, not just Logiqx XML format.

-   Added Germany, Ireland, Israel, Latin America, New Zealand, and Taiwan
    locales.

-   Fixed user input bugs.

-   Fixed excessive looping in some sections.

-   Fixed title exclusion bugs.

-   Added more error checking.

-   Removed `-re` and `-ra` flags until refactor is finished next version.


## 0.10 (2019-10-05)

-   Initial release.
