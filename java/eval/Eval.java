import org.bukkit.Bukkit;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;

public class Eval extends JavaPlugin {
    @Override
    public void onEnable() {
    }

    @Override    
    public void onDisable() {
    }
    
    int pow(int a, int b) {
        if (b <= 0) return 1;
        return a * pow(a, b-1);
    }
    
    int eval(String exp) {
        int number = 0;
        int i = 0;
        if (exp.charAt(0) == '(') {
            int depth = 1;
            while (depth > 0) {
                ++i;
                if (exp.charAt(i) == '(') {
                    ++depth;
                    continue;
                }
                if (exp.charAt(i) == ')') {
                    --depth;
                    continue;
                }
            }
            ++i;
            number = eval(exp.substring(1, i-1));
        } else {
            char c;
            while (i < exp.length()) {
                c = exp.charAt(i);
                int digit = ((int) c) - ((int) '0');
                if (digit < 0 || digit > 9) break;
                number = 10 * number + digit;
                ++i; 
            }
        }
        if (i == exp.length()) {
            return number;
        }
        char muvelet = exp.charAt(i);
        int rest = eval(exp.substring(i+1));
        switch (muvelet) {
            case '+': return number + rest;
            case '-': return number - rest;
            case '*': return number * rest;
            case '/': return number / rest;
            case '^': return pow(number, rest);
        }
        return -1;
    }
    
    @Override
    public boolean onCommand(CommandSender sender, Command command, String commandName, String[] args) {
        if (commandName.equals("eval")) {
            helper2 h = new helper2();
            String sor = h.getFirstLine((Player) sender);
            sender.sendMessage("First line: '" + sor + "'");
            try {
                if (sor != null) {
                    int result = eval(sor);
                    sender.sendMessage("Result: " + result);
                    h.setLastLine((Player) sender, "" + result);
                }
            } catch (Exception e) {
                sender.sendMessage("Evaluation error");
            }
            return true;
        }
        return false;
    }
}
