---
hide:
  - footer
---

# Options

Options change Retool's behavior either at the title level, or the broader DAT file level.

To set options, in the **Global settings** or **System settings** tab, click the
**Options** tab.

![A screenshot of Retool's options tab](images/options.png)

## Title options

These options change how Retool handles certain titles.

* **Disable 1G1R filtering**
  <br>Ignore clone lists, and treat each title as unique. Useful if you want to keep
  everything from a specific set of regions and/or languages. You can use this in
  combination with **Split output into multiple DAT files based on region** to treat
  Retool as a region splitter and nothing more.
  <br>
  <br>If this option is disabled, it's because you've enabled
  **Output DAT files in legacy parent/clone format**, which isn't compatible with this feature.

* **Prefer regions over languages**
  <br>By default, if a title from a higher priority region doesn't support your preferred
  languages but a lower priority region does, Retool selects the latter. This option
  disables this behavior, forcing strict adherence to region priority regardless of
  language support
  <br>
  <br>This option also overrides similar behavior in superset selection, which means you
  might get a title that was released in your preferred region that has less content,
  instead of one that was released in another region that contains more content and
  supports your preferred languages.

* **Prefer titles ripped from modern rereleases over original system releases**
  <br>For the sake of emulator compatibility, Retool prefers versions of games released
  on the original system instead of those ripped from rereleases on platforms like
  Virtual Console and Steam. This option reverses that behavior.

* **Prefer oldest production versions instead of newest**
  <br>Useful for speedrunners and those concerned about censorship, who often want
  unpatched versions of games.

* **Prefer licensed versions over unlicensed titles**
  <br>Sometimes games are rereleased long after the lifespan of a console, in regions they
  weren't originally available in. By default Retool selects these titles if they match
  your preferred region/language priorities.
  <br>
  <br>Enable this option to choose a production version of a title over the unlicensed or
  aftermarket title if possible. This might select titles from a lower priority region, or
  with lower priority languages, or with less features.

* **Disable global and system overrides**
  <br>Ignore both global and system overrides.

## Compilations handling

This option changes how compilations are managed by Retool.

* **Default**
  <br>Chooses individual titles most of the time. Only chooses compilations when they have
  a higher region, language, or clone list priority, or contain unique titles. When
  choosing a compilation for unique titles, if other titles in the compilation have
  individual equivalents, the individual titles are also included, leading to some title
  duplication.

* **Prefer individual titles**
  <br>Chooses individual titles regardless of region, language, and clone list priorities,
  and discards compilations unless they contain unique games. You\'re likely to prefer
  this mode if you use ROM hacks or Retro Achievements. When choosing a compilation for
  unique titles, if other titles in the compilation have individual equivalents, the
  individual titles are also included, leading to some title duplication.

* **Keep individual titles and compilations**
  <br>Ignores the relationship between individual titles and compilations, meaning
  individual titles are only compared against other individual titles, and compilations
  against other compilations. This option has the most title duplication.

* **Optimize for least possible title duplication**
  <br>**Beta**. Not recommended. Prefers compilations to minimize file count. While this
  mode can save disk space, it can be hard to tell what compilations contain based on
  their filename. This mode might not choose the most optimal solution when supersets or
  clone list priorities are involved.

## Output options

These options change the files that Retool outputs as part of its process.

* **Allow processing of already processed files**
  <br>Let DAT files be processed even if Retool has already processed them.

* **Don't modify input DAT file's existing header fields**
  <br>By default Retool changes header fields so you can tell in ROM managers if DAT files
  have been modified. Enable this if you want to load Retool DAT files as updates to
  original Redump and No-Intro DAT files already loaded in your ROM manager.

* **Use `<machine>` instead of `<game>` in output DAT files**
   <br>Exports each title node using the MAME standard of `<machine>` instead of `<game>`.

* **Split the output into multiple DAT files based on region**
  <br>Instead of one output DAT file containing all the filtered results, split the output
  into multiple DAT files based on the regions you've selected. If this is disabled, it's
  because you've enabled **Output DAT files in legacy parent/clone format**, which isn't
  compatible with this option.

* **Also output DAT files of all the removed titles**
  <br>In addition to output DAT files, create DAT files containing the titles Retool
  removed.

* **Also output reports of what titles have been kept and removed**
  <br>In addition to output DAT files, produce TXT files that list what titles have been
  kept, and what titles have been removed.

* **Also output lists of title names from output DAT files**
  <br>In addition to output DAT files, produce TXT files that list only the name of each
  title in the output DAT files, and optionally add a prefix and suffix to each name.
  If you add a prefix that starts with `http://`, `https://` or `ftp://`, each line in the
  file is URL encoded.

## Online features

These features use data supplied by third parties. When those third parties stop updating,
Retool might make choices that are out of date.

* **Add MIA attributes to DAT files**
  <br>For files that no one has, adds `mia="yes"` to `rom/file` tags.

* **Add RetroAchievements attributes to DAT files**
  <br>For titles that support RetroAchievements, adds `retroachievements="yes"` to
  `game/machine` tags. The data source uses hashes from CHD/RVZ files for disc-based
  images, so for this feature to work on Redump DAT files you need to use CHD/RVZ
  versions, like those found at [MAME Redump](https://github.com/MetalSlug/MAMERedump).

* **Prefer titles with RetroAchievements**
  <br>Prioritizes titles that support RetroAchievements. The data source uses hashes from
  CHD/RVZ files for disc-based images, so for this feature to work on Redump DAT files you
  need to use CHD/RVZ versions, like those found at
  [MAME Redump](https://github.com/MetalSlug/MAMERedump).

## Debug options

These options are useful for developing and testing Retool.

* **Report clone list warnings during processing**
  <br>Turn on warnings when there are mismatches between the clone list and the DAT file.

* **Pause on clone list warnings**
  <br>Pause Retool each time a clone list warning is issued.

* **Output DAT files in legacy parent/clone format**
  <br>Not recommended unless you're debugging or comparing outputs between DAT file
  versions. If this is disabled, it's because you've disabled 1G1R filtering or chosen to
  split by region, which isn't compatible with this option.

* **Disable multiprocessor usage**
  <br>Forces Retool to use only a single CPU core, at the cost of performance. This can
  be useful when debugging Retool, as multiprocessor doesn't cope well with `input`
  statements.

* **Trace a title through Retool's process**
  <br>Follows a title through Retool's selection process for debugging. Accepts a regular
  expression. To function properly, this disables using multiple processors during parent
  selection.

!!! tip
    If you don't know regular expressions, also known as "regexes", you can
    [learn the basics at regexlearn.com](https://regexlearn.com/learn/regex101). You want
    to be well practiced before using them, as without proper care they can lead to
    unintended consequences.
