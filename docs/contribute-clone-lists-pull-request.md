---
hide:
  - footer
---

# Prepare your pull request

Before you make a pull request for a clone list, make sure it observes the following
standards.

## Format clone lists

Clone lists follow a particular format to keep maintainence easy:

* Valid JSON.

* Tabbed indenting.

* LF line endings.

* Top-level keys should be kept in [the correct order](../contribute-clone-lists#clone-list-structure).

* Object keys should be in the order shown in the clone list structure examples.

* Array contents should be in alphabetical order, sorted by an object's top key. This is
  either going to be `group` or `searchTerm`.

## Test clone lists

Before submitting a pull request, it's important to test your changes to make sure they're
correct.

Test your clone list update against the newest version of a DAT from No-Intro or Redump,
and enable the following settings:

=== ":fontawesome-regular-window-maximize: GUI"
    * In the **Global settings** tab, click **Options**.

    * Enable **Report clone list warnings during processing** and
      **Pause on clone list warnings**.

=== ":simple-windowsterminal: Command line"

    `--warnings --warningpause`

Run Retool on the DAT file, and fix your clone list until no warnings are given.

## Make your pull request

When you make your pull request, make sure to justify the choices you have made. For
example, if you add new clones, provide a link or images that show the titles are clones.

## Update hashes

Retool manages clone list updates via the `hash.json` file in the clone lists subfolder.
When looking for updates, the newest `hash.json` is downloaded from from the location
specified in `internal-config.json`:

```json
"cloneListMetadataUrl": "https://raw.githubusercontent.com/unexpectedpanda/retool-clonelists-metadata/",
```

The SHA256 hashes in that file are then compared against the clone lists on the local
disk. If a clone list hash doesn't match, then a new version of that file is downloaded
from the same location as listed above.

After your PR has been merged, the `hash.json` is updated by unexpectedpanda with the
SHA256 hash of the updated or new clone lists.