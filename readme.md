# Retool

Retool is a command line tool that creates 1G1R versions of
[Redump](http://redump.org/) dats, deduping them by marking titles as parents
or clones. This is not an official Redump project.

You will need a 1G1R capable dat manager to use the files it
outputs, such as [CLRMamePro](https://mamedev.emulab.it/clrmamepro/) or
[Romcenter](https://www.romcenter.com/), and you'll need to learn how to
configure them correctly.

## Installation

There are two ways you can install and run Retool.

### Binaries

If Git and Python aren't your thing, you can download ZIP files containing
Windows and macOS binaries from the
[dist](https://github.com/unexpectedpanda/retool/tree/master/dist) folder. Make
sure to grab the clonelists + config ZIP file as well, and extract them both
into the same folder to install.

### Python

For more code-savvy users, you can clone Retool from this repo and run it with
[Python](https://www.python.org/), which will give you better performance.
Retool requires a minimum of Python 3.5, and needs two additional modules.

To install the modules, assuming you already have Python installed, open
Terminal, Command Prompt, or whatever the CLI is on your system, and type:

```
pip install bs4
pip install lxml
```

## Usage

Retool is a command line tool. If you have Python, you use it with the
following syntax:

```
python retool.py -i <input dat/folder> <options>
```

Or for the binary version:

```
retool  -i <input dat/folder> <options>
```

A new file is automatically generated, the original file isn't altered.

### Options

* `-o` Set an output folder
* `-g` All options (-abcdemps)
* `-a` Remove applications
* `-b` Remove coverdiscs
* `-c` Remove compilations that don't have unique titles
* `-d` Remove demos
* `-e` Remove educational titles
* `-m` Remove multimedia titles
* `-p` Remove betas and prototypes
* `-s` Promote supersets: make things like Game of the Year editions parents
  of regular editions

You can learn more about
[Retool's options](https://github.com/unexpectedpanda/retool/wiki/Usage-and-options#More-options-information)
and how it works on the [wiki](https://github.com/unexpectedpanda/retool/wiki/).

## Clone lists

While Retool is smart enough to automatically pair certain types of parents and
clones, there are certain situations that require manual assignment. This
requires clone lists to achieve.

Clone lists are updated independently of the program, and are formatted as JSON
files. You can either download them manually from the
[clonelists folder](https://github.com/unexpectedpanda/retool/tree/master/clonelists),
pull everything into your local repo, or download the clonelists + config ZIP file
from the
[dist](https://github.com/unexpectedpanda/retool/tree/master/dist) folder. The
JSON files must be uncompressed, and stored in a folder called `clonelists` in the
same folder as Retool for them to be recognized.

<hr>

# Clonerel

Clonerel is a tool that helps you more easily visualize parent/clone
relationships in dat files, by generating an Excel file. Useful to track down
titles that haven't been assigned parents yet.

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