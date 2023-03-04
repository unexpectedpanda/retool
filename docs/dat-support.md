---
hide:
  - footer
---

# DAT support

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
formats. DAT files derived from Redump that keep the same title names, such as those from
[dats.site](https://dats.site/custom_system_datslist.php), are also supported.

Clone lists exist for most sets except IBM PC Compatible, which is too huge and has far
too much activity without community contribution to maintain.

## Unsupported

While anything not in the supported list should be considered unsupported, there are two
sets in particular that need to be called out, as from time to time there are requests to
add support. It is unlikely Retool will ever support these DAT files.

### :fontawesome-regular-circle-xmark:{: .redcross} MAME and other arcade sets

Filtering [MAME](https://www.mamedev.org) DAT files is an entirely different beast, and a
massive undertaking to do well. The naming scheme is different, the things you can filter
on are different, and whether arcade or software list support, huge amounts of data need
to be parsed to do it justice. It's more than enough work just keeping up with No-Intro
and Redump.

Thankfully there are other options for MAME filtering:

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

While [TOSEC](https://www.tosecdev.org/) DAT files are in LogiqX
format, support for their naming system hasn't been built into Retool.

Support is technically possible, but largely pointless to implement without also supplying
clone lists. This isn't a small effort &mdash; with over 3,000 TOSEC DAT files as of 2022,
and with TOSEC's tendency to include many, many variants, there'd have to be significant
community effort not only to bridge that gap, but to test the clone lists too. At this
point in time, the momentum doesn't exist to justify the work.