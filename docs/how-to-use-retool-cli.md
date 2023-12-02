---
hide:
  - footer
---

# How to use Retool CLI

What follows is a step-by-step walkthrough of using Retool CLI and all of its features. If
you're new to DAT management, it might be beneficial to spend some time reading about
[terminology](terminology.md), and after you've filtered a DAT file with Retool, check
out the help documentation for your favorite ROM manager to learn how to use it.

!!! Info
    Depending on your operating system, all Python commands in this guide might need to be
    prefixed with `python` or `python3` to work.

## Get started

The following sections cover the initial setup for Retool.

### Download DAT files and Retool

Before you can filter DAT files, they need to be on your hard drive.

1.  Download the DAT files for the system you want to verify. Retool supports DAT files
    from the following groups:

    * [No-Intro](https://datomatic.no-intro.org/index.php?page=download)

    * [Redump](http://redump.org/downloads/)

    You might need to extract a ZIP file containing the DAT files to access them.

1.  [Download Retool](download.md), and follow the installation and update instructions for
    your platform.

## Basic usage

In your terminal/Command Prompt, change the folder to where Retool is installed, and
then run the following command:

```
retool.py -h
```

This shows all the options available to you.

To process a DAT file without any options, enter the following command:

<pre><code>retool.py <span class="variable">PATH_TO_DAT_FILE</span></code></pre>

## The user-config.yaml file

This file is user-editable, and contains the following configuration options for Retool.
By default it is found in the `config` folder. See [an example of a `user-config.yaml` file](user-config.md).

### Language order

Optional. This is defined by the `language order` array. If you leave all languages
commented out (preceded by a `#`), then Retool includes all languages during processing,
and uses an [implied language order](terminology.md#implied-languages)
derived from your region order.

Order is important. For example, if you have the following title names in an input DAT
file:

```
This is a title (Europe) (En,Fr,De)
This is a title (Europe) (En,Fr,De,Es,It)
This is a title (Europe) (Es)
This is a title (Europe) (Fr,De,Es,It)
```

And the following language order:

1.  English

1.  Spanish

1.  Italian

Then the following title is selected as the 1G1R title:

```
This is a title (Europe) (En,Fr,De,Es,It)
```

And these titles are removed from consideration:

```
This is a title (Europe) (Es)
This is a title (Europe) (Fr,De,Es,It)
This is a title (Europe) (En,Fr,De)
```

This is because `This is a title (Europe) (En,Fr,De,Es,It)` supports all three languages.

The array doesn't just define an order &mdash; languages are also treated like filters.
This means if you only add `English` as a language, for example, then only titles that
support English or have unknown languages are included by Retool in the final result.

The `language order` array is only used by Retool if you pass the `-l` command line
option, otherwise it assumes you want all languages.

### Region order

This is defined by the `region order` array. At least one region must be uncommented.

### Video order

This is defined by the `video order` array. Video standards are processed after regions,
languages, and many other criteria like versions and supersets. Additionally, a video
standard is only determined by an explicit tag in a title's name, for example
`This is a title (World) (NTSC)`. As such, the video order is effectively only used as a
tie-breaker when choosing between two titles that both specify a video standard in their
names. Don't expect to get NTSC titles if you prioritize NTSC as a video standard, but
put Europe first in your region order.

### List prefix and suffix
Optional. Defined by the `list prefix` and `list suffix` arrays. Only one entry is
permitted per array. If you are using the `--listnames` option, this defines the prefix
and suffix to add to each line. If a prefix starts with `http://`, `https://`, or
`ftp://`, then each line in the output file is URL encoded.

### Global exclude and include overrides

Optional. Defined by the `exclude` and `include` arrays.

You can override the default choices Retool makes by force including or excluding
titles whose names match a certain string. Each string must be on its own line.

An excluded title forces Retool to act as if the title was never in the input DAT in the
first place. This means that an exclude can force Retool to select a different title when
choosing 1G1R titles.

An included title makes it into the output DAT regardless of Retool's choices. Even if
Retool has removed a title as part of the filtering process, a matching include brings it
back. Only a post filter can remove an included title.

There are rules when it comes to overrides, and how they interact at the global settings
and system settings level:

* System includes override all excludes.
* System excludes override global includes.
* Global includes override global excludes.

To read about the different ways you can match titles, see
[Override and post filter match types](#override-and-post-filter-match-types).

!!! note
    If Retool has genuinely missed a relationship between titles, please don't just
    create an override &mdash; [create an issue](https://github.com/unexpectedpanda/retool/issues)
    too so the clone lists or Retool can be updated.

### Post filters

Optional. Defined by the `filters` array.

After Retool has finished processing, you can filter the results to only include titles
that match the text you provide. Each match must be on its own line.

To read about the different ways you can match titles, see
[Override and post filter match types](#override-and-post-filter-match-types).

### Override and post filter match types

There are three different match types for overrides and post filters:

* Plain text indicates a partial string match.
* A prefix of `/` indicates a regular expression match.
* A prefix of `|` indicates a full string match.

Additionally, you can wrap any of these strings in `<>` when using overrides to also
include or exclude any match's related clones. Wrapping strings in `<>` is not supported
for post filters.

!!! warning
    If you need to use a backslash (`\`) or double quote (`"`) in your overrides, you
    must escape them with a backslash. For example:

    * `\\`
    * `\"`

#### Partial matches
If a line isn't prefixed with `|` (full match) or `/` (regular expression) in an
**Exclude** or **Include**, then it's interpreted as a partial match. A partial match
looks for the specified text inside all title names.

For example, if an input DAT contains the following title names:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

And your `user-config.yaml` has the following excludes:

```
exclude:
- "Hot"
- "Cold"
```

Every title in the example list is excluded from the output DAT file. This is because
`Cold` matches `It's Pretty Cold (Japan)`, and `Hot` matches every other title, as it's
found in both the word `Hot` and `Hotel`.

Now let's add an include:

```
exclude:
- "Hot"
- "Cold"

include:
- "Ho"
```

The behavior changes again:

* The include for `Ho` overrides the exclude for `Hot`.
* The include for `Ho` prevents Retool from assigning
  `Do You Think it's Hot (USA) (Alt)` to `Do You Think it's Hot (USA)` as a clone,
  meaning _both_ titles end up in the output DAT file.

As you can see, you need to be careful when using partial matches.

#### Regular expressions

If you're familiar with regular expressions, also known as "regexes", you know the power
(and pain) that they can bring. To define an include or exclude as a regex, prefix it
with a forward slash (`/`).

!!! tip
    If you don't know regex, you can [learn the basics at regexlearn.com](https://regexlearn.com/learn/regex101).
    You want to be well practiced before using them, as without proper care they can lead
    to unintended consequences.

For example, if an input DAT contains the following title names:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

And your `user-config.yaml` has the following exclude:

```
exclude:
- "/^I
```

All titles beginning with `I` are excluded from the output DAT file.

Now let's add an include:

```
exclude:
- "/^I

include:
- "/\(USA\)"
```

Here all USA titles are kept, even if they start with `I`, because includes override
excludes. In the example list the `(Alt)` title is usually removed by Retool as a clone
of the original, but the include filter of `/\(USA\)` makes sure it's kept.

#### Full matches

Full matches only apply to titles with the exact same name. To define an include or
exclude as a full match, prefix it with a pipe (`|`).

For example, if an input DAT contains the following titles:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

And your `user-config.yaml` has the following exclude:

```
exclude:
- "|Do You Think it's Hot (USA)"
```

Then that title is excluded from the output DAT file.

If you remove the exclude, and then put the following include in:

```
include:
- "|Do You Think it's Hot (USA) (Alt)"
```

Then that title is kept in the output DAT file, and the final titles chosen are:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

In the example list the `(Alt)` title is usually removed by Retool as a clone of the
original, but the include filter makes sure it's kept.

### GUI settings

Don't edit these. They are used by the GUI and ignored during CLI operation.

## System settings config files

Settings are available at two levels in Retool: global and system.

* **Global settings** are applied to every DAT Retool processes, so long as system
  settings don't override them. These are stored in [`config/user-config.yaml`](#the-user-configyaml-file).

* **System settings** are applied to a specific system named in a DAT file. For example,
  you can have settings for just the _Sony - PlayStation_ DAT file from Redump.
  System settings are mostly the same as global settings, although their config files are
  slightly different. They are stored in the `config/systems` folder, and are YAML files
  named after their system and release group.
  [See an example of a system settings config file](system-config.md).

While it's possible to construct a system settings file by hand, it's more convenient to
set the options in Retool's GUI and let it generate one for you. After the system config
file exists, Retool CLI references it every time it processes that system.

## Command line options

In addition to the settings found in [`user-config.yaml`](#the-user-configyaml-file), you
can pass other settings via command line options.

### Options

These options change how Retool handles certain titles.

* **`-d` Disable 1G1R filtering**{:#disable-1g1r}
  <br>Ignore clone lists, and treat each title as unique. Useful if you want to keep
  everything from a specific set of regions and/or languages. You can use this in
  combination with [`--regionsplit`](#region-split) to treat Retool as a region splitter
  and nothing more.
  <br>
  <br>This option isn't compatible with [`--legacy`](#legacy).

* **`-e` Include titles without hashes or sizes specified in the input DAT file**
  <br>Some DAT files don't list any hashes or sizes for some files, and Retool overrides
  these out by default. This option makes sure those files are kept.

* **`-l` Filter by languages using a list**
  <br>If a title doesn't support any of the languages on the list, it's removed (see
  `config/user-config.yaml`).

* **`-r` Prefer regions over languages**
  <br>By default, if a title from a higher priority region doesn't support your preferred
  languages but a lower priority region does, Retool selects the latter. This option
  disables this behavior, forcing strict adherence to region priority regardless of
  language support
  <br>
  <br>This option also overrides similar behavior in superset selection, which means you
  might get a title that was released in your preferred region that has less content,
  instead of one that was released in another region that contains more content and
  supports your preferred languages.

* **`-y` Prefer licensed versions over unlicensed, aftermarket, or homebrew titles**
  <br>Sometimes games are rereleased long after the lifespan of a console, in regions they
  weren't originally available in. By default Retool selects these titles if they match
  your preferred region/language priorities.
  <br>
  <br>Enable this option to choose a production version of a title over the
  unlicensed/aftermarket/homebrew title if possible. This might select titles from a lower
  priority region, or with lower priority languages, or with less features.


* **`-z` Prefer titles ripped from modern rereleases over original system releases**
  <br>For the sake of emulator compatibility, Retool prefers versions of games released
  on the original system instead of those ripped from rereleases on platforms like
  Virtual Console and Steam. This option reverses that behavior.

* **`--nooverrides` Disable global and system overrides**
  <br>Ignore both global and system overrides.

### Exclusions

Retool can exclude specific types of titles from the output DAT file. These exclusions are
either based on the `<category>` tag found in DAT files, or on a string in the title's
name.

To add exclusions, use the `--exclude` option followed by the single letter filters that
indicate each title type. For example, `--exclude aAbcdD`.

The available exclusions are as follows:

* **`a` Applications**
  <br>Titles with the DAT category `Applications`, or with the following text in the name:
    * `(Program)`
    * `(Test Program)`
    * `Check Program`
    * `Sample Program`

* **`A` Audio**
  <br>Titles with the DAT category `Audio`. These might be used as soundtracks by games.

* **`b` Bad dumps**
  <br>Titles marked as bad dumps with a `[b]` in the name.

* **`B` BIOS and other chips**
  <br>Titles with the DAT category `Console`, or with the following text in the name:
    * `[BIOS]`
    * `(Enhancement Chip)`

* **`c` Coverdiscs**
  <br>Titles with the DAT category `Coverdiscs`. These were discs that were attached to
  the front of magazines, and could contain demos, or rarely, full games.

* **`d` Demos, kiosks, and samples**
  <br>Titles with the DAT category `Demos`, or with the following text in the name:
    * `@barai`
    * `(Demo [1-9])`
    * `(Demo-CD)`
    * `(GameCube Preview)`
    * `(Kiosk *|* Kiosk)`
    * `(Preview)`
    * `Kiosk Demo Disc`
    * `PS2 Kiosk`
    * `PSP System Kiosk`
    * `Sample`
    * `Taikenban`
    * `Trial Edition`

* **`D` Add-ons**
  <br>Titles with the DAT category `Add-Ons`. This includes expansion packs and additional
  materials for titles.

* **`e` Educational**
  <br>Titles with the DAT category `Educational`.

* **`g` Games**
  <br>Titles with the DAT category `Games`, or no DAT category.

* **`k` MIA**
  <br>Titles or ROMs declared as missing in action in the clone lists or DAT files.

* **`m` Manuals**
  <br>Titles with `(Manual)` in the name.

* **`M` Multimedia**
  <br>Titles with the DAT category `Multimedia`. These might include games.

* **`o` Bonus discs**
  <br>Titles with the DAT category `Bonus Discs`. These could be anything other than the
  main title content, like patches, manuals, collector discs, or otherwise.

* **`p` Pirate**
  <br>Titles with `(Pirate)` in the name.

* **`P` Preproduction**
  <br>Titles with the DAT category `Preproduction`, or with the following text in the
  name:
    * `(Alpha [0-99])`
    * `(Beta [0-99])`
    * `(Pre-Production)`
    * `(Possible Proto)`
    * `(Proto [0-99])`
    * `(Review Code)`

* **`r` Promotional**
  <br>Titles with the DAT category `Promotional`, or with the following text in the name:
    * `(Promo)`
    * `EPK`
    * `Press Kit`

* **`u` Unlicensed**
  <br>Titles unauthorized by console manufacturers, marked by the following text in the
  name:
    * `(Unl)`
    * `(Aftermarket)`
    * `(Homebrew)`
    * `(Pirate)`

* **`v` Video**
  <br>Titles with the DAT category `Video`.

### Outputs
* **`--listnames` Also output a TXT file of just the kept title names**
  <br>See [`config/user-config.yaml`](#the-user-configyaml-file) to add a prefix and/or
  suffix to each line.

* **`--log` Also output a TXT file of what titles have been kept, removed, and set as clones**

* **`--originalheader` Use the original input DAT header in the output DAT**
  <br>Useful if you want to load Retool DATs as an update to original Redump and No-Intro
  DATs already in CLRMAMEPro.

* **`--output <folder>` Set an output folder where the new 1G1R DAT file/s will be created**

* **`--regionsplit` Split the result into multiple DAT files based on region**{:#region-split}
  <br>Use with `-d` to only split by region with no 1G1R processing. Not compatible with
  [`--legacy`](#legacy).

* **`--removesdat` Also output a DAT file containing the titles that were removed from the 1G1R DAT file**

### Debug
* **`--config <file>` Set a custom user config file to use instead of the default**
  <br>Useful for testing.

* **`--clonelist <file>` Set a custom clone list to use instead of the default**
  <br>Useful if you want to use your own, or if Redump or No-Intro renames their DAT file
  and the clone list isn't automatically detected anymore. Often used together with
  `--metadata`.

* **`--metadata <file>` Set a custom metadata file to use instead of the default**
  <br>Useful if you want to use your own, or if Redump or No-Intro renames their DAT
  file and the metadata file isn't automatically detected anymore. Often used together
  with `--clonelist`.

* **`--legacy` Output DAT file/s in legacy parent/clone format**{:#legacy}
  Not recommended unless you're debugging or comparing outputs between DAT versions. Not
  compatible with [`-d`](#disable-1g1r).

* **`--nodtd` Bypass DTD validation**
  <br>Skips DTD validation of DAT files, useful if validation is causing issues.

* **`--singlecpu` Disable multiprocessor usage**
  br>Forces Retool to use only a single CPU core, at the cost of performance. This can
  be useful when debugging Retool, as multiprocessor doesn't cope well with `input`
  statements.

* **`--trace  [ ...]` Trace a title through the Retool process for debugging**
  <br>Follows a title through Retool's selection process for debugging. Accepts a regular
  expression. To function properly, this disables using multiple processors during parent
  selection.
  <br>
  <br>Usage:
  <br>
  ```
  --trace "regex of titles to trace"
  ```

* **`--warnings` Report clone list warnings during processing**

* **`--warningpause` Pause when a clone list warning is found**
  <br>Useful when batch processing DAT files.

!!! tip
    If you don't know regular expressions, also known as "regexes", you can
    [learn the basics at regexlearn.com](https://regexlearn.com/learn/regex101). You want
    to be well practiced before using them, as without proper care they can lead to
    unintended consequences.
