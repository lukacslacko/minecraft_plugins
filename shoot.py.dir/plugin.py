from org.bukkit.entity import Player

import traceback

from org.bukkit.event import EventPriority
from org.bukkit.event.player import PlayerInteractEvent

from org.bukkit.scheduler import BukkitRunnable

from java.lang import Runnable

FILENAME = "template.txt"

class TemplateListener(PythonListener):
    @PythonEventHandler(PlayerInteractEvent, EventPriority.NORMAL)
    def onEvent(self, event):
        sender = event.getPlayer()
        try:
            pass
        except Exception:
            sender.sendRawMessage(traceback.format_exc())
            
class ShootRunnable(Runnable):
    def run():
        print("Haho!")

class ShootPlugin(PythonPlugin):
    def onEnable(self):
        try:
            self.data = []
            open(FILENAME,"a").write("")
            if not open(FILENAME,"r").read() == "":
                self.data = eval(open(FILENAME,"r").read())
            self.getServer().getPluginManager().registerEvents(TemplateListener(), self)
        except Exception:
            traceback.print_exc()
        
    def onCommand(self, sender, command, label, args):
        try:
            if isinstance(sender, Player):
                if command.name == "shoot":
                    self.getServer().getScheduler().runTaskLater(self, ShootRunnable(), 40)
        except Exception as e:
            sender.sendRawMessage(traceback.format_exc())
        return True
