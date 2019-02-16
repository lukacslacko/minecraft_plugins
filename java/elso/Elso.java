import org.bukkit.Bukkit;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;

public class Elso extends JavaPlugin {
    @Override
    public void onEnable() {
        this.getLogger().info("Hello world!");
    }

    @Override    
    public void onDisable() {
    }
    
    @Override
    public boolean onCommand(CommandSender sender, Command command, String commandName, String[] args) {
        if (commandName.equals("Elso")) {
            Bukkit.broadcastMessage("Hello world!");
            return true;
        }
        if (commandName.equals("vissza")) {
            String szoveg = String.join(" ", args);
            Bukkit.broadcastMessage(new StringBuilder(szoveg).reverse().toString());
            return true;
        }
        if (commandName.equals("noveszt")) {
            // Milyen blokkra nezek?
            // Masodpercenkent egyet lerakni ugyanabbol.
            Player player = (Player) sender;
            Blokk blokk = new helper().getBlock(player);
            getServer().getScheduler().runTaskLater(
                this, new Countdown(
                    this, player, blokk.material, blokk.x, blokk.y, blokk.z, 10), 20);
            return true;
        }
        return false;
    }
}
