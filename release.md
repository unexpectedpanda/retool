# 0.35
- It's now optional to filter by English titles, so you can identify all unique
  titles regardless of language. Use the `-en` option to only include English
  titles.
- Massively expanded dupe list in _regional_renames.py to take into account
  translated titles as a result of the above option.
- Moved Brazil and Latin America out of the native English list. Modern games
  aren't guaranteed to have an English translation.
- Removed requirement for Logiqx doctype on input files, as some dats that
  weren't from Redump were erroring.
- Removed requirement for Redump to be the dat author.
- Handled empty name, description, author, url, and version fields in XML files.
- Fixed bug where things broke if the input or output file name included any of
  the option flags.
- Found a similar app called [FilterQuest](https://github.com/UnluckyForSome/FilterQuest).
  Skimmed its dupe list for valid dupes that I'd missed.

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
- Fixed CLRMAMEPro header so the user wasn't prompted with false update
  warnings.

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