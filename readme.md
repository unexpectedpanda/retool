# Retool
Retool dedupes [Redump](http://redump.org/) dats. This is not an official
Redump project.

## Installation
If you don't know Python or don't want to deal with code, download the
appropriate ZIP file in the `dist` folder for Windows or MacOS. Only 64-bit
executables are available, 32-bit operating systems are not supported. Extract
and run the executable files directly, no installation is required.

Otherwise, _Retool_ requires a minimum of [Python 3.5](https://www.python.org/)
with `pip`.

You'll need to install two modules with `pip` before using _Retool_. To do so,
open Terminal, Command Prompt, or whatever the CLI is on your system, and type:

```python
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

## Options
* `-en` Only include English titles
* `-a` Remove applications
* `-d` Remove demos and coverdiscs
* `-e` Remove educational
* `-l` Remove titles with (Alt) tags
* `-m` Remove multimedia
* `-o` Set an output folder
* `-p` Remove betas and prototypes
* `-r` Split dat into regional dats
* `-s` Split dat into regional dats, don't dedupe
* `-1` Generate a CLRMAMEPro 1G1R dat

## How it works
There are multiple stages for eliminating dupes.

### By region
The input dat is split into regions, then each region is processed in a
specific order. Each region cannot include titles that are in the regions
that precede it. The USA version of a title is usually considered canonical.

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

As the program progresses through the regions, `_renames.py` is
referenced to check if any titles in the current region are the same as
another region's title, but with a different name. For example, apart from the
name, **_Dancing Stage Unleashed 3 (Europe)_** and
**_Dance Dance Revolution Ultramix 3 (USA)_** are the same title, and so
only **_Dance Dance Revolution Ultramix 3 (USA)_** would be kept.

Titles are also deduped if they span multiple regions, preferencing titles with
more regions. For example, out of **_Grim Fandango (USA)_** and
**_Grim Fandango (USA, Europe)_**, the latter will be kept.

### By language
Titles with the same name from the same region, but with different language
sets are also handled. The rules are complex:
- If one title is in English, but the other isn't, keep the English version.
- If one title from Europe has no languages listed, and the other has
  languages listed but English isn't one of them, keep the title with no
  languages listed (on the assumption that English may be in there).
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

## FAQs
#### How did you figure out what the dupes were?
I went through each dat for titles that weren't tagged as USA. I then used
[Wikipedia](https://www.wikipedia.org),
[Moby Games](https://www.mobygames.com),
[Retroplace](https://www.retroplace.com), [GameTDB](https://www.gametdb.com),
[VDGB](https://vgdb.io), [VGM](https://www.video-games-museum.com),
[YouTube](https://www.youtube.com), [Amazon.jp](https://www.amazon.co.jp),
[PlayAsia](https://www.play-asia.com/), and good old web searching to turn up
information. I went through Redump's site for Japanese and Chinese characters
for the titles, so I could do translations and find out the equivalent English
titles. Later in the process I discovered
[FilterQuest](https://github.com/UnluckyForSome/FilterQuest), a similar tool,
and added some missing titles from there.

#### Does this create a dat for the perfect 1G1R Redump set?
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

#### Doesn't remove single titles in favor of compilation titles
For example, **_Assassin's Creed - Ezio Trilogy_** does not supersede
**_Assassin's Creed II_**, **_Assassin's Creed - Brotherhood_**, and
**_Assassin's Creed - Revelations_**. Both the original titles and the
compilation will be kept.

#### Can only follow Redump language tags
If Redump missed tagging titles from regions where English isn't the region's
first language (for example, Japan), those titles won't be included if you've
set the `-en` flag.

#### Will remove titles that have the same name in different regions, regardless of which version is better, or unique content
For example, some versions of singing titles have additional local tracks, but
because they share the same name, only one version of the title will be
kept. Likewise, if a title from Europe has more content than its equivalent
from the USA, but has the same name, the USA title will be kept.

#### Doesn't handle the (Rerelease) tag
At this stage it's unclear which of these are the newest version:

* Title
* Title (v1.1)
* Title (Rerelease)

Is the rerelease of 1.1? Is it of the original? Redump doesn't make this choice
easy as it doesn't version all titles. As such, rereleases are still included
and may be dupes. Sometimes, titles that were originally released on multiple
CDs were later released on DVD, which makes things harder to work with again.