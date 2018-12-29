from org.bukkit.entity import Player

class MsgPlugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("Msg plugin loaded") 
        self.spies = {}
        self.nicks = {}
        open("nick.txt","a").write("")
        if not open("nick.txt","r").read() == "":
            self.nicks = eval(open("nick.txt","r").read())
        print('Betoltes utan: ' + str(self.nicks))
        print('Tipus: ' + str(type(self.nicks)))

    def nick(self, s, np):
        return str(self.nicks.get(s,{}).get(np,np))

    def onCommand(self, sender, command, label, args):
        if isinstance(sender, Player):
            if command.name == "spylist":
                f = []
                for i in self.spies:
                    if sender in self.spies[i]:
                        f.append(nick(sender.name,i))
                if not " ".join(f) == "":
                    sender.sendRawMessage(" ".join(f))
                return True
            if command.name == "spy":
                if len(args) < 1: return False
                target = nick(sender.name,args[0])
                if sender in self.spies.get(target, []):
                    self.spies.get(target, []).remove(sender)
                    sender.sendRawMessage("You are no longer spying on %s" % target)
                else:
                    if target in self.spies:
                        self.spies[target].append(sender)
                    else:
                        self.spies[target] = [sender]
                    sender.sendRawMessage("You are now spying on %s" % target)
                return True

            if command.name == "msg":
                player_name = args[0]
                message = " ".join(args[1:])
                players = self.getServer().getOnlinePlayers()
                if player_name not in set(p.name for p in players):
                    return True
                player = [p for p in players if p.name == player_name][0]
                player.sendRawMessage(u"\u00A7b%s\u00A78\u21e8\u00A7b%s \u00A77%s" % (self.nick(player_name,sender.name),self.nick(player_name,player_name),message))
                if not sender == player:
                    sender.sendRawMessage(u"\u00A7b%s\u00A78\u21e8\u00A7b%s \u00A77%s" % (self.nick(sender.name,sender.name),self.nick(sender.name,player_name),message))
                for spy in set(self.spies.get(player_name, [])) | set(self.spies.get(sender.name, [])):
                    if not spy == sender and not spy == player:
                        spy.sendRawMessage(u"\u00A7b%s\u00A78\u21e8\u00A7b%s \u00A77%s" % (self.nick(spy.name,sender.name),self.nick(spy.name,player_name),message))
                return True
            if command.name == "nick":
                if len(args) == 0: return True
                if len(args) == 1:
                    if not sender.name in self.nicks: self.nicks[sender.name] = {}
                    self.nicks[sender.name][args[0]] = args[0]
                    open("nick.txt","w").write(str(self.nicks))
                if len(args) == 2:
                    try:
                        if not sender.name in self.nicks: self.nicks[sender.name] = {}
                        self.nicks[sender.name][args[0]] = args[1]
                        open("nick.txt","w").write(str(self.nicks))
                    except Exception as e:
                        print("Hiba: " + str(e))
                return True
            if command.name == "nicklist":
                f = []
                for i in self.nicks[sender.name]:
                    if not i == self.nicks[sender.name][i]:
                        f.append("%s : %s" % (self.nicks[sender.name][i],i))
                if len(f) > 0:
                    sender.sendRawMessage("  ".join(f))
                return True
