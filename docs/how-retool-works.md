---
hide:
  - footer
---

# How Retool works

This is a technical piece, and is best suited to developers who want to create similar
functionality for their tools. It's correct as of Retool v2.03.0, but isn't yet
finished.

## Overview

Retool has two primary functions:

1.  To filter DAT files based on user criteria, including:

    * Language preference

    * Region preference

    * Title type (for example, demo, preproduction)

    * User-defined strings

1.  To discover titles that have relationships with each other, and use that to implement
    [1G1R](terminology.md#1g1r). It does not make use of existing parent/clone data found
    in DAT files.

Retool uses the following data sources to achieve this:

* **The input DAT file itself**. This includes data like the title filename, category, and
  statuses (for example, "missing in action"). Relevant information is broken down into
  consituent parts for Retool to use later, for example, regions, languages, revisions,
  and so on.

* [**Clone lists**](contribute-clone-lists.md). Manually curated files that establish
  relationships between titles where automatic detection fails. Also used to break
  relationships where Retool gets automatic detection wrong.

* [**Metadata files**](contribute-metadata-files.md). These contain language and local
  name data taken from Redump and No-Intro's databases. Metadata is generally updated
  every few months. Redump's site is scraped, whereas No-Intro databases are manually
  downloaded to generate the metadata.

Titles are put through a series of stages in a specific order, with many stages acting
like filters that remove candidates that don't meet specific criteria.

!!! note "A note about updating clone lists and metadata"
    Clone lists and metadata need to be kept regularly up to date to ensure Retool's
    effectiveness. When they stop updating, Retool gradually becomes less accurate over
    time as changes are made to DAT files. Automatic detection picks up a lot, but it's
    not foolproof, especially as vital information is regularly missing from the DAT files
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

    This means that every now and then No-Intro makes a wide-ranging change that breaks
    things, which can mean updates are required for clone lists, metadata files, the
    Retool application, or sometimes all three. It also means that the ideal cadence for
    Retool's No-Intro updates is every few weeks, a pace that's hard to keep for a site
    that covers so many systems.

    You can download most system databases directly from No-Intro's Dat-O-Matic site,
    and these serve as the source for Retool's metadata. However, databases are not
    available for all systems. The database daily packs are often bugged or out of date,
    requiring you to download individual databases. The site also has incredibly
    aggressive anti-flood protection that can block access to resources and slows down the
    process. This makes keeping No-Intro data up-to-date an incredibly time consuming and
    frustrating task.

## Stage 1: Parsing the input DAT and sanitizing the data

The DAT file is read in by Retool. A title object is created from each `<game>` or
`<machine>` node, which contains useful, sanitized information about each title. This
object is a foundational piece of Retool's comparison process.

The data inside a title object is supplemented with data from additional sources, namely
manually curated clone lists and metadata scraped from Redump and No-Intro's websites.

The data in title objects is mutable, and changed as Retool continues throughout its
process.

### Building the title objects

The following example shows a `<game>` node from Redump's `Sony - PlayStation` DAT file,
and how Retool interprets it as an object of the `DatNode` class:

```xml title="Metal Gear Solid (USA) (Disc 1) (Rev 1), from Redump's Sony - PlayStation DAT"
<game name="Metal Gear Solid (USA) (Disc 1) (Rev 1)">
    <category>Games</category>
    <description>Metal Gear Solid (USA) (Disc 1) (Rev 1)</description>
    <rom name="Metal Gear Solid (USA) (Disc 1) (Rev 1).cue" size="105" crc="f2ac185c" md5="91fc49ae51815d04c3bb4384e9fe8bd7" sha1="bb026baeb18f92365172c93494c07381f76bb8cd"/>
    <rom name="Metal Gear Solid (USA) (Disc 1) (Rev 1).bin" size="705614112" crc="21b5d15d" md5="e31ce17570897c323b7a539a2c616c72" sha1="37498e6598ce4eabf00630b6a9197b20861e55a0"/>
</game>
```

```ini title="The <code>DatNode</code> object Retool builds that represents Metal Gear Solid (USA) (Disc 1) (Rev 1)"
○ full_name:                  Metal Gear Solid (USA) (Disc 1) (Rev 1) # (1)!
├ numbered_name:              None # (2)!
├ local_name:                 None # (3)!
├ description:                Metal Gear Solid (USA) (Disc 1) (Rev 1) # (4)!
├ region_free_name:           Metal Gear Solid (Disc 1) (Rev 1) # (5)!
├ short_name:                 metal gear solid (disc 1) # (6)!
├ group_name:                 metal gear solid # (7)!
├ group_moved_by_condition:   False # (8)!
├ tags:                       {'(USA)', '(Disc 1)', '(Rev 1)'} # (9)!
├ regions:                    ('USA',) # (10)!
├ primary_region:             USA # (11)!
├ secondary_region:           None # (12)!
├ languages_title_orig_str:   None # (13)!
├ languages_title:            None # (14)!
├ languages_implied:          ('En',) # (15)!
├ languages_online:           ('En',) # (16)!
├ languages:                  ('En',) # (17)!
├ cloneof:                    None # (18)!
├ is_superset:                False # (19)!
├ contains_titles:            None # (20)!
├ clonelist_priority:         1 # (21)!
├ region_priority:            0 # (22)!
├ language_priority:          0 # (23)!
├ exclude_reason:             None # (24)!
├ include_reason:             None # (25)!
├ exclude_include_related:    False # (26)!
├ categories:                 ['Games'] # (27)!
└ roms ┐
       ├ name: Metal Gear Solid (USA) (Disc 1) (Rev 1).cue | header: None | mia: None | crc: f2ac185c | md5: 91fc49ae51815d04c3bb4384e9fe8bd7 | sha1: bb026baeb18f92365172c93494c07381f76bb8cd | sha256: None | size: 105
       └ name: Metal Gear Solid (USA) (Disc 1) (Rev 1).bin | header: None | mia: None | crc: 21b5d15d | md5: e31ce17570897c323b7a539a2c616c72 | sha1: 37498e6598ce4eabf00630b6a9197b20861e55a0 | sha256: None | size: 705614112
```

1.  The `name` attribute from the `<game>` element as found in the DAT file. If the DAT
    is a No-Intro numbered DAT, then the number prefix is removed for clone matching.
2.  If the DAT is a No-Intro numbered DAT, the full name as found in the DAT file is
    stored here.
3.  If a [local name](contribute-clone-lists-variants-local.md) is found in the metadata
    or clone lists, it's stored here.
4.  The content of the `<description>` tag as found in the DAT file.
5.  The [region-free name](naming-system.md#region-free-names) generated for the title.
6.  The [short name](naming-system.md#short-names) generated for the title.
7.  The [group name](naming-system.md#group-names) generated for the title.
8.  Whether the title has already been moved by clone list to another group. If `True`,
    Retool won't permit it to be moved again.
9.  A set of all the tags of the title. This mainly exists so Retool doesn't have to
    search through entire filenames when doing string and regex matches, although only
    part of the code relies on it for now.
10. A tuple of regions, extracted from the full name. The order is determined as follows:
    larger regions first that are likey to turn up in multi-region titles: `USA`, then
    `Europe`, `Japan`, `Asia`. The rest of the order is determined by the remaining
    regions in the `defaultRegionOrder` key found in `config/internal-config.json`.
11. The entry in the `regions` key that is the highest match in the user's region order.
    Retool uses this for initial title comparisons, bundling them into individual regions
    and choosing "winners" in each region. These regional winners ultimately get compared
    against each other. Retool does this because things like revisions and versions are
    usually only relevant within a single region. A `(USA) (Rev 2)` is not better than a
    `(Europe) (Rev 1)` for instance.
12. The second entry in the `regions` key. Not used by Retool for any processing. Should
    probably be removed to improve performance.
    <br>
    There's no need for a `tertiary_region` key, as titles with more than two regions are
    assigned wider geographical designations by No-Intro and Redump:
    <br>
    *   `World`: This variation of the title was released in the USA, Europe, and Japan.
        Considerd a "global" release. Recently Redump has changed multi-region titles that
        listed "Asia" to "World" as well.
    *   `Europe`: This variation of the title was released in multiple European countries,
        which you can usually figure out from the languages involved.
    *   `Scandinavia`: This variation of the title was released in some combination of
        Sweden, Denmark, Norway, or Finland.
    *   `Asia`: Bucking the trend, it seems `Asia` tends to get used more as "we don't
        know where in Asia this came from". Given the languages involved, the most likely
        suspects are Hong Kong, Taiwan, or China.
13. The original language string from the title full name. For example, a full name of
    `Ace Combat 3 - Electrosphere (Europe) (En,Fr,De,Es,It)` has a
    `languages_title_orig_str` of `En,Fr,De,Es,It`. It's only used to create the
    region-free name for the object, and to figure out if the language string uses the GBA
    language formatting of `En+En,De` for assigning different language sets to different
    titles inside a compilation.
14. A tuple of languages as defined in the filename.
15. A tuple of the [implied language](terminology.md#implied-languages) for the title, as
    defined by the region. Only used as a guess at a title's language if it has no
    languages in the filename or the metadata. Implied languages are assigned in the
    `defaultRegionOrder` key in `config/internal-config.json`.
16. A tuple of languages from the scraped Redump and No-Intro databases, stored in
    Retool's metadata files.
17. The canonical languages for the title. This is chosen from the following options, in
    this order:<br>
    1. `languages_online`, if it exists.
    1. `languages_title`, if it exists.
    1. `languages_implied`, if it exists.
18. What title full name the title is a clone of.
19. Whether the title is a superset. This is important for title comparisons.
20. If the title is a compilation, the short names of the titles that the compilation
    contains.
21. The priority of the title as set in a clone list. Defaults to `1`. Lower numbers are
    higher priorities.
22. What priority the title is based on its regions, given the user's region preferences.
23. What priority the title is based on its languages, given the user's language
    preferences.
24. The reason the title was excluded from the final output. Used as a `<comment>` when
    someone also exports a DAT file of all the titles that have been removed.
25. The reason the title was force included by the user in the final output. Only here for
    tracing if someone reports an issue.
26. Whether this title is related to any other titles that have been included or excluded
    by a user override. A user specifies if they want titles related to their overrides
    included/excluded by wrapping their override strings in `<>`.
27. The categories for the title, either taken from the DAT file, inferred from the full
    name, or overridden by the related clone list.
28. The relevant content of the `<rom>` nodes for the title.

These `DatNode` objects are what's primarily used to compare titles against each other,
and are updated as Retool operates.

!!! tip
    You can output a `DatNode` object to screen that looks like the previous example by
    adding <code>input(<span class="variable">DATNODE_OBJECT_NAME</span>)</code> at
    appropriate points in the Python code, replacing
    <code><span class="variable">DATNODE_OBJECT_NAME</span></code> with the actual
    object name (often `title`, `title_1`, or `title_2`). This can give you insight as
    to what a title object looks like as it goes through through Retool's process.

    Make sure to use the `--singlecpu` flag when doing this, as `input()` doesn't play
    well with multi-processing.

Here's how it's built:

1.  Many of the names Retool uses are generated from the full name taken from the DAT
    file. To make sure there are no errors here, it's passed through the following checks:
    *  Invalid filename characters are stripped or replaced.
    *  Retool has previously checked if a numbered DAT file is in use, by verifying that
       all `<game>` or `<machine>` `name` attributes match the regex
       `^([0-9]|x|z)([0-9]|B)[0-9]{2,2} - `. A numbered DAT file is one that prefixes
       title full names with a release number, for example: <br>
       ```
       0001 - F-Zero for Game Boy Advance (Japan)
       ```
       Is the numbered version of:
       ```
       F-Zero for Game Boy Advance (Japan)
       ```
       If a numbered DAT file is in use, the original full name is stored in
       `numbered_name`, which is only used again when the output DAT file is written. The
       `full_name` gets set to the `numbered_name` stripped of the first 7 characters,
       which is the number prefix. This is so the release numbers don't influence
       comparison later on. No-Intro metadata also doesn't include the release number, so
       this name is required for metadata lookup.
1.  Language codes are retrieved from the full name and stored in `languages_title` as a
    tuple, and `languages_title_orig_str` as a string that's found by using a regular
    expression. This doesn't just involve searching for individual language codes:
    No-Intro Game Boy Advance titles can assign languages to a compilation's constituent
    titles in the following format: `(En+En,De)`, meaning many language combinations need
    to be taken into account to capture everything. As such, the languages regular
    expression is generated using the following template:<br>
    ```
    '\(((' + LANGUAGES + ')(,\s?)?)*\)'
    ```
    Where `LANGUAGES` is generated by doing the following:
    *   Creating a list that contains the language values stored in the `languages` key in
        `config/internal-config.json`.
    *   Creating a list that contains all two-language combinations of the previous
        languages and formatting them with the `+` notation (for example, `(Af, Sq)` becomes
        `Af+Sq` and `Sq+Af`).
    *   Creating a list with the combination `En+En+En` as an exception. No-Intro only uses
        this once, so it's not worth computing triple language combinations.
    *   Joining all previous lists together as a string with `|` as a delimiter.
1.  Regions are retrieved from the full name using the region order found in the
    `defaultRegionOrder` key in `config/internal-config.json`. The `primary_region` is
    also defined, based on the highest match found in the user's region order.
1.  The languages are retrieved from the matching title in the metadata, and stored in
    `languages_online`.
1.  The [implied language](terminology.md#implied-languages) is set based on
    `primary_region`. Implied languages are stored in the `defaultRegionOrder` key in
    `config/internal-config.json`.
1.  The canonical languages for the title are set in `languages`. The canonical languages
    are chosen from one of the following language sets, in priority order:
    1.  Languages taken from metadata, if they exist or don't equal `nolang`.
    1.  Languages taken from the title full name.
    1.  The implied language for the title.
1.  If the language code `Zh` is specified in languages, Retool tries to determine if
    it's traditional or simplified Chinese based on region. If China or Singapore are in
    `regions`, the code is changed to `Zh-Hans`. If Hong Kong or Taiwan are in `regions`,
    the code is changed to `Zh-Hant`.
1.  The short name is created. The most useful reference that Retool uses, the short name
    is initially used to automatically find titles that are related to each other. It's
    also used in clone lists to make referencing multiple titles easier. See
    [Short names](naming-system.md#short-names) for more on how this is generated.
1.  The region-free name is generated. This is the same as the full name, but with regions
    and languages removed. It is most useful in clone lists when you need more precision
    than a short name, and when [`filters`](contribute-clone-lists-variants-filters.md)
    aren't an elegant solution.
1.  The group name is created. See [Group names](naming-system.md#group-names) for more on
    how this is generated.
1.  [Local names](contribute-clone-lists-variants-local.md) are imported from metadata
    files, but only if the title has a maximum of 2 languages. This is because Redump and
    No-Intro generally only use a single alternate name field, which can't represent more
    than one alternate language. There are exceptions &mdash; No-Intro sometimes includes
    local names for multiple languages in different fields in their database, but these
    aren't consistent so Retool ignores them. Local names are pre-sanitized before they're
    stored in metadata files. After the local name has been retrieved, tags from the full
    name are appended.
1.  The `<description>` and `<rom>` nodes are parsed from inside the `<game>` or
    `<machine>` node and stored in `description` and `roms`.
1.  Categories are assigned. First, values from the `<category>` nodes are parsed from
    inside the `<game>` or `<machine>` node. Then, other categories are assigned based on
    the following criteria:
    *   Redump BIOS DAT files come in CLRMAMEPro format. They have a DAT file category of
        `Console`. As part of the ingestion process, Retool adds the CLRMAMEPro DAT file
        category to all of its constituent titles. When a title object is created, all
        categories of `Console` are renamed to `BIOS`.
    *   The `Applications` category is added to titles whose full name matches the regex
        pattern `\((?:Test )?Program\)|(Check|Sample) Program`.
    *   The `BIOS` category is added to titles whose full name matches the
        case-insensitive regex pattern `\[BIOS\]|\(Enhancement Chip\)`.
    *   The `Demos` category is added to titles whose full name matches any of the
        following case-insensitive regex patterns:
        *   `\((?:\w[-.]?\s*)*Demo(?:,?\s[\w0-9\.]*)*\)`
        *   `Taikenban`
        *   `\(@barai\)`
        *   `\(GameCube Preview\)`
        *   `\(Preview\)`
        *   `\(Sample(?:\s[0-9]*|\s\d{4}-\d{2}-\d{2})?\)`
        *   `Trial (Disc|Edition|Version|ver\.)`
        *   `\((?:Full )?Trial\)`
        *   `\((?:\w-?\s*)*?Kiosk,?(?:\s\w*?)*\)|Kiosk Demo Disc|(PSP System|PS2) Kiosk`
    *   The `Multimedia` category is added to titles whose full namematches the
        case-insensitive regex pattern `\(Magazine\)`.
    *   The `Preproduction` category is added to titles whose full name matches any
        of the following case-insensitive regex patterns:
        *   `\((?:\w*?\s)*Alpha(?:\s\d+)?\)`
        *   `\((?:\w*?\s)*Beta(?:\s\d+)?\)`
        *   `\((?:\w*?\s)*Proto(?:type)?(?:\s\d+)?\)`
        *   `\((?:Pre-production|Prerelease)\)`
        *   `\(DEV|DEBUG\)`
    *   The `Video` category is added to titles whose full name matches any of the
        following case-insensitive regex patterns:
        *   `Game Boy Advance Video`
        *   `- (Preview|Movie) Trailer`
        *   `\((?:\w*\s)*Trailer(?:s|\sDisc)?(?:\s\w*)*\)`
1.  If a title has a category of `Demo`, but it doesn't have a `(Demo)` or similar tag in
    the full name, Retool adds the `(demo)` tag to both `short_name` and `region_free`
    name, so demos don't get mixed up with retail titles. The demo tags Retool looks for
    are the same as the ones it uses for auto-assigning the `Demos` category.
1.  The title's `region_priority` is a 0-index number based on the user's region order and
    what's stored in `primary_region`. Lower is better. For example, if a user sets USA
    followed by Europe as their region order, and the title's primary region is `USA`, its
    `region_priority` is set to `0`. If the title's primary region is `Europe`, it's set
    to `1`.
1.  The title's `language_priority` is a 0-index number based on the user's language order
    and what's stored in `languages`. Lower is better. If the title supports multiple
    languages, the highest priority language is used for this number. If the user hasn't
    provided a language order, an order is inferred using implied languages based on their
    region order. For example, if a user sets English followed by Japanese as their
    language order, and the title's top language is English, its `language_priority` is
    set to `0`. If the title's top language is Japanese, it's set to `1`.

### Assigning title objects to groups

An empty dictionary (`processed_titles`) is created, and all title objects are iterated
over. Each time a new `group_name` is discovered in a title object, it is added to the
dictionary as a key, with that title object added to the key's value as a set. If Retool
finds another title object with the same `group_name`, it is added to the existing set
found at that key in the dictionary. This groups alike titles together so they can be
compared later.

The `processed_titles` dictionary is what Retool operates on during its comparison
process. The dictionary's final state is what's written to the output DAT file.

A copy of this dictionary is made after it is initially created as an original version
that is never modified, in case a user tries to force include titles and Retool needs
to quickly retrieve those details.

***To be continued...***
