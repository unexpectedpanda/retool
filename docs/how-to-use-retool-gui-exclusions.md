---
hide:
  - footer
---

# Exclusions

Retool can exclude specific types of titles from the output DAT file. These exclusions are
either based on the `<category>` tag found in DAT files, or on a string in the title's
name.

To add exclusions, in the **Global settings** or **System settings** tab, click the
**Exclusions** tab.

![A screenshot of Retool's exclusions tab](images/exclusions.png)

!!! note
    Clearing an exclusion checkbox doesn't mean that the type is included, just that it's
    not excluded. For example, if you don't select **Games**, this doesn't mean that all
    games get included in the output DAT file &mdash; some might still be removed due to
    other processes in Retool, like 1G1R filtering.

The available exclusions are as follows:

* **Add-ons**
  <br>Titles with the DAT file category `Add-Ons`. This includes expansion packs and
  additional materials for titles.

* **Applications**
  <br>Titles with the DAT file category `Applications`, or with the following text in the
  name:
    * `(Program)`
    * `(Test Program)`
    * `Check Program`
    * `Sample Program`

* **Audio**
  <br>Titles with the DAT file category `Audio`. These might be used as soundtracks by
  games.

* **Bad dumps**
  <br>Titles marked as bad dumps with a `[b]` in the name.

* **BIOS and other chips**
  <br>Titles with the DAT file category `Console`, or with the following text in the name:
    * `[BIOS]`
    * `(Enhancement Chip)`

* **Bonus discs**
  <br>Titles with the DAT file category `Bonus Discs`. These could be anything other than
  the main title content, like patches, manuals, collector discs, or otherwise.

* **Coverdiscs**
  <br>Titles with the DAT file category `Coverdiscs`. These were discs that were attached
  to the front of magazines, and could contain demos, or rarely, full games.

* **Demos, kiosks, and samples**
  <br>Titles with the DAT file category `Demos`, or with the following text in the name:
    * `@barai`
    * `(Demo [1-9])`
    * `(Demo-CD)`
    * `(GameCube Preview)`
    * `(Kiosk *|* Kiosk)`
    * `(Preview)`
    * `Kiosk Demo Disc`
    * `PS2 Kiosk`
    * `PSP System Kiosk`
    * `Sample`
    * `Taikenban`
    * `Trial Edition`

* **Educational**
  <br>Titles with the DAT file category `Educational`.

* **Games**
  <br>Titles with the DAT file category `Games`, or no DAT file category.

* **Manuals**
  <br>Titles with `(Manual)` in the name.

* **MIA**
  <br>Titles with ROMs declared as missing in action in the clone lists or DAT files.

* **Multimedia**
  <br>Titles with the DAT file category `Multimedia`. These might include games.

* **Pirate**
  <br>Titles with `(Pirate)` in the name.

* **Preproduction**
  <br>Titles with the DAT file category `Preproduction`, or with the following text in the
  name:
    * `(Alpha [0-99])`
    * `(Beta [0-99])`
    * `(Pre-Production)`
    * `(Possible Proto)`
    * `(Proto [0-99])`
    * `(Review Code)`

* **Promotional**
  <br>Titles with the DAT file category `Promotional`, or with the following text in the
  name:
    * `(Promo)`
    * `EPK`
    * `Press Kit`

* **Unlicensed**
  <br>Titles unauthorized by console manufacturers, marked by the following text in the
  name:
    * `(Unl)`
    * `(Aftermarket)`
    * `(Pirate)`

* **Video**
  <br>Titles with the DAT file category `Video`.
