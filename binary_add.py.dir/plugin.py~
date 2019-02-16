from org.bukkit.entity import Player

import traceback

import blocks

def binary_op(blocks, sender, op):
    if blocks == "" or len(blocks) < 2:
        return
    total = 0
    x = 0
    y = 0
    z = 0
    for row in blocks:
        x = row[0][0] + 1
        y = row[0][1]
        z = row[0][2]
        number = 0
        pow = 1
        for i in range(100):
            blue_blocks = row[1]
            if [x+i,y,z] in blue_blocks:
                number += pow
            pow *= 2
        if op == "+":
            total += number    
        if op == "*":
            total *= number
        if op == "-":
            total -= number
        if op == "/":
            total = int(total / number)
    loc = sender.getLocation()
    z += 1
    x -= 1
    loc.setX(x)
    loc.setY(y)
    loc.setZ(z)
    world = sender.getWorld()
    world.getBlockAt(loc).setType(bukkit.Material.PURPLE_WOOL)
    while total > 0:
        loc.setX(1 + loc.getX())
        if total % 2 == 1:
            world.getBlockAt(loc).setType(bukkit.Material.LIGHT_BLUE_WOOL)
            total -= 1
        else:
            world.getBlockAt(loc).setType(bukkit.Material.AIR)
        total = int(total / 2)

class BinaryAddPlugin(PythonPlugin):
    def onEnable(self):
        try:
            pass
        except Exception:
            traceback.print_exc()
        
    def onCommand(self, sender, command, label, args):
        try:
            if isinstance(sender, Player):
                if command.name == "binary_op":
                    binary_op(blocks.blocks(sender, bukkit.Material), sender, args[0])
        except Exception as e:
            sender.sendRawMessage(traceback.format_exc())
        return True
