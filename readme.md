# Retool
Strips [Redump](http://redump.org/) dats to only include English titles from
all regions, with no dupes. US titles are preferenced. This is not an
official Redump project.

## Usage
`python retool.py -i input.dat -o output.dat <options>`

## Options
* `-a` Remove applications
* `-d` Remove demos and coverdiscs
* `-e` Remove educational
* `-m` Remove multimedia
* `-p` Remove betas and prototypes
* `-ra` Split into regions, all languages (not checked for dupes)
* `-re` Split into regions, English only (not checked for dupes)

## How it works
The input dat is split into regions, then each region is processed in a
specific order. Each region cannot include titles that are in the regions
that precede it. The USA version of a title is considered canonical.

Regions are parsed in the following order:

1. USA
2. World
3. UK
4. Australia
5. Canada
6. Brazil
7. Asia
8. Austria
9. Belgium
10. Switzerland
11. China
12. Germany
13. Denmark
14. Spain
15. Finland
16. France
17. Greece
18. Croatia
19. India
20. Italy
21. Japan
22. Korea
23. Netherlands
24. Norway
25. Poland
26. Portugal
27. Russia
28. South Africa
29. Scandinavia
30. Sweden

As the program progresses through the regions, `_regional_renames.py` is
referenced to check if any titles in the current region are the same as
another region's title, but with a different name. For example, apart from the
title, *Dancing Stage Unleashed 3 (Europe)* and
*Dance Dance Revolution Ultramix 3 (USA)* are the same title, and so
*Dancing Stage Unleashed 3 (Europe)* would not be included.

## Known limitations
Be aware of the following limitations when using Retool. These may or may not be addressed in the future.

#### Doesn't remove older versions of titles
For example, *Halo - Combat Evolved (USA)*,
*Halo - Combat Evolved (USA) (Rev 1)* and
*Halo - Combat Evolved (USA) (Rev 2)* will all be included.

#### Doesn't remove single titles in favor of compilation titles
For example, *Assassin's Creed - Ezio Trilogy* does not supersede
*Assassin's Creed II*, *Assassin's Creed - Brotherhood*, and
*Assassin's Creed - Revelations*.

#### Doesn't remove different language versions from the same region
For example, *Suffering, The - Ties That Bind (Europe) (En,Es,It)* and
*Suffering, The - Ties That Bind (Europe) (En,Fr)*.

#### Can't preference a non-US title over a US title, when the non-US title is arguably superior
For example, *Fahrenheit (Europe) (En,Fr,De,Es,It)* versus *Indigo Prophecy (USA)*,
where the latter is censored.

#### Can only follow Redump language tags for non-English countries
If Redump missed tagging titles from regions where English isn't their first language (for example, Japan),
those titles won't be included.

#### Will remove titles that have the same name in different regions, even if those titles have different content
For example, versions of singing titles that have additional local tracks.