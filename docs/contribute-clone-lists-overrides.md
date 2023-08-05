---
hide:
  - footer
---

# Overrides

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
            "elseGroup": "Tomb Raider III - Adventures of Lara Croft",// (4)!
            "priority": 1
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

A `regionOrder` object can include the following keys:

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
