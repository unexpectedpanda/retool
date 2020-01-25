# Last updated: 21 Jan 2020
# When the logic fails, and all you can do is manually set parents
# and clones. There's no intelligence here, just straightforward assignment.

# Sega Saturn
def saturn_override_list():
    return {
        'Daytona USA (USA)': [
            'Daytona USA (Japan)',
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
        'Silent Hill 2 (USA) (En,Ja) (v1.20)': [
            'Silent Hill 2 (Europe) (En,Ja,Fr,De,Es,It)',
            'Silent Hill 2 (Japan) (En,Ja)',
            'Silent Hill 2 (Korea) (En,Fr,De,Es,It)',
        ],
        'Silent Hill 2 (USA) (En,Ja,Fr,De,Es,It) (v2.01)': [
            'Silent Hill 2 - Director\'s Cut (Europe) (En,Fr,De,Es,It)',
            'Silent Hill 2 - Saigo no Uta (Japan) (En,Ja)', # (サイレント・ヒル2 ～最期の詩～)
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