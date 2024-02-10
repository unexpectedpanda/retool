---
hide:
  - footer
---

# DAT file support

While Retool understands both [LogiqX](https://github.com/SabreTools/SabreTools/wiki/DatFile-Formats#logiqx-xml-format)
and
[CLRMAMEPro](https://github.com/SabreTools/SabreTools/wiki/DatFile-Formats#clrmamepro-format)-formatted
DAT files, it only has support for DAT files released by certain groups based on their
naming conventions.

## Supported

DAT files are supported from the following groups.

### :fontawesome-regular-circle-check:{: .greentick} No-Intro

[No-Intro](https://datomatic.no-intro.org/index.php?page=download)
DAT files are supported, in both LogiqX(ish) and their newer XSD-validated format.

Clone lists exist for the more popular sets, and contributions are always welcome for both
maintenance and providing new lists.

### :fontawesome-regular-circle-check:{: .greentick} Redump

[Redump](http://www.redump.org) DAT files are supported in both LogiqX(ish) and CLRMAMEPro
formats. DAT files derived from Redump that keep the same title names are also supported.

Clone lists exist for most sets except IBM PC Compatible, which is too huge and has far
too much activity without community contribution to maintain.

## Unsupported

While anything not in the supported list should be considered unsupported, there are two
sets in particular that need to be called out, as from time to time there are requests to
add support. It is unlikely Retool will ever support these DAT files.

### :fontawesome-regular-circle-xmark:{: .redcross} MAME, FBNeo, and other arcade sets

There's a reason there isn't a decent 1G1R solution for [MAME](https://www.mamedev.org)
and [FBNeo](https://github.com/finalburnneo/FBNeo) DAT files &mdash; the data structure
doesn't lend itself to that sort of processing. The lack of naming standard in the DAT
descriptions also makes it extremely challenging to automate anything, meaning the most
likely path for 1G1R is an inflexible, curated, massive, high-effort list that needs
frequent updating. This isn't a path Retool is going to take.

You can, however, get a filtered MAME DAT file with the following options:

* Do a web search for `All killer no filler`. These are lists and tools that filter MAME's
  ROMs to only the top games as defined by their authors.

* [Arcade Manager](https://github.com/cosmo0/arcade-manager) can handle filtering MAME
  sets, including removing bad and non-working ROMs, and comes with built-in lists for the
  "top" sets and "all killer no filler".

* [RomLister](https://www.waste.org/~winkles/ROMLister/) and
  [Lightspeed Game List Generator](http://forum.arcadecontrols.com/index.php?topic=150785.0)
  haven't been updated for a long time, but there are a lot of options in them to sate your
  filtering desires.

### :fontawesome-regular-circle-xmark:{: .redcross} TOSEC

While [TOSEC](https://www.tosecdev.org/) DAT files are in LogiqX format, support for their
naming system hasn't been built into Retool.

Support is technically possible, but largely pointless to implement without also supplying
clone lists. This isn't a small effort &mdash; with over 3,000 TOSEC DAT files as of 2022,
and with TOSEC's tendency to include many, many variants, there'd have to be significant
community effort not only to bridge that gap, but to test the clone lists too. At this
point in time, the momentum doesn't exist to justify the work.
