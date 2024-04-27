---
hide:
  - footer
---

# Filters

Filters are a way to isolate specific titles in a search result, and apply `results` to
them based on `conditions`.

```json hl_lines="6-10"
{
  "group": "Bomberman GB 2",
  "titles": [
    {
      "searchTerm": "Bomberman GB 2",
      "filters": [
        {
          "conditions": {"matchRegions": ["Japan"]},
          "results": {"group": "Bomberman GB"}
        }
      ]
    }
  ]
}
```

In the previous example the `searchTerm` of `Bomberman GB2` finds all titles
with the short name `Bomberman GB2`, and gathers them in the `Bomberman GB2`
group. If the region of a title happens to include `Japan`, then that title
is moved to the group `Bomberman GB` instead.

Because the `filters` key is an array, you can add as many conditions and
results pairs as you like.

The valid conditions are:

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
      <td><code>matchLanguages</code></td>
      <td><code>array[str]</code></td>
      <td>
        <p>Optional. A list of languages using
          <a href="https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes">
            ISO-639-1</a>
        two-letter language codes, that a title must match for the condition to
        be true.</p>
        ```json
        "conditions": {
          "matchLanguages": ["Fr", "Nl" , "Sv", "No", "Da", "Fi"]
        }
        ```
      </td>
    </tr>
    <tr>
      <td><code>matchRegions</code></td>
      <td><code>array[str]</code></td>
      <td>
        <p>Optional. A list of regions that a title must match for the condition
        to be true.</p>
        ```json
        "conditions": {
          "matchRegions": ["Europe", "Japan"]
        }
        ```
      </td>
    </tr>
    <tr>
      <td><code>matchString</code></td>
      <td><code>str</code></td>
      <td>
        <p>Optional. A regex string that must match against the title's full name
        for the condition to be true.</p>
        ```json
        "conditions": {
          "matchString": "\\(Special Edition\\)"
        }
        ```
      </td>
    </tr>
    <tr>
      <td><code>regionOrder</code></td>
      <td><code>obj[str[array[str]]]</code></td>
      <td>
        <p>Optional. A list of regions that must be higher than others in the
        user's region priority for the condition to be true.</p>
        <p>If <em>any</em> of the regions in the <code>higherRegions</code>
        array is higher in the user region order than <em>all</em> of the
        regions in the <code>lowerRegions</code> array, then the condition is
        true.
        ```json
        "regionOrder": {
          "higherRegions": ["Europe"],
          "lowerRegions": ["Spain"]
        }
        ```
        <p>You can also use <code>All other regions</code> as the only region in
        either the <code>higherRegions</code> or <code>lowerRegions</code>
        arrays, and the remaining regions will be calculated automatically based
        on the array you've already populated.</p>
        ```json
        "regionOrder": {
          "higherRegions": ["Japan", "Korea", "Taiwan", "Asia"],
          "lowerRegions": ["All other regions"]
        }
        ```
        </td>
    </tr>
  </tbody>
</table>

The valid results are:

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
      <td><code>categories</code></td>
      <td><code>array[str]</code></td>
      <td>Optional. A category is a class of titles, like Demos, Games, and
        Multimedia. Multiple categories can be assigned to a title, and existing
        categories are overridden.</td>
    </tr>
    <tr>
      <td><code>englishFriendly</code></td>
      <td><code>bool</code></td>
      <td>
        <p>Optional, defaults to <code>false</code>. An English-friendly title
          is one that hasn't been marked as supporting English, but an
          English-speaking player can easily play to completion. Setting
          <code>englishFriendly</code> to <code>true</code> makes Retool treat a
          title as if it supports English.</p>
      </td>
    </tr>
    <tr>
      <td><code>group</code></td>
      <td><code>str</code></td>
      <td>Optional. The <code>group</code> value is used as the new
        <a href="../naming-system#group-names">group name</a> and
        <a href="../naming-system#short-names">short name</a> for all the titles
        that match the filter.</td>
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
      <td><code>superset</code></td>
      <td><code>bool</code></td>
      <td>Optional. Designates the title as a superset. Supersets are variants
        of titles that contain more content, or for some reason are superior to
        another version. This might include, for example, a Game of the Year
        edition, an all-in-one pack that bundles a game and all its DLC, or a
        DVD version of a title previously released on multiple CDs.</td>
    </tr>
    <tr>
      <td><code>localNames</code></td>
      <td><code>object[str, str]</code></td>
      <td>
        <p>Optional. Contains the local names of a title. Add names for all
          available languages, including English.</p>
        <p>Language keys must be lowercase versions of languages found in the
          <code>user-config.yaml</code> file or RetoolGUI languages list. For
          example, <code>japanese</code>, <code>russian</code>,
          <code>chinese (traditional)</code>.</p>
        ```json
        "localNames": {
          "english": "Example title",
          "chinese (traditional)": "標題範例",
          "japanese": "タイトルの例"
        }
        ```
        <p>See <a href="../contribute-clone-lists-variants-local">Local names</a>
        for more information on specifying local names.</p></td>
    </tr>
    <tr>
      <td><code>priority</code></td>
      <td><code>int</code></td>
      <td>
        <p>Optional, defaults to <code>1</code>. Lower numbers are considered higher
          priority, with <code>1</code> being the highest priority. Typically, a title
          with a higher priority wins when Retool is choosing a 1G1R title.</p>
        <p>Priorities for <code>titles</code> are only taken into account for titles in
          the same region, with same group and short name.</p></td>
    </tr>
  </tbody>
</table>
