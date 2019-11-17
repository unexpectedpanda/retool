# 0.40
- It's now optional to filter by English titles, so you can identify all unique
  titles regardless of language. Use the `-en` option to only include English
  titles.
- You can now remove alternate (Alt) titles with the `-l` option.
- Now removes titles that aren't the latest revisions or versions. This doesn't
  support release versioning, like 0.100 being larger than 0.99, however this
  system generally isn't used for console titles.
- Now removes multi-region dupes (for example, **_Grim Fandango (USA)_**,
  **_Grim Fandango (USA, Europe)_**).
- Massively `_regional_renames.py` to take into account translated titles as a
  result of the above option.
- Moved Brazil and Latin America out of the native English list. Modern games
  from these regions aren't guaranteed to have an English translation.
- Removed requirement for Logiqx doctype on input files, as some dats that
  weren't from Redump and missed the dtd string were erroring.
- Removed requirement for Redump to be the dat author.
- Escaped characters that aren't valid in XML (<, >, &, ", ').
- Handled empty name, description, author, url, and version fields in XML files.
- Added DTD validation for Logiqx dat files. Redump dat files are invalid by
  default as the category tag isn't in the spec. A modified DTD file has been
  included in the release with the category tag added.
- Fixed bug where things broke if the input or output file name included any of
  the option flags.
- Found a similar app called [FilterQuest](https://github.com/UnluckyForSome/FilterQuest).
  Skimmed its dupe list for valid dupes that I'd missed.
- Reorganized `_regional_renames.py` to be master title above dupe titles,
  instead of an inline comment. It makes the file larger, but should make 1G1R
  dupe management easier later on.
- Added title count to output file name.
- The `-o` flag is no longer mandatory, and is now only used to define an
  output folder. Output files are now automatically named.
- Fixed missing title count when splitting dat into regions.

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