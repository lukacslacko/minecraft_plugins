from org.bukkit.entity import Player
from random import choice

import traceback

from org.bukkit.event import EventPriority
from org.bukkit.event.player import PlayerInteractEvent

def rotateSide(sender, center, a, b, c):
    loc = sender.getLocation()
    p = loc.clone()
    q = loc.clone()
    r = loc.clone()
    s = loc.clone()
    t = loc.clone()
    w = sender.getWorld()
    for i in range(1, 7):
        for j in range(7):
            for k in range(3, 7):
                p.setX(center[0])
                p.setY(center[1])
                p.setZ(center[2])
                
                q.setX(center[0] + i*a[0] + j*b[0] + k*c[0])
                q.setY(center[1] + i*a[1] + j*b[1] + k*c[1])
                q.setZ(center[2] + i*a[2] + j*b[2] + k*c[2])
                
                r.setX(center[0] + j*a[0] - i*b[0] + k*c[0])
                r.setY(center[1] + j*a[1] - i*b[1] + k*c[1])
                r.setZ(center[2] + j*a[2] - i*b[2] + k*c[2])
                
                s.setX(center[0] - i*a[0] - j*b[0] + k*c[0])
                s.setY(center[1] - i*a[1] - j*b[1] + k*c[1])
                s.setZ(center[2] - i*a[2] - j*b[2] + k*c[2])
                
                t.setX(center[0] - j*a[0] + i*b[0] + k*c[0])
                t.setY(center[1] - j*a[1] + i*b[1] + k*c[1])
                t.setZ(center[2] - j*a[2] + i*b[2] + k*c[2])
                
                print(p.getX(), p.getY(), p.getZ())
                print(q.getX(), q.getY(), q.getZ())
                print(r.getX(), r.getY(), r.getZ())
                print(s.getX(), s.getY(), s.getZ())
                print(t.getX(), t.getY(), t.getZ())
                
                w.getBlockAt(p).setType(w.getBlockAt(q).getType())
                w.getBlockAt(q).setType(w.getBlockAt(r).getType())
                w.getBlockAt(r).setType(w.getBlockAt(s).getType())
                w.getBlockAt(s).setType(w.getBlockAt(t).getType())
                w.getBlockAt(t).setType(w.getBlockAt(p).getType())
                
def rotateTop(sender, xyz):
    rotateSide(sender, [xyz[0] + 6, xyz[1] + 6, xyz[2] + 6], [1, 0, 0], [0, 0, 1], [0, 1, 0])

def rotateBottom(sender, xyz):
    rotateSide(sender, [xyz[0] + 6, xyz[1] + 6, xyz[2] + 6], [1, 0, 0], [0, 0, 1], [0, -1, 0])

def rotateLeft(sender, xyz):
    rotateSide(sender, [xyz[0] + 6, xyz[1] + 6, xyz[2] + 6], [0, 1, 0], [0, 0, 1], [1, 0, 0])

def rotateRight(sender, xyz):
    rotateSide(sender, [xyz[0] + 6, xyz[1] + 6, xyz[2] + 6], [0, 1, 0], [0, 0, 1], [-1, 0, 0])

def rotateFront(sender, xyz):
    rotateSide(sender, [xyz[0] + 6, xyz[1] + 6, xyz[2] + 6], [0, 1, 0], [1, 0, 0], [0, 0, 1])

def rotateBack(sender, xyz):
    rotateSide(sender, [xyz[0] + 6, xyz[1] + 6, xyz[2] + 6], [0, 1, 0], [1, 0, 0], [0, 0, -1])
    
def rotateRandom(sender, xyz):
    choice([rotateTop, rotateBottom, rotateLeft, rotateRight, rotateFront, rotateBack])(sender, xyz)

class ButtonListener(PythonListener):
    @PythonEventHandler(PlayerInteractEvent, EventPriority.NORMAL)
    def onEvent(self, event):
        sender = event.getPlayer()
        try:
            l = sender.getLocation()
            bl = sender.getLineOfSight(None,30)
            for b in bl:
                if b.getType() == bukkit.Material.AIR:
                    l = b.getState().getLocation()
                else:
                    l = b.getState().getLocation()
                    break
            targetblock = sender.getWorld().getBlockAt(l)
            loc = targetblock.getState().getLocation()
            xyz = [int(loc.getX()), int(loc.getY()), int(loc.getZ())]
            kockak_str = open("kockak.txt","r").read()
            kockak = eval(kockak_str)
            for kocka in kockak:
                if xyz in kocka:
                    i = kocka.index(xyz)
                    if i == 1:
                        rotateBack(event.getPlayer(), kocka[0])
                    if i == 2:
                        rotateFront(event.getPlayer(), kocka[0])
                    if i == 3:
                        rotateBottom(event.getPlayer(), kocka[0])
                    if i == 4:
                        rotateTop(event.getPlayer(), kocka[0])
                    if i == 5:
                        rotateRight(event.getPlayer(), kocka[0])
                    if i == 6:
                        rotateLeft(event.getPlayer(), kocka[0])
        except Exception:
            sender.sendRawMessage(traceback.format_exc())

class RubikPlugin(PythonPlugin):
    def onEnable(self):
        try:
            self.kockak = []
            open("kockak.txt","a").write("")
            if not open("kockak.txt","r").read() == "":
                self.kockak = eval(open("kockak.txt","r").read())
            self.getServer().getPluginManager().registerEvents(ButtonListener(), self)
        except Exception:
            traceback.print_exc()
        
    def block(self,sender):
         block = sender.getTargetBlock(None,6).getState().getLocation()
         return [int(block.getX()),int(block.getY),int(block.getZ)]
    
    def kocka(self,x,y,z):
        self.kockak.append([[x,y,z],[x+6,y+6,z-1],[x+6,y+6,z+13],[x+6,y-1,z+6],[x+6,y+13,z+6],[x-1,y+6,z+6],[x+13,y+6,z+6]])
        open("kockak.txt","w").write(str(self.kockak))
    
    def onCommand(self, sender, command, label, args):
        try:
            if isinstance(sender, Player):
                if command.name == "rubik":
                    p = sender.getLocation()
                    x = int(sender.getLocation().getX()) - 7
                    y = int(sender.getLocation().getY()) + 5
                    z = int(sender.getLocation().getZ()) - 7
                    for i in range(13):
                        for j in range(13):
                            for k in range(13):
                                p.setX(x+i)
                                p.setY(y+j)
                                p.setZ(z+k)
                                sender.getWorld().getBlockAt(p).setType(bukkit.Material.BLACK_CONCRETE)
                    for i in range(3):
                        for j in range(3):
                            for k in range(3):
                                for l in range(3):
                                    p.setX(x + 1 + i*4 + k)
                                    p.setY(y)
                                    p.setZ(z + 1 + j*4 + l)
                                    sender.getWorld().getBlockAt(p).setType(bukkit.Material.WHITE_CONCRETE)
                                    p.setY(y + 12)
                                    sender.getWorld().getBlockAt(p).setType(bukkit.Material.YELLOW_CONCRETE)

                                    p.setX(x + 1 + i*4 + k)
                                    p.setZ(z)
                                    p.setY(y + 1 + j*4 + l)
                                    sender.getWorld().getBlockAt(p).setType(bukkit.Material.BLUE_CONCRETE)
                                    p.setZ(z + 12)
                                    sender.getWorld().getBlockAt(p).setType(bukkit.Material.GREEN_CONCRETE)

                                    p.setZ(z + 1 + i*4 + k)
                                    p.setX(x)
                                    p.setY(y + 1 + j*4 + l)
                                    sender.getWorld().getBlockAt(p).setType(bukkit.Material.RED_CONCRETE)
                                    p.setX(x + 12)
                                    sender.getWorld().getBlockAt(p).setType(bukkit.Material.ORANGE_CONCRETE)
                    for _ in range(20): 
                        rotateRandom(sender, [x, y, z])
                    gomb = sender.getLocation()
                    gomb.setX(x+6)
                    gomb.setY(y-1)
                    gomb.setZ(z+6)
                    sender.getWorld().getBlockAt(gomb).setType(bukkit.Material.STONE_BUTTON)
                    sender.getWorld().getBlockAt(gomb).setData(0,False)
                    gomb.setY(y+13)
                    sender.getWorld().getBlockAt(gomb).setType(bukkit.Material.STONE_BUTTON)
                    sender.getWorld().getBlockAt(gomb).setData(5,False)
                    gomb.setY(y+6)
                    gomb.setX(x-1)
                    sender.getWorld().getBlockAt(gomb).setType(bukkit.Material.STONE_BUTTON)
                    sender.getWorld().getBlockAt(gomb).setData(2,False)
                    gomb.setX(x+13)
                    sender.getWorld().getBlockAt(gomb).setType(bukkit.Material.STONE_BUTTON)
                    sender.getWorld().getBlockAt(gomb).setData(1,False)
                    gomb.setX(x+6)
                    gomb.setZ(z-1)
                    sender.getWorld().getBlockAt(gomb).setType(bukkit.Material.STONE_BUTTON)
                    sender.getWorld().getBlockAt(gomb).setData(4,False)
                    gomb.setZ(z+13)
                    sender.getWorld().getBlockAt(gomb).setType(bukkit.Material.STONE_BUTTON)
                    sender.getWorld().getBlockAt(gomb).setData(3,False)
                    
                    self.kocka(x,y,z)             
        except Exception as e:
            sender.sendRawMessage("Exception " + str(e))
            sender.sendRawMessage(str(e) + traceback.format_exc())
        return True
