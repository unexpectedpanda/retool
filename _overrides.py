# Last updated: 05 Mar 2020
# When the logic fails, and all you can do is manually set parents
# and clones. There's no intelligence here, just straightforward assignment.

# IBM PC-Compatible
def ibm_override_list():
    return {
        'Monopoly (USA) (Alt)': [ # Looks like the script doesn't know how to handle when an alt title is the parent
            'Monopoly (USA) (Alt 2)',
            'Monopoly (USA) (Alt 3)',
        ],
    }

# Microsoft Xbox 360
def x360_override_list():
    return {
        'Mass Effect (USA) (En,Fr,De,Es,It,Pt,Pl) (Bonus Content Disc)': [ # Script gets confused between the parent here, and the first clone listed. Probably related to the Kagerou II and Tales of Destiny 2 issues below.
            'Mass Effect (USA, Europe) (Bonus Content Disc) (Rerelease)',
            'Mass Effect (Japan) (Bonus Disc)',
            'Mass Effect (Germany) (Bonus DVD)',
        ],
    }

# Sega Saturn
def saturn_override_list():
    return {

    }

# SNK Neo Geo CD
def neogeo_override_list():
    return {
        'Garou Densetsu 3 - Road to the Final Victory ~ Fatal Fury 3 - Road to the Final Victory (USA) (En,Ja,Es,Pt) (Rev 3)': [
            'Garou Densetsu 3 - Road to the Final Victory ~ Fatal Fury 3 - Road to the Final Victory (USA) (En,Ja,Es,Pt) (Rev 2)',
            'Garou Densetsu 3 - Road to the Final Victory ~ Fatal Fury 3 - Road to the Final Victory (Japan, USA) (En,Ja,Es,Pt) (Rev 1)',
            'Garou Densetsu 3 - Road to the Final Victory ~ Fatal Fury 3 - Road to the Final Victory (Japan) (En,Ja,Es,Pt)',
            ]
    }

# Sony PlayStation
def psx_override_list():
    return {
        'Motor Toon Grand Prix (Japan) (Rev 1)': ['Motor Toon Grand Prix (Japan)']
    }

# Sony PlayStation 2
def ps2_override_list():
    return {
        'Kagerou II - Dark Illusion (Japan) (PlayStation 2 the Best)': ['Kagerou II - Dark Illusion (Japan, Asia)'], # Script weirdly ignores this match -- possibly because same region is included in both
        'Silent Hill 2 (USA) (En,Ja) (v1.20)': [
            'Silent Hill 2 (Europe) (En,Ja,Fr,De,Es,It)',
            'Silent Hill 2 (Japan) (En,Ja)',
            'Silent Hill 2 (Korea) (En,Fr,De,Es,It)',
        ],
        'Silent Hill 2 (USA) (En,Ja,Fr,De,Es,It) (v2.01)': [
            'Silent Hill 2 - Director\'s Cut (Europe) (En,Fr,De,Es,It)',
            'Silent Hill 2 - Saigo no Uta (Japan) (En,Ja)', # (サイレント・ヒル2 ～最期の詩～)
        ],
        'Tales of Destiny 2 (Japan) (PlayStation 2 the Best)': [ # Unsure why, but script currently selects Korea over Japan, so this is needed
            'Tales of Destiny 2 (Japan, Asia)',
            'Tales of Destiny 2 (Korea)',
        ],
    }

# Sony PlayStation 2
def ps2_superset_override_list():
    return {
        'Silent Hill 2 (USA) (En,Ja,Fr,De,Es,It) (v2.01)': [
            'Silent Hill 2 - Director\'s Cut (Europe) (En,Fr,De,Es,It)',
            'Silent Hill 2 - Saigo no Uta (Japan) (En,Ja)', # (サイレント・ヒル2 ～最期の詩～)
            'Silent Hill 2 (USA) (En,Ja) (v1.20)',
            'Silent Hill 2 (Europe) (En,Ja,Fr,De,Es,It)',
            'Silent Hill 2 (Japan) (En,Ja)',
            'Silent Hill 2 (Korea) (En,Fr,De,Es,It)',
        ],
    }
