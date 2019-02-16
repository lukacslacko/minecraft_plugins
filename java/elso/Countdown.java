import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.command.Command;
import org.bukkit.entity.Player;
import org.bukkit.Material;

public class Countdown implements Runnable {
    private JavaPlugin plugin;
    private int times;
    private Player player;
    private int x;
    private int y;
    private int z;
    private Material material;
        
    Countdown(JavaPlugin plugin, Player player, Material material, int x, int y, int z, int times) {
        this.plugin = plugin;
        this.times = times;
        this.player = player;
        this.material = material;
        this.x = x;
        this.y = y;
        this.z = z;
    }
        
    @Override
    public void run() {
        player.getWorld().getBlockAt(x,y,z).setType(material);
        Bukkit.broadcastMessage("" + times);
        if (times > 0) {
            plugin.getServer().getScheduler().runTaskLater(plugin, new Countdown(plugin, player, material, x, y+1, z, times - 1), 20);
        }
    }
}
