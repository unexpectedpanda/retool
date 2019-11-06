# 0.35
- Moved Brazil and Latin America out of the native English list. Modern games
  aren't guaranteed to have an English translation.
- Removed requirement for Logiqx doctype on input files, as some dats that
  weren't from Redump were erroring.
- Removed requirement for Redump to be the dat author.
- Handled empty name, description, author, url, and version fields in XML files.
- Found a similar app called [FilterQuest](https://github.com/UnluckyForSome/FilterQuest).
  Skimmed its dupe list for titles I'd missed, while leaving out the titles
  that weren't actually dupes.

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

# 0.2
- Refactored for performance, code readability, and usability.
- Can handle CLRMAMEPro dat files now, not just Logiqx XML format.
- Added Germany, Ireland, Israel, Latin America, New Zealand, and Taiwan
  locales.
- Fixed user input bugs.
- Fixed excessive looping in some sections.
- Fixed title exclusion bugs.
- Added more error checking.
- Removed -re and -ra flags until refactor until next version.

# 0.1
- Initial release.