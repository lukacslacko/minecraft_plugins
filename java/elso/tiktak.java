import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.command.CommandExecutor;

public class tiktak extends JavaPlugin implements CommandExecutor,Runnable{
    public void onEnable(){
        getServer().getScheduler().runTaskLater(this,this,20);
    }
    public void run(){
        this.getLogger().info("tiktak");
        getServer().getScheduler().runTaskLater(this,this,20);
    }
    public void onDisable(){
    }
}