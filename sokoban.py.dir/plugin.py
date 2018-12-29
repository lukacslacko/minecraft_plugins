from org.bukkit.event import EventPriority
from org.bukkit.event.player import PlayerToggleSneakEvent
from org.bukkit.entity import Player
import levels
class ListenerPlugin(PythonListener):
    @PythonEventHandler(PlayerToggleSneakEvent,EventPriority.NORMAL)
    def onEvent(self,event):
        try:
            sender = event.getPlayer()
            h = sender.getLocation()
            n = int(h.getYaw())
            x = h.getX()
            z = h.getZ()
            ef = h.clone()
            mh = h.clone()
            uh = h.clone()
            ef.setY(ef.getY()+1)
            efee = ef.clone()
            efke = ef.clone()
            elke = h.clone()
            elke.setY(elke.getY()-1)

            # Pozitiv z
            if (n < 46 or n > 360 - 46) and 0.6 < z-int(z):
                f = False
                uh.setZ(uh.getZ()+1)
                mh.setZ(mh.getZ()+2)
                efee.setZ(efee.getZ()+1)
                efke.setZ(efke.getZ()+2)
                elke.setZ(elke.getZ()+2)
                for i in eval(open("blocks.txt","r").read()):
                    if sender.getWorld().getBlockAt(uh).getType() == eval(i):
                        f = True
                if f and sender.getWorld().getBlockAt(ef).getType() == sender.getWorld().getBlockAt(mh).getType():
                    block = sender.getWorld().getBlockAt(uh).getType()
                    sender.getWorld().getBlockAt(efee).setType(bukkit.Material.AIR)
                    sender.getWorld().getBlockAt(uh).setType(bukkit.Material.AIR)
                    sender.getWorld().getBlockAt(mh).setType(block)
                    if str(sender.getWorld().getBlockAt(elke).getType()) == "bukkit.Material.DIAMOND_BLOCK":
                        sender.getWorld().getBlockAt(efke).setType(bukkit.Material.PINK_GLASS)

            # Negativ z
            elif (n < 180+46 or n > 180-46) and 0.4 > z-int(z):
                f = False
                uh.setZ(uh.getZ()-1)
                mh.setZ(mh.getZ()-2)
                for i in eval(open("blocks.txt","r").read()):
                    if sender.getWorld().getBlockAt(uh).getType() == eval(i):
                        f = True
                if f and sender.getWorld().getBlockAt(ef).getType() == sender.getWorld().getBlockAt(mh).getType():
                    block = sender.getWorld().getBlockAt(uh).getType()
                    sender.getWorld().getBlockAt(uh).setType(bukkit.Material.AIR)
                    sender.getWorld().getBlockAt(mh).setType(block)

            # Pozitiv x
            elif (n < 270+46 or n > 270-46) and 0.6 < x-int(x):
                f = False
                uh.setX(uh.getX()+1)
                mh.setX(mh.getX()+2)
                for i in eval(open("blocks.txt","r").read()):
                    if sender.getWorld().getBlockAt(uh).getType() == eval(i):
                        f = True
                if f and sender.getWorld().getBlockAt(ef).getType() == sender.getWorld().getBlockAt(mh).getType():
                    block = sender.getWorld().getBlockAt(uh).getType()
                    sender.getWorld().getBlockAt(uh).setType(bukkit.Material.AIR)
                    sender.getWorld().getBlockAt(mh).setType(block)

            # Negativ x
            elif (n < 90+46 or n > 90-46) and 0.4 > x-int(x):
                f = False
                uh.setX(uh.getX()-1)
                mh.setX(mh.getX()-2)
                for i in eval(open("blocks.txt","r").read()):
                    if sender.getWorld().getBlockAt(uh).getType() == eval(i):
                        f = True
                if f and sender.getWorld().getBlockAt(ef).getType() == sender.getWorld().getBlockAt(mh).getType():
                    block = sender.getWorld().getBlockAt(uh).getType()
                    sender.getWorld().getBlockAt(uh).setType(bukkit.Material.AIR)
                    sender.getWorld().getBlockAt(mh).setType(block)

        except Exception as e:
            print(e)
class SokobanPlugin(PythonPlugin):
    def onEnable(self):
        pluginManager = self.getServer().getPluginManager()
        join = ListenerPlugin()
        pluginManager.registerEvents(join,self)
        print("sokoban")
        try:
            self.blocks = []
            open("blocks.txt","a").write("")
            if not open("blocks.txt","r").read() == "":
                self.blocks = eval(open("blocks.txt","r").read())
            else:
                open("blocks.txt","w").write("[]")
        except Exception as e:
            print("Exception " + str(e))

    def onCommand(self, sender, command, label, args):
        try:
            if isinstance(sender, Player): 
                if command.name == "enable_push" and len(args) > 0:
                    if not "bukkit.material."+args[0].upper() in self.blocks:
                        self.blocks.append("bukkit.Material."+args[0].upper())
                        open("blocks.txt","w").write(str(self.blocks))
                    else:
                        pass
                if command.name == "disable_push" and len(args) > 0:
                    if "bukkit.material."+args[0].upper() in self.blocks:
                        self.blocks.remove("bukkit.Material."+args[0].upper())
                        open("blocks.txt","w").write(str(self.blocks))
                    else:
                        pass
                if command.name == "list_pushable":
                    if len(self.blocks) > 0:
                        f = []
                        for i in self.blocks:
                            f.append(i[16:])
                        sender.sendRawMessage(" ".join(f))
                    else:
                        sender.sendRawMessage("fa")
                if command.name == "list_levels":
                    sender.sendRawMessage("   ".join(levels.levels.keys()))
                if command.name == "generate_level":
                    loc = sender.getLocation()
                    x = int(loc.getX())
                    y = int(loc.getY())
                    z = int(loc.getZ())
                    tp = levels.generate(levels.levels[args[0]], x, y, z, bukkit.Material.STONE, bukkit.Material.GOLD_BLOCK, bukkit.Material.DIAMOND_BLOCK, bukkit.Material.QUARTZ_BLOCK, bukkit.Material.GLASS, bukkit.Material.AIR, sender)
                    loc.setX(tp[0]+0.5)
                    loc.setY(tp[1]+1)
                    loc.setZ(tp[2]+0.5)
                    sender.teleport(loc)
        except Exception as e:
            sender.sendRawMessage('Exception ' + str(e)) 
        
        return True
