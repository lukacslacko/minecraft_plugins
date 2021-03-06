import org.bukkit.Bukkit;
import org.bukkit.plugin.PluginManager;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.entity.Player;
import org.bukkit.event.Listener;
import org.bukkit.event.block.BlockPlaceEvent;
import org.bukkit.event.player.PlayerMoveEvent;
import org.bukkit.event.EventHandler;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;

public class Stopper extends JavaPlugin {
    @Override
    public void onEnable() {
        System.out.println("onEnable");
        PluginManager pluginManager = this.getServer().getPluginManager();
        MoveListener moveListener = new MoveListener(this);
        pluginManager.registerEvents(moveListener, this);
    }
    
    @Override
    public void onDisable() {}
    
    public class MoveListener implements Listener {
        private Stopper stopper;
        
        public MoveListener(Stopper stopper) { this.stopper = stopper; }
    
        @EventHandler
        public void onEvent(PlayerMoveEvent event) {
            Bukkit.broadcastMessage("PlayerMoveEvent");
            Player player = event.getPlayer();
            int x = (int) player.getLocation().getX();
            int z = (int) player.getLocation().getZ();
            player.sendMessage("Itt vagy: " + x + " " + z);
            if (x == stopper.startX && z == stopper.startZ) {
                player.sendMessage("Start");
            }
            if (x == stopper.celX && z == stopper.celZ) {
                player.sendMessage("Cel");
            }
        }
        
        @EventHandler
        public void onBlockPlace(BlockPlaceEvent event) {	
            Bukkit.broadcastMessage("Block placed");
        }
    }
    
    public int startX, startZ, celX, celZ;
    
    @Override
    public boolean onCommand(CommandSender sender, Command command, String commandName, String[] args) {
        Player player = (Player) sender;
        if (commandName.equals("startmezo")) {
            startX = (int) player.getLocation().getX();
            startZ = (int) player.getLocation().getZ();
        }
        if (commandName.equals("celmezo")) {
            celX = (int) player.getLocation().getX();
            celZ = (int) player.getLocation().getZ();
        }
        if (commandName.equals("stopper")) {
            player.sendMessage("Start " + startX + " " + startZ + " cel " + celX + " " + celZ);
        }
        
        return true;
    } 
}
