---
hide:
  - footer
---

# Categories

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
