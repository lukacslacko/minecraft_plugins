from org.bukkit.event.player import PlayerChatEvent
from org.bukkit.event.player import PlayerQuitEvent
from org.bukkit.event.player import PlayerJoinEvent
from org.bukkit.event import EventPriority
from org.bukkit.entity import Player

class Join(PythonListener):
    @PythonEventHandler(PlayerJoinEvent,EventPriority.NORMAL)
    def onEvent(self,event):
        sender = event.getPlayer()
        event.setJoinMessage("")
        name = sender.name
        self.g = eval(open("nick.txt","r").read())
        for i in self.getServer().getOnlinePlayers():
            if not i.name in eval(open("nick.txt","r").read()):
                self.g[i.name] = {}
                open("nick.txt","w").write(str(self.g))
            for f in self.getServer().getOnlinePlayers():
                if not f.name in g[i.name]:
                    self.g[i.name][f.name] = f.name
        open("nick.txt","w").write(str(self.g))
        for i in eval(open("nick.txt","r").read()):
            if not i == name:
                if i in set(p.name for p in self.getServer().getOnlinePlayers()):
                    self.getServer().getPlayer(i).sendRawMessage(u"\u00A7b[\u00A74+\u00A7] \u00A7b%s" % self.g[i][name])

class Quit(PythonListener):
    @PythonEventHandler(PlayerQuitEvent,EventPriority.NORMAL)
    def onEvent(self,event):
        sender = event.getPlayer()
        event.setQuitMessage("")
        name = sender.name
        self.g = eval(open("nick.txt","r").read())
        for i in self.getServer().getOnlinePlayers():
            if not i.name in eval(open("nick.txt","r").read()):
                self.g[i.name] = {}
                open("nick.txt","w").write(str(self.g))
            for f in self.getServer().getOnlinePlayers():
                if not f.name in self.g[i.name]:
                    g[i.name][f.name] = f.name
        open("nick.txt","w").write(str(self.g))
        for i in eval(open("nick.txt","r").read()):
            if not i == name:
                if i in set(p.name for p in self.getServer().getOnlinePlayers()):
                    self.getServer().getPlayer(i).sendRawMessage(u"\u00A7b[\u00A74-\u00A7] \u00A7b%s" % self.g[i][name])

class Chat(PythonListener):
    @PythonEventHandler(PlayerChatEvent,EventPriority.NORMAL)
    def onEvnet(self,event):
        pass

class NickPlugin(PythonPlugin):
    def onEnable(self):
        open("nick.txt","a").write("")
        self.nicks = {}
        if not open("nick.txt","r").read() == "":
            self.nicks = eval(open("nick.txt","r").read())
        else:
            open("nick.txt","w").write("{}")
        m = self.getServer().getPluginManager()
        m.registerEvents(Join(),self)
        m.registerEvents(Quit(),self)
        m.registerEvents(Chat(),self)

    def onCommand(self,sender,command,label,args):
        if isinstance(sender, Player):
            parancs = command.name
            self.nicks = {}
            if not open("nick.txt","r").read() == "":
                self.nicks = eval(open("nick.txt","r").read())
            if parancs == "nick":
                if len(args) == 1:
                    self.nicks.get(sender.name,{})
                    self.nicks[sender.name][args[0]] == args[0]
                if len(args) == 2:
                    self.nicks.get(sender.name,{})
                    self.nicks[sender.name][args[0]] = args[1]
            if parancs == "nicklist":
                f = []
                for i in self.nicks.get(sender.name,{}):
                    if not self.nicks[sender.name][i] == i:
                        f.append("%s : %s" % (self.nicks[sender.name][i],i))
                if len(f) > 0:
                    sender.sendRawMessage("  ".join(f))
            open("nick.txt","w").write(str(self.nicks))
        return True 