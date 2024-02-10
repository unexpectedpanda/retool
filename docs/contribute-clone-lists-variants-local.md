---
hide:
  - footer
---

# Local names

The No-Intro and Redump standard is to romanize title names from languages that don't
use a Latin-based alphabet. They also restrict filenames to the
[7-bit ASCII character set](https://montcs.bloomu.edu/Information/Encodings/ascii-7.html),
which removes vital pronunciation cues from even latin-derived alphabets.

While this is useful as a standard for those who primarily speak English or are managing a
collection, it's not great for those looking to operate in their own language, or for
people who are multilingual.

The following examples show how to correct for common local naming scenarios.

## Single language names

These names fall into one of the following categories:

* Names that have have been romanized (given Latin characters to represent the original
  characters) or reduced to 7-bit ASCII in a DAT file, but have a proper local name.

* Names that copy the American or European name for the sake of easily bundling together
  clones, but don't actually feature that English name on the title screen or box.

For example, `Shining Force II - Inishie no Fuuin` is the romanized version of the proper
Japanese name, `シャイニング●フォースII 『古の封印』`. The title doesn't support English, and
when someone chooses local names for Japanese titles in Retool, the name should be
replaced with the Japanese version.

Here's how to add this information to a clone list:

```json hl_lines="7-9"
"variants": [
  {
    "group": "Shining Force II - Inishie no Fuuin",
    "titles": [
      {
        "searchTerm": "Shining Force II - Inishie no Fuuin",
        "localNames": [
          {"japanese": "シャイニング●フォースII 『古の封印』"}
        ]
      }
    ]
  }
]
```

If a user adds Japanese to their local names list in Retool and then processes the DAT
file related to this clone list, the following process occurs:

1.  Retool looks up the short name `Shining Force II - Inishie no Fuuin` in the input DAT
    file, and finds that the full name `Shining Force II - Inishie no Fuuin (Japan)`
    matches.

1.  Because the user has indicated that they want Japanese local names, if a
    `localNames` object is present within a `searchTerm`, Retool checks for a
    `japanese` key. If found, it uses the key's value for the title's new full name:
    `シャイニング●フォースII 『古の封印』`.

    Retool doesn't check if the title actually supports Japanese &mdash; because No-Intro
    and Redump language data can be incomplete, this is up to the clone list maintainer
    to determine.

1.  All tags are copied from the original title to the new full name. In this case,
    `(Japan)` is appended to `シャイニング●フォースII 『古の封印』`.

1.  `シャイニング●フォースII 『古の封印』 (Japan)` is used instead of
    `Shining Force II - Inishie no Fuuin (Japan)` in the output DAT file.

All languages supported in Retool are also supported in the `localNames` object. Use
the lowercase representation of the language as shown in `config/internal-config.json` or
RetoolGUI. For example, `Chinese (Simplified)` becomes `chinese (simplified)` in a clone
list.

!!! warning
    Romanized or translated English names by definition don't have native English titles,
    so don't include `english` in their `localNames` object.
    See [multi-language names](#multi-language-names) for situations where you can use the
    `english` key.

## Multi-language names

When a title displays a different name depending on the hardware or software configuration
it's loaded on, then it's a multi-region name.

For example, _Streets of Rage_ shows exactly that name on the title screen if loaded in a
US Sega Genesis. But load the exact same cartridge in a Japanese Mega Drive, and you'll see
the English _Bare Knuckle_ on the title screen. The Japanese box has both _Bare Knuckle_
on it in English, _and_ the katakana and kanji combination
`ベアナックル 怒りの鉄拳` &mdash; roughly translated, `Bare Knuckle: Fists of Fury`. Still, a
Japanese person is far more likely to think of the series as `ベアナックル` than
`Bare Knuckle` or `Streets of Rage`.

You're also likely to see multi-region names for European titles, which can include many
languages.

Here's how to add this information to a clone list:

```json hl_lines="7-10"
"variants": [
  {
    "group": "Streets of Rage",
    "titles": [
      {
        "searchTerm": "Streets of Rage",
        "localNames": [
          {"english": "Streets of Rage"},
          {"japanese": "ベアナックル 怒りの鉄拳"}
        ]
      }
    ]
  }
]
```

Depending on what languages a user adds to their localization list, a different name is
written to the output DAT file:

* If a user adds no languages to the localization list, the default name,
  `Streets of Rage (Japan, USA)`, is used.

* If a user adds only Japanese to the localization list,
 `ベアナックル 怒りの鉄拳 (Japan, USA)` is used.

* If a user adds Japanese and English to the localization list, but ranks Japanese above
  English, then `ベアナックル 怒りの鉄拳 (Japan, USA)` is used. If they rank English above
  Japanese, then `Streets of Rage (Japan, USA)` is used.

!!! Tip
    You might have figured out that you can use local names to rename a title to
    whatever you want. As a general rule, official Retool clone lists won't change English
    names as recorded by No-Intro or Redump. If you need to correct a name,
    [report the issue upstream](contribute-metadata-files.md).

## Automated local names

In many circumstances, No-Intro and Redump have listed local names in their databases.
This information is stored in files found in the `metadata` folder. If there's no
corresponding clone list entry for a title, Retool uses the `localName` value in the
relevant `metadata` file for a title's local name.

## Standards

The following standards should be adhered to when adding local titles to a clone list.

### Use filters for multi-region titles

While there might only be one _Example Title (USA, Japan)_ in a DAT file at the time you
make a clone list, at some point in time an _Example Title (Europe)_ or
_Example Title (Japan)_ might be added. To avoid a title getting the wrong local name,
it's good practice to set a [filter](contribute-clone-lists-variants-filters.md)
on a `searchTerm`, and set the `localNames` inside the filter so only the correct
title is renamed.

It's likely good enough to use a `matchRegions` condition in most circumstances:

```json
{
  "group": "Raiden Trad",
  "titles": [
    {
      "searchTerm": "Raiden Trad",
      "filters": [
        {
          "conditions": {
            "matchRegions": ["Japan", "USA"]
          },
          "results": {
            "localNames": {
              "english": "Raiden Trad",
              "japanese": "雷電伝説"
            }
          }
        }
      ]
    }
  ]
}
```

### Japanese titles

* Many Japanese titles show English names on their title screens and boxes, but are
  referred to online using katakana/hiragana/kanji. Follow the Redump standard and use
  Japanese kana wherever possible. When in doubt, search through Japanese sites that
  sell classic titles or Japanese Wikipedia to check what title is used.

* Use zenkaku (full width) characters, not hankaku (half width). This includes
  kana, punctuation, arabic numerals, and latin characters.

### Chinese titles

Many entries in the Redump and No-Intro databases don't specify which written Chinese
variant is being used: traditional (language code: `Zh-Hant`) or simplified (`Zh-Hans`).
A lot of the time they just list the unspecified Chinese language code, `Zh`. Both
databases also don't make a distinction between spoken languages (Mandarin or Cantonese in
this case), written languages, or the availability of subtitles or dubs in a title.

For Retool, thankfully we're only dealing with the local written name for a title, and
so can stick with one of the following languages in the `localNames` object:

* `chinese (simplified)`

* `chinese (traditional)`

For non-Chinese speakers trying to find out which language is used, you can make an
educated guess. The following table serves as a cheat sheet for the Chinese variants that
regions around the world mostly use.

| Region                             | Written language    | Spoken language |
|------------------------------------|---------------------|-----------------|
| Most of mainland China             | Simplified          | Mandarin        |
| Guangdong province, mainland China | Simplified          | Cantonese       |
| Hong Kong                          | Traditional         | Cantonese       |
| Macao                              | Traditional         | Cantonese       |
| Malaysia                           | Simplified          | Mandarin        |
| Singapore                          | Simplified          | Mandarin        |
| Taiwan                             | Traditional         | Mandarin        |

For extra confirmation of the written language being used, try putting a Chinese
title name into Google Translate, and see what language the auto-detect suggests.
