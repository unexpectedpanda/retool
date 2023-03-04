---
hide:
  - footer
---

# Beginner's guide to ROM managers

This guide is for those who've never used ROM managers before, and don't understand how to
manage their files.

For those new to dat managers, we'll cover one option in brief: CLRMAMEPro.

Download and install [CLRMAMEPro](https://mamedev.emulab.it/clrmamepro/), then run it. The first screen you see is called the Profiler. This is where you load your various dats.

1. Click **Add DatFile**.
1. Select the Retool dat you created.
1. CLRMAMEPro will ask you where you want to put the dat. This is just folder organization, if you want to keep your No-Intro dats separate from your Retool dats, for instance. Choose a location, then click **OK**.
1. Click **[NEW DATFILES]**, then double click the Retool dat you added.
1. On the next prompt, click **Default**. You should now see the main CLRMAMEPro panel:
1. Click **Settings**.

### Optional setup: compression formats

If you prefer compressing in RAR or 7z:

1. Download and install [WinRAR](https://www.rarlab.com/).
1. Download and install [7zip](https://www.7-zip.org/).
1. Copy `WinRAR.exe` from your WinRAR install folder to your CLRMAMEPro folder.
1. Copy `7z.exe` from your 7z install folder to your CLRMAMEPro folder.
1. Return to CLRMAMEPro, then in the **Settings** window click **Compressor**.
1. In the **RAR** tab, enter the following:
   * **Executable** &mdash; `winrar.exe`
   * **Compress** &mdash; `a -y -r -ibck -m5 -s- %1 %2`
   * **Delete** &mdash; `d -y -ibck -m5 -s- %1 %2`
   * **Rename** &mdash; `rn -y -ibck -m5 -s- %1 %2 %3`
1. In the **7z** tab, enter the following:
   * **Executable** &mdash; `7z.exe`
   * **Compress** &mdash; `a -y -r -ms=off -mx9 %1 %2`
   * **Delete** &mdash; `d -y -ms=off -mx9 %1 %2`

   > **NOTE:** I could never get rename for 7z to work, all it seemed to do was recompress a brand new archive anyway, so it didn't seem worth the fuss. Also, this is max compression, so expect it to be very slow.
1. Click **OK**.
1. Click **Save As Def.** to make everything from **Backup/Download** and below your default settings. Now whenever you load a dat and select **Default**, these compression settings will load.

### Set up Rom- and Add-Paths

1. From the top left dropdown, select **Rom-Paths**. This is where your ROM set will ultimately end up.
1. Click **Add** to select your Rom-Paths folder. You have a choice here as to what type of folder you select:
    * Point your Rom-Paths folder to an existing set with the intention to trim it. To do this, add the folder, close the settings, then head to the Scanner section of these instructions.
    * Point your Roms-Paths folder to an empty folder, then build the set from scratch using the contents of one or more other folders. To do this, add the folder, then head to the Rebuilder section of these instructions. You can also use the rebuilder if you are slowly building/updating your set from various sources.

#### Option A: Scanner

CLRMAMEPro's scanner checks a folder against a dat for mismatches. It checks names, hashes, sizes, and other things, renaming and changing files where necessary.

1. From the CLRMAMEPro panel, click **Scanner**.
1. Below **Fix**, click the plus (**+**) button to enable all fixes.
1. Click **New Scan**. Whenever prompted, click **Yes To All**. Any unneeded files should be moved to the backup folder.

    > **Note:** CLRMAMEPro might give you a lot of warnings about renaming files to something that doesn't seem to be related to the original title. Usually there's no error here, it's just CLRMAMEPro [not giving enough information](https://github.com/unexpectedpanda/retool/wiki/FAQs#when-i-scan-an-existing-set-with-clrmamepro-and-a-retool-dat-why-do-i-see-a-lot-of-wrong-name-messages-that-match-unrelated-titles) as to what's happening. Just keep clicking **Yes To All** and you'll end up with a set that's fine when it finishes processing.

1. When the scan is complete, you'll get a list of the files that you're missing in CLRMAMEPro's **Scan results** window. You can use the Rebuilder to integrate those into your set if you find them later.

After your first scan, you can click **Scan** instead, which should be quicker than **New Scan**.

#### Option B: Rebuilder
CLRMAMEPro's Rebuilder checks one or more folders for files it might need as specified by a dat, then puts them where required. It can also be used if you decide you want to change how your files are compressed.

1. In **Settings**, change the top left dropdown to **Add-Paths**. An Add-Path is where CLRMAMEPro checks for files it might need. Add the folders you want, then close settings.
1. From the CLRMAMEPro panel, click **Rebuilder**.
1. Click **Use Add-Paths** to use your Add-Paths as the source instead of an arbitrary folder.
   > **Note:** CLRMAMEPro will also use your backup path automatically as an Add-Path.
1. If you're going to be changing your Rom-Path a lot, it's usually a good idea to click
   **Use 1st RomPath** before proceeding. Otherwise CLRMAMEPro remembers your old folder, and you'll get things
   going to the wrong place.
1. Choose your compression settings, and whether or not you want to **Remove Matched Sourcefiles**.
1. Click **Rebuild**.

To check your progress after a rebuild, use the Scanner.