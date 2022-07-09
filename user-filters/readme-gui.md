# Retool GUI: Override which titles are included/excluded with custom filters

**This readme is for the GUI version of Retool. For the CLI version, open**
**`readme-cli.md`. It contains extra details required to use that version.**

---

Retool GUI features two tabs that give the user power to include or exclude
titles that Retool ordinarily wouldn't. They are called
**Custom global filters** and **Custom system filters**. As you fill in the
input boxes in those tabs, files are generated in the `user-filters` folder that
record your preferences.

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


## Includes and excludes

Both global and system filters have include and exclude lists. Include lists
contain the titles you want to keep, while exclude lists contain the titles you
want to remove.

You can specify titles in three different ways: [full matches](#full-matches),
[partial matches](#partial-matches), and
[regular expressions](#regular-expressions).

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

And you put the following text in an **Exclude** box:

```
|Do You Think it's Hot (USA)
```

Then this title would be removed from the output dat.

If you removed the exclude, then put the following text in an **Include** box:

```
|Do You Think it's Hot (USA) (Alt)
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
If a line isn't prefixed with `|` (full match) or `/` (regular expression) in an
**Exclude** or **Include** box, then it's interpreted as a partial match.

A partial match looks for the specified text inside all titles.

For example, if an input dat contains the following titles:

```
Do You Think it's Hot (USA)
Do You Think it's Hot (USA) (Alt)
It's Pretty Cold (Japan)
I Can't Find My Hotel (Europe)
```

And you put the following text in an **Exclude** box:

```
Hot
Cold
```

Every title would be removed from the output dat. `Cold` would match
`It's Pretty Cold (Japan)`, and `Hot` would match every other title, as it's
found in both the word `Hot` and `Hotel`.

But let's say we added this text to an **Include** box as well:

```
Ho
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

And you put the following text in an **Exclude** box:

```
/^I
```

All titles beginning with `I` would be removed from the output dat.

If you put the following text in an **Include** box:

```
/\(USA\)
```

All USA titles would now be kept, so long as they don't start with `I`. In our
example, the `(Alt)` title would usually be removed by Retool as a clone of the
original, but the include filter has made sure it's kept.