from org.bukkit.entity import Player

ABC = [
    ' ###  ####   #### ####  ##### #####  #### #   #  ###      # #   # #     #   # #   #  ###  ####   ###  ####   #### ##### #   # #   # #   # #   # #   # ##### ',
    '#   # #   # #     #   # #     #     #     #   #   #       # #  #  #     ## ## ##  # #   # #   # #   # #   # #       #   #   # #   # #   #  # #   # #     #  ',
    '##### ####  #     #   # ###   ###   #  ## #####   #       # ###   #     # # # # # # #   # ####  # # # ####   ###    #   #   # #   # # # #   #     #     #   ',
    '#   # #   # #     #   # #     #     #   # #   #   #   #   # #  #  #     #   # #  ## #   # #     #  ## #   #     #   #   #   #  # #  # # #  # #    #    #    ',
    '#   # ####   #### ####  ##### #      ###  #   #  ###   ###  #   # ##### #   # #   #  ###  #      #### #   # ####    #    ###    #    # #  #   #   #   ##### ',
    '                                                                                                                                                            ',
    ]
    
abc = [
    '      #               #  ###    ##        #       #      #   #     #                                          ##                                            ',
    '      #               # #   #  #  #  ## # #                  #     #                                         #     #                                   #### ',
    ' ##   ####   ####  #### ##### ###   #  #  ####    #      #   # #   #    ## #   ##     #    ##     ##  # ##    ##  ###   #   # #   # # # #  # #  #   #    #  ',
    '#  #  #   # #     #   # #      #     ###  #   #   #      #   ##    #    # # #  # #   # #   # #   # #  ##        #  #    #   #  # #  # # #   #    # #    #   ',
    ' ## # ####   ####  ####  ####  #       #  #   #   #   ###    # #    ##  # # #  # #    #    ##     ##  #       ##    ##   ###    #    # #   # #    #    #### ',
    '                               #     ##                                                    #       #  #                                         ##          ',
    ]
    
SZAKECE = [
    ' ###     #   ###  ####     #  #####  #### #####  ###   ###  ',
    '#   #   ##  #   #     #   #   #     #        #  #   # #   # ',
    '#   #    #     #   ###   #    ####  ####    #    ###   #### ',
    '#   #    #    #       # #####     # #   #  #    #   #     # ',
    ' ###    ###  #### ####    #   ####   ###  #      ###  ####  ',
    '                                                            ',
    ]

SZOKOZ = [
    '      ',
    '      ',
    '      ',
    '      ',
    '      ',
    '      ',
    ]

class BannerTextPlugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("Msg plugin loaded")
        
    def banner(self, bf, jf, bk, jk, ba, ja, x, z):
        ered = "setblock ~" + str(x) + ' ~' + str(z) + " ~ minecraft:"
        if bk or jk:
            ered += 'black'
        else:
            ered += 'white'
        ered += '_wall_banner[facing=south]{Patterns:['
        if bk or jk:
            ered += '{Pattern:ts,Color:0},{Pattern:bs,Color:0},'
            if jk and not bk:
                ered += '{Pattern:vh,Color:0},'
            if bk and not jk:
                ered += '{Pattern:vhr,Color:0},'
        if bf:
            ered += '{Pattern:tl,Color:15},'
        if ba:
            ered += '{Pattern:bl,Color:15},'
        if jf:
            ered += '{Pattern:tr,Color:15},'
        if ja:
            ered += '{Pattern:br,Color:15},'
        if bf or jf or bk or jk or ba or ja:
            ered = ered[:len(list(ered))-1]
        ered += ']}'
        return [ered, 'setblock ~' + str(x) + ' ~' + str(z) + ' ~-1 minecraft:quartz_block', 'setblock ~' + str(x) + ' ~' + str(z-1) + ' ~-1 minecraft:quartz_block']



    def betudarab(self, ABC, i, j, x, y):
        return self.banner(ABC[j+0][i+0] == '#', ABC[j+0][i+1] == '#', ABC[j+1][i+0] == '#', ABC[j+1][i+1] == '#', ABC[j+2][i+0] == '#', ABC[j+2][i+1] == '#', x, y)

    def betu(self, c, x=0):
        honnan = ABC
        i = 6*(ord(c) - ord('A'))
        if c == ' ':
            honnan = SZOKOZ
            i = 0
        if c >= 'a' and c <= 'z':
            honnan = abc
            i = 6*(ord(c) - ord('a'))
        if c >= '0' and c <= '9':
            honnan = SZAKECE
            i = 6*(ord(c) - ord('0'))
        bf = self.betudarab(honnan, i, 0, x+0, 2)
        ba = self.betudarab(honnan, i, 3, x+0, 0)
        kf = self.betudarab(honnan, i+2, 0, x+1, 2)
        ka = self.betudarab(honnan, i+2, 3, x+1, 0)
        jf = self.betudarab(honnan, i+4, 0, x+2, 2)
        ja = self.betudarab(honnan, i+4, 3, x+2, 0)
        return bf + ba + kf + ka + jf + ja
            
    def szoveg(self, s):
        result = []
        for i in enumerate(s):
            result += self.betu(i[1], 3*i[0])
        return result


    def onCommand(self, sender, command, label, args):
        if isinstance(sender, Player):
            if command.name == "bannertext":
                commands = self.szoveg(' '.join(args))
                for c in commands:
                    sender.chat("/"+c)
                return True
