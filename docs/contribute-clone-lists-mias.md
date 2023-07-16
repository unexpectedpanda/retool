---
hide:
  - footer
---

# MIAs

A missing in action (MIA) title is one that has had its sizes and hashes indexed, but the
title itself hasn't been made available to the public.

The `mias` array is only required in clone lists for Redump DAT files, as No-Intro
specifies MIAs directly in its DAT files. MIAs are scraped from [Redump's wiki](http://wiki.redump.org/index.php?title=MIA_Lists),
and as a general rule shouldn't be manually added or removed.

An `mias` array looks similar to the following example:

```json
"mias": [// (1)!
  "Arc the Lad III (Japan) (Demo 2)",// (2)!
  "Cochons de GuerreLes (France) (Rev 1)"
]
```

1.  The MIAs array.
2.  The full name of the title to search for in the input DAT file.

MIAs only use [full names](../naming-system/#full-names) to search for matching titles in
the associated DAT file, and so an `mias` array only contains strings that match those
full names.
