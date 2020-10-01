# Retool
* [What it does](#what-it-does)
* [Why not use CLRMAMEPro or Romcenter's 1G1R mode with a parent/clone dat?](#why-not-use-clrmamepro-or-romcenters-1g1r-mode-with-a-parentclone-dat)
* [Clone lists](#clone-lists)
* [Installation](#installation)
  * [For those familiar with Git and Python](#for-those-familiar-with-git-and-python)
  * [For Windows users only familiar with graphical interfaces](#for-windows-users-only-familiar-with-graphical-interfaces)
* [Using Retool from the command line](#using-retool-from-the-command-line)
* [Clonerel](#clonerel)


## What it does

Retool converts [Redump](http://redump.org/) and
[No-Intro](https://www.no-intro.org/) dats to 1G1R, doing a better job than
dat managers with parent/clone dats. It has both GUI and CLI versions.

You'll still need a dat manager to use the files Retool creates, such as
[CLRMamePro](https://mamedev.emulab.it/clrmamepro/),
[RomVault](https://www.romvault.com/), or
[Romcenter](https://www.romcenter.com/) &mdash; you just won't need to use
their 1G1R modes, as Retool will have already done the work for you.

![Retool GUI](https://github.com/unexpectedpanda/retool/wiki/images/retool-gui.png)

## Why not use CLRMAMEPro or Romcenter's 1G1R mode with a parent/clone dat?

Historically if you wanted to create a 1G1R set, you'd use a parent/clone dat in
combination with a dat manager like CLRMAMEPro or Romcenter. After loading the
dat into the dat manager, you'd set your desired regions and region order, and
whether or not to filter by languages (assuming the dat has `<release>` tags
properly set up &mdash; something which is vanishingly rare). You'd then trust
the dat manager to choose the perfect parent title for you from your favorite
region, discarding the clones from other regions.

Here's the thing. The parent/clone dat format was created for
[MAME](https://www.mamedev.org), to enable one of the ways in which it organizes
its ROMs. A "parent" ROM in MAME contains the base or common files for a game,
while "clone" ROMs only contain files that are different from the parent. If you
load a clone game in MAME, it's smart enough to load the base files from the
parent, and any of the modified files it needs from the clone.

Standard 1G1R through a dat manager is effectively a hack on top of this system.
In 1G1R mode a dat manager takes the parent and ignores the clones, in an effort
to only include the "best" or most desired version of a title. While on the
surface this seems reasonable, if you look a little closer you start to see the
cracks.

The primary issue is that dat managers and parent/clone dats don't have a
concept of title priority. For example, what happens when there are two copies
of the same title from the same region, but they have different names? Or
different version numbers? Or were published by different companies at different
times? Which title does the dat manager choose then?

Retool figures this out for you. It even identifies the languages of each title
by using multiple sources &mdash; the implied language spoken in the region the
title is from, languages explicitly listed in the title's filename, and
languages listed on Redump's website, which aren't always included in filenames.

After you set up the GUI or `user-config.yaml` to your liking, Retool's output
is already 1G1R, meaning you don't need to select 1G1R mode, regions, or
languages in your dat manager &mdash; just load the dat and go.


## Clone lists

While Retool is smart enough to automatically match certain types of parents and
clones, there are certain situations that require manual assignment, like when
a title has a different name in different regions. To achieve this, Retool keeps
[clone lists](https://github.com/unexpectedpanda/retool/wiki/Clone-lists).

At the time of writing, Retool's clone lists are the most thorough that I know
of. I manually combed through titles in most dats, and cross referenced them on
[Wikipedia](https://www.wikipedia.org),
[Moby Games](https://www.mobygames.com),
[Retroplace](https://www.retroplace.com), [GameTDB](https://www.gametdb.com),
[VDGB](https://vgdb.io), [VGM](https://www.video-games-museum.com),
[YouTube](https://www.youtube.com), [Amazon.jp](https://www.amazon.co.jp),
[PlayAsia](https://www.play-asia.com/),
[Sega Retro](https://segaretro.org/), [PSCX2 Wiki](https://wiki.pcsx2.net),
[PlayStation DataCenter](https://psxdatacenter.com/),
[The Cutting Room Floor](https://tcrf.net),
and [Atari Mania](http://www.atarimania.com). I checked out the parent/clone
dats for No-Intro, and occasionally I went through Redump's site for Japanese,
Korean, Russian, and Chinese characters for titles, so I could do
translations and find out what they were called in other languages. When all
else failed, I did some good old web searching in order to turn up information.
 At some point I discovered
[FilterQuest](https://github.com/UnluckyForSome/FilterQuest), a similar tool,
and added some missing titles from there.

Clone lists are updated independently of the program, and are formatted as JSON
files. They are stored in a subfolder called `clonelists`, which is in the same
folder as Retool.

You can update them from the GUI using the **File** menu, by running
`updateclonelists.py`, or by downloading them yourself from this repository.


## Installation

### For those familiar with Git and Python
Clone Retool from this repo and run it with
[Python](https://www.python.org/). Retool requires a minimum of Python 3.8,
and needs additional modules to be installed.

To install the modules, assuming you already have Python installed, open
Terminal, Command Prompt, or whatever the CLI is on your system, and type:

```shell
pip install bs4 lxml strictyaml pysimpleguiqt
```

#### I'm seeing a libxcb error in Linux when using retool-gui.py

Looks like some installs are a bit wonky when it comes to libxcb. This worked
for me on a fresh install of Ubuntu 20.04:

```
sudo apt-get install libxcb-randr0-dev libxcb-xtest0-dev libxcb-xinerama0-dev libxcb-shape0-dev libxcb-xkb-dev
```

### For Windows users only familiar with graphical interfaces
Fear not, you can get going in a few steps:

1. Make sure you're connected to the internet for the entire procedure.
1. Download [Python](https://www.python.org/downloads/) and run the installer.
1. On the first screen, select **Add Python [version] to PATH**, then click **INSTALL NOW**.
1. After the installation completes,
   [download the most recent release of Retool as a ZIP file](https://github.com/unexpectedpanda/retool/archive/master.zip),
   then extract it to a folder of your choice.
1. In that folder, double click `install-dependencies.bat`.
1. When the command line window disappears, double click `retool-gui.py` to
   run Retool.

From this point onwards, you'll only need to double click `retool-gui.py` to run the
program.

When opportunity presents, take some time to learn the command line &mdash; it can
do some pretty cool things.


## Using Retool from the command line

For those who like a bit more power and are comfortable in the command line,
Retool offers a CLI version.

### Usage

Retool uses the following syntax:

```shell
python retool.py <input dat/folder> <options>
```

Alternatively, your system might be configured to run the py file directly:

```shell
retool.py <input dat/folder> <options>
```

A new dat file is automatically generated, the original file isn't altered.

Edit the `user-config.yaml` file to set region order and filter languages.
Remove languages or regions by adding a `#` to the beginning of the relevant
line to comment it out.

#### The user-config.yaml file

The `user-config.yaml` file determines the region order that Retool processes
dat files in, from most to least important. In the `region order` section of
the file, you can change the order, or comment out regions by adding a `#` to
the beginning of the line they're on so they're not included.

The file also contains a `language filter` section. When you set the `-l`
option in Retool, this section is referenced and Retool will only include
titles that contain the languages listed there. The order doesn't matter here,
just the content. Comment out languages you don't want to include by adding a
`#` to the beginning of the line. You can't process a dat file only by
languages &mdash; you must also set a region order.

Titles with a region of "Unknown" will be included no matter which language you
filter by. If titles in the following regions don't have languages specified,
they will be included if you select any of their respective languages:

- **Asia** &mdash; English, Chinese, Japanese
- **Hong Kong, Taiwan** &mdash; Chinese, English
- **Latin America** &mdash; Spanish, Portuguese
- **South Africa** &mdash; Afrikaans, English
- **Switzerland** &mdash; German, French, Italian
- **Ukraine** &mdash; Ukranian, Russian

#### Options

* `-o <output folder>` Set an output folder
* `--log` Also export a list of what titles have been kept and removed in the
  output dat/s
* `--errors` Verbose mode: report clone list errors
* `-x` Export dat in legacy parent/clone format
* `-g` Enable most filters (-bcdefmrs)
* `-l` Filter by languages using a list (see `user-config.yaml`)
* `-s` Enable supersets: special editions, game of the year
  editions, and collections replace standard editions
* `-a` Exclude applications
* `-b` Exclude bad dumps
* `-c` Exclude compilations with no unique titles
* `-d` Exclude demos and samples
* `-e` Exclude educational titles
* `-f` Exclude coverdiscs
* `-m` Exclude multimedia titles
* `-n` Exclude pirate titles
* `-p` Exclude preproduction titles (alphas, betas, prototypes)
* `-r` Exclude promotional titles
* `-u` Exclude unlicensed titles

You can learn more about
[Retool's options](https://github.com/unexpectedpanda/retool/wiki/Usage-and-options#More-options-information)
and how it works in the [wiki](https://github.com/unexpectedpanda/retool/wiki/).

<hr>

# Clonerel

Clonerel is a CLI program that generates an Excel file from any parent/clone
dat file. It helps you more easily visualize parent/clone relationships
in the dat, and track down titles that haven't been assigned parents yet.

You can create a parent/clone dat file in Retool by using the `-x` option, or
by selecting **Export dat in legacy parent/clone format** in the GUI.


## Installation

Clonerel uses openpyxl to generate an Excel file. You'll need at least OpenPyxl
v3.03 to avoid a fun crash bug. Install it and other dependencies with `pip`.

```shell
pip install openpyxl bs4 lxml
```

## Usage

```shell
python clonerel.py <input dat>
```