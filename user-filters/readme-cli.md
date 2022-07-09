# Retool CLI: Override which titles are included/excluded with custom filters

**This readme is for the CLI version of Retool. For the GUI version, open**
**`readme-gui.md`**.

---

The contents of the files in the `user-filters` folder determine whether titles
in a dat are to be manually included or excluded. They give the user the power
to add their own inclusions/exclusions if they have needs beyond what Retool is
producing.

This is a power user feature that requires an understanding of YAML.

> If Retool has genuinely missed a relationship between titles, please don't
> just create a filter &mdash;
> [create an issue](https://github.com/unexpectedpanda/retool/issues) too so the
> clone lists or Retool can be updated.


## Global versus system filters

There are two different types of custom filters: global and system.

* Global filters apply to all dats you process in Retool.
* System filters only apply when you load a dat that matches that system (for
  example, PC Engine). Retool figures out the name of the system from the
  `<name>` tag in the dat. You need to load a dat in Retool GUI before you
  can edit its system filters.

The following rules apply when using global and system filters together:

* System includes override all excludes.
* System excludes override global includes.
* Global includes override global excludes.

Global filters are stored in `user-filters/global.yaml`. This file is created
the first time you run Retool.

System filters are stored in YAML files named after their system in the
`user-filters` folder, and unless you're using Retool GUI, you'll need to create
them yourself.

To do so, open the dat you want to process in a text editor, then look for the
`<name>` tag near the top. For example:

```
<name>Atari - 2600</name>
```

In the `user-filters` folder, create a YAML file with the same name as the
string between the `<name>` tags. In this case, the file would be called
`Atari - 2600.yaml`.

Retool now automatically references that file whenever a dat with the name
`Atari - 2600` is loaded. Redump and No-Intro usually keep dat names for a long
time, so your system filters should largely remain relevant between updates.

Edit the file you created, then add exclude and include sections to it, using
`user-filters/global.yaml` as an example. If the `user-filters/global.yaml` file
doesn't exist yet, run Retool to generate it.


## Includes and excludes

Both global and system filters have include and exclude lists. Include lists
contain the titles you want to keep, while exclude lists contain the titles you
want to remove.

You can specify titles in three different ways: [full matches](#full-matches),
[partial matches](#partial-matches), and
[regular expressions](#regular-expressions).

### Important: escaping special characters

If you need to use a backslash (`\`) or double quote (`"`) in your filters, you
must escape them with a backslash. For example:

* `\\`
* `\"`

### Full matches

Full matches only apply to titles with the exact same name. You mark a full
match in an include or exclude list by prefixing the text with a pipe (`|`).

For example, if an input dat contains the following titles:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

And your `user-config/global.yaml` has the following exclude:

```
exclude:
- "|Do You Think it's Hot (USA)"
```

Then this title would be removed from the output dat.

If you removed the exclude, then put the following include in:

```
include:
- "|Do You Think it's Hot (USA) (Alt)"
```

Then this title would be kept in the output dat, and the final list of titles
would be:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

The `(Alt)` title would usually be removed by Retool as a clone of the original,
but the include filter has made sure it's kept.

### Partial matches
If a string isn't prefixed with `|` (full match) or `/` (regular expression),
each line in the `exclude` and `include` sections represents a partial match.

For example, if an input dat contains the following titles:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

And your `user-config/global.yaml` has the following excludes:

```
exclude:
- "Hot"
- "Cold"
```

Every title would be removed from the output dat. `Cold` would match
`It's Pretty Cold (Japan)`, and `Hot` would match every other title, as it's
found in both the word `Hot` and `Hotel`.

But let's say we add an include as well:

```
exclude:
- "Hot"
- "Cold"

include:
- "Ho"
```

Now a few things would happen:

* The include for `Ho` would override the exclude for `Hot`.
* The include for `Ho` would prevent Retool from assigning
  `Do You Think it's Hot (USA) (Alt)` to `Do You Think it's Hot (USA)` as a
  clone, meaning _both_ titles end up in the output dat.

As you can see, you need to be careful when using partial matches.

### Regular expressions

If you're familiar with regular expressions (regexes), you know the power (and
pain) that they can bring. To define an include or exclude as a regex, prefix it
with a forward slash (`/`).

For example, if an input dat contains the following titles:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

And your `user-config/global.yaml` has the following exclude:

```
exclude:
- "/^I
```

All titles beginning with `I` would be removed from the output dat.

Now let's add an include:

```
exclude:
- "/^I

include:
- "/\(USA\)"
```

All USA titles would now be kept, so long as they don't start with `I`. In our
example, the `(Alt)` title would usually be removed by Retool as a clone of the
original, but the include filter has made sure it's kept.