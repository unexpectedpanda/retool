# Retool
Retool creates 1G1R versions of [Redump](http://redump.org/) dats, deduping
them by marking titles as parents or clones. This is not an official Redump
project. You will need a 1G1R capable dat manager to use the files it
outputs, like [CLRMamePro](https://mamedev.emulab.it/clrmamepro/) or
[Romcenter](https://www.romcenter.com/).

## Installation
The preferred method of using Retool is through Python. If you don't know
Python or don't want to deal with code, download the appropriate ZIP file in
the [dist](https://github.com/unexpectedpanda/retool/tree/master/dist) folder
for Windows or MacOS. Extract and run the executable files directly, no
installation is required. Only 64-bit executables are supported.

Otherwise, Retool requires a minimum of
[Python 3.5](https://www.python.org/). Clone this repo and run `retool.py` to
get started.

You'll need to install two modules before using Retool. To do so, open
Terminal, Command Prompt, or whatever the CLI is on your system, and type:

```
pip install bs4
pip install lxml
```

## Usage
`python retool.py -i <input dat/folder> <options>`

Or for the binary version:

`retool  -i <input dat/folder> <options>`

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

You can learn more about Retool's options and how it works on the
[wiki](https://github.com/unexpectedpanda/retool/wiki/Usage-and-options).

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