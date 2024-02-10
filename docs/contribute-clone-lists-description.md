---
hide:
  - footer
---

# Description

The `description` object holds information related to the clone list itself, and is
always at the top of the file. It is mandatory to include.

## Structure

A `description` object looks similar to the following example:

```json
"description": {
  "name": "Sony - PlayStation (Redump)",
  "lastUpdated": "26 December 2023",
  "minimumVersion": "2.02"
}
```

A `description` object contains the following keys:

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
      <td><code>name</code></td>
      <td><code>str</code></td>
      <td>The system name and release group of the DAT file the clone list is related
      to.</td>
    </tr>
    <tr>
      <td><code>lastUpdated</code></td>
      <td><code>str</code></td>
      <td>The last time the clone list was updated, in DD-MMMM-YYYY format.</td>
    </tr>
    <tr>
      <td><code>minimumVersion</code></td>
      <td><code>str</code></td>
      <td>
      <p>The minimum version of Retool required to understand all of the features of the
      clone list.</p>
      <p>The <code>minimumVersion</code> key is the only data in the description used by
      Retool, the rest is to make parsing and updating the clone list easier for humans.</p>
      </td>
    </tr>
  <tbody>
</table>
