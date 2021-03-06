from org.bukkit.entity import Player

import traceback

import helper

from org.bukkit.event import EventPriority
from org.bukkit.event.player import PlayerInteractEvent

class WaterPlugin(PythonPlugin):
    def onEnable(self):
        pass
        
    def onCommand(self, sender, command, label, args):
        try:
            if isinstance(sender, Player):
                if command.name == "water":
                    to_fill = []
                    to_visit = [helper.getplayerlocation(sender)]
                    max_number = 1000
                    visited = 0
                    while len(to_visit) > 0 and visited < max_number:
                        visited += 1
                        block = to_visit[0]
                        to_visit = to_visit[1:]
                        if block in to_fill:
                            continue
                        if helper.getair(block, sender, bukkit):
                            to_fill.append(block)
                            for neighbor in helper.neighbors(block):
                                if not neighbor in to_fill:
                                    to_visit.append(neighbor)
                    sender.sendRawMessage("Visited " + str(visited) + " blocks")
                    sender.sendRawMessage("Filling " + str(len(to_fill)) + " blocks with water")
                    for water in to_fill:
                        helper.setblock(water, bukkit.Material.WATER, sender)
        except Exception as e:
            sender.sendRawMessage(traceback.format_exc())
        return True
