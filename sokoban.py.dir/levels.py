# Source: http://borgar.net/programs/sokoban
levels = {
    'tutorial': [
        '+++++  ',
        '+*  +  ',
        '+ +O+++',
        '+ O ..+',
        '+++++++',
        ],
    'level1': [
        '    +++++          ',
        '    +   +          ',
        '    +O  +          ',
        '  +++  O++         ',
        '  +  O O +         ',
        '+++ + ++ +   ++++++',
        '+   + ++ +++++  ..+',
        '+ O  O          ..+',
        '+++++ +++ +*++  ..+',
        '    +     +++++++++',
        '    +++++++        ',
        ], 
    'level2': [
        '++++++++++++  ',
        '+..  +     +++',
        '+..  + O  O  +',
        '+..  +O++++  +',
        '+..    * ++  +',
        '+..  + +  O ++',
        '++++++ ++O O +',
        '  + O  O O O +',
        '  +    +     +',
        '  ++++++++++++',
        ],
    'level3': [
        '        ++++++++ ',
        '        +     *+ ',
        '        + O+O ++ ',
        '        + O  O+  ',
        '        ++O O +  ',
        '+++++++++ O + +++',
        '+....  ++ O  O  +',
        '++...    O  O   +',
        '+....  ++++++++++',
        '++++++++         ',
        ],
    'jr1-level1': [
        '+++++++',
        '+.   .+',
        '+  O  +',
        '+ O*O +',
        '+  O  +',
        '+.   .+',
        '+++++++',
        ],
    'jr1-level2': [
        '+++++++++',
        '+.     .+',
        '+ +   + +',
        '+   O   +',
        '+  O*O  +',
        '+   O   +',
        '+ +   + +',
        '+.     .+',
        '+++++++++',
        ],
    'jr1-level3': [
        '+++++++',
        '+.   .+',
        '+.OOO.+',
        '++O*O++',
        '+.OOO.+',
        '+.   .+',
        '+++++++',
        ],
    'jr1-level4': [
        '+++++++',
        '+.   .+',
        '+ O*O +',
        '+ +++ +',
        '+ O O +',
        '+.   .+',
        '+++++++',
        ],
    'jr1-level5': [
        '+++++++',
        '+. O .+',
        '+ O*O +',
        '+. O .+',
        '+++++++',
        ],
    'jr1-level6': [
        ' +++++ ',
        '++. .++',
        '+.OOO.+',
        '+ O*O +',
        '+.OOO.+',
        '++. .++',
        ' +++++ ',
        ],
    'jr1-level7': [
        '+++++++',
        '+. O..+',
        '+. O  +',
        '+OO+OO+',
        '+ *O .+',
        '+..O .+',
        '+++++++',
        ],
    'jr1-level8': [
        '++++++++',
        '+.  O .+',
        '+.OOOO.+',
        '+. *O .+',
        '++++++++',
        ],
    'jr1-level9': [
        '+++++++++',
        '+.     .+',
        '+ +   + +',
        '+ .OOO. +',
        '+  O*O  +',
        '+ .OOO. +',
        '+ +   + +',
        '+.     .+',
        '+++++++++',
        ],
}
    
# Returns the start position of the player
def generate(level, x, y, z, wall, box, target, floor, ceiling, air, sender):
    world = sender.getWorld()
    loc = sender.getLocation()
    start = None
    for row in enumerate(level):
        for col in enumerate(row[1]):
            loc.setX(x + row[0])
            loc.setY(y)
            loc.setZ(z + col[0])
            if col[1] == ' ' or col[1] == '*':
                world.getBlockAt(loc).setType(floor)
                loc.setY(y+3)
                world.getBlockAt(loc).setType(ceiling)
                loc.setY(y+1)
                world.getBlockAt(loc).setType(air)
                loc.setY(y+2)
                world.getBlockAt(loc).setType(air)
                if col[1] == '*':
                    start = [x + row[0], y, z + col[0]]
            elif col[1] == '.':
                world.getBlockAt(loc).setType(target)
                loc.setY(y+3)
                world.getBlockAt(loc).setType(ceiling)
                loc.setY(y+1)
                world.getBlockAt(loc).setType(air)
                loc.setY(y+2)
                world.getBlockAt(loc).setType(air)
            elif col[1] == 'O':
                world.getBlockAt(loc).setType(floor)
                loc.setY(y+3)
                world.getBlockAt(loc).setType(ceiling)
                loc.setY(y+1)
                world.getBlockAt(loc).setType(box)
                loc.setY(y+2)
                world.getBlockAt(loc).setType(air)
            elif col[1] == '+':
                world.getBlockAt(loc).setType(floor)
                loc.setY(y+3)
                world.getBlockAt(loc).setType(ceiling)
                loc.setY(y+1)
                world.getBlockAt(loc).setType(wall)
                loc.setY(y+2)
                world.getBlockAt(loc).setType(air)
    return start
