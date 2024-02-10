---
hide:
  - footer
---

# Metadata files

Metadata files are JSON files that contain scraped data from No-Intro's and Redump's
websites. They're stored in the `metadata` folder, and are used to provide extra language
information and local title names not included in DAT files.

Retool selects the correct metadata file for the loaded DAT file by checking the
`<name>` and `<url>` tags in the header of the DAT file, and then looking for a
matching filename with the release group appended in the `metadata` folder. For
example, for Redump's Sony PlayStation DAT file, the `<name>` is `Sony -
PlayStation`. Therefore Retool looks for the clone list `Sony - PlayStation
(Redump).json` in the `metadata` folder.

Metadata files are generated, and as a general rule shouldn't be manually edited. To
make a change, don't submit a PR. Instead, report the issue upstream:

#### No-Intro

  1. Go to [Dat-o-matic](https://datomatic.no-intro.org/).

  1. Select the system the title is on.

  1. Do a search for the archive name of the title with the issue.

  1. Click on the title's name to open its page.

  1. Click **New ticket**, fill out the form, and then submit it.

#### Redump

Go to Redump's [**Fixes & additions** forum](http://forum.redump.org/forum/15/fixes-additions/),
and request the issue be fixed.
