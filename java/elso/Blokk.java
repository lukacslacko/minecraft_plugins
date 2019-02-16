import org.bukkit.Material;

class Blokk {
    public int x;
    public int y;
    public int z;
    public Material material;
    
    public Blokk(Material material, int x, int y, int z) {
        this.material = material;
        this.x = x;
        this.y = y;
        this.z = z;
    }
}
