# Retool
Retool creates 1G1R versions of [Redump](http://redump.org/) dats, effectively
deduping them by marking titles as parents or clones. This is not an official
Redump project.

* [Installation](#Installation)
* [Usage](#Usage)
  * [Options](#Options)
* [How it works](#How-it-works)
* [Working with _renames.py](#Working-with-_renamespy)
* [Working with _compilations.py](#Working-with-_compilationspy)
* [Working with _supersets.py](#Working-with-_supersetspy)
* [Working with _overrides.py](#Working-with-_overridespy)
* [FAQs](#FAQs)
* [Known limitations](#Known-limitations)
* [Clonerel](#Clonerel)

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
* `-s` Promote supersets: make things like Game of the Year editions parents
  of regular editions

#### More options information
There are nuances to each of the options you should be aware of before using
them.

##### Demos
Not only does the `-d` option remove any title with a category of _Demos_ or
_Coverdiscs_, it will remove titles that contain the following:

* _(@barai)_
* _(Demo)_
* _(Sample)_
* _(Taikenban)_
* _Trial Edition_

This is because Redump sometimes misses adding demos to the
_Demos_ category, or adds them to another category that takes priority like
_Bonus Discs_.

##### Compilations
Compilations are discs that include multiple titles that aren't part of the
same game series. For example, the title _Project-X & Ultimate Body Blows_.
Importantly, setting `-c` doesn't treat the following as compilations, and
so doesn't remove them:

* **Collections** &mdash; Collections are different from compilations, in that
  they tend to include the latest versions of a series of games. For example,
  _Assassin's Creed - Ezio Trilogy_ includes _Assassin's Creed II_,
  _Assassin's Creed - Brotherhood_, _Assassin's Creed - Revelations_, and some
  DLC. As a rule of thumb, at least three games should be in a collection. If
  a collection only contains the original release of its games, not the
  expanded editions (for example, _Assassin's Creed - Heritage Collection_
  doesn't include the _Assassin's Creed II - Game of the Year_ DLC), then it is
  demoted to a compilation.
* **Demos** &mdash; Demo compilations aren't removed with `-c`, but will be
  removed if you set `-d`.

Compilations are only removed if they contain no games that are unique in the
current Redump set.

##### Supersets
Supersets include Game of the Year Editions, Special Editions, expansions and
refinements of the original title (for example, _Ninja Gaiden Black_ compared
to _Ninja Gaiden_), 32X versions of Sega CD games, and collections of titles
(refer to [Compilations](#Compilations) to understand the difference between
compilations and collections). They don't include Collectors Editions that were
released simultaneously with the original title &mdash; these are set to
parents as default.

Setting the `-s` option makes the superset title the parent of the original
title. For example,
_Elder Scrolls III, The - Morrowind - Game of the Year Edition_ would become
the parent of _Elder Scrolls III, The - Morrowind_.

Because many supersets have more discs than the original title, setting
up a proper parent/clone relationship often involves assigning the original
title as a clone of disc one of the superset.

###### Superset exclusions

* Fighting games that have received rebalancing are excluded from supersets.
  There's such strong preferences for different versions, it's worth keeping
  them all. This means _Virtua Fighter Remix_ on Saturn is a superset, as it's
  just a bug fixed, visually enhanced version of _Virtua Fighter_.
  _Street Fighter II: Champion Edition_ on the other hand is not a superset of
  _Street Fighter II_, as in addition to the new playable characters, the
  gameplay has changed due to rebalancing.
* It's incredibly Anglo-centric, but if a superset of an English-speaking
  title doesn't exist in a Redump dat yet, the standard English title won't get
  demoted under, say, the German version of the superset title.

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

The `parent_rf_tag_strip_title` on the left is the parent's "region free tag
strip title". From hereon in, we'll call it the "short name". It's the full
Redump title, stripped of the following tags:

* (Region)
* (Languages)
* (Version)
* (Revision)
* (Date)

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

### Disc order
During the matching process, disc names are normalised. That is, everything
becomes `(Disc 1)`, `(Disc 2)`, `(Disc 3)` and so on, instead of variants such
as `(Disc A)`, `(Disco A)`, `(Disc 01)`, and `(Disco Uno)`. While this is great
to help match titles automatically, it does mean that when you're setting a
clone's short name in `_renames.py`, you will need to manually change
non-standard disc names in the title to the standard (for example, `(Disco 1)`
 to `(Disc 1)`) to get a match.

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
    'Motor Toon Grand Prix 2 (Disc 1)',
    'Motor Toon Grand Prix 2 (Disc 2) (Taisen Sen\'you Disc)',
    'Motor Toon Grand Prix - USA Edition',
    ],
```

## Working with _compilations.py
The purpose of `_compilations.py` is to list compilations that don't have
unique titles. When using the `-c` option, `_compilations.py` is referenced.

The compilations file is different from others, in that you use an entire
title's name, not the short name. You'll notice commented out tiles in there
as well &mdash; these are compilations that still have unique titles compared
to Redump's dat.

## Working with _supersets.py
When you use the `-s` option, `_supersets.py` is referenced. It follows a
similar structure to `_renames.py`.

There's a trap here &mdash; if you add a title as a superset, but the original
has alternative titles associated with it in `_renames.py`, you will also have
to list those alternative titles under the superset in `_supersets.py`.

## Working with _overrides.py
Sometimes all the logic in the world still fails. Whether this is because a
title is named oddly, or doesn't quite follow Redump's intended naming scheme,
the result is the same &mdash; you're going to have to force an override.

The structure is similar to `_renames.py`, except here you always use a title's
full name, not its short name.


## FAQs
#### How did you figure out what the clones were?
I went through each dat's titles to find obvious clones. I then used
[Wikipedia](https://www.wikipedia.org),
[Moby Games](https://www.mobygames.com),
[Retroplace](https://www.retroplace.com), [GameTDB](https://www.gametdb.com),
[VDGB](https://vgdb.io), [VGM](https://www.video-games-museum.com),
[YouTube](https://www.youtube.com), [Amazon.jp](https://www.amazon.co.jp),
[PlayAsia](https://www.play-asia.com/),
[Sega Retro](https://segaretro.org/), and good old web searching to turn up
information. Occasionally I went through Redump's site for Japanese, Korean
and Chinese characters for the titles, so I could do translations and find out
the equivalent English titles. At some point I discovered
[FilterQuest](https://github.com/UnluckyForSome/FilterQuest), a similar tool,
and added some missing titles from there.

#### Does this create perfect 1G1R Redump dat?
Unlikely. There are bound to be false positives as a result of bad assumptions,
and titles I've missed. But it'll get you a lot closer than the default Redump
set.

#### Shouldn't you preference less regions in multi-region titles, or less languages in multi-language titles?
I'm following a philosophy that the superset should be the primary title.
Anything with less content is by definition secondary. This is also why I
added the [superset](#Supersets) option.

#### What do the warnings about clones and parents not matching mean?
This will likely happen if the version of the Redump dat you're using doesn't
match the one that the clone lists were compiled from. A 1G1R dat file will
still be generated, it just means Redump renamed or removed something, and so a
parent/clone relationship was lost.

The older the `_*.py` files get, the less accurate the 1G1R dat becomes
when generated from the most recent Redump dats. You should be able to fix most
issues by updating the `_*.py` files.

In the ideal world, Redump takes this work as a basis for their own
parent/clone project and works the removal options into a Dat-O-Matic-style
interface, extincting this tool in the process.

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

#### Disc ring codes

It's unclear whether disc ring codes represent a different version of a game,
or just a different pressing. For the sake of order, I've assigned ring codes
with the highest name as the parent. For example, `SABS` is higher than `SAAS`,
`3S` is higher than `2S`. For grouped ring codes, `1S, 4S` is treated as higher
than `2S`.

This is done manually for now in `_renames.py`, rather than through an
automated process, as it seems ring codes can be anything.

# Clonerel
A small tool that helps you more easily visualize parent/clone relationships,
to track down titles that haven't been assigned parents yet. Exports an Excel
file.


## Installation
Clonerel uses openpyxl to generate an Excel file. Install it with `pip`.

```
pip install openpyxl
```

If you haven't already installed them for Retool, you'll need lxml and bs4 as
well.

```
pip install bs4
pip install lxml
```

## Usage
```
python clonerel.py <input dat>
```