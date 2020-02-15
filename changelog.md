# 0.51
- Added Zh as a language.
- Fixed a crash if a dat had no titles, and Retool was trying to process
  supersets.

# 0.50
- A huge architectural shift to move Retool to a 1G1R dat generator. Due to
  this, the `_regional_renames.py` file has been renamed to `_renames.py` and
    massively expanded to take into account localized title dupes. The file has
    also been reorganized to make future dupe additions easier.
- The `-re`, `-ra`, and `-en` options have been removed.
- The `-o` flag is no longer mandatory, and now defines an output folder.
  Output files are automatically named.
- You can now remove alternate (Alt) titles with the `-l` option.
- You can now promote supersets (for example, Game of the Year editions) to
  parents with the  `-s` option.
- Expanded demo removal criteria, as Redump does not always put demos in the
  "Demos" category.
- Region processing is now much faster.
- OEM and Hibaihin titles that have a matching commercial title with the same
  name are now marked as clones.
- Titles that aren't the latest revisions or versions are now marked as clones.
  This doesn't support release versioning, like 0.100 being larger than 0.99,
  however there's not much evidence of that style of versioning being used
  across Redump titles.
- Titles that include multiple regions are now deduped, preferencing titles
  with more regions. For example, out of **_Grim Fandango (USA)_** and
  **_Grim Fandango (USA, Europe)_**, the former is marked as a clone.
- Titles with the same name from the same region that include different
  language sets are now handled. The rules are quite complex:
  - If one title is in English, but the other isn't, mark the English title as
    the parent.
  - If one title from Europe has no languages listed, and the other has
    languages listed but English isn't one of them, mark the title with no
    languages listed as the parent (on the assumption that English may be in
    there).
  - If English is listed for both titles, and one title has more languages,
    mark the title with more languages as the parent.
  - If English is listed for both titles, and both titles have the same number
    of languages, check for preferred languages one by one, in the order listed
    below. The first title that doesn't support a preferred language is marked
    as a clone.
    1. Spanish
    1. French
    1. Japanese
    1. Portuguese
    1. German
    1. Italian
    1. Swedish
    1. Danish
    1. Norwegian
    1. Polish
    1. Greek
    1. Dutch
    1. Finnish
    1. Swiss
    1. Hungarian
    1. Russian
- Brazil and Latin America have been moved off the native English list. Modern
  games from these regions aren't guaranteed to have English translations.
- Japan has been moved up to second highest priority for non-native English
  regions, after Europe. The Asia region being higher priority than Japan was
  stealing titles that should have had Japanese parents.
- The requirement for the Logiqx doctype string in input files has been
  removed, as some non-Redump dats didn't have the string and were erroring.
- DTD validation has been added for Logiqx-style dat files. Redump dat files
  are invalid by default, as the category tag isn't in the spec. A modified DTD
  file has been included in the release with the category tag added, so Redump
  dats should pass.
- When you add a newer version of a dat to CLRMAMEPro that has been generated
  by Retool, it now triggers an update prompt where appropriate.
- Redump is no longer required to be the dat author.
- Characters that aren't valid in XML (<, >, &) have been escaped in generated
  dat files.
- Empty name, description, author, url, and version fields in dats are now
  handled, instead of crashing the program.
- Several bugs involving options flags were fixed.
- The title count was missing when dats were split into regions. This is now fixed.
- Bye bye ASCII logo. Vertical screen real estate is now more important.
- Added CloneRel tool, that exports an Excel file from a dat to better display
  existing parent/clone relationships.
- Dealt with the "_King's Field_ problem". _King's Field (Japan)_ didn't get a
  Western release. _King's Field_ in the USA is known as _King's Field II_ in
  Japan. **_King's Field II_** in the USA is **_King's Field III_** in Japan.
  Without extra logic, the program would mark all **_King's Field II_** titles as
  clones, which is not what we want.

# 0.34
- Added textwrap module for better readability on MacOS/Linux.
- Bundled MacOS and Windows binaries.

# 0.33
- Added ability to operate on folders.
- Fixed output file naming bugs.
- Fixed some user input issues.
- Tidied up some output for increased readability.
- Added the following regions: Argentina, Czech, Hungary, Singapore, Slovakia,
  Thailand, Turkey, Ukraine, United Arab Emirates.

# 0.32
- Reimplemented -re and -ra flags.
- Fixed header so the user wasn't prompted with false update warnings when the
  dat was loaded in CLRMAMEPro.

# 0.31
- Used dictionaries and classes to greatly increase performance and improve.
  code readability.
- Removed minidom dependency.
- Removed unused importlib dependency.
- Usability tweaks.

# 0.20
- Refactored for performance, code readability, and usability.
- Can handle CLRMAMEPro dat files now, not just Logiqx XML format.
- Added Germany, Ireland, Israel, Latin America, New Zealand, and Taiwan
  locales.
- Fixed user input bugs.
- Fixed excessive looping in some sections.
- Fixed title exclusion bugs.
- Added more error checking.
- Removed -re and -ra flags until refactor until next version.

# 0.10
- Initial release.