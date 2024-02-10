---
hide:
  - footer
---

# Variants

When Retool doesn't automatically detect titles that are related to each other,
you can manually group them together in the `variants` array. The `variants`
array can also be used to set certain properties on titles that aid with
filtering.

You can do the following things in a `variants` array:

* Assign titles with different names to the same group.

* Move titles to different groups than Retool initially assigns them to.

* Group supersets and compilations with individual titles.

* Set priorities on titles to make sure Retool selects the correct one during
  1G1R processing.

* Assign categories to titles.

* Set local names for titles.

* Tell Retool to ignore titles (not recommended).

* Use `filters` to conditionally do some of the above things based on a title's
  regions, languages, a regex match against its full name, or the user's region
  order.

## Structure

A `variants` array contains objects, and looks similar to the following example:

```json
"variants": [// (1)!
  {
    "group": "Example Title",// (2)!
    "categories": ["Demos", "Games"],// (8)!
    "titles": [// (3)!
      {"searchTerm": "Example Title"},// (4)!
      {"searchTerm": "Exemple de Titre"},
      {"searchTerm": "Titolo di Esempio"},
      {"searchTerm": "Example Title Budget Edition", "priority": 2}// (5)!
    ],
    "supersets": [// (6)!
      {"searchTerm": "Example Title Special Edition"}
    ],
    "compilations": [// (7)!
      {"searchTerm": "Example Title I & II Series Collection", "titlePosition": 1}
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
6.  The `supersets` array contains singular titles that contain more content, or for some
    reason are superior to standard versions. For example, game of the year editions, or a
    DVD version of a title that was previously released on multiple CDs.
7.  The `compilations` array contains titles that in themselves contain multiple titles.
    They might be from the same series of games, a single publisher, from a single genre,
    or otherwise.
8.  The `categories` array overrides an existing title's categories, and replaces them
    with the ones in the list. When applied at this level, all `titles`, `supersets`,
    and `compilations` are assigned the listed categories.

Each object in the `variants` array describes a group of titles, and can include the
following keys:

<table>
  <thead>
    <tr>
      <th width="20%">Key</th>
      <th width="20%">Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>group</code></td>
      <td><code>str</code></td>
      <td>The <code>group</code> value is used as the new
      <a href="../naming-system#group-names">group name</a> and
      <a href="../naming-system#short-names">short name</a> for all of the titles in the
      object.</td>
    </tr>
    <tr>
      <td><code>categories</code></td>
      <td><code>array[str]</code></td>
      <td>Optional. A category is a class of titles, like Demos, Games, and Multimedia.
      Multiple categories can be assigned to a title, and existing categories are
      overridden. If assigned at this level, all <code>titles</code>,
      <code>supersets</code>, and <code>compilations</code> in the object inherit the
      listed categories.</td>
    </tr>
    <tr>
      <td><code>ignore</code></td>
      <td><code>bool</code></td>
      <td>
      <p>Optional. Force removes the title from Retool's consideration. If assigned at
      this level, all <code>titles</code>, <code>supersets</code>, and
      <code>compilations</code> in the object are ignored.</p>
      <div class="admonition warning">
        <p class="admonition-title">Caution</p>
        <p>The <code>ignore</code> key should almost never be used, as ignored titles are
          completely removed from Retool's consideration during processing, and their
          relationship with other titles is destroyed. This makes it particularly hard to
          keep track of relationships when updating clone lists, and can frustrate any
          traces you perform to debug issues.</p>
      </div>
      </td>
    </tr>
    <tr>
      <td><a href="../contribute-clone-lists-variants-titles"><code>titles</code></a></td>
      <td><code>array[obj]</code></td>
      <td>
        <p>Optional. Contains singular, standard titles that belong to a group.</p>
        <p>A <code>variants</code> object must contain at least one <code>titles</code>,
        <code>supersets</code>, or <code>compilations</code> array.</p>
      </td>
    </tr>
    <tr>
      <td><a href="../contribute-clone-lists-variants-supersets"><code>supersets</code></a></td>
      <td><code>array[obj]</code></td>
      <td>
        <p>Optional. Contains singular titles that contain more content, or for some
          reason are superior to standard versions. This might include, for example,
          a game of the year edition, an all-in-one pack that bundles a game and all its
          DLC, or a DVD version of a title that was previously released on multiple
          CDs.</p>
        <p>A <code>variants</code> object must contain at least one <code>titles</code>,
        <code>supersets</code>, or <code>compilations</code> array.</p>
      </td>
    </tr>
    <tr>
      <td><a href="../contribute-clone-lists-variants-compilations"><code>compilations</code></a></td>
      <td><code>array[obj]</code></td>
      <td>
        <p>Optional. Contains titles that in themselves contain multiple titles. They might
        be from the same series of games, a single publisher, from a single genre, or
        otherwise.</p>
        <p>A <code>variants</code> object must contain at least one <code>titles</code>,
        <code>supersets</code>, or <code>compilations</code> array.</p>
      </td>
    </tr>
  <tbody>
</table>

## Standards

The following standards should be adhered to when contributing to a `variants` array. This
helps to keep clone lists maintainable.

### Order

1.  Keep all the objects in the `variants` array in alphabetical order, based on the
    `group` name.

1.  Within an object inside the `variants` array, keep the key order as follows:

    1.  `group`

    1.  `categories`

    1.  `ignore`

    1.  `titles`

    1.  `supersets`

    1.  `compilations`

1.  Make sure the objects inside the `titles`, `supersets`, and `compilations` arrays are
    ordered by priority first, and then alphabetically within those priorities.

    For example, this is correct:

    ```json  hl_lines="4-9"
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

    ```json  hl_lines="4-9"
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

### Group names

The `group` key in each array object should be based on one of the title names in the
group, preferably from a USA variant and in English. Some titles won't exist in all
regions, so follow this order for naming the `group` key:

1.  USA name in English

1.  United Kingdom name in English

1.  European name in English

1.  Any other region in English

1.  Japanese name

1.  Spanish name

1.  Portuguese name

1.  French name

1.  German name

1.  Whatever other name is available

#### Avoid certain group names

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
