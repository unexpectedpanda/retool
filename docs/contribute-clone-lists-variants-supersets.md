---
hide:
  - footer
---

# The supersets array

The `supersets` array is found in objects inside the [`variants`](contribute-clone-lists-variants.md#structure)
array. The objects inside the `supersets` array list variants of titles that belong to a
`group`.

!!! tip
    Make sure you've read how the [`titles`](contribute-clone-lists-variants-titles.md)
    array works before learning about supersets.

Supersets are variants of titles that contain more content, or for some reason are
superior to another version. This might include, for example, a Game of the Year edition,
an all-in-one pack that bundles a game and all its DLC, or a DVD version of a title
previously released on multiple CDs.

A `supersets` array looks similar to the following example:

```json hl_lines="10-12"
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

You can use the following keys in an object that's in a `supersets` array:

<table>
  <thead>
    <tr>
      <th width="20%">Key</th>
      <th width="18%">Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>searchTerm</code></td>
      <td><code>str</code></td>
      <td>The search term used when looking for a title in an input DAT file.</td>
    </tr>
    <tr>
      <td><code>nameType</code></td>
      <td><code>str</code></td>
      <td>
        <p>Optional. What name type the search term is, so Retool can match it
        accurately against names in the input DAT file. The valid values are:</p>
        <ul>
          <li><code>short</code>: Default. The
            <a href="../naming-system#short-names">short name</a>.
          </li>
          <li><code>full</code>: The
            <a href="../naming-system#full-names">full name</a>.
          </li>
          <li><code>regionFree</code>: The
            <a href="../naming-system#region-free-names">region-free name</a>.
          </li>
          <li><code>regex</code>: A regex match on the full name.</td>
    </tr>
    <tr>
      <td><code>priority</code></td>
      <td><code>int</code></td>
      <td>
        <p>Optional, defaults to <code>1</code>. Lower numbers are considered higher
          priority, with <code>1</code> the highest priority. Typically, a title with a
          higher priority wins when Retool is choosing a 1G1R title.</p>
        <p>Superset priorities are compared against <code>supersets</code> and
        <code>compilations</code> priorities, but not <code>titles</code> priorities.</p>
      </td>
    </tr>
    <tr>
      <td><code>categories</code></td>
      <td><code>array[str]</code></td>
      <td>
        <p>Optional, A category is a class of titles, like Demos, Games, and Multimedia.
          Multiple categories can be assigned to a title, and existing categories are
          overridden.</p>
      </td>
    </tr>
    <tr>
      <td><code>englishFriendly</code></td>
      <td><code>bool</code></td>
      <td>
        <p>Optional, defaults to <code>false</code>. An English-friendly title is one that
          hasn't been marked as supporting English, but an English-speaking player can
          easily play to completion. Setting <code>englishFriendly</code> to
          <code>true</code> makes Retool treat a title as if it supports English.</p>
      </td>
    </tr>
    <tr>
      <td><code>isOldest</code></td>
      <td><code>bool</code></td>
      <td>
        <p>Optional, defaults to <code>false</code>. When a user selects
        <b>Prefer oldest production versions instead of newest</b>, this can
        be used to manually override Retool's automatic choice, or override priority
        settings in clone lists. Setting <code>isOldest</code> to <code>true</code>
        manually marks which title is the oldest in the group.</p>
      </td>
    </tr>
    <tr>
      <td><code>localNames</code></td>
      <td><code>obj[str, str]</code></td>
      <td>
        <p>Optional. Contains the local names of a title. Add names for all available
        languages, including English.</p>
        <p>Language keys must be lowercase versions of languages found in the
        <code>user-config.yaml</code> file or RetoolGUI languages list. For example,
        <code>japanese</code>, <code>russian</code>, <code>chinese (traditional)</code>.</p>
        ```json
        "localNames": {
          "english": "Example title",
          "chinese (traditional)": "標題範例",
          "japanese": "タイトルの例"
        }
        ```
        <p>See <a href="../contribute-clone-lists-variants-local">Local names</a>
        for more information on specifying local names.</p>
      </td>
    </tr>
    <tr>
      <td><code>filters</code></td>
      <td><code>array[obj]</code></td>
      <td>
        <p>Optional. Treat some titles found by a search term differently based on
        <code>conditions</code>. If all <code>conditions</code> are true, then Retool
        executes the <code>results</code>.</p>
        ```json
        "filters": [
          {
            "conditions": {"matchRegions": ["Japan"]},
            "results": {"group": "Somewhere else"}
          }
        ]
        ```
        <p>See <a href="../contribute-clone-lists-variants-filters">Filters</a>
        for more information, including the valid <code>conditions</code> and
        <code>results</code>.</p>
      </td>
    </tr>
  <tbody>
</table>

## How it works

Assume a DAT file contains the following titles:

```
Example Title (USA)
Example Title Budget Edition (USA)
Example Title - Game of the Year Edition (United Kingdom)
Example Title (Europe)
Exemple de Titre (France)
Titolo di Esempio (Italy)
```

Most are exactly the same title, just different versions or from different regions.
_Example Title - Game of the Year Edition (United Kingdom)_, however, contains the latest
version of the game plus all of its DLC, but was never released in the USA or Europe. If
the user is an English speaker and puts USA first, then how do we make sure this title
gets selected as the superior version of the game? With the `supersets` array.

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

By default, supersets look at language support over a user's region order. If a
superset supports the top language found in a group of titles (in this example,
that's English), then it's selected over other standard titles in higher regions
as it's considered superior.

In this example, because no language order is specified but USA is listed first, Retool
infers a preference for English, finds the superset
_Example Title - Game of the Year Edition (United Kingdom)_, and selects it as the 1G1R
title above the standard USA title, as it supports the same language and is considered
superior due to having more content.

!!! note
    A user can force adherence to region order  with the **Prefer regions over languages**
    option. In that scenario, _Example Title (USA)_ is selected at the cost of losing the
    extra content in _Example Title - Game of the Year Edition (United Kingdom)_.

Supersets are also useful to manage things like DVD releases of titles that were
previously distributed on multiple CDs. For example, if a DAT file contains the following
title names, all of which represent the same title:

```
Example Title (Disc 1) (USA)
Example Title (Disc 2) (USA)
Example Title (Disc 3) (USA)
Beispieltitel (Disc 1) (Germany)
Beispieltitel (Disc 2) (Germany)
Beispieltitel (Disc 3) (Germany)
Example Title (USA)
```

And _Example Title (USA)_ is the DVD version of the three-disc CD release
_Example Title (USA)_ and _Beispieltitel (Germany)_ titles, then you can set up a
`variants` object as follows:

```json hl_lines="8 9 10 18 19 20 28 29 30"
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
