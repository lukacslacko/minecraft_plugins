from org.bukkit.entity import Player

def setblock(p, x, y, z, s, meta=''):
    return 'setblock ' + str(p[0] + x) + ' ' + str(p[1] + y) + ' ' + str(p[2] + z) + ' minecraft:' + s + '[' + meta + ']';

def gold(p, x, y, z):
    return setblock(p, x, y, z, 'gold_block')
    
def blue(p, x, y, z):
    return setblock(p, x, y, z, 'blue_concrete')
    
def wire(p, x, y, z, meta=''):
    return setblock(p, x, y, z, 'redstone_wire', meta)
    
def repe(p, x, y, z, meta=''):
    return setblock(p, x, y, z, 'repeater', meta)
    
def torc(p, x, y, z, meta=''):
    return setblock(p, x, y, z, 'redstone_wall_torch', meta)
    
def build_1bit(p, x):
    return [
        wire(p, x, 0, 0, 'north=side,south=side'),
        wire(p, x, 0, 1, 'north=side,south=side'),
        blue(p, x, 0, 2),
        repe(p, x, 0, 3, 'delay=1,facing=south,locked=true'),
        blue(p, x, 0, 4),
        blue(p, x, 1, 4),
        wire(p, x, 2, 4, 'east=side,west=side'),
        wire(p, x, 0, 5, 'north=side,south=side'),
        wire(p, x, 0, 6, 'north=side,south=side'),
        blue(p, x+1, 1, 4),
        wire(p, x+1, 2, 4, 'east=side,west=side'),
        repe(p, x+1, 0, 3, 'delay=1,facing=east,powered=true'),
        wire(p, x+2, 0, 3, 'west=side,power=15'),
        torc(p, x+2, 1, 3, 'facing=north,lit=true'),
        blue(p, x+2, 1, 4),
        wire(p, x+2, 2, 4, 'east=side,west=side'),
        ]

def build_4bit_memory(p):    
    return [
        blue(p, 0, 0, 4),
        wire(p, 0, 1, 4, 'east=up'),
        repe(p, 0, 0, 5, 'facing=south,delay=1'),
        wire(p, 0, 0, 6, 'north=side,south=side'),
        blue(p, 1, 1, 4),
        wire(p, 1, 2, 4, 'east=side,west=side'),       
        ] + build_1bit(p, 2) + build_1bit(p, 5) + build_1bit(p, 8) + build_1bit(p, 11)

class RedstonePlugin(PythonPlugin):
    def onEnable(self):
        pass

    def senderxyz(self,sender):
        x = int(sender.getLocation().getX())
        y = int(sender.getLocation().getY())
        z = int(sender.getLocation().getZ())
        return [x,y,z]

    def arany(self,p,sender):
        w = sender.getWorld()
        h = sender.getLocation()
        h.setX(p[0])
        h.setY(p[1])
        h.setZ(p[2])
        return w.getBlockAt(h).getType() == bukkit.Material.GOLD_BLOCK
        
    def findGold(self, sender):
        p = self.senderxyz(sender)
        gold = None
        for i in range(-3, 4):
            if not gold is None:
                break
            for j in range(-3, 4):
                if not gold is None:
                    break
                for k in range(-3, 4):
                    if not gold is None:
                        break
                    g = [p[0] + i, p[1] + j, p[2] + k]
                    if self.arany(g, sender):
                        gold = g                                
        return gold
    
    def setBits(self, sender, gold, args):
        loc = sender.getLocation()
        loc.setX(gold[0] + 2)
        loc.setY(gold[1])
        loc.setZ(gold[2] + 3)
        for i in range(len(args)):
            pass
        #while sender.getWorld().getBlockAt(loc).getType() == bukkit.Material.DIODE_BLOCK_ON and i < len(args):
        #    if args[1] == '1':
                
            

    def onCommand(self, sender, command, label, args):
        try:
            if isinstance(sender, Player):
                if command == 'four_bit_unit': 
                    gold = self.findGold(sender)
                    if gold is None:
                        sender.sendRawMessage('No gold block found')
                        return True
                    for c in build_4bit_memory(gold):
                        sender.chat('/' + c)       
                    return True
                if command == 'set_memory_bits':
                    gold = self.findGold(sender)
                    if gold is None:
                        sender.sendRawMessage('No gold block found')
                        return True
                    self.setBits(sender, gold, args)
                    return True
                    
        except Exception as e:
            sender.sendRawMessage('Exception ' + str(e)) 
        
        return True
