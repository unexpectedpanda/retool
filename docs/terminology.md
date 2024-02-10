---
hide:
  - footer
---

# Terminology

Retool inherits a lot of terminology already established by ROM managers, and adds its
own. This page contains the definitions for many of the terms used in Retool and its
documentation.

## 1G1R

"One game, one ROM." Putting aside the fact that not everything is a ROM, 1G1R
is an ideal that states that for the many, many different versions of a single
title that are available around the world, you should only really possess one.
It then becomes a question of which one... which is what Retool is designed to
help with.

## Clone lists

Clone lists are JSON files that manually define relationships between titles
that Retool ordinarily wouldn't automatically pick up. They're useful both for
matching titles of completely different names, and for overriding some of the
default choices that
Retool makes.

## Compilations

A title that in itself contains multiple titles. They might be from the same series of
games, a single publisher, or completely unrelated.

## DATs/DAT files

Short for "data files", they're called DATs or DAT files because they usually
have the extension `.dat`. They contain a catalog of titles, usually focused on
a single system like the Atari 2600 or Sega Master System. A DAT file often
contains attributes for each of its titles, including file names, hashes, and
sizes.

Used in combination with a ROM manager, the information in a DAT file can be
used to audit files on your hard drive to ensure that they are named correctly,
and that they match the recorded attributes in the file.

DAT files usually follow one of two standards: either a variant on the XML-based
[LogiqX](https://github.com/SabreTools/SabreTools/wiki/DatFile-Formats#logiqx-xml-format)
format, or the less commonly used [CLRMAMEPro](https://github.com/SabreTools/SabreTools/wiki/DatFile-Formats#clrmamepro-format)
format. There are [many more](https://github.com/SabreTools/SabreTools/wiki/DatFile-Formats)
less common formats.

[Retool supports DAT files released by two groups](dat-support.md): No-Intro and Redump.

## Implied languages

An implied language is the dominant language for a region. For the USA, it's English,
Brazil has an implied language of Portuguese, and so on. Implied languages are used when a
title doesn't have languages listed explicitly in its name, or in an associated
metadata file. They're also used when a user doesn't set an explicit language priority
&mdash; when this happens, Retool builds an implied language priority based on the user's
region choices.

Implied languages help Retool to determine the intent of a user when it comes to selecting
a 1G1R title. For example, if a user has set the following region order:

1.  USA

1.  Canada

And Retool is considering the following titles:

```
This is a title (USA) (Es)
This is a title (Canada)
```

If the user doesn't explicitly set any language priorities, Retool implies from the choice
of USA as the top region that the user's preferred language in this situation is English,
and the USA title in this example only supports Spanish.
It also knows that English is the dominant anguage in Canada, and so even though that
title has no explicit language tags, there's a good chance it's in English. In this
scenario, even though USA is ranked higher than Canada, the Canadian title is chosen as
it has a higher chance of being in English.

Some regions don't have an implied language. For example, a title from Asia could be in
Chinese, Japanese, English, or otherwise, but because you can't tell without explicit
data, an implied language isn't assigned.

## Metadata files

Metadata files are JSON files that contain scraped data from No-Intro's and Redump's
websites. They're stored in the `metadata` folder, and are used to provide extra language
information and local title names not included in DAT files.

## Parents and clones

DAT files can mark titles as being a "clone" of a "parent" title &mdash;
effectively setting up a relationship between two or more titles. Some DAT files
are even marked as specifically containing parent/clone relationships, and these
relationships are used to produce the [poor standard of 1G1R experienced in most
other tools](retool-1g1r.md).

The parent/clone concept comes from [MAME](https://www.mamedev.org), and enables
one of the ways in which it organizes its ROMs. In a [split set](https://docs.mamedev.org/usingmame/aboutromsets.html#parents-clones-splitting-and-merging),
the parent ROM contains the base or common files for a game, and is often the
latest version of a game. It is in itself a complete version of a game. Clone
ROMs, on the other hand, only contain files that are different from the parent.
If you load a clone game in MAME, it's smart enough to load the required base
files from the parent, and then any of the modified files it needs from the
clone to create a full title.

This existing parent/clone infrastructure in DAT files was taken advantage of by
No-Intro as a way to introduce 1G1R into its sets. The parent and clone
designation starts to lose meaning here, as all ROMs, discs, or otherwise are
complete titles in No-Intro, not a series of files. In this scenario it doesn't
matter which title is designated as a parent or clone in the DAT &mdash; it's
just a way to indicate a relationship so ROM managers can select a 1G1R title
based on a user's region and language preferences.

In the case of Retool, when using this terminology every title that's related to each
other is considered a clone. The selected 1G1R title is called exactly that &mdash; the
1G1R title.

## ROM managers

ROM managers read DAT files, and organize files on your hard drive according to
the data found inside those DAT files. They are primarily used to verify that
you have a known good dumps of ROMs or disc images according to certain datting
groups like [No-Intro](https://datomatic.no-intro.org/index.php?page=download),
[Redump](http://www.redump.org), and [TOSEC](https://www.tosecdev.org/), and
authors of emulators like [MAME](https://www.mamedev.org).

The most popular ROM managers are [CLRMamePro](https://mamedev.emulab.it/clrmamepro/) and
[RomVault](https://www.romvault.com/). If you've never used a ROM manager before, the
learning curve can be quite steep.

## Supersets

Supersets are versions of titles that contain more content, or for some reason
are superior to another version. This might include, for example, a Game of the
Year edition, an all-in-one pack that bundles a game and all its DLC, or a DVD
version of a title previously released on multiple CDs.

Occasionally a superset might be a title with a minor advantage compared to the others in
its group: for example, the Japanese version of _Sonic the Hedgehog_ is in English, but
compared to the USA version has additional parallax effects. _Fahrenheit_, the European
version of _Indigo Prophecy_ has uncensored content. These are still considered supersets.

!!! warning "Caution"
	Censorship or licensing changes aren't always a reason for designating something as a
	superset. Quite often such changes involve a simple sprite or palette swap that
	doesn't materially affect a game, and there's no guarantee there weren't other bug
	fixes included along the way. If you disagree with a choice Retool makes, you can
	always [set your own overrides](how-to-use-retool-gui-overrides-post-filters.md).

## Tags

Tags indicate properties of a title, and are usually appended to a title's name in a DAT
file. They are always surround by parentheses. For example, `(USA)`, `(Disc 1)`,
`(En,De)`, `(Special Edition)` and so on.

## Titles

Entire games or applications. A title has properties, like a name, the regions it was
released in, the languages it supports, and more. In an XML-based DAT file, it's often
represented by the `<game>` node.
