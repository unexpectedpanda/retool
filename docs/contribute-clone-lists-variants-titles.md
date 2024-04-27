---
hide:
  - footer
---

# The titles array

The `titles` array is found in objects inside the [`variants`](contribute-clone-lists-variants.md#structure)
array. The objects inside the `titles` array list variants of titles that belong to a
`group`.

A `titles` array looks similar to the following example:

```json hl_lines="4-9"
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

You can use the following keys in an object that's in a `titles` array:

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
          priority, with <code>1</code> being the highest priority. Typically, a title
          with a higher priority wins when Retool is choosing a 1G1R title.</p>
        <p>Priorities for <code>titles</code> are only taken into account for titles in
          the same region, with same group and short name.</p>
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
Example Title (Europe)
Example Title Budget Edition (USA)
Exemple de Titre (France)
Titolo di Esempio (Italy)
```

They are all the same title, just different versions or from different regions. A user in
Retool loads the DAT file, and selects the following region order:

```
USA
Europe
United Kingdom
France
Italy
```

When the DAT file is processed, Retool automatically links together _Example Title (USA)_
and _Example Title (Europe)_, as they have the same short name: `example title`. However,
it misses the other titles, as they have different short names.

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
is a short name, and looks in the related DAT file for names that have the same short
name. When it finds those titles, it assigns the same group and short name to them,
`example title`, and then Retool knows they are related.

The `priority` of `2` for `Example Title Budget Edition` indicates that when Retool is
processing the USA region, to select _Example Title (USA)_ over
_Example Title Budget Edition (USA)_ when Retool considers clone list priority. There are
other factors that might eliminate a title before Retool gets to clone list priority.

In this example, because the user has set USA first in the region order,
_Example Title (USA)_ is selected as the 1G1R title, and the others are discarded.
