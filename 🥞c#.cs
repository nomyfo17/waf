using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;

namespace PancakeConsoleApp
{
    class Program
    {
        static void Main()
        {
            var commandHistory = new List<string>();

            while (true) // Main loop
            {
                // ----- Collect commands until "run" or a break condition -----
                while (true)
                {
                    Console.Write("🥞 </> (  ");
                    string command = Console.ReadLine() ?? string.Empty;

                    if (command == "run")
                    {
                        Console.WriteLine("</> (🥞) -1/2-");
                        break; // exit inner command‑collecting loop
                    }
                    else if (command.Contains("name"))
                    {
                        commandHistory.Add(command);
                        break;
                    }
                    else if (command == "clear")
                    {
                        // simulate the animated clear sequence from the Python script
                        PrintWithDelay(".  ");
                        PrintWithDelay(".. ");
                        PrintWithDelay("...");
                        PrintWithDelay(".  ");
                        PrintWithDelay(".. ");
                        PrintWithDelay("...");
                        commandHistory.Add(command);
                        break;
                    }
                    else
                    {
                        commandHistory.Add(command);
                    }
                }

                Console.WriteLine("</> (🥞) -  ");

                // ----- Process the accumulated history -----
                foreach (var _ in commandHistory) // iterate just to mirror the original structure
                {
                    // echo all stored commands when any contain "txt"
                    if (commandHistory.Any(s => s.Contains("txt")))
                    {
                        foreach (var cmd in commandHistory)
                        {
                            Console.WriteLine("</>  " + cmd);
                        }
                    }

                    // print Hello World when any command contains "hw"
                    if (commandHistory.Any(s => s.Contains("hw")))
                    {
                        Console.WriteLine("</>  Hello World!");
                    }

                    // clear history and console when any command contains "clear"
                    if (commandHistory.Any(s => s.Contains("clear")))
                    {
                        commandHistory.Clear();
                        Console.Clear();
                        Console.WriteLine("</>  history cleared");
                    }

                    // show option help text when any command contains "option"
                    if (commandHistory.Any(s => s.Contains("option")))
                    {
                        commandHistory.Clear();

                        var helpLines = new[]
                        {
                            "txt = what you type will type back",
                            "hw = print Hello World",
                            "clear = clear past commands",
                            "search = command vocab",
                            "name = file a new file",
                            "save = save a file must be under name"
                        };

                        foreach (var line in helpLines)
                        {
                            Console.WriteLine("</>  " + line);
                            Thread.Sleep(3000);
                        }
                    }

                    // auxiliary message when any command contains "name"
                    if (commandHistory.Any(s => s.Contains("name")))
                    {
                        Console.WriteLine("code or txt");
                    }
                }

                Thread.Sleep(200);

                // ----- Collect lines of code to be saved -----
                var fullCodeLines = new List<string>();
                while (true)
                {
                    Thread.Sleep(500);
                    Console.Write(" -  ");
                    string line = Console.ReadLine() ?? string.Empty;

                    if (line == "save")
                    {
                        break;
                    }
                    else
                    {
                        fullCodeLines.Add(line);
                    }
                }

                Thread.Sleep(200);
                Console.Write("file name -  ");
                string fileName = Console.ReadLine() ?? "output.txt";

                // ----- Write collected lines to the specified file -----
                try
                {
                    using (var writer = new StreamWriter(fileName, append: true))
                    {
                        foreach (var line in fullCodeLines)
                        {
                            writer.WriteLine(line);
                        }
                    }
                    Console.WriteLine("file successfully saved!");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error saving file: {ex.Message}");
                }
            }
        }

        /// <summary>
        /// Helper that prints a line then waits 500 ms,
        /// replicating the animated clear sequence from the original script.
        /// </summary>
        private static void PrintWithDelay(string text)
        {
            Console.WriteLine(text);
            Thread.Sleep(500);
        }
    }
}
