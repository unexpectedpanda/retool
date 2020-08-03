# Retool

Retool is a command line tool that creates 1G1R versions of
[Redump](http://redump.org/) and
[No-Intro](https://www.no-intro.org/) dats.

## Installation

Clone Retool from this repo and run it with
[Python](https://www.python.org/). Retool requires a minimum of Python 3.8,
and needs three additional modules.

To install the modules, assuming you already have Python installed, open
Terminal, Command Prompt, or whatever the CLI is on your system, and type:

```shell
pip install bs4
pip install lxml
pip install strictyaml
```

## Usage

Retool is a command line tool. If you have Python, you use it with the
following syntax:

```shell
python retool.py -i <input dat/folder> <options>
```

Alternatively, your system might be configured to run the py file directly:

```shell
retool.py -i <input dat/folder> <options>
```

A new dat file is automatically generated, the original file isn't altered.

Edit the `user-config.yaml` file to set region order and filter languages.
Remove languages or regions by adding a `#` to the beginning of the relevant
line to comment it out.

### The user-config.yaml file

The `user-config.yaml` file determines the region order that Retool processes
dat files in, from most to least important. In the `region order` section of
the file, you can change the order, or comment out regions by adding a `#` to
the beginning of the line they're on so they're not included.

The file also contains a `language filter` section. When you set the `-l`
option in Retool, this section is referenced and Retool will only include
titles that contain the languages listed there. The order doesn't matter here,
just the content. Comment out languages you don't want to include by adding a
`#` to the beginning of the line. You can't process a dat file only by
languages -- you must also set a region order.

Titles with a region of "Unknown" will be included no matter which language you
filter by. If titles in the following regions don't have languages specified,
they will be included if you select any of their respective languages:

- **Asia** &mdash; English, Chinese, Japanese
- **Hong Kong, Taiwan** &mdash; Chinese, English
- **Latin America** &mdash; Spanish, Portuguese
- **South Africa** &mdash; Afrikaans, English
- **Switzerland** &mdash; German, French, Italian
- **Ukraine** &mdash; Ukranian, Russian

### Options

* `-o <output folder>` Set an output folder
* `-x` Export dat in legacy parent/clone format
  (for use with Clonerel, [not dat managers](/unexpectedpanda/retool/wiki/Usage-and-options#export-in-legacy-parentclone-dat-form))
* `-v` Verbose mode: report clone list errors
* `-l` Filter languages using a list (see `user-config.yaml`)
* `-g` Enable most filters (-a -b -c -d -e -f -m -r -s)
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
and how it works on the [wiki](https://github.com/unexpectedpanda/retool/wiki/).

### Clone lists

While Retool is smart enough to automatically match certain types of parents and
clones, there are certain situations that require manual assignment. To achieve
this, Retool keeps
[clone lists](https://github.com/unexpectedpanda/retool/wiki/Clone-lists).

Clone lists are updated independently of the program, and are formatted as JSON
files. They are stored in a subfolder called `clonelists`, which is in the same
folder as Retool.

<hr>

# Clonerel

Clonerel generates an Excel file from a parent/clone dat file that has been
created by Retool using the `-x` option. It helps you to more easily
visualize parent/clone relationships, and track down titles that haven't
been assigned parents yet.

## Installation

Clonerel uses openpyxl to generate an Excel file. You'll need at least OpenPyxl
v3.03 to avoid a fun crash bug. Install it with `pip`.

```shell
pip install openpyxl
```

If you haven't already installed them for Retool, you'll need also lxml and
bs4.

```shell
pip install bs4
pip install lxml
```

## Usage

```shell
python clonerel.py <input dat>
```