---
hide:
  - footer
---

# Top level keys

Each clone list JSON file contains different top level keys that determine how Retool
treats the titles in the related input DAT file. The keys are as follows:

* [`description (obj[str, str])`](contribute-clone-lists-description.md)

* [`categories (array[obj])`](contribute-clone-lists-categories.md)

* [`mias (array[str])`](contribute-clone-lists-mias.md)

* [`overrides (array[obj])`](contribute-clone-lists-overrides.md)

* [`removes (array[obj])`](contribute-clone-lists-removes.md)

* [`variants (array[obj])`](contribute-clone-lists-variants.md)

All keys are optional, except for `description`. They should be kept in the same order in
the clone list as shown in the previous list.
