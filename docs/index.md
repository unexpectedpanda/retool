---
hide:
  - footer
---

![Retool logo](images/retool.png){: style="height:150px;width:150px"}

# Retool

!!! info "Retool is no longer maintained"
    [Read the thread](https://github.com/unexpectedpanda/retool/issues/337) for more
    information on what this means.

Retool is a filter utility for [Redump](http://www.redump.org/) and [No-Intro](https://datomatic.no-intro.org/index.php?page=download)
DAT files. By customizing the DAT files before you load them into a ROM manager, you can more
effectively trim, consolidate, and deduplicate your ROM sets.

![A screenshot of the main Retool screen](images/main-app.png)

Retool offers the following features:

* [Superior One Game, One ROM (1G1R) functionality compared to other tools](retool-1g1r.md).

* Priority-based region and language filtering.

* Exclusions of unwanted title types like demos, applications, and more.

* Custom regular expression filters for including or excluding titles.

* Local filenames for titles, such as ``シャイニング●フォースⅡ 『古の封印』` instead of
  `Shining Force II - Inishie no Fuuin`.

* CLI and GUI versions.

You add your DAT files to Retool, and it creates new DAT files with all your preferences,
leaving the originals intact. You can then load the new DAT files in a ROM manager like
[RomVault](https://www.romvault.com/), [CLRMamePro](https://mamedev.emulab.it/clrmamepro/),
or [IGIR](https://www.igir.io) to do your file management &mdash; you just don't need to
use their 1G1R modes, as Retool has already done the work for you.

[**Download Retool**](download.md){:style="font-size:1.2em;"}
