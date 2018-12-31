# Returns:
#   list of rows. Every row is [yellow block, [blue blocks]], every block is [x,y,z].
# spz
# kpx
def blocks(sender, Material):
    ered = []
    w = sender.getWorld()
    block = sender.getTargetBlock(None,100)
    if not block.getType() == Material.YELLOW_WOOL:
        return ""
    while block.getType() == Material.YELLOW_WOOL:
        ered.append([[block.getLocation().getX(),block.getLocation().getY(),block.getLocation().getZ()]])
        for i in range(100):
            h = block.getLocation()
            h.setX(h.getX()+i+1)
            block1 = w.getBlockAt(h)
            ered[len(ered)-1].append([])
            if block1.getType() == Material.LIGHT_BLUE_WOOL:
                ered[len(ered)-1][1].append([block1.getLocation().getX(),block1.getLocation().getY(),block1.getLocation().getZ()])
            else:
                del ered[len(ered)-1][len(ered[len(ered)-1])-1]
        h = block.getLocation()
        h.setZ(h.getZ()+1)
        block = w.getBlockAt(h)
    return ered
