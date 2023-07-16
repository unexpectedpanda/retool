---
hide:
  - footer
---

# Removes

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
