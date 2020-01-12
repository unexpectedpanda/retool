# Retool
Retool creates 1G1R versions of [Redump](http://redump.org/) dats, effectively
deduping them by marking titles as parents or clones. This is not an official
Redump project.

* [Installation](#Installation)
* [Usage](#Usage)
  * [Options](#Options)
* [How it works](#How-it-works)
* [Working with _renames.py](#Working-with-_renames.py)
* [FAQs](#FAQs)

## Installation
If you don't know Python or don't want to deal with code, download the
appropriate ZIP file in the `dist` folder for Windows or MacOS. Only 64-bit
executables are available, 32-bit operating systems are not supported. Extract
and run the executable files directly, no installation is required.

Otherwise, _Retool_ requires a minimum of [Python 3.5](https://www.python.org/)
with `pip`.

You'll need to install two modules with `pip` before using _Retool_. To do so,
open Terminal, Command Prompt, or whatever the CLI is on your system, and type:

```
pip install bs4
pip install lxml
```
### Troubleshooting pip
* Some systems have multiple versions of Python installed. You might need to
run `pip3` instead of `pip`.
* Python will complain that the `bs4` module doesn't exist if `pip`
is installing modules to the wrong folder for Python 3.x access. If using
`pip3` instead of `pip` doesn't fix the issue, do a web search to solve the
problem on your OS of choice.

## Usage
`python retool.py -i <input dat/folder> <options>`

Or for the binary version:

`retool  -i <input dat/folder> <options>`

**Note:** Some systems have the Python 3.x binary installed separately as
`python3`. You might need to run this instead of `python`.

### Options
* `-o` Set an output folder
* `-a` Remove applications
* `-c` Remove compilations that don't have unique titles
* `-d` Remove demos and coverdiscs
* `-e` Remove educational titles
* `-l` Remove titles with (Alt) tags
* `-m` Remove multimedia titles
* `-p` Remove betas and prototypes
* `-s` Promote supersets: make things like game of the year editions parents
  of regular editions

#### Extra information on options
There are nuances within each of the options you should be aware of before
using them.

* **Demos** &mdash; Not only does this remove any title with a category of
  _Demos_ or _Coverdiscs_, it will remove titles with _(Demo)_, _(Sample)_
  or _(Taikenban)_ in the title, as sometimes Redump doesn't add demos to
  the _Demos_ category, or will add them to another category that takes
  priority like _Bonus Discs_.
* **Compilations** &mdash; Compilations are discs that include multiple titles
  that aren't part of the same game series. For example,
  _Project-X & Ultimate Body Blows_. Importantly, they are not _collections_.
  Collections tend to include the latest versions of a series of games, for
  example, _Assassin's Creed - Ezio Trilogy_ includes _Assassin's Creed II_,
  _Assassin's Creed - Brotherhood_, and _Assassin's Creed - Revelations_. If
  you set `-c`, compilations will be removed, but collections will stay.
* **Supersets** &mdash; Supersets include Game of the Year Editions, Special
  Editions, expansions and refinements like _Ninja Gaiden Black_, and
  collections (see the above dot point to understand the difference between
  compilations and collections). The exception to supersets are fighting games:
  there's so much rebalancing between fighting game editions, and such strong
  preferences for different versions, it's worth keeping them all.

## How it works
There are multiple stages for determining which title is a parent, and which is
a clone.

### By region
The input dat is split into regions, then each region is processed in a
specific order. If a region has a title of the same name in one of the regions
that precedes it, it is marked as a clone. The USA version of a title is usually
considered canonical.

Regions are parsed in the following order:

1. USA
1. World
1. UK
1. Canada
1. Australia
1. New Zealand
1. Singapore
1. Ireland
1. Europe
1. Asia
1. Scandinavia
1. Japan
1. Argentina
1. Austria
1. Belgium
1. Brazil
1. China
1. Croatia
1. Czech
1. Denmark
1. Finland
1. France
1. Germany
1. Greece
1. Hungary
1. India
1. Israel
1. Italy
1. Korea
1. Latin America
1. Netherlands
1. Norway
1. Poland
1. Portugal
1. Russia
1. Slovakia
1. South Africa
1. Spain
1. Sweden
1. Switzerland
1. Taiwan
1. Thailand
1. Turkey
1. Ukraine
1. United Arab Emirates
1. Unknown

As the program progresses through the regions,
[`_renames.py`](#Working-with-_renames.py) is referenced to check if any titles
in the current region are the same as another region's title, but with a
different name. For example, apart from the name,
_Dancing Stage Unleashed 3 (Europe)_ and
_Dance Dance Revolution Ultramix 3 (USA)_ are the same title, and so
only _Dance Dance Revolution Ultramix 3 (USA)_ would be kept.

Titles are also deduped if they span multiple regions, preferencing titles with
more regions. For example, out of _Grim Fandango (USA)_ and
_Grim Fandango (USA, Europe)_, the latter will be kept.

If `-c` is set, then `_compilations.py` is referenced for the compilation
title names to remove. If `-s` is set, then `_supersets.py` is referenced so
original titles can be matched with their superset titles.

### By language
Titles with the same name from the same region, but with different language
sets are also handled. The rules are complex:
- If one title is in English, but the other isn't, keep the English version.
- If one title from Europe has no languages listed, and the other has
  languages listed but English isn't one of them, keep the title with no
  languages listed (on the assumption that English is likely in there).
- If English is listed for both titles, and one title has more languages,
  take the title with more languages.
- If English is listed for both titles, and both titles have the same number
  of languages, check for preferred languages one by one, in the order listed
  below. The first title that doesn't support a preferred language is removed.
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

## Working with _renames.py
You only need to care about this if you're going to add your own clone titles
for Retool to assign to parents.

There is a specific format for matching clones with parents in the
`_renames.py` file:

```
'parent_rf_tag_strip_title': ['clone_rf_tag_strip_title_1', 'clone_rf_tag_strip_title_2']
```

The `parent_rf_tag_strip_title` on the left is the parent's "region free tag strip
title". From hereon in, we'll call it the "short name". It's the full Redump title,
stripped of the following tags:

* (Region)
* (Languages)
* (Version)
* (Revision)
* (Date)

For matching purposes, disc names are also normalised so everything is
`(Disc 1)`, `(Disc 2)`, `(Disc 3)` and so on, instead of `Disc A`, `Disco A`,
`Disco Uno` and other variants.

Using the parent short name, Retool goes through the titles list in region order
until it finds the first title that matches. This becomes a parent.

Short names are also used for clones, so one short name can pick up the same
alternate naming in many regions, and not require multiple
entries. For example, `FIFA 99` on the right side as a clone short name would
match both `FIFA 99 (Spain)`, and `FIFA 99 (Germany)`.

Let's take a look at a working example. To match the parent
``Oddworld - Abe's Exoddus (USA) (Disc 1)`` to its clones, the match code might
look like this:

```
'Oddworld - Abe\'s Exoddus (Disc 1)': [
            'Abe \'99 (Disc 1)',
            'Oddworld - L\'Exode d\'Abe (Disc 1)',
            ],
```

Using `Oddworld - Abe\'s Exoddus (Disc 1)` as the parent short name, Retool goes
through the titles in the relevant Redump dat in region order. It finds
`Oddworld - Abe's Exoddus (USA) (Disc 1)` as the first full title that matches
the shorter version, and assigns it as the parent.

Retool then goes through the title list in region order to find the longer
versions of the clone short names, and finds `Abe '99 (Japan) (Disc 1)` and
`Oddworld - L'Exode d'Abe (France) (Disc 1)`, assigning them both as clones to
`Oddworld - Abe's Exoddus (USA) (Disc 1)`.

You only need to list titles that are named differently to the parent. Titles
that are identical to the parent in other regions automatically get assigned as
clones -- that is the following titles get assigned as clones without you
having to do anything:

* `Oddworld - Abe's Exoddus (Europe) (Disc 1)`
* `Oddworld - Abe's Exoddus (Spain) (Disc 1)`
* `Oddworld - Abe's Exoddus (Germany) (Disc 1)`
* `Oddworld - Abe's Exoddus (Italy) (Disc 1)`
* `Oddworld - Abe's Exoddus (USA) (Disc 1)`

### Excluding unintended title matches: the _King's Field_ problem
While using short names has its benefits, it also has shortcomings.

For example, take the _King's Field_ problem. The first _King's Field_ was only
released in Japan. The second was named _King's Field II_ in Japan, but
_King's Field_ in Western countries, while the Japanese _King's Field III_
was called _King's Field II_ overseas. This means the parent/clone
relationship according to Retool's region ordering should be this:


PARENT                 | CLONES
-----------------------|----------------------------
King's Field (Japan)   | -
King's Field (USA)     | King's Field II (Japan)
King's Field II (USA)  | King's Field III (Japan)

Because of the sequel desync, however, What gets matched is completely
different.

PARENT                   | CLONES
-------------------------|----------------------------
King's Field (USA)       | King's Field (Japan)
King's Field II (USA)    | King's Field II (Japan)
King's Field III (Japan) |

Fixing this is a two step process.

#### Step one: excluding unintended matches for clone short names
First, let's look at `King's Field (USA)`. We want
`King's Field II (Japan)` to be assigned to it as a clone, but not
`King's Field II (USA)`. Here's how you do it.

```
'King\'s Field': [
    ['King\'s Field II', 'King\'s Field II (USA)'],
    'King\s Field II (PlayStation the Best)'
    ],
```

You'll notice the first clone short name is in a list, instead of being just a
string. This indicates that there are full titles _not_ to match the short name
against. In this example, we've told Retool not to match `King\'s Field II`
against `King's Field II (USA)`, but it will still happily match with the
needed `King's Field II (Japan)`. You can add as many excluded titles as you
like &mdash; anything after the [0] position is considered an exclusion title.

#### Step two: excluding unintended matches for parent short names
Now we need to rescue `King's Field (Japan)`, so it's not marked as a clone of
`King's Field (USA)`. It's as simple as adding another entry to the list, but
this time with the same short name as the parent.

```
'King\'s Field': [
    ['King's Field', 'King\'s Field (Japan)'],
    ['King\'s Field II', 'King\'s Field II (USA)'],
    'King\s Field II (PlayStation the Best)'
    ],
```

This removes `King's Field (Japan)` from the clone processing altogether, and
adds it back in as a parent after the processing has finished.

At this stage,  if you want to take multiple titles out of clone processing that
have the same short name as the parent, you'll need to make multiple entries, as
per the example below:

```
'Motor Toon Grand Prix': [
    ['Motor Toon Grand Prix', 'Motor Toon Grand Prix (Japan)'],
    ['Motor Toon Grand Prix', 'Motor Toon Grand Prix (Japan) (Rev 1)'],
    'Motor Toon Grand Prix 2',
    'Motor Toon Grand Prix 2 (Disc 1)', # (モータートゥーン・グランプリ2)
    'Motor Toon Grand Prix 2 (Disc 2) (Taisen Sen\'you Disc)', # (As far as I can find out, a second disc in the Japanese version you'd give to friends so you could play multiplayer)
    'Motor Toon Grand Prix - USA Edition', # (モータートゥーン・グランプリ USAエディション)
    ],
```

## FAQs
#### How did you figure out what the dupes were?
I went through each dat's titles. I then used
[Wikipedia](https://www.wikipedia.org),
[Moby Games](https://www.mobygames.com),
[Retroplace](https://www.retroplace.com), [GameTDB](https://www.gametdb.com),
[VDGB](https://vgdb.io), [VGM](https://www.video-games-museum.com),
[YouTube](https://www.youtube.com), [Amazon.jp](https://www.amazon.co.jp),
[PlayAsia](https://www.play-asia.com/), and good old web searching to turn up
information. Occasionally I went through Redump's site for Japanese and Chinese
characters for the titles, so I could do translations and find out the
equivalent English titles. Later in the process I discovered
[FilterQuest](https://github.com/UnluckyForSome/FilterQuest), a similar tool,
and added some missing titles from there.

#### Does this create perfect 1G1R Redump dat?
Unlikely. There are bound to be false positives as a result of bad assumptions,
and titles I've missed. But it'll get you a lot closer than the default Redump
set.

#### Shouldn't you preference less regions in multi-region titles, or less languages in multi-language titles?
I'm following a philosophy that the superset should be the primary title.
Anything with less content is by definition secondary. At this stage,
compilations aren't considered.

## Known limitations
Be aware of the following limitations when using _Retool_. These might or
might not be addressed in the future.

#### Titles marked with (Rerelease) tags are always clones
At this stage it's unclear which of these are the newest version:

* Title
* Title (v1.1)
* Title (Rerelease)

Is the rerelease of version 1.1? Is it of the original? Is it a newer version
than both? Does it have extra content? Redump doesn't make this clear as it
doesn't version all titles. Sometimes, titles that were originally released
on multiple CDs were later released on DVD, which can only be determined by
ISO size.

As such, rereleases are currently marked as clones.

# Clonerel
A small tool to help more easily visualize parent/clone relationships, to track
down titles that haven't been assigned parents yet. Exports an Excel file.


## Installation
Clonerel uses openpyxl to generate an Excel file. Install it with `pip`.

```
pip install openpyxl
```

If you haven't already installed them for Retool, you'll need lxml and bs4 as well.

```
pip install bs4
pip install lxml
```

## Usage
```
python clonerel.py <input dat>
```