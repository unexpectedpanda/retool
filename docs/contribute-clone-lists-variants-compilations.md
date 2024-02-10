---
hide:
  - footer
---

# The compilations array

The `compilations` array is found in objects inside the [`variants`](contribute-clone-lists-variants.md#structure)
array. The objects inside the `compilations` array list variants of titles that belong to
a `group`.

!!! tip
    Make sure you've read how the [`titles`](contribute-clone-lists-variants-titles.md)
    array works before learning about compilations.

You add compilations to the groups of each individual title that's
found in the compilation. For example, for a compilation of
_Example Title 1 & Example Title 2 (Europe) (En,De,Fr+En,Ja)_ you add it to the groups
_Example Title_ and _Example Title 2_.

Even if a title in the compilation is not available separately, for Retool to
work properly you must create a group as if the standalone title exists, and add
the compilation to it.

A `compilations` array looks similar to the following example:

```json hl_lines="10 11 12 16 17 18"
"variants": [
  {
    "group": "Example Title",
    "titles": [
      {"searchTerm": "Example Title"},
      {"searchTerm": "Exemple de Titre"},
      {"searchTerm": "Titolo di Esempio"},
      {"searchTerm": "Example Title Budget Edition", "priority": 2}
    ],
    "compilations": [
      {"searchTerm": "Example Title 1 & Example Title 2", "titlePosition": 1}
    ]
  },
  {
    "group": "Example Title 2",
    "compilations": [
      {"searchTerm": "Example Title 1 & Example Title 2", "titlePosition": 2}
    ]
  }
]
```

When Retool is comparing titles, a compilation inside a group is treated as if
it is only one of the titles in the compilation. For example,
`Example Title 1 & Example Title 2` inside a group of `Example Title 2` is
treated as if it is only _Example Title 2_ for comparison purposes. This is
known as a _virtual title_.

You can use the following keys in an object that's in a `compilations` array:

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
        <p>Setting a priority on a compilation sets it for the virtual title, not the
          compilation itself. Virtual title priorities are compared against
          <code>titles</code> and <code>supersets</code> priorities.</p>
      </td>
    </tr>
    <tr>
      <td><code>titlePosition</code></td>
      <td><code>int</code></td>
      <td>
        <p>Optional. Sometimes No-Intro uses the <code>+</code> notation in
        language tags for compilations, using it as a separator to assign different
        languages to each title in the compilation. For example,
        <em>Example Title 1 + Example Title 2 (Europe) (En,De,Fr<strong>+</strong>En,Ja)</em>
        means that <em>Example Title 1</em> in the compilation supports English, German,
        and French, whereas <em>Example Title 2</em> supports English and Japanese.</p>
        <p>To assign the correct languages to the appropriate virtual title when the
        <code>+</code> notation is used, you need to set a <code>titlePosition</code>. As
        <em>Example Title</em> is first in the compilation name, in the
        <code>Example Title</code> group you set a <code>titlePosition</code> of
        <code>1</code> on the compilation. This creates the virtual title
        <em>:V: Example Title (Europe) (En,De,Fr)</em>, which is used to compare against
        the individual variants of that title also listed in the group. In the
        <code>Example Title 2</code> group you set a <code>titlePosition</code> of
        <code>2</code>. This creates the virtual title
        <em>:V: Example Title 2 (Europe) (En,Ja)</em> for the sake of comparison.</p>
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
  <tbody>
</table>


## How it works

Assume a DAT file contains the following titles:

```
Example Title (USA)
Example Title (Europe)
Example Title Budget Edition (USA)
Example Title 1 & Example Title 2 (Europe) (En,Fr,De+En,Ja)
Exemple de Titre (France)
Titolo di Esempio (Italy)
Example Title 2 - Special Edition (USA)
```

They are all individual titles, except for
_Example Title 1 & Example Title 2 (Europe) (En,Fr,De+En,Ja)_, which is a compilation of
_Example Title_ and _Example Title 2_. How do we make sure that
compilation is properly compared against the individual titles it's made of?

The answer is to add the compilation to a group for each individual title.

```json hl_lines="10 11 12 19 20 21"
"variants": [
  {
    "group": "Example Title",
    "titles": [
      {"searchTerm": "Example Title"},
      {"searchTerm": "Exemple de Titre"},
      {"searchTerm": "Titolo di Esempio"},
      {"searchTerm": "Example Title Budget Edition", "priority": 2}
    ],
    "compilations": [
      {"searchTerm": "Example Title 1 & Example Title 2", "titlePosition": 1}
    ]
  },
  {
    "group": "Example Title 2",
    "titles": [
        {"searchTerm": "Example Title 2 - Special Edition"}
      ],
    "compilations": [
      {"searchTerm": "Example Title 1 & Example Title 2", "priority": 2, "titlePosition": 2}
    ]
  }
]
```

Assuming a user sets USA as their highest region, here's what happens when Retool
processes these groups:

1.  Retool looks at the `Example Title` group, and finds
    _Example Title 1 & Example Title 2 (Europe) (En,Fr,De+En,Ja)_ in the DAT file via the
    compilations search term `Example Title 1 & Example Title 2`.

1.  That compilation is assigned a virtual name that matches the group name, and includes
    region and language information: _:V: Example Title (Europe) (En,Fr,De)_. The languages
    of `En,Fr,De` are added because a `titlePosition` of `1` has been set, so Retool knows
    to use the first set of languages out of `(En,Fr,De+En,Ja)`.

    Creating a virtual title effectively splits out that indvidual title from the
    compilation for comparison, meaning the second title in the compilation isn't
    considered when comparing titles in this group. Because no `priority` is defined, the
    virtual title is assigned a priority of `1`.

1.  Retool looks at the `Example Title 2` group, and finds
    _Example Title 1 & Example Title 2 (Europe) (En,Fr,De+En,Ja)_ in the DAT file via the
    compilations search term `Example Title 1 & Example Title 2`.

1.  Although it's the same compilation as before, it's assigned a virtual name that
    matches the `Example Title 2` group name: _:V: Example Title 2 (Europe) (En,Ja)_. The languages
    of `En,Ja` are added because a `titlePosition` of `2` has been set, so Retool knows
    to use the second set of languages out of `(En,Fr,De+En,Ja)`.

    This means the first title in the compilation isn't considered when comparing titles in
    this group. This variant of the title inside the compilation is a lower version than
    _Example Title 2 - Special Edition (Europe)_, so it is assigned a priority of `2`.

1.  _Example Title (USA)_ wins against other individual titles in its group, because the
    user has set USA as their highest region, and `Example Title Budget Edition` has been
    set to a priority of `2`.

1.  _Example Title 2 - Special Edition (Europe)_ wins as the individual title in its group,
    because it is the only individual title in the `Example Title 2` group.

1.  Retool compares the virtual compilation titles against the individual titles in the
    same groups:

    * _Example Title (USA)_ is compared against _:V: Example Title (Europe) (En,Fr,De)_.
      The individual USA title wins due to region priority.

    * _Example Title 2 - Special Edition (Europe)_ is compared against
      _:V: Example Title 2 (Europe) (En,Ja)_. The latter is discarded because it has a lower
      priority.

Ultimately _Example Title (USA)_ and _Example Title 2 - Special Edition (Europe)_ become the
1G1R titles, and _Example Title 1 & 2 (Europe) (En,Fr,De+En,Ja)_ is discarded.
