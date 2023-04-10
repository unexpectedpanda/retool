---
hide:
  - footer
---

# Create and edit clone lists

Contributing to Retool's clone lists directly involves code and being familiar with Git
and GitHub. If that's not something you're interested in, you can still request clone list
changes by [filing an issue](https://github.com/unexpectedpanda/retool/issues).

If you want to contribute directly, [fork the clone lists and metadata repository](https://github.com/unexpectedpanda/retool-clonelists-metadata), read the following guidelines, make your
changes, and then submit a [pull request](https://github.com/unexpectedpanda/retool-clonelists-metadata/pulls).

## Before you begin

If you want to create or edit clone lists, you need to understand [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
and the following data structures:

* Key/value pairs
* Strings
* Integers
* Arrays
* Objects

It also helps to understand Retool's [terminology](../terminology), and the different
[names](../naming-system) it assigns to titles to help match and group them together
accurately.

## Titles that Retool automatically detects as clones

Before referencing clone lists, Retool parses a DAT file and creates objects for all of
its titles. If multiple titles have the same [group name](../naming-system/#group-names) and
[short name](../naming-system/#short-names), Retool assumes they're related to each other.

Names should only be added to clone lists in the following situations:

* To link together titles that ordinarily would have different group/short names due to
  regional naming, for example [_Indigo Prophecy_ and _Fahrenheit_](https://en.wikipedia.org/wiki/Fahrenheit_(2005_video_game)).

* To override Retool's default grouping.

* To assign categories to titles.

* To designate a title as missing in action (MIA).

## Clone list location and names

Clone lists are found by default in the `clonelists` subfolder. What subfolder Retool
looks for clone lists in is defined in `config/internal-config.json` in the
`cloneLists` object:

```json
"cloneLists": {
  "localDir": "clonelists"
}
```

Retool selects the correct clone list and metadata files for the loaded DAT file by
checking the `<name>` and `<url>` tags in the header of the DAT file, and then looking for
a matching filename with the release group appended in the clone lists and metadata
folders. For example, for Redump's Sony PlayStation DAT file, the `<name>` is
`Sony - PlayStation`. Therefore Retool looks for the clone list
`Sony - PlayStation (Redump).json` in the clone lists folder. If a matching file isn't
found, then only Retool's automatic clone detection is used.

## Clone list structure

Each clone list JSON file contains different top-level keys that determine how Retool
treats the titles in the related input DAT file. The keys are as follows:

* [`description (obj[str, str])`](#description)

* [`categories (array[obj])`](#categories)

* [`mias (array[str])`](#mias)

* [`overrides (array[obj])`](#overrides)

* [`removes (array[obj])`](#removes)

* [`variants (array[obj])`](#variants)

All keys are optional, except for `description`. They should be kept in the same order in
the clone list as the previous list.

### Description

The `description` object holds information related to the clone list itself, and is
always at the top of the file. It is mandatory to include.

A `description` object looks similar to the following example:

```json
"description": {
  "name": "Sony - PlayStation (Redump)",
  "lastUpdated": "24 July 2022",
  "minimumVersion": "2.00"
}
```

A `description` object contains the following keys:

* `name (str)`: The system name and release group of the DAT the clone list is related to.

* `lastUpdated (str)`: The last time the clone list was updated, in DD-MMMM-YYYY format.

* `minimumVersion (str)`: The minimum version of Retool required to understand all the
  features of the clone list.

The `minimumVersion` key is the only data in the description used by Retool, the rest is
to make parsing and updating the clone list easier for humans.

### Categories

The `categories` array specifies titles that should have their categories reassigned. A
category is a class of titles, like `Demos`, `Games`, and `Multimedia`. Multiple
categories can be assigned to a title.

A `categories` array looks similar to the following example:

```json
"categories": [// (1)!
  {
    "searchTerm": "Ace Combat 3 - Electrosphere - Direct Audio with AppenDisc",// (2)!
    "nameType": "short",// (3)!
    "categories": ["Audio"]// (4)!
  },
  {
    "searchTerm": "Arc the Lad III (Japan) (Demo 2)",
    "nameType": "full",
    "categories": ["Demos", "Multimedia"]
  },
  {
    "searchTerm": "Derby Stallion Magazine Furoku.*",
    "nameType": "regex",
    "categories": ["Coverdisc"]
  }
]
```

1.  The categories array.
2.  The search term used when looking for a title in an input DAT file.
3.  What name type the search term is, so Retool can match it accurately against names in
    the input DAT file.
4.  The categories to assign to the title if it's found in the input DAT file.

Each object in the `categories` array can include the following keys:

* `searchTerm (str)`: The search term used when looking for a title in an input DAT file.

* `nameType (str)`: Optional, defaults to `tagFree`. What name type the search term is,
  so Retool can match it accurately against names in the input DAT file. Valid options
  include:

    * `full (str)`: The [full name](../naming-system/#full-names).

    * `short (str)`: The [short name](../naming-system/#short-names).

    * `regionFree (str)`: The [region-free name](../naming-system/#region-free-names).

    * `tagFree (str)`: The [tag-free name](../naming-system/#tag-free-names).

    * `regex (str)`: A regex match on the full name.

* `categories (array[str])`: An array containing each category to assign to the title.
  Retool overrides existing categories, so if you want the original category to be kept,
  include it in the array.

### MIAs

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

MIAs only use [full names](../naming-system/#full-names) to search for matching titles in the
associated DAT file, and so an `mias` array only contains strings that match those full names.

### Overrides

The `overrides` array assigns titles different [group](../naming-system/#group-names) and
[short names](../naming-system/#short-names), manually bundling together specific games
instead of using Retool's automatic grouping.

Because Retool groups together titles with the same [short name](../naming-system/#short-names)
by default, this is particularly useful to work around the problem where games have the
same short name, but are entirely different in content.

For example, the Japanese version of _King's Field_ was never released in the USA.
Japan's _King's Field II_ was released in the USA, however it was given the original
game's name, _King's Field_. By default, Retool sees _King's Field (USA)_ and
_King's Field (Japan)_, and incorrectly groups them together as the same title as they
have the same short name, `King's Field`.

To get around this, we can assign _King's Field (Japan)_ a unique group and short name
through the `overrides` array, to stop it being grouped automatically with
_King's Field (USA)_.

An `overrides` array looks similar to the following example:

```json
"overrides": [// (1)!
  {
    "searchTerm": "King's Field (Japan)",// (2)!
    "newGroup": "King's Field Japan"// (3)!
  },
  {
    "searchTerm": "Mobile Suit Gundam - Version 2.0 (.*)",
    "nameType": "regex",// (4)!
    "newGroup": "Mobile Suit Gundam Veetwo"// (5)!
  }
]
```

1.  The overrides array.
2.  The search term used when looking for a title in an input DAT file.
3.  The new group and short name to assign to the title, if it's found in an input DAT
    file. This isn't the literal group name that is assigned, Retool takes this as a
    base and then changes it based on its naming rules.
4.  What name type the search term is, so Retool can match it accurately against names in
    the input DAT file.
5.  Don't put version strings or strings in parentheses in `newGroup` values, as they are
    stripped.

Each object in the `overrides` array can include the following keys:

* `searchTerm (str)`: The search term used when looking for a title in an input DAT file.

* `nameType (str)`: Optional, defaults to `tagFree`. What name type the search term is,
  so Retool can match it accurately against names in the input DAT file. Valid options
  include:

    * `full (str)`: The [full name](../naming-system/#full-names).

    * `short (str)`: The [short name](../naming-system/#short-names).

    * `regionFree (str)`: The [region-free name](../naming-system/#region-free-names).

    * `tagFree (str)`: The [tag-free name](../naming-system/#tag-free-names).

    * `regex (str)`: A regex match on the full name.

* `newGroup (str)`: The new group and short name to assign to the title.

!!! caution
    To keep things easy, avoid parentheses `()` where possible in `newGroup` values.
    Additionally, avoid adding anything that looks like version string, for example,
    `v2.00`.

    You want to do this because the group and short names assigned to overridden titles
    aren't an exact copy of the `newGroup` value. Instead, the value is used as a basis to
    generate these names using Retool's [naming rules](../naming-system/#names).

#### Override conditions

You can specify a `condition` as to whether or not an override should be implemented. The
only condition supported is based on the user's region order. Conditions are rare, and are
often only used to deal with clashes when outputting DAT files in legacy parent/clone
format.

A `condition` looks similar to the following example:

```json
"overrides": [
  {
    "searchTerm": "Tomb Raider III - (Adventures of|Les Aventures de) Lara Croft \\((Europe|France|Germany|Italy|Spain|USA)\\)(.*)?",
    "nameType": "regex",
    "newGroup": "Tomb Raider III - Adventures of Lara Croft Disc 2 International Version",
    "condition": {// (1)!
        "regionOrder": {// (2)!
            "higherRegions": ["Japan", "Asia"],// (3)!
            "lowerRegions": ["USA", "Europe", "France", "Germany", "Italy", "Spain"],
            "elseGroup": "Tomb Raider III - Adventures of Lara Croft"// (4)!
        }
    },
  }
]
```

1.  The condition object.
2.  The `regionOrder` condition.
3.  If any of these regions is higher in the user order than all of the regions in the
    `lowerRegions` array, then the condition is `True`.
4.  If the condition is `False`, set the group and short name to this group instead of
    the `newGroup` value.

A `condition` object can include the following keys:

* `regionOrder (object)`: Specifies to use the region order condition.

* `higherRegions (array[str])`: If any of the regions in the `higherRegions` array is
   higher in the user region order than all of the regions in the `lowerRegions` array,
   then the condition is `True`.

* `lowerRegions (array[str])`: If any of the regions in the `higherRegions` array is
   higher in the user region order than all of the regions in the `lowerRegions` array,
   then the condition is `True`.

* `elseGroup (str)`: Optional, defaults to the automatic group and short names assigned by
  Retool. If the condition is `False`, set the group and short name to this group instead
  of the `newGroup` value.

* `priority (int)`: Optional. If the condition is `True`, set the title to this clone list
  priority. If the condition is `False`, set the clone list priority to `2`. A priority
  directs Retool to choose one title over another if they are in the same region, and have
  the same group name and short name.

### Removes

The `removes` array lists all titles to force remove from the output DAT for that
particular system. It should only be used if `overrides` or `variants` can't achieve the
same result.

!!! caution
    The `removes` array should almost never be used, as any titles listed are completely
    removed from Retool's consideration during processing, and their relationship with
    other titles is destroyed. This makes it particularly hard to keep track of
    relationships when updating clone lists, and can frustrate any traces you perform to
    debug issues.

A `removes` array looks similar to the following example:

```json
"removes": [
  {
    "searchTerm": "King of Fighters 2000-2001, The (Europe)",
    "nameType": "full"
  }
]
```

Each object in the `removes` array can include the following keys:

* `searchTerm (str)`: The search term used when looking for a title in an input DAT file.

* `nameType (str)`: Optional, defaults to `tagFree`. What name type the search term is,
  so Retool can match it accurately against names in the input DAT file. Valid options
  include:

    * `full (str)`: The [full name](../naming-system/#full-names).

    * `short (str)`: The [short name](../naming-system/#short-names).

    * `regionFree (str)`: The [region-free name](../naming-system/#region-free-names).

    * `tagFree (str)`: The [tag-free name](../naming-system/#tag-free-names).

!!! note
        Unlike other clone list features, the `regex` name type isn't supported for
        `removes`.

### Variants

The `variants` array is where all the different regional names and variations for titles
are stored, grouping titles together that Retool would otherwise miss. By default, Retool
already groups together titles that have the same [short name](../naming-system/#short-names).

A basic `variants` array looks similar to the following example:

```json
"variants": [// (1)!
  {
    "group": "Example Title",// (2)!
    "titles": [// (3)!
      {"searchTerm": "Example Title"},// (4)!
      {"searchTerm": "Exemple de Titre"},
      {"searchTerm": "Titolo di Esempio"},
      {"searchTerm": "Example Title Budget Edition", "priority": 2}// (5)!
    ]
  }
]
```

1.  The variants array.
2.  The new group and short name to assign to the contained titles, if they're found in an
    input DAT file.
3.  The `titles` array contains singular, standard titles that belong to this group.
4.  The search term used when looking for a title in an input DAT file.
5.  If there are two titles from the same region, a `priority` can determine which should
    be selected. Lower numbers are higher priority. If no `priority` is specified, the
    priority of the entry is `1`.

Each object in the `variants` array can include the following keys:

* `group (str)`: The `group` value is used as the basis for a new [group name](../naming-system/#group-names)
   and [short name](../naming-system/#short-names) for all of the titles in the object.

* `titles (array[obj])`: Optional. Contains singular, standard titles that belong to the
  group.

* `supersets (array[obj])`: Optional. Contains singular titles that contain more content,
  or for some reason are superior to standard versions. This might include, for example, a
  Game of the Year edition, an all-in-one pack that bundles a game and all its DLC, or a
  DVD version of a title that was previously released on multiple CDs.

* `compilations (array[obj])`: Optional. Contains titles that in themselves contain
  multiple titles. They might be from the same series of games, a single publisher, from
  a single genre, or otherwise.

!!! caution
    The group and short names assigned to the contained titles aren't an exact copy of the
    top-level key. Instead, the key is used as a basis to generate these names. The rules
    for how these names are created are detailed in [Retool's naming system](../naming-system).

Each object in the `titles`, `supersets`, and `compilations` arrays can include the
following keys:

* `searchTerm (str)`: The search term used when looking for a title in an input DAT file.

* `nameType (str)`: Optional, defaults to `short`. What name type the search term is,
  so Retool can match it accurately against names in the input DAT file. Valid options
  include:

    * `full (str)`: The [full name](../naming-system/#full-names).

    * `short (str)`: The [short name](../naming-system/#short-names).

    * `regionFree (str)`: The [region-free name](../naming-system/#region-free-names).

    * `tagFree (str)`: The [tag-free name](../naming-system/#tag-free-names).

    * `regex (str)`: A regex match on the full name.

* `priority (int)`: Optional, defaults to `1`. Lower numbers are considered higher
  priority, with `1` the highest priority. Typically, a title with a higher priority wins
  when Retool is choosing a 1G1R title> However, _when_ priority is calculated in Retool's
  process, and how it interacts across `titles`, `supersets`, and `compilations` arrays
  can change the outcome. Read [Example: working with priorities](#example-working-with-priorities)
  for more information.

* `titlePosition (int)`: Optional, defaults to `none`, `compilations` objects only. This
  determines whether a title comes first, second, third, or later in a compilation's name.
  This is only really useful for GameBoy Advance titles, as No-Intro's DAT differentiates
  languages supported by each title in a compilation by using a `+` symbol. Still, it's
  wise to include where possible in case that naming standard eventually makes it to other
  DAT files.

#### Ordering variants arrays

The order of variants arrays is always:

1.  `titles`

1.  `supersets`

1.  `compilations`.

The `group` key in each array object should be based on one of the title names in the
group, preferably from the USA version and in English. Some titles won't exist in all
regions, so follow this order for the `group` name:

1.  USA name in English

1.  United Kingdom name in English

1.  European name in English

1.  Any other region in English

1.  Japanese name

1.  Spanish name

1.  Portuguese name

1.  French name

1.  German name

1.  Whatever name is available

To ease maintenance, make sure the objects inside the `titles`, `compilations`, and
`supersets` arrays are ordered by priority, and then alphabetically within those
priorities.

For example, this is correct:

```json
"variants": [
  {
    "group": "Example Title",
    "titles": [
      {"searchTerm": "Example Title"},
      {"searchTerm": "Exemple de Titre"},
      {"searchTerm": "Titolo di Esempio"},
      {"searchTerm": "Example Title Budget Edition", "priority": 2}
    ]
  }
]
```

This is incorrect:

```json
"variants": [
  {
    "group": "Example Title",
    "titles": [
      {"searchTerm": "Example Title"},
      {"searchTerm": "Example Title Budget Edition", "priority": 2},
      {"searchTerm": "Titolo di Esempio"},
      {"searchTerm": "Exemple de Titre"}
    ]
  }
]
```

!!! warning
    Avoid setting a `searchTerm` with the same name as its `group` to a lower priority.
    For example:

    ```json
    {
      "group": "Title",
      "titles": [
        {"searchTerm": "Title Director's Cut"}
        {"searchTerm": "Title", "priority": 2}
      ]
    }
    ```

    In this scenario, Retool sees the first entry `Title Director's Cut`, and goes looking
    for titles with the short name `title director's cut`. When it finds a match, it
    changes that title's short name to match the group, `title`.

    When it gets to the second entry, `Title`, it goes looking for titles with the short
    name `title`... but that's what we just renamed the _Director's Cut_ short name to.
    Everything ends up being assigned a priority of 2 as a result.

    If you run into this situation, the easiest solution is to rename the group to match
    the higher priority title:

    ```json
    {
      "group": "Title Director's Cut",
      "titles": [
        {"searchTerm": "Title Director's Cut"}
        {"searchTerm": "Title", "priority": 2}
      ]
    }
    ```

#### Example: working with titles

If we have the following title names in a DAT file, that are all the same title across
different regions:

```
Example Title (USA)
Example Title Budget Edition (USA)
Example Title (Europe)
Exemple de Titre (France)
Titolo di Esempio (Italy)
```

And a user selects the following region order:

```
USA
Europe
United Kingdom
France
Italy
```

Then Retool automatically links together _Example Title (USA)_ and
_Example Title (Europe)_, as they have the same short name, `example title`. However it
misses the other titles, as by default they have different short names.

A `variants` object like the following example links them all together:

```json
"variants": [
  {
    "group": "Example Title",
    "titles": [
      {"searchTerm": "Example Title"},
      {"searchTerm": "Exemple de Titre"},
      {"searchTerm": "Titolo di Esempio"},
      {"searchTerm": "Example Title Budget Edition", "priority": 2}
    ]
  }
]
```

Because no `nameType` is specified in each title object, Retool assumes the `searchTerm`
is a short name, and looks in the related DAT for names that have the same short name.
When it finds those titles, it assigns the same group and short name to them,
`example title`, and then Retool knows they are related.

The `priority` of `2` for `Example Title Budget Edition` indicates that when Retool is
processing the USA region, to select _Example Title (USA)_ over
_Example Title Budget Edition (USA)_ when Retool considers clone list priority. There are
other factors that might eliminate a title before Retool gets to clone list priority.

In this example, because the user has set USA first in the region order, then
_Example Title (USA)_ is selected as the 1G1R title, and the others are discarded.

#### Example: working with supersets

Let's take the titles example, but add another title into the mix:
_Example Title - Game of the Year Edition (United Kingdom)_.

```
Example Title (USA)
Example Title Budget Edition (USA)
Example Title - Game of the Year Edition (United Kingdom)
Example Title (Europe)
Exemple de Titre (France)
Titolo di Esempio (Italy)
```

This edition contains the latest version of the game, plus all of its DLC, but was never
released in the USA or Europe. If the user is an English speaker, then how do we make sure
this title gets selected as the superior version of a game, even if the USA or Europe is
higher up their region order? With the `supersets` array.

```json
"variants": [
  {
    "group": "Example Title",
    "titles": [
      {"searchTerm": "Example Title"},
      {"searchTerm": "Exemple de Titre"},
      {"searchTerm": "Titolo di Esempio"},
      {"searchTerm": "Example Title Budget Edition", "priority": 2}
    ],
    "supersets": [
      {"searchTerm": "Example Title - Game of the Year Edition"}
    ]
  }
]
```

The objects in the `supersets` array list [supersets](../terminology/#supersets). By
default, supersets look at language support over region order. If a superset supports the
top language found in a group of titles (in this example, that's English), then it's
selected over other standard titles in higher regions as it's considered superior.

In this example, because no language order is included but USA is listed first, Retool
infers a preference for English, finds the superset
_Example Title - Game of the Year Edition (United Kingdom)_, and selects it as the 1G1R
title above the standard USA title, as it supports the same language and is considered
superior due to having more content.

!!! note
    A user can force adherence to region order  with the **Prefer regions over languages**
    option. In that scenario, _Example Title (USA)_ is selected at the cost of losing the
    extra content in _Example Title - Game of the Year Edition (United Kingdom)_.

Supersets are also useful to manage things like DVD releases of titles that were
previously distributed on multiple CDs. For example, if a DAT contains the following title
names, all of which represent the same title:

```
Example Title (Disc 1) (USA)
Example Title (Disc 2) (USA)
Example Title (Disc 3) (USA)
Beispieltitel (Disc 1) (Germany)
Beispieltitel (Disc 2) (Germany)
Beispieltitel (Disc 3) (Germany)
Example Title (USA)
```

And _Example Title (USA)_ is the DVD version of the three-disc CD release _Example Title_
and _Beispieltitel_, then you can set up a `variants` object as follows:

```json
"variants": [
  {
    "group": "Example Title (Disc 1)",
    "titles": [
      {"searchTerm": "Example Title (Disc 1)"},
      {"searchTerm": "Beispieltitel (Disc 1)"}
    ],
    "supersets": [
      {"searchTerm": "Example Title"}
    ]
  },
  {
    "group": "Example Title (Disc 2)",
    "titles": [
      {"searchTerm": "Example Title (Disc 2)"},
      {"searchTerm": "Beispieltitel (Disc 2)"}
    ],
    "supersets": [
      {"searchTerm": "Example Title"}
    ]
  },
  {
    "group": "Example Title (Disc 3)",
    "titles": [
      {"searchTerm": "Example Title (Disc 3)"},
      {"searchTerm": "Beispieltitel (Disc 3)"}
    ],
    "supersets": [
      {"searchTerm": "Example Title"}
    ]
  }
]
```

Note that the `Example Title` superset is in all three groups. In this scenario, if a
user selects USA as their highest region, then _Example Title (USA)_ is selected as the
1G1R title over the original, multidisc CD version. If they select Germany, then the three
German discs are chosen instead.

#### Example: working with compilations

Individual titles and compilations have their relationships defined in clone lists. When
Retool considers these titles and looks to deduplicate, it chooses a solution that
results in as many individual titles as possible being selected. This is because [patches](https://www.romhacking.net/)
and [retro achievements](https://retroachievements.org/) tend to only be available for
individual titles, and compilation filenames often don't tell you what titles they
contain, making your collection less browsable.

This method results in some duplicates being left in the output. For example, when Retool
analyzes the following titles:

* _Title A (USA)_
* _Title B (USA)_
* _Title A + Title C (USA)_

It includes them all in the output, despite that not being the most optimal space saving
solution (which would remove _Title A (USA)_). This is because when comparing the
following titles:

* _Title A (USA)_
* _Title A + Title C (USA)_

_Title A (USA)_ wins for the _Title A_ selection as it's an individual title (and
preferred over compilation versions), and _Title A + Title C (USA)_ wins for _Title C_
as that title is only contained in the compilation, a standalone variation doesn't exist.

Compilations in a `variants` array are handled in a similar way to the following example:

```json
"variants": [
  {
    "group": "3-D Ultra Pinball",
    "titles": [
      {"searchTerm": "3-D Ultra Pinball"}
    ],
    "compilations": [
      {"searchTerm": "3-D Ultra Pinball & Trophy Bass", "titlePosition": 1}
    ]
  },
  {
    "group": "Trophy Bass",
    "compilations": [
      {"searchTerm": "3-D Ultra Pinball & Trophy Bass", "titlePosition": 2}
    ]
  }
]
```

Note that `3-D Ultra Pinball & Trophy Bass` belongs to both the `3-D Ultra Pinball` and
`Trophy Bass` groups. During processing, Retool splits compilations into virtual versions
of their consituent titles. This means that when you add a compilation to a variant
object, it's only being judged on the individual title associated with that group, not all
titles in the compilation.

As far as Retool is concerned in this example, `3-D Ultra Pinball & Trophy Bass` in the
`3-D Ultra Pinball` group is just another version of _3-D Ultra Pinball_, and
`3-D Ultra Pinball & Trophy Bass` in the `Trophy Bass` group is just another version of
_Trophy Bass_. It's important to list a compilation in all groups it's related to, even
if a standalone title doesn't exist. This way Retool knows which titles make up the
compilation and can make more accurate choices.

In this example, if a related DAT contains the following title names:

```
3-D Ultra Pinball (Europe)
3-D Ultra Pinball & Trophy Bass (USA)
```

And a user selects the following region order:

```
USA
Europe
```

Then Retool selects _3-D Ultra Pinball & Trophy Bass (USA)_ as the single 1G1R title for
both _3-D Ultra Pinball_ and _Trophy Bass_, as that solution includes the USA version of
the titles, and the least duplication.

However, if a user selects the following region order:

```
Europe
USA
```

Then Retool selects _3-D Ultra Pinball (Europe)_ for _3-D Ultra Pinball_ as it's an
individual title in a preferred region, while _3-D Ultra Pinball & Trophy Bass (USA)_ is
chosen for _Trophy Bass_ as a standalone version of that title doesn't exist, and the
compilation is the only remaining option.

#### Example: working with priorities

It's useful to understand how priorities work across the `titles`, `supersets`, and
`compilations` arrays.

##### Titles

If you use `priority` in a titles array, it's taken into account for titles in the
same region, with same group and short name. The `priority` does not take effect for
titles in different regions.

For example, if a DAT file contains the following title names:

```
Example Title (USA)
Example Title Budget Edition (USA)
Example Title (Europe)
```

And the following variants array is in the related clone list:

```json
{
  "variants": [
    {
      "group": "Example Title",
      "titles": [
        {"searchTerm": "Example Title"}
        {"searchTerm": "Example Title Budget Edition", "priority": 2}
      ]
    }
  ]
}
```

Then both _Example Title (USA)_ and _Example Title (Europe)_ receive a priority of 1, as
no priority has been specified. _Example Title Budget Edition (USA)_ is assigned a
priority of 2 as defined by the clone list.

Because Retool first bundles games from the same region together for comparison,
_Example Title (USA)_ and _Example Title Budget Edition (USA)_ are compared, and the
latter is dropped because it has a lower priority of 2.

Afterwards cross-region comparisons are made, so _Example Title (USA)_ and
_Example Title (Europe)_ are compared, however priority is not taken into account here,
only things like user region and language order.

##### Supersets

While the behavior for priorities in supersets is similar to that in titles, superset
priorities are only compared against other superset priorities, and compilation
priorities.

For example, if a DAT file contains the following title names:

```
Example Title (USA)
Example Title Budget Edition (USA)
Example Title - Special Edition (Europe)
Example Title - Super Special Edition (Europe)
```

A user selects the following region order:

```
USA
Europe
```

And the following variants array is in the related clone list:

```json
{
  "variants": [
    {
      "group": "Example Title",
      "titles": [
        {"searchTerm": "Example Title"}
        {"searchTerm": "Example Title Budget Edition", "priority": 2}
      ],
      "supersets": [
        {"searchTerm": "Example Title - Super Special Edition"}
        {"searchTerm": "Example Title - Special Edition", "priority": 2}
      ]
    }
  ]
}
```

Then the following happens:

1.  Because the supersets are in English (and English is this user's highest language in
    their implied language order), they get selected over the standard titles even though
    they are from Europe, a lower ordered region. This has nothing to do with priority
    set in the clone list &mdash; it's just how supersets work.

1.  _Example Title - Super Special Edition (Europe)_ then gets chosen over
    _Example Title - Special Edition_, as the latter has a lower priority.

##### Compilations

Priorities affect compilations slightly differently, as Retool splits compilations into
individual virtual titles to compare against the other titles.

For example, if a DAT file contains the following title names:

```
Example Title (USA)
Example Title (Europe)
Example Title 2 - Special Edition (USA)
Example Title 1 & 2 (Europe)
```

A user selects the following region order:

```
USA
Europe
```

And the following variants array is in the related clone list:

```json
{
  "variants": [
    {
      "group": "Example Title",
      "titles": [
        {"searchTerm": "Example Title"}
      ],
      "compilations": [
        {"searchTerm": "Example Title 1 & 2"}
      ]
    },
    {
      "group": "Example Title 2",
      "titles": [
        {"searchTerm": "Example Title 2 - Special Edition"}
      ],
      "compilations": [
        {"searchTerm": "Example Title 1 & 2", "priority": 2}
      ]
    }
  ]
}
```

Then the following happens with the compilations:

1.  Retool looks at the `Example Title` group, and finds _Example Title 1 & 2 (Europe)_
    in the DAT via the compilations search term `Example Title 1 & 2`.

1.  That compilation is then assigned a virtual name that matches the group name, and
    includes region and language information: _:V: Example Title (Europe) (En)_. This
    effectively splits out that indvidual title from the compilation for comparison,
    meaning the second title in the compilation isn't considered when comparing titles in
    this group. Because no `priority` is defined, the virtual title is assigned a priority
    of 1.

1.  Retool looks at the `Example Title 2` group, and finds _Example Title 1 & 2 (Europe)_
    in the DAT via the compilations search term `Example Title 1 & 2`.

1.  Although it's the same compilation as before, it's assigned a virtual name that
    matches the `Example Title 2` group name: _:V: Example Title 2 (Europe) (En)_. This
    means the first title in the compilation isn't considered when comparing titles in
    this group. The virtual title is assigned a priority of 2, as specified in the clone
    list.

1.  Retool compares the virtual compilation titles against the individual titles in the
    same groups:

    * _Example Title (USA)_ is compared against _:V: Example Title (Europe) (En)_. The USA
      title wins due to region priority.

    * _Example Title 2 - Special Edition (USA)_ is compared against
      _:V: Example Title 2 (Europe) (En)_. The latter is discarded because it has a lower
      priority (which is assessed before region order).

    * Ultimately _Example Title (USA)_ and _Example Title 2 - Special Edition (USA)_
      become the 1G1R titles, and _Example Title 1 & 2 (Europe)_ is discarded.

Superset priorities are compared directly against compilation priorities, just like title
priorities are.

## Format clone lists

Clone lists follow a particular format to keep maintainence easy:

* Valid JSON.

* Tabbed indenting.

* LF line endings.

* Top-level keys should be kept in [the order listed in this guide](#clone-list-structure).

* Object keys should be in the order shown in the examples in this guide.

* Array contents should be in alphabetical order, sorted by an object's top key. This is
  either going to be `searchTerm` or `group`.

Make sure your format is correct before submitting a pull request.

## Test clone lists

Before submitting a pull request, it's important to test your changes to make sure they're
correct.

Test your clone list update against the newest version of a DAT from No-Intro or Redump,
and enable the following settings:

=== ":fontawesome-regular-window-maximize: GUI"
    * In the **Global settings** tab, click **Options**.

    * Enable **Report clone list warnings during processing** and
      **Pause on clone list warnings**.

=== ":simple-windowsterminal: Command line"

    `--warnings --warningpause`

Run Retool on the DAT file, and fix your clone list until no warnings are given.


## Hashing for updates

Retool manages clone list updates via the `hash.json` file in the clone lists subfolder.
When looking for updates, the newest `hash.json` is downloaded from from the location
specified in `internal-config.json`:

```json
"cloneListMetadataUrl": "https://raw.githubusercontent.com/unexpectedpanda/retool-clonelists-metadata/",
```

The SHA256 hashes in that file are then compared against the clone lists on the local
disk. If a clone list hash doesn't match, then a new version of that file is downloaded
from the same location as listed above.

After your PR has been merged, the `hash.json` is updated by unexpectedpanda with the
SHA256 hash of the updated or new clone lists.