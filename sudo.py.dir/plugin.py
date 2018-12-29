class SudoPlugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("Hallo Sudo Welt!")

    def onCommand(self, sender, command, label, args):
        self.getLogger().info("Command: sender=%s, command=%s, label=%s, args=%s!" % (sender,command,label,args))
        #self.getLogger().info("Command name: %s" % command.name)
        #self.getServer().broadcastMessage("Hallo %s!" % sender.name)
        if len(args) < 2:
            return True
        
        player_name = args[0]
        message = " ".join(args[1:])
        self.getLogger().info("X: %s, %s" % (player_name, message))
        
        players = self.getServer().getOnlinePlayers()
        if player_name not in set(p.name for p in players):
            return True

        player = self.getServer().getPlayer(player_name)
        player.chat(message)
        return True
