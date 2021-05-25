
using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using System.Globalization;

namespace CreateImage
{
    class LineComplete
    {
        /// <remarks>
        /// https://stackoverflow.com/a/8946847/1188513
        /// </remarks>>

        private IEnumerable<string> directory;
        private char seperator;
        public LineComplete(IEnumerable<string> directoryValues, char sep)
        {
            directory = directoryValues;
            seperator = sep;
        }

        public string ReadLine()
        {
            List<string> lineText = new List<string> { };
            StringBuilder builder = new StringBuilder();
            ConsoleKeyInfo input = Console.ReadKey(intercept: true);

            while (input.Key != ConsoleKey.Enter)
            {
                if (input.Key == ConsoleKey.Tab)
                {
                    HandleTabInput(builder, directory, lineText);
                }
                else
                {
                    if (HandleKeyInput(builder, input, lineText) == seperator)
                    {
                        lineText.Add(builder.ToString());
                        builder.Clear();
                    }
                }
                input = Console.ReadKey(intercept: true);
            }
            lineText.Add(builder.ToString());
            return string.Join(seperator.ToString(), lineText);
        }


        private static void ClearCurrentLine()
        {
            int currentLine = Console.CursorTop;
            Console.SetCursorPosition(0, Console.CursorTop);
            Console.Write("".PadRight(Console.BufferWidth));
            Console.SetCursorPosition(0, currentLine);

        }

        private void HandleTabInput(StringBuilder builder, IEnumerable<string> data, List<string> lineText)
        {
            string match = data.FirstOrDefault(item => item != builder.ToString() && item.StartsWith(builder.ToString(), StringComparison.Ordinal));

            if (string.IsNullOrEmpty(match))
            {
                return;
            }

            ClearCurrentLine();
            builder.Clear();

            if (lineText.Count > 0)
            {
                Console.Write(string.Join(seperator.ToString(), lineText) + seperator + match);
            }
            else
            {
                Console.Write(match);
            }

            builder.Append(match);
        }

        private char HandleKeyInput(StringBuilder builder, ConsoleKeyInfo input, List<string> lineText)
        {
            int vk = (int)input.Key;
            if (input.Key == ConsoleKey.Backspace && builder.ToString().Length > 0)
            {
                builder.Remove(builder.Length - 1, 1);
                ClearCurrentLine();

                if (lineText.Count > 0)
                {
                    Console.Write(string.Join(seperator.ToString(), lineText) + seperator + builder.ToString());
                }
                else
                {
                    Console.Write(builder.ToString());
                }
            }
            else if ((vk >= 0x30 && vk <= 0x39) // numbers
                  || (vk >= 0x41 && vk <= 0x5A) // letters
                  || (vk >= 0x60 && vk <= 0x69) // numpad
                  || (vk >= 0xBA && vk <= 0xC0) // VK_OEM_1, VK_OEM_PLUS, VK_OEM_COMMA, VK_OEM_MINUS, VK_OEM_PERIOD, VK_OEM_2, VK_OEM_3
                  || (vk >= 0xDB && vk <= 0xDE) // VK_OEM_4, VK_OEM_5, VK_OEM_6, VK_OEM_7
                  || vk == 0x20) // spacebar // https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
            {
                char key = input.KeyChar;

                if (key != seperator)
                {
                    builder.Append(key);
                }
                Console.Write(key);
            }
            else if (lineText.Count > 0 && input.Key == ConsoleKey.Backspace)
            {
                ClearCurrentLine();
                Console.Write(string.Join(seperator.ToString(), lineText));
                builder.Append(lineText.Last());
                lineText.RemoveAt(lineText.Count - 1);

            }
            return input.KeyChar;
        }
    }
}