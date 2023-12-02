---
hide:
  - footer
---

# How Retool works

This is a technical piece, and is best suited to developers who want to create similar
functionality for their tools. It's correct as of Retool v2.01.6.

Retool has two primary functions:

1.  To filter DATs based on user criteria, including:

    * Language preference

    * Region preference

    * Title type (for example, demo, preproduction)

    * User-defined strings

1.  To discover titles that have relationships with each other, and use that to implement
    [1G1R](terminology.md#1g1r). It does not make use of existing parent/clone data found in DATs.

Retool uses the following data sources to achieve this:

* **The input DAT file itself**. This includes data like the title filename, category, and
  statuses (for example, "missing in action"). Relevant information is broken down into
  consituent parts for Retool to use later, for example, regions, languages, revisions,
  and so on.

* [**Clone lists**](clone-lists.md). Manually curated files that establish relationships
  between titles where automatic detection fails. Also used to break relationships where
  Retool gets automatic detection wrong.

* [**Metadata files**](clone-lists.md). These contain language data taken from Redump
  and No-Intro's databases. Metadata is generally updated every few months. Redump's
  site is scraped, whereas No-Intro databases are manually downloaded to generate the
  metadata.

Titles are put through a series of stages in a specific order, with many stages acting
like filters that remove candidates that don't meet specific criteria.

!!! note "A note about updating clone lists and metadata"
    Clone lists and metadata need to be kept regularly up to date to ensure Retool's
    effectiveness. When they stop updating, Retool gradually becomes less accurate over
    time as changes are made to DATs. Automatic detection picks up a lot, but it's not
    foolproof, especially as vital information is regularly missing from the DATs
    themselves.

    Users are more likely to notice when Retool gets out of sync with No-Intro than
    Redump, particularly in the chaotic NES DAT.

    Redump's naming structure tends to be more standardized than No-Intro, there tends to
    be more title additions than updates, and its website can be easily scraped for
    metadata updates. A good cadence for Redump updates might be once every month, two at
    the most.

    No-Intro is more of a problem. It's prone to making sweeping naming changes across its
    database, and isn't particularly great at adhering to its own standards. I suspect a
    lack of validation in its backend and a lot of free text fields are at fault, along
    with multiple contributors who don't necessarily agree on how a title should be named
    or classified.

    This means that every now and then No-Intro makes an epic change that breaks things,
    which can mean updates are required for clone lists, metadata files, the Retool
    application, or sometimes all three. It also means that the ideal cadence for Retool's
    No-Intro updates is every few weeks, a pace that's hard to keep for a site that
    covers so many systems.

    You can download most system databases directly from No-Intro's Dat-O-Matic site,
    and these serve as the source for Retool's metadata. However, databases are not
    available for all systems. The database daily packs are often bugged or out of date,
    requiring you to download individual databases. The site also has incredibly
    aggressive anti-flood protection that can block access to resources and slows down the
    process. This makes keeping No-Intro data up-to-date an incredibly time consuming and
    frustrating task.

## Stage 1: Parsing the input DAT

The DAT file is read in by Retool. An object is created from each `<game>` node that contains
useful information about the title. It's supplemented with data from additional sources,
namely manually curated clone lists, and metadata scraped from Redump and No-Intro's site.

```xml title="Metal Gear Solid (USA) (Disc 1) (Rev 1), from Redump's Sony - PlayStation DAT"
<game name="Metal Gear Solid (USA) (Disc 1) (Rev 1)">
    <category>Games</category>
    <description>Metal Gear Solid (USA) (Disc 1) (Rev 1)</description>
    <rom name="Metal Gear Solid (USA) (Disc 1) (Rev 1).cue" size="105" crc="f2ac185c" md5="91fc49ae51815d04c3bb4384e9fe8bd7" sha1="bb026baeb18f92365172c93494c07381f76bb8cd"/>
    <rom name="Metal Gear Solid (USA) (Disc 1) (Rev 1).bin" size="705614112" crc="21b5d15d" md5="e31ce17570897c323b7a539a2c616c72" sha1="37498e6598ce4eabf00630b6a9197b20861e55a0"/>
</game>
```

```ini title="The object Retool builds that represents Metal Gear Solid (USA) (Disc 1) (Rev 1)"
○ full_name:                  Metal Gear Solid (USA) (Disc 1) (Rev 1) # (1)!
├ numbered_name:              None # (2)!
├ description:                Metal Gear Solid (USA) (Disc 1) (Rev 1) # (3)!
├ region_free_name:           Metal Gear Solid (Disc 1) (Rev 1) # (4)!
├ tag_free_name:              Metal Gear Solid (USA) (Disc 1) # (5)!
├ short_name:                 metal gear solid (disc 1) # (6)!
├ group_name:                 metal gear solid # (7)!
├ regions:                    ('USA',) # (8)!
├ primary_region:             USA # (9)!
├ secondary_region:           None # (10)!
├ languages_title_orig_str:   None
├ languages_title:            None
├ languages_implied:          ('En',)
├ languages_online:           ('En',)
├ languages:                  ('En',)
├ cloneof:                    None
├ is_superset:                False
├ contains_titles:            None
├ clonelist_priority:         1
├ region_priority:            0
├ language_priority:          0
├ exclude_reason:             None
├ include_reason:             None
├ exclude_include_related:    False
├ categories:                 ['Games']
└ roms ┐
       ├ name: Metal Gear Solid (USA) (Disc 1) (Rev 1).cue | header: None | mia: None | crc: f2ac185c | md5: 91fc49ae51815d04c3bb4384e9fe8bd7 | sha1: bb026baeb18f92365172c93494c07381f76bb8cd | sha256: None | size: 105
       └ name: Metal Gear Solid (USA) (Disc 1) (Rev 1).bin | header: None | mia: None | crc: 21b5d15d | md5: e31ce17570897c323b7a539a2c616c72 | sha1: 37498e6598ce4eabf00630b6a9197b20861e55a0 | sha256: None | size: 705614112
```

1. The `name` attribute from the `<game>` element as found in the DAT file. If the DAT
    is a No-Intro numbered DAT, then the number prefix is removed for clone matching.
2. If the DAT is a No-Intro numbered DAT, the full name as found in the DAT file is
    stored here.
3. The content of the `<description>` tag as found in the DAT file.
4. The [region-free name](naming-system.md#region-free-names) generated for the title.
5. The [tag-free name](naming-system.md#tag-free-names) generated for the title.
6. The [short name](naming-system.md#short-names) generated for the title.
7. The [group name](naming-system.md#group-names) generated for the title.
8. A tuple of regions, extracted from the full name. The order is determined as follows:
   larger regions first that are likey to turn up in multi-region titles: `USA`, then
   `Europe`, `Japan`, `Asia`. The rest of the order is determined by the
   remaining regions in the `defaultRegionOrder` key found in `internal-config.json`.
9. The first entry in the `regions` key. Retool uses this for initial title comparisons,
   bundling them into individual regions and choosing "winners" in each region. These
   winners then get compared across all regions. Retool does this because things like
   revisions and versions are only relevant within each individual region. A
   `(USA) (Rev 2)` is not better than a `(Europe) (Rev 1)` for instance.
10. The second entry in the `regions` key. Not used by Retool for any processing.

    There's no need for a `tertiary_region` key, as titles with more than two regions are assigned wider geographical designations by No-Intro and Redump:

    * `World`: This variation of the title was released in the USA, Europe, and Japan.
      Considerd a "global" release.
    * `Europe`: This variation of the title was released in multiple European countries,
      which you can usually figure out from the languages involved.
    * `Scandinavia`: This variation of the title was released in some combination of
      Sweden, Denmark, Norway, or Finland.

    Bucking the trend, `Asia` isn't treated by Redump and No-Intro as containing multiple
    Asian countries. It tends to get used more as "we don't know where in Asia this came
    from". Given the languages involved, the most likely suspects are Hong Kong, Taiwan,
    or China.

## Automatic clone detection

## Clone lists

## Metadata

## Language and region priority