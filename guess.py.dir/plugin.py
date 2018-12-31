from org.bukkit.entity import Player

import traceback

from org.bukkit.event import EventPriority
from org.bukkit.event.block import BlockPlaceEvent

class GuessListener(PythonListener):
    @PythonEventHandler(BlockPlaceEvent, EventPriority.NORMAL)
    def onEvent(self, event):
        sender = event.getPlayer()
        try:
            for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
                pos = event.getBlock().getLocation()
                pos.setX(pos.getX() + dir[0])
                pos.setZ(pos.getZ() + dir[1])
                w = sender.getWorld()
                if not w.getBlockAt(pos).getType() == bukkit.Material.CYAN_CONCRETE:
                    continue
                pos.setX(pos.getX() + dir[0])
                pos.setZ(pos.getZ() + dir[1])
                if not w.getBlockAt(pos).getType() == bukkit.Material.BLUE_CONCRETE:
                    continue
                pos.setX(pos.getX() + dir[0])
                pos.setZ(pos.getZ() + dir[1])
                if w.getBlockAt(pos).getType() == bukkit.Material.AIR:
                    event.setBuild(False)
        except Exception:
            sender.sendRawMessage(traceback.format_exc())

class GuessPlugin(PythonPlugin):
    def onEnable(self):
        try:
            self.getServer().getPluginManager().registerEvents(GuessListener(), self)
        except Exception:
            traceback.print_exc()
        
