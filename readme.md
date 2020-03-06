# Retool
Retool creates 1G1R versions of [Redump](http://redump.org/) dats, effectively
deduping them by marking titles as parents or clones. This is not an official
Redump project.

* [Installation](#Installation)
* [Usage](#Usage)
  * [Options](#Options)
* [Known limitations](#Known-limitations)
* [FAQs](#FAQs)
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
  collections tend to include the latest versions of a series of games. For
  example, _Assassin's Creed - Ezio Trilogy_ includes _Assassin's Creed II_,
  _Assassin's Creed - Brotherhood_, _Assassin's Creed - Revelations_, and some
  DLC. If a collection only contains the original release of its games, not the
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

## Known limitations
Be aware of the following limitations when using _Retool_. These might or
might not be addressed in the future.

### Titles marked with (Rerelease) tags are always clones

At this stage it's unclear which of these are the newest version:

* Title
* Title (v1.1)
* Title (Rerelease)

Is the rerelease of version 1.1? Is it of the original? Is it a newer version
than both? Does it have extra content? Redump doesn't make this clear as it
doesn't version all titles. Sometimes, titles that were originally released
on multiple CDs were later released on DVD, which can only be determined by
ISO size.

As such, rereleases are generally marked as clones.

### Disc ring codes

It's unclear whether disc ring codes represent a different version of a game,
or just a different pressing. For the sake of order, I've assigned ring codes
with the highest name as the parent. For example, `SABS` is higher than `SAAS`,
`3S` is higher than `2S`. For grouped ring codes, `1S, 4S` is treated as higher
than `2S`.

This is done manually for now in `_renames.py`, rather than through an
automated process, as it seems ring codes can be anything.

## FAQs
#### How did you figure out what the clones were?
I went through each dat's titles to find obvious clones. I then used
[Wikipedia](https://www.wikipedia.org),
[Moby Games](https://www.mobygames.com),
[Retroplace](https://www.retroplace.com), [GameTDB](https://www.gametdb.com),
[VDGB](https://vgdb.io), [VGM](https://www.video-games-museum.com),
[YouTube](https://www.youtube.com), [Amazon.jp](https://www.amazon.co.jp),
[PlayAsia](https://www.play-asia.com/),
[Sega Retro](https://segaretro.org/), the [PSCX2 Wiki](https://wiki.pcsx2.net)
and good old web searching to turn up information. Occasionally I went through
Redump's site for Japanese, Korean, and Chinese characters for the titles, so I
could do translations and find out the equivalent English titles. At some point
I discovered [FilterQuest](https://github.com/UnluckyForSome/FilterQuest), a
similar tool, and added some missing titles from there.

#### Does this create perfect 1G1R Redump dat?
Unlikely. There are bound to be false positives as a result of bad assumptions,
and titles I've missed. There will also be scenarios where the USA title has
been selected, but the version from another region is superior.

But look, it'll get you a lot closer than the default Redump set.

#### Shouldn't you preference less regions in multi-region titles, or less languages in multi-language titles?
I'm following a philosophy that the superset should be the primary title.
Anything with less content is by definition secondary. This is also why I
added the [superset](#Supersets) option.

#### What do the warnings about clones and parents not not being found mean?
There are two reasons these warnings could appear. The first is that you've
used one of the options, like `-d` to remove demos, and as a result that
title is no longer found in the dat.

The second is if the version of the Redump dat you're using doesn't match the
one that the clone lists were compiled from. A 1G1R dat file will still be
generated, it just means Redump renamed or removed something, and so a
parent/clone relationship was lost.

The older the `_*.py` files get, the less accurate the 1G1R dat becomes
when generated from the most recent Redump dats. You should be able to fix most
issues by updating the `_*.py` files.

In the ideal world, Redump would take this work as a basis for their own
parent/clone project and work the removal options into a Dat-O-Matic-style
interface, extincting this tool in the process.

<hr>

# Clonerel
A small tool that exports an Excel file to help you more easily visualize
parent/clone relationships. Useful to track down titles that haven't been
assigned parents yet.

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