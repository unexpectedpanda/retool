---
hide:
  - footer
---

# CLRMAMEPro "wrong name" issue

When scanning with [CLRMAMEPro](https://mamedev.emulab.it/clrmamepro/) you might see a lot
of "wrong name" messages that match unrelated titles.

This isn't Retool making a mistake or anything going wrong; it's CLRMAMEPro not giving
enough detail about what's happening. If you let CLRMAMEPro do its thing and say yes to
everything, you'll end up with a set that's fine after it's finished processing.

## The full explanation

CLRMAMEPro gives misleading messages when it scans existing non-1G1R
Redump sets with a Retool DAT file, and finds matching files that were shared between
titles in the original Redump DAT file. This mainly happens with DAT files that contain
multitrack discs (CUE/BIN) like Saturn or Mega CD, where it's common to find the same file
across multiple unrelated titles.

Here's an example to help clarify. Let's assume you have the following things:

* Redump's Saturn DAT file.
* A Retool version of the Saturn DAT file with a region order of USA > Europe > Japan.
* A folder with a complete Redump Saturn collection.

You run a scan with CLRMAMEPro using the Retool DAT file against your existing Saturn
collection, and CLRMAMEPro reports something like this:

> wrong name: Z:\Saturn\Area 51 (Japan).zip [wrong: Z:\Saturn\Area 51 (Japan)] [right: Gungriffon (USA)]

On the surface it looks like CLRMAMEPro is claiming that _Area 51_ is _Gungriffon_ &mdash;
which is not true. So what's going on?

First, let's take a look at _Area 51 (Japan)_ and _Gungriffon (USA)_ in the original
Redump Saturn DAT file, since those are the titles mentioned by CLRMAMEPro:

```xml hl_lines="5"
<game name="Area 51 (Japan)">
	<category>Games</category>
	<description>Area 51 (Japan)</description>
	...
	<rom name="Area 51 (Japan) (Track 2).bin" size="1413552" crc="5af76f8c" md5="5fedd4a8361a9c6ca005b5d48a38ca68" sha1="db9145b3f24a83bcb28a93889001c778d7ab656a"/>
</game>
```

```xml hl_lines="5"
<game name="Gungriffon (USA)">
	<category>Games</category>
	<description>Gungriffon (USA)</description>
	...
	<rom name="Gungriffon (USA) (Track 33).bin" size="1413552" crc="5af76f8c" md5="5fedd4a8361a9c6ca005b5d48a38ca68" sha1="db9145b3f24a83bcb28a93889001c778d7ab656a"/>
	...
</game>
```

While these titles are not the same game, they _do_ share a file. Name aside, `Area 51
(Japan) (Track 2).bin` is the exact same file as `Gungriffon (USA) (Track 33).bin`, with
matching sizes and checksums (CRC/MD5/SHA1). This is common &mdash; this particular file
can also be found in the following titles:

* _Area 51 (Europe) (En,Fr,De,Es)_
* _Area 51 (USA)_
* _Gun Griffon (Europe)_ (multiple times)
* _House of the Dead, The (Japan) (Demo)_
* _Maximum Force (Europe)_
* _Maximum Force (USA)_

Second, if we look at the Retool DAT file, we can see that due to the region priority
(USA > Europe > Japan), _Area 51 (Japan)_ has been removed in favor of _Area 51 (USA)_.
_GunGriffon (USA)_, being a USA title, makes it in.

When the Retool DAT file is used in CLRMAMEPro to scan the existing Saturn folder, and
CLRMAMEPro comes across `Area 51 (Japan).zip`, the process goes something like this:

1. I've found a file called `Area 51 (Japan).zip`.
1. I've checked the current DAT file, and a set with the same name doesn't exist.
1. I did find a file inside the ZIP file though that matches a file in the _GunGriffon
   (USA)_ set, which _is_ in the DAT file.
1. I'm making an educated (but incorrect) guess that this is meant to be _GunGriffon
   (USA)_ because of that matching file. Regardless of whether that's true, I want to get
   that file into the _GunGriffon_ set if it needs it, then I'll deal with the remaining
   files.
1. Let's tell the user I'm being helpful with the following misleading message!

    > wrong name: Z:\Saturn\Area 51 (Japan).zip [wrong: Z:\Saturn\Area 51 (Japan)] [right: Gungriffon (USA)]

**Ultimately, it doesn't matter that _Area 51 (Japan)_ isn't the same game as _GunGriffon (USA)_, all that's happening here is that CLRMAMEPro is rescuing the one file from `Area 51 (Japan).zip` it thinks is useful.**

If you let CLRMAMEPro do its thing and say yes to everything, you'll end up with a set
that's fine after its finished processing. If you're worried about affecting a current set
and are looking for peace of mind, there's a way you can verify things are working as
they're meant to:

1. Point the Retool DAT file in CLRMAMEPro at a new ROM path that's an empty folder.
1. Set your original folder with the existing Redump set in it as an Add path.
1. Use the rebuilder function to create the 1G1R set in the new folder from the existing
   set (make sure to select **Use Add-Paths**).
1. Scan the new 1G1R set with the original Redump DAT file to verify that the 1G1R titles
   properly match their Redump counterparts. RomVault does a better job than CLRMAMEPro
   here of visually showing you what sets are complete.