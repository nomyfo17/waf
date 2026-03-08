import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class InteractiveConsole {
    private static final Scanner SCANNER = new Scanner(System.in);
    private static final List<String> history = new ArrayList<>();

    public static void main(String[] args) {
        while (true) {
            while (true) {
                System.out.print("🥞 </> (  ");
                String command = SCANNER.nextLine().trim();
                if ("run".equals(command)) {
                    System.out.println("</> (🥞) -1/2-");
                    break;
                } else if (command.contains("name") || "clear".equals(command)) {
                    if ("clear".equals(command)) printClearAnimation();
                    history.add(command);
                    break;
                } else {
                    history.add(command);
                }
            }

            System.out.println("</> (🥞) -  ");
            for (String entry : history) {
                if (history.contains("txt")) System.out.println("</>  " + entry);
                if (history.contains("hw")) System.out.println("</>  Hello World!");
                if (history.contains("clear")) {
                    history.clear();
                    clearConsole();
                    System.out.println("</>  history cleared");
                    break;
                }
                if (history.contains("option")) {
                    showOptions();
                    break;
                }
                if (history.contains("name")) System.out.println("code or txt");
            }

            sleepSilently(200);
            List<String> fullCode = new ArrayList<>();
            while (true) {
                System.out.print(" -  ");
                String line = SCANNER.nextLine();
                if ("save".equals(line)) break;
                fullCode.add(line);
            }

            System.out.print("file name -  ");
            String fileName = SCANNER.nextLine().trim();
            try (FileWriter writer = new FileWriter(fileName, true)) {
                for (String line : fullCode) writer.write(line + System.lineSeparator());
                System.out.println("file successfully saved!");
            } catch (IOException e) {
                System.err.println("Error: " + e.getMessage());
            }
        }
    }

    private static void printClearAnimation() {
        for (String frame : new String[]{".  ", ".. ", "...", ".  ", ".. ", "..."}) {
            System.out.println(frame);
            sleepSilently(500);
        }
    }

    private static void showOptions() {
        history.clear();
        String[] msgs = {"txt = what you type back", "hw = print Hello World", "clear = clear commands", "search = command vocab", "name = file a new file", "save = save a file"};
        for (String msg : msgs) {
            System.out.println("</>  " + msg);
            sleepSilently(3000);
        }
    }

    private static void clearConsole() {
        try {
            if (System.getProperty("os.name").startsWith("Windows")) new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            else System.out.print("\033[H\033[2J");
        } catch (Exception ignored) {}
    }

    private static void sleepSilently(long millis) {
        try { Thread.sleep(millis); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    }
}
