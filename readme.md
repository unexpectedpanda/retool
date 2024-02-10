# Retool

> [!TIP]
> **This is the source repository for Retool. For downloads, installation instructions, and
  documentation, see the [website](https://unexpectedpanda.github.io/retool/).**

Retool is a filter utility for [Redump](http://www.redump.org/) and [No-Intro](https://datomatic.no-intro.org/index.php?page=download)
DAT files. By customizing the DAT files before you load them into a ROM manager, you can more
effectively trim, consolidate, and deduplicate your ROM sets.

![A screenshot of the main Retool screen](https://unexpectedpanda.github.io/retool/images/main-app.png)

Retool offers the following features:

* Superior One Game, One ROM (1G1R) functionality compared to other tools.

* Priority-based region and language filtering.

* Exclusions of unwanted titles like demos, applications, and more.

* Custom regular expression filters for including or excluding titles.

* Local filenames for titles, such as <code>`シャイニング●フォースⅡ 『古の封印』</code>
  instead of <code>Shining Force II - Inishie no Fuuin</code>.

* CLI and GUI versions.

You add your DAT files to Retool, and it creates new DAT files with all your preferences,
leaving the originals intact. You can then load the new DAT files in a ROM manager like
[RomVault](https://www.romvault.com/), [CLRMamePro](https://mamedev.emulab.it/clrmamepro/),
or [IGIR](https://www.igir.io) to do your file management &mdash; you just don't need to
use their 1G1R modes, as Retool has already done the work for you.

Retool is supported on Windows 10+, Ubuntu 20+, and macOS 10+ on x86 processors. It should
work on M-series MacBooks too, however I don't own the hardware to test it. Non-binary
versions require Python 3.10 or higher.

## Contribute to Retool

If you've found something Retool has missed, like a clone or a local name for a title, you
can contribute to Retool's clone lists at their [dedicated repository](https://github.com/unexpectedpanda/retool-clonelists-metadata).
