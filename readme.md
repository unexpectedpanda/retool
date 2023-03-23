# Retool

> **:mega: Retool v2 is now available**
>
> Retool v2 is much faster, with several new features and better accuracy.
>
> A working version of Retool v1 is still available for download from the [v1 branch](https://github.com/unexpectedpanda/retool/tree/v1),
however it's unsupported and issues should only be filed for v2. Clone lists and metadata
are only being updated for v2.

**This is the source repository for Retool. For downloads, installation instructions, and
documentation, see the [website](https://unexpectedpanda.github.io/retool/).**

Retool filters [Redump](http://redump.org/) and [No-Intro](https://www.no-intro.org/)
DATs, offering the following features:

* Superior One Game, One ROM (1G1R) functionality compared to other tools.

* Priority-based region and language filtering.

* Exclusions of unwanted titles like demos, applications, and more.

* Custom regular expression filters for including or excluding titles.

* CLI and GUI versions.

You feed Retool an input DAT, and it creates a new DAT from it with all your preferences,
leaving the original intact. You can then load that new DAT in a ROM manager
like [CLRMamePro](https://mamedev.emulab.it/clrmamepro/), [RomVault](https://www.romvault.com/),
or [Romcenter](https://www.romcenter.com/) &mdash; you just won't need to use their
1G1R modes, as Retool has already done the work for you.

Retool is supported on Windows 10+, Ubuntu 20+, and macOS 10+ on x86 processors. It should
work on M-series MacBooks too, however I don't own the hardware to test it. Non-binary
versions require Python 3.10 or higher.

![A screenshot of the main Retool screen](https://unexpectedpanda.github.io/retool/images/main-app.png)

## Contribute to clone lists

You can contribute to Retool's clone lists at their [dedicated repository](https://github.com/unexpectedpanda/retool-clonelists-metadata).
