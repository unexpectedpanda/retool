---
hide:
  - footer
---

# Create and edit clone lists

Clone lists are JSON files that primarily define relationships between titles that Retool
doesn't automatically pick up. They're useful both for matching titles of completely
different names, and for overriding some of the default choices that Retool makes.
Additionally, they can add more accurate filter criteria like different categories to
titles, and even additional data like local title names.

Contributing to Retool's clone lists directly involves code and being familiar with Git
and GitHub. If that's not something you're interested in, you can still request clone list
changes by [filing an issue](https://github.com/unexpectedpanda/retool/issues).

If you want to contribute directly, [fork the clone lists and metadata repository](https://github.com/unexpectedpanda/retool-clonelists-metadata), read the following guidelines, make your
changes, and then submit a [pull request](https://github.com/unexpectedpanda/retool-clonelists-metadata/pulls).

## Before you begin

If you want to create or edit clone lists, you need to understand [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
and the following data structures:

* Key/value pairs

* Strings

* Integers

* Arrays

* Objects

It also helps to understand Retool's [terminology](terminology.md), and the different
[names](naming-system.md) it assigns to titles to help match and group them together
accurately.

## Titles that Retool automatically detects as clones

Before referencing clone lists, Retool parses a DAT file and creates objects for all of
its titles. If multiple titles have the same [group name](naming-system.md#group-names) and
[short name](naming-system.md#short-names), Retool assumes they're related to each other.

Names should only be added to clone lists in the following situations:

* To link together titles that ordinarily would have different group/short names due to
  regional naming, for example [_Indigo Prophecy_ and _Fahrenheit_](https://en.wikipedia.org/wiki/Fahrenheit_(2005_video_game)).

* To override Retool's default grouping.

* To assign categories to titles.

* To assign local names to titles.

* To designate a title as missing in action (MIA).

## Clone list location and names

Clone lists are found by default in the `clonelists` subfolder. What subfolder Retool
looks for clone lists in is defined in `config/internal-config.json` in the
`cloneLists` object:

```json
"cloneLists": {
  "localDir": "clonelists"
}
```

Retool selects the correct clone list for the loaded DAT file by checking the `<name>` and
`<url>` tags in the header of the DAT file, and then looking for a matching filename with
the release group appended in the `clonelists` folder. For example, for Redump's Sony
PlayStation DAT file, the `<name>` is `Sony - PlayStation`. Therefore Retool looks for the
clone list `Sony - PlayStation (Redump).json` in the `clonelists` folder. If a matching
file isn't found, then only Retool's automatic clone detection is used.

## Reference sites

The following sites can help in identifying titles that are related to each other, or
for finding local title names.

DAT release groups:

- [No-Intro](http://datomatic.no-intro.org)
  <br>
  Lists clones on individual title pages.

- [Redump](http://www.redump.org)
  <br>
  Useful for local title names that use non-Latin characters like Japanese, Chinese,
  Korean, and Russian. You can then use these in [Google Search](https://www.google.com)
  or [Translate](https://translate.google.com) to help make connections. Sometimes
  there's useful information in the comments of a disc page.

Databases:

- [Atari Mania](http://www.atarimania.com) (Atari titles)
- [Bootleg Games Wiki](https://bootleggames.fandom.com/)
- [GameTDB](https://www.gametdb.com)
- [Handheld Underground](https://hhug.me/)
- [LaunchBox Games Database](https://gamesdb.launchbox-app.com/)
- [Moby Games](https://www.mobygames.com)
- [Online Games DatenBank](https://ogdb.eu/)
- [PlayStation DataCenter](https://psxdatacenter.com/) (PlayStation, PlayStation 2,
  and PlayStation Portable titles)
- [PSCX2 Wiki](https://wiki.pcsx2.net) (PlayStation 2 titles)
- [Renascene](https://renascene.com/psv/) (PlayStation Vita titles)
- [Retroplace](https://www.retroplace.com)
- [Sega Retro](https://segaretro.org/) (Sega console titles)
- [SMS Power](https://www.smspower.org/) (Sega 8-bit console titles)
- [The PC Engine Software Bible](http://www.pcengine.co.uk/) (NEC PC Engine/TurboGrafx-16
  titles)
- [The Cutting Room Floor](https://tcrf.net)
- [The World of CDI](https://www.theworldofcdi.com) (Philips CD-I titles)
- [VDGB](https://vgdb.io)
- [VGM](https://www.video-games-museum.com)

General sites and retail stores:

- [Amazon.jp](https://www.amazon.co.jp)
- [PlayAsia](https://www.play-asia.com/)
- [Wikipedia](https://www.wikipedia.org)
- [YouTube](https://www.youtube.com)
