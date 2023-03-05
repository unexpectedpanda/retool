---
hide:
  - footer
---

# Clone lists and metadata files

**Clone lists** are JSON files that primarily define relationships between titles that
Retool doesn't automatically pick up. They're useful both for matching titles of
completely different names, and for overriding some of the default choices that Retool
makes. Additionally, they can add more accurate filter criteria like different categories
to titles. They are manually curated, and pull requests are welcome.

**Metadata files** are also JSON files, contain scraped data from the No-Intro and Redump
sites, and are used to provide extra language information not included in DAT files. They
are generated, and as a general rule shouldn't be manually edited.

!!! info
    No-Intro no longer provides DB downloads for some systems, such as
    Nintendo Entertainment System, Super Nintendo, and Nintendo 3DS. As such, some
    metadata files are out of date and the title names might not match those used in their
    respective DAT files. Although this is unfortunate, there are still many matches
    inside those metadata files which keep them relevant.

Clone lists are stored in the `clonelists` subfolder, and metadata files are stored in the
`metadata` folder. Retool selects the correct clone list and metadata files for the loaded
DAT by checking the `<name>` and `<url>` tags in the header of the DAT file,
and then looking for a matching filename with the release group appended in the
`clonelists` and `metadata` folders &mdash; for example,
`Sony - PlayStation (Redump).json`. If a matching file isn't found, then only Retool's
automatic clone detection is used.

## Update clone lists

Clone lists and metadata files are updated every now and then to match the latest DAT
files. When processing new DAT files, it's a good idea to check for clone list updates
first.

!!! info
    Sometimes clone list functionality needs to be changed to support new features. To
    ensure things work as intended, make sure you're always running the latest version of
    Retool.

To update clone lists and metadata files, complete the following instructions:

=== ":fontawesome-regular-window-maximize: GUI"
    Click **File > Update clone lists**.

=== ":simple-windowsterminal: Command line"
    In your terminal or command prompt, enter the following command:

    ```
    retool.py --update
    ```

    !!! Info
        Depending on your operating system, all Python commands in this guide might need
        to be prefixed with `python` or `python3` to work.

## Edit and create clone lists

You can [contribute to Retool's clone lists](../contribute-clone-lists) to help make them
more accurate.