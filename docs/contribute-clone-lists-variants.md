---
hide:
  - footer
---

# Variants

The `variants` array is where all the different regional names and variations for titles
are stored, grouping titles together that Retool would otherwise miss. By default, Retool
already groups together titles that have the same [short name](naming-system.md#short-names).

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

* `group (str)`: The `group` value is used as the basis for a new [group name](naming-system.md#group-names)
   and [short name](naming-system.md#short-names) for all of the titles in the object.

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
    for how these names are created are detailed in [Retool's naming system](naming-system.md).

Each object in the `titles`, `supersets`, and `compilations` arrays can include the
following keys:

* `searchTerm (str)`: The search term used when looking for a title in an input DAT file.

* `nameType (str)`: Optional, defaults to `short`. What name type the search term is,
  so Retool can match it accurately against names in the input DAT file. Valid options
  include:

    * `full (str)`: The [full name](naming-system.md#full-names).

    * `short (str)`: The [short name](naming-system.md#short-names).

    * `regionFree (str)`: The [region-free name](naming-system.md#region-free-names).

    * `tagFree (str)`: The [tag-free name](naming-system.md#tag-free-names).

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

## Ordering variants arrays

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

## Avoid certain group names

Avoid having a `group` name that is the same as a lower priority `searchTerm` in the
titles array, or a `searchTerm` in a superset. For example:

```json
{
  "group": "Title",
  "titles": [
    {"searchTerm": "Title Director's Cut"}
    {"searchTerm": "Title", "priority": 2}
  ]
}
```

In this scenario, Retool sees the first entry `Title Director's Cut`, and goes looking for
titles with the short name `title director's cut`. When it finds a match, it changes that
title's short name to match the group, `title`.

When it gets to the second entry, `Title`, it goes looking for titles with the short name
`title`... but that's what we just renamed the _Director's Cut_ short name to. Retool
promptly assigns everything in the group a priority of `2` as a result.

A similar thing happens if you have a a superset with a `searchTerm` that's the same as
the `group`:

```json
{
  "group": "Title",
  "titles": [
    {"searchTerm": "Title Director's Cut"}
  ],
  "supersets": [
    {"searchTerm": "Title"}
  ]
}
```

In this scenario, _everything_ in the group gets assigned as a superset as a result.

If you run into this situation, the easiest solution is to rename the group to match the
first `searchTerm` in the `titles` array, which should be the highest priority:

```json
{
  "group": "Title Director's Cut",
  "titles": [
    {"searchTerm": "Title Director's Cut"}
    {"searchTerm": "Title", "priority": 2}
  ]
}
```

Alternatively, you can give the group a name that matches none of the entries.

## Example: working with titles

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

## Example: working with supersets

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

The objects in the `supersets` array list [supersets](terminology.md#supersets). By
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

## Example: working with compilations

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

## Example: working with priorities

It's useful to understand how priorities work across the `titles`, `supersets`, and
`compilations` arrays.

### Titles

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

### Supersets

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

### Compilations

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
