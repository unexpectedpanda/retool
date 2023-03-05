---
hide:
  - footer
---

# Why Retool's 1G1R is better

Standard ["One Game, One ROM" (1G1R)](../terminology/#1g1r) has problems.

[Way back in 2008](https://forum.no-intro.org/viewtopic.php?f=2&t=544) Eric Bole-Feysot
raised that 1G1R would be an appealing concept to implement in No-Intro DAT files. The
various groups involved at the time ultimately settled on repurposing the existing
[parent/clone](../terminology/#parents-and-clones) implementation established by [MAME](https://www.mamedev.org),
added an extra `<release>` tag to define what region a title was from and what languages
it supported, and built user-enabled 1G1R support into ROM managers to select titles based
on the user's region and language preferences. It was, at the time, enough.

As DAT files became more detailed, 1G1R filtering failed to keep pace.

## The problems with ROM manager 1G1R and parent/clone DAT files

The criteria for 1G1R title selection outside of Retool is based purely on regions and
languages, and the way ROM managers like CLRMAMEPro and Romcenter handle this is far from
ideal. For a more code-focused approach to how this works, check out
[LogiqX's pseudo-code on the No-Intro forums](https://forum.no-intro.org/viewtopic.php?f=2&t=544)
(search the page for "I do this kind of thing for a living").

The code essentially sets up the following standard:

1.  Titles are given a score based on a combination of region and language priorities
	provided by the user.

1.  Regions are more important than languages.

1.  Titles should be prioritized _and_ filtered by user-defined regions.

1.  Languages are added as a prioritized bonus score to a title's region score. They
	should not be used as a filter.

Unfortunately, this creates a few problems.

### The language filter/priority problem

The existing parent/clone algorithm creates uncomfortable situations like the
following. For example, consider a DAT with the following three titles:

```xml
<game name="Test Title (Canada) (Fr)">
    <description>Test Title (Canada) (Fr)</description>
    <release name="Test Title (Canada) (Fr)" region="Canada" language="Fr"/>
    <rom crc="00000000" md5="00000000000000000000000000000000" name="Test Title (Canada) (Fr).bin" sha1="0000000000000000000000000000000000000000" size="100000000"/>
</game>
<game name="Test Title (Japan)" cloneof="Test Title (Canada) (Fr)">
    <description>Test Title (Japan)</description>
    <release name="Test Title (Japan)" region="Japan" language="Ja"/>
    <rom crc="00000000" md5="00000000000000000000000000000000" name="Test Title (Japan).bin" sha1="0000000000000000000000000000000000000000" size="100000000"/>
</game>
<game name="Test Title (Norway)" cloneof="Test Title (Canada) (Fr)">
    <description>Test Title (Norway)</description>
    <release name="Test Title (Norway)" region="Norway" language="En"/>
    <rom crc="00000000" md5="00000000000000000000000000000000" name="Test Title (Norway).bin" sha1="0000000000000000000000000000000000000000" size="100000000"/>
</game>
```

You want to filter the DAT in a 1G1R fashion, and you only speak English. You set your
regions in an order that you hope should give you a balance between English titles and
higher frame rates courtesy of NTSC:

1.  Canada

1.  Japan

1.  Norway

As insurance, you set your languages in an order that prioritizes English:

1. En

1. Ja

1. Fr

A cursory look at the XML data shows that the Norwegian title is the _only_ one
that supports English, and is arguably what the user would want.

What title gets chosen in CLRMAMEPro's 1G1R process? _Test Title (Canada) (Fr)_, because
Canada is the highest priority region.

What if you remove _Fr_ from the language list? You still get _Test Title (Canada) (Fr)_,
as languages are treated as a bonus score, not a filter.

### The version problem

The current DAT and ROM manager ecosystem doesn't have a concept of versioning. Say you
have the following titles in a DAT file:

```xml
<game name="Test Title (USA) (v1.2)">
    <description>Test Title (USA) (v1.2)</description>
    <release name="Test Title (USA) (v1.2)" region="USA" language="En"/>
    <rom crc="00000000" md5="00000000000000000000000000000000" name="Test Title (USA) (v1.2).bin" sha1="0000000000000000000000000000000000000000" size="100000000"/>
</game>
<game name="Test Title (USA) (v1.1)" cloneof="Test Title (USA) (v1.2)">
    <description>Test Title (USA) (v1.1)</description>
    <release name="Test Title (USA) (v1.1)" region="USA" language="En"/>
    <rom crc="00000000" md5="00000000000000000000000000000000" name="Test Title (USA) (v1.1).bin" sha1="0000000000000000000000000000000000000000" size="100000000"/>
</game>
<game name="Test Title (Europe) (v0.6)" cloneof="Test Title (USA) (v1.2)">
    <description>Test Title (Europe) (v0.6)</description>
    <release name="Test Title (Europe) (v0.6)" region="Europe" language="En"/>
    <rom crc="00000000" md5="00000000000000000000000000000000" name="Test Title (Europe) (v0.6).bin" sha1="0000000000000000000000000000000000000000" size="100000000"/>
</game>
<game name="Test Title (Europe) (v2.0)" cloneof="Test Title (USA) (v1.2)">
    <description>Test Title (Europe) (v2.0)</description>
    <release name="Test Title (Europe) (v2.0)" region="Europe" language="En"/>
    <rom crc="00000000" md5="00000000000000000000000000000000" name="Test Title (Europe) (v2.0).bin" sha1="0000000000000000000000000000000000000000" size="100000000"/>
</game>
<game name="Test Title (Europe) (v1.1)" cloneof="Test Title (USA) (v1.2)">
    <description>Test Title (Europe) (v1.1)</description>
    <release name="Test Title (Europe) (v1.1)" region="Europe" language="En"/>
    <rom crc="00000000" md5="00000000000000000000000000000000" name="Test Title (Europe) (v1.1).bin" sha1="0000000000000000000000000000000000000000" size="100000000"/>
</game>
```

If you set USA as the top priority region in your ROM manager, you get whatever title is
marked as the parent, in this case, _Test Title (USA) (v1.2)_.

However, if you set Europe as the top priority region, since the parent is from the USA,
you get something unexpected. In CLRMAMEPro, you get whatever is the first European title
in the DAT file: in this case _Test Title (Europe) (v0.6)_. In RomCenter, you get whatever
is the last: in this case _Test Title (Europe) (v1.1)_. In both cases, the wrong version of
the title gets selected: it should be _Test Title (Europe) (v2.0)_.

### The broader priority problem

These issues expand beyond language issues and easily identifiable versions: how do you
deal with versions vs revisions? Production vs preproduction? How about Hibaihin/Not for
Resale titles? What about disc IDs used by the likes of PlayStation? Or OEM titles or
release dates? What do you do when you have a production title in a lower priority region,
but only an unlicensed, badly dumped, or preproduction version in a higher priority
region? How do compilations play a part, or supersets like _Game of the Year_ editions,
or DVD rereleases of games that were originally on multiple CDs?

There are numerous questions like these that crop up when trying to determine the best
possible 1G1R title to select, which is complicated again by user defined and ordered
regions and languages, and their own specific curation desires.

### The human problem

Parent/clone DAT files are generally administered by hand. There's no automatic logic that
highlights that titles might be related as a human enters them into a database &mdash;
they need to manually make that link themselves, and be aware that the clones of multiple
different names might exist. On a single DAT with multiple contributors, where the focus
can be "DAT all the things" over attention to detail, this lends itself to oversights and
clones being missed.

## What Retool does differently

Retool ignores the parent/clone data manually entered into DAT files, and analyzes title
names to automatically group them together. It makes use of [clone lists](../clone-lists)
to not only close the gap where automatic detection doesn't work out, but to recategorize
and prioritize titles accordingly.

It doesn't use a scoring system based on region and language to determine which title to
pick, but instead puts titles through a series of filters based on detailed criteria. It
makes use of scraped data from Redump and No-Intro's websites to provide additional
language details not present in title names.

Finally, it can treat languages as both a filter _and_ something that should have higher
priority than regions, although you can absolutely prioritize regions if you desire.

Want to know more? Find out how [Retool works](../how-retool-works).