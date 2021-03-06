﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Text.RegularExpressions;
using CreateImage.Dithering;

namespace CreateImage
{
    class Program
    {
        public struct AskGetDitherResult
        {
            public IErrorDiffusion DitherAlgorithm;
            public IPixelTransform Transform;
            public byte Threshold;
        }

        public static int closestColor2(List<Color> colors, Color target)
        {
            var colorDiffs = colors.Select(n => ColorDiff(n, target)).Min(n => n);
            return colors.FindIndex(n => ColorDiff(n, target) == colorDiffs);
        }

        // distance in RGB space
        public static int ColorDiff(Color c1, Color c2)
        {
            return (int)Math.Sqrt((c1.R - c2.R) * (c1.R - c2.R)
                                   + (c1.G - c2.G) * (c1.G - c2.G)
                                   + (c1.B - c2.B) * (c1.B - c2.B));
        }

        public static string GetFileName()
        {
            string fileName;
            LineComplete ln = new LineComplete(
                new DirectoryInfo(Directory.GetCurrentDirectory()).EnumerateFiles(".", SearchOption.TopDirectoryOnly).Select(x => x.Name).ToList(), '|');
            while (true)
            {
                Console.WriteLine("enter file name");
                fileName = ln.ReadLine();

                if (File.Exists(fileName))
                {
                    return fileName;
                    //return Path.GetFileNameWithoutExtension(fileName) + "_convert.png";
                }
            }
        }

        public static AskGetDitherResult AskGetDithering()
        {
            string input;
            int index = -2;

            AskGetDitherResult result = new AskGetDitherResult();

            while (true)
            {
                Console.WriteLine("\nwould you like to dither the image? (y/n)");
                input = Console.ReadLine().Trim().ToLower();

                if (input == "n")
                    return result;
                
                if (input == "y")
                    break;
            }

            while (true)
            {
                Console.WriteLine("\nplease input the number of the pixel transform you'd like to use (-1 to cancel)");
                Console.WriteLine(
                    "\t0 : Monochrome\n\t" + 
                    "1 : Color 232\n\t" 
                    );
                input = Console.ReadLine().Trim().ToLower();

                if(int.TryParse(input, out index))
                {
                    if (index == -1)
                        return result;

                    if (index == 0)
                    {
                        byte i = 128;
                        while (true)
                        {
                            Console.WriteLine("input the color threshold (0 - 255)");
                            input = Console.ReadLine().Trim().ToLower();

                            if(byte.TryParse(input, out i))
                            {
                                i = ((int)i).ToByte();
                                break;
                            }
                        }

                        result.Threshold = i;
                        result.Transform = GetPixelTransform(1, i);
                        break;
                    }

                    if(index > 0 && index < 4)
                    {
                        result.Transform = GetPixelTransform(index.ToByte(), 0);
                        break;
                    }
                }
            }

            while (true)
            {
                Console.WriteLine("\nplease input the number of the dithering algorithm you'd like to use (-1 to cancel)");
                Console.WriteLine(
                    "\t0 : Floyd Steinberg\n\t" +
                    "1 : Burks\n\t" +
                    "2 : Jarvis Judice Ninke\n\t" +
                    "3 : Stucki\n\t" +
                    "4 : Sierra 3\n\t" +
                    "5 : Sierra 2\n\t" +
                    "6 : Sierra Lite\n\t" +
                    "7 : Atkinson\n\t" +
                    "8 : Random\n\t" +
                    "9 : Bayer 2\n\t" +
                    "10 : Bayer 3\n\t" +
                    "11 : Bayer 4\n\t" +
                    "12 : Bayer 8\n"
                    );
                input = Console.ReadLine().ToLower().Trim();

                if (int.TryParse(input, out index))
                {
                    if (index == -1)
                        return result;

                    if (index < 13 && index > -1)
                    {
                        result.DitherAlgorithm = GetDitheringInstance(index.ToByte());
                        break;
                    }
                }
            }

            return result;
        }

        public static Size AskGetSize()
        {
            string input;

            while (true)
            {
                Console.WriteLine("\nwould you like to resize the image before converting? (y/n)");
                input = Console.ReadLine().Trim().ToLower();

                if (input == "n")
                    return Size.Empty;

                if (input == "y")
                    break;
            }

            while (true)
            {
                Console.WriteLine("\nplease input the size you'd like");
                input = Console.ReadLine().Trim().ToLower();
                Size s = ParseSize(input);

                if (s != Size.Empty)
                    return s;
            }
        }

        public static bool AskCreateScanFile()
        {
            string input;

            while (true)
            {
                Console.WriteLine("do you want to create a scan file? (y/n)");
                input = Console.ReadLine().Trim().ToLower();

                if (input == "n")
                    return false;
                if (input == "y")
                    return true;
            }
        }

        public static Bitmap LoadImage(string path)
        {
            if (string.IsNullOrEmpty(path))
                return null;

            if (!File.Exists(path))
                return null;

            try
            {
                return (Bitmap)Image.FromStream(new MemoryStream(File.ReadAllBytes(path)));
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            return null;
        }

        public static Size ParseSize(string str)
        {
            try
            {
                var a = str.Split(new char[] { 'x' });
                return new Size()
                {
                    Width = int.Parse(a[0]),
                    Height = int.Parse(a[1])
                };
            }
            catch { }
            return Size.Empty;
        }

        public static IErrorDiffusion GetDitheringInstance(byte input)
        {
            switch (input)
            {
                default:
                    return null;
                case 0:
                    return new FloydSteinbergDithering();
                case 1:
                    return new BurksDithering();
                case 2:
                    return new JarvisJudiceNinkeDithering();
                case 3:
                    return new StuckiDithering();
                case 4:
                    return new Sierra3Dithering();
                case 5:
                    return new Sierra2Dithering();
                case 6:
                    return new SierraLiteDithering();
                case 7:
                    return new AtkinsonDithering();
                case 8:
                    return new RandomDithering();
                case 9:
                    return new Bayer2();
                case 10:
                    return new Bayer3();
                case 11:
                    return new Bayer4();
                case 12:
                    return new Bayer8();
            }
        }

        public static IPixelTransform GetPixelTransform(byte input, byte threshold = 0)
        {
            if (threshold != 0)
                return new MonochromePixelTransform(threshold);

            return new MinecraftMapColorPalettePixelTransform();
            /*switch (input)
            {
                
                case 0:
                    return new SimpleIndexedPalettePixelTransform8();
                case 1:
                    return new SimpleIndexedPalettePixelTransform16();
                default:
                case 2:
                    return new SimpleIndexedPalettePixelTransform256();
            }*/
        }

        public static void CreateScanFile(Bitmap data, string outName)
        {
            int count = 0;
            int xpos;
            int ypos;
            List<string> outputList = new List<string> { };

            Console.WriteLine("Scanning...");

            for (int x = 0; x < (int)data.Width / 32; x++)
                for (int y = 0; y < (int)data.Height / 32; y++)
                {
                    for (int i = 0; i < 32; i++)
                    {
                        xpos = i + (32 * x);
                        for (int ii = 0; ii < 32; ii++)
                        {
                            ypos = ii + (32 * y);
                            outputList.Add(dyeNameList[closestColor2(dye, data.GetPixel(xpos, ypos))]);
                        }
                    }

                    count++;
                    using (StreamWriter w = File.AppendText(outName + "_scan.txt"))
                    {
                        if (count == 1)
                            w.WriteLine($"|${count}$|");
                        else
                            w.WriteLine($"\n\n|${count}$|");

                        int loopNums = 1;
                        foreach (string col in outputList)
                        {
                            if (loopNums == 32)
                            {
                                w.Write($"|{col}\n");
                                loopNums = 0;
                            }
                            else if (loopNums == 1)
                            {
                                w.Write($"{col}");
                            }
                            else
                            {
                                w.Write($"|{col}");
                            }
                            loopNums++;
                        }
                    }
                    outputList.Clear();
                }
        }

        static void Main(string[] args)
        {
            string fileName, outName;
            bool createScanFile = false;
            Size autoSizeOutImage = Size.Empty;
            AskGetDitherResult dither = new AskGetDitherResult();

            if (args.Length > 0)
            {
                fileName = args[0];
                if (File.Exists(fileName))
                {
                    outName = Path.GetFileNameWithoutExtension(fileName) + "_convert.png";
                }
                else
                {
                    fileName = GetFileName();
                    outName = Path.GetFileNameWithoutExtension(fileName) + "_convert.png";
                }

                switch (args.Length)
                {
                    case 2:
                        autoSizeOutImage = ParseSize(args[1]);
                        break;
                    case 3:
                        int w = -1, h = -1;

                        autoSizeOutImage = new Size(-1, -1);
                        if (int.TryParse(args[1], out w))
                        {
                            autoSizeOutImage.Width = w;
                        }
                        if (int.TryParse(args[2], out h))
                        {
                            autoSizeOutImage.Height = h;
                        }

                        if (autoSizeOutImage.Width == -1 || autoSizeOutImage.Height == -1)
                        {
                            autoSizeOutImage = Size.Empty;
                            break;
                        }
                        break;
                }
            }
            else
            {
                fileName = GetFileName();
                outName = Path.GetFileNameWithoutExtension(fileName) + "_convert.png";
                Console.WriteLine("");
                autoSizeOutImage = AskGetSize();
                Console.WriteLine("");
                dither = AskGetDithering();
                createScanFile = AskCreateScanFile();
            }

            Bitmap data = LoadImage(fileName);

            if (data == null)
            {
                Console.WriteLine("there was an error loading image, program will exit");
                Console.ReadLine();
                return;
            }

            if (autoSizeOutImage != Size.Empty)
            {
                Bitmap newScaled = new Bitmap(autoSizeOutImage.Width, autoSizeOutImage.Height);

                using (Graphics g = Graphics.FromImage(newScaled))
                {
                    g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                    g.DrawImage(data, new Rectangle(0, 0, autoSizeOutImage.Width, autoSizeOutImage.Height), new Rectangle(0, 0, data.Width, data.Height), GraphicsUnit.Pixel);
                }

                data.Dispose();
                data = newScaled;
            }

            

            Console.WriteLine("\nconverting...");

            // user wants dithering
            if (dither.DitherAlgorithm != null)
            {
                // request image tansform disposes of the input image so we don't need to
                // do anythign special to dispose of the unused data
                using (Bitmap bmp = DitherHelper.RequestImageTransform(data, dither.Transform, dither.DitherAlgorithm))
                {
                    if (createScanFile)
                    {
                        CreateScanFile(bmp, outName);
                    }
                    bmp.Save(outName, ImageFormat.Png);
                }
            }
            else
            {
                Color color;
                Bitmap newBitmap = new Bitmap(data.Width, data.Height);

                using (Graphics g = Graphics.FromImage(newBitmap))
                {
                    for (int x = 0; x < data.Width; x++)
                        for (int y = 0; y < data.Height; y++)
                        {
                            color = data.GetPixel(x, y);
                            newBitmap.SetPixel(x, y, dye[closestColor2(dye, color)]);
                        }

                    g.DrawImage(newBitmap, new Point(0, 0));

                    
                }

                if (createScanFile)
                {
                    CreateScanFile(newBitmap, outName);
                }
                newBitmap.Save(outName, ImageFormat.Png);
                data.Dispose();
            }

            Console.WriteLine("done.\n");
            Console.WriteLine(outName);
            //Console.ReadLine();

        }



        public static List<Color> dye = new List<Color>
        {
            Color.FromArgb(75, 75, 75),
            Color.FromArgb(64, 64, 64),
            Color.FromArgb(52, 52, 52),
            Color.FromArgb(39, 39, 39),
            Color.FromArgb(37, 22, 16),
            Color.FromArgb(31, 18, 13),
            Color.FromArgb(26, 15, 11),
            Color.FromArgb(19, 11, 8),
            Color.FromArgb(25, 25, 25),
            Color.FromArgb(21, 21, 21),
            Color.FromArgb(17, 17, 17),
            Color.FromArgb(13, 13, 13),
            Color.FromArgb(86, 91, 91),
            Color.FromArgb(74, 78, 78),
            Color.FromArgb(60, 63, 63),
            Color.FromArgb(45, 47, 47),
            Color.FromArgb(111, 111, 111),
            Color.FromArgb(95, 95, 95),
            Color.FromArgb(78, 78, 78),
            Color.FromArgb(58, 58, 58),
            Color.FromArgb(151, 151, 151),
            Color.FromArgb(130, 130, 130),
            Color.FromArgb(107, 107, 107),
            Color.FromArgb(80, 80, 80),
            Color.FromArgb(165, 165, 165),
            Color.FromArgb(142, 142, 142),
            Color.FromArgb(116, 116, 116),
            Color.FromArgb(87, 87, 87),
            Color.FromArgb(197, 197, 197),
            Color.FromArgb(169, 169, 169),
            Color.FromArgb(138, 138, 138),
            Color.FromArgb(104, 104, 104),
            Color.FromArgb(252, 249, 242),
            Color.FromArgb(217, 214, 208),
            Color.FromArgb(178, 175, 170),
            Color.FromArgb(133, 131, 127),
            Color.FromArgb(252, 252, 252),
            Color.FromArgb(217, 217, 217),
            Color.FromArgb(178, 178, 178),
            Color.FromArgb(133, 133, 133),
            Color.FromArgb(162, 166, 182),
            Color.FromArgb(139, 142, 156),
            Color.FromArgb(114, 117, 127),
            Color.FromArgb(85, 87, 96),
            Color.FromArgb(252, 0, 0),
            Color.FromArgb(217, 0, 0),
            Color.FromArgb(178, 0, 0),
            Color.FromArgb(133, 0, 0),
            Color.FromArgb(101, 125, 50),
            Color.FromArgb(87, 108, 43),
            Color.FromArgb(71, 88, 35),
            Color.FromArgb(53, 66, 27),
            Color.FromArgb(101, 75, 50),
            Color.FromArgb(87, 64, 43),
            Color.FromArgb(71, 52, 35),
            Color.FromArgb(53, 39, 27),
            Color.FromArgb(50, 75, 175),
            Color.FromArgb(43, 64, 151),
            Color.FromArgb(36, 52, 123),
            Color.FromArgb(27, 39, 93),
            Color.FromArgb(125, 62, 175),
            Color.FromArgb(108, 53, 151),
            Color.FromArgb(88, 43, 123),
            Color.FromArgb(66, 33, 93),
            Color.FromArgb(75, 125, 151),
            Color.FromArgb(64, 108, 130),
            Color.FromArgb(52, 88, 106),
            Color.FromArgb(39, 66, 80),
            Color.FromArgb(239, 125, 162),
            Color.FromArgb(206, 108, 140),
            Color.FromArgb(168, 88, 114),
            Color.FromArgb(126, 66, 86),
            Color.FromArgb(125, 202, 25),
            Color.FromArgb(108, 174, 21),
            Color.FromArgb(88, 142, 17),
            Color.FromArgb(66, 107, 13),
            Color.FromArgb(225, 225, 50),
            Color.FromArgb(195, 195, 43),
            Color.FromArgb(159, 159, 35),
            Color.FromArgb(120, 120, 27),
            Color.FromArgb(101, 151, 213),
            Color.FromArgb(87, 130, 183),
            Color.FromArgb(71, 107, 150),
            Color.FromArgb(53, 80, 112),
            Color.FromArgb(176, 75, 213),
            Color.FromArgb(151, 64, 183),
            Color.FromArgb(124, 52, 150),
            Color.FromArgb(93, 39, 112),
            Color.FromArgb(213, 125, 50),
            Color.FromArgb(184, 108, 43),
            Color.FromArgb(150, 88, 35),
            Color.FromArgb(113, 66, 27),
            Color.FromArgb(244, 230, 160),
            Color.FromArgb(210, 199, 138),
            Color.FromArgb(172, 162, 113),
            Color.FromArgb(128, 122, 85),
            Color.FromArgb(149, 108, 76),
            Color.FromArgb(128, 93, 65),
            Color.FromArgb(105, 75, 53),
            Color.FromArgb(78, 56, 39),
            Color.FromArgb(111, 2, 0),
            Color.FromArgb(95, 1, 0),
            Color.FromArgb(78, 1, 0),
            Color.FromArgb(58, 1, 0),
            Color.FromArgb(91, 216, 210),
            Color.FromArgb(78, 186, 180),
            Color.FromArgb(63, 152, 148),
            Color.FromArgb(47, 114, 110),
            Color.FromArgb(125, 176, 55),
            Color.FromArgb(108, 151, 47),
            Color.FromArgb(88, 124, 38),
            Color.FromArgb(66, 93, 29),
            Color.FromArgb(247, 235, 76),
            Color.FromArgb(212, 203, 65),
            Color.FromArgb(174, 166, 53),
            Color.FromArgb(130, 125, 39),
            Color.FromArgb(158, 158, 251),
            Color.FromArgb(136, 136, 217),
            Color.FromArgb(111, 111, 177),
            Color.FromArgb(83, 83, 133),
            Color.FromArgb(0, 123, 0),
            Color.FromArgb(0, 105, 0),
            Color.FromArgb(0, 86, 0),
            Color.FromArgb(0, 64, 0),
            Color.FromArgb(63, 63, 251),
            Color.FromArgb(5, 54, 217),
            Color.FromArgb(44, 44, 177),
            Color.FromArgb(33, 33, 133),
            Color.FromArgb(141, 118, 71),
            Color.FromArgb(122, 101, 61),
            Color.FromArgb(99, 83, 49),
            Color.FromArgb(74, 62, 37),
            Color.FromArgb(151, 50, 50),
            Color.FromArgb(130, 43, 43),
            Color.FromArgb(107, 36, 35),
            Color.FromArgb(80, 27, 27),
            Color.FromArgb(73, 126, 251),
            Color.FromArgb(62, 109, 217),
            Color.FromArgb(51, 89, 117),
            Color.FromArgb(39, 66, 133),
            Color.FromArgb(0, 214, 57),
            Color.FromArgb(0, 185, 49),
            Color.FromArgb(0, 151, 39),
            Color.FromArgb(0, 113, 30),
            Color.FromArgb(127, 85, 48),
            Color.FromArgb(110, 73, 41),
            Color.FromArgb(90, 59, 33),
            Color.FromArgb(67, 44, 25),
            Color.FromArgb(207, 175, 158),
            Color.FromArgb(178, 150, 136),
            Color.FromArgb(145, 123, 111),
            Color.FromArgb(109, 92, 84),
            Color.FromArgb(157, 81, 35),
            Color.FromArgb(135, 69, 31),
            Color.FromArgb(111, 56, 25),
            Color.FromArgb(83, 42, 19),
            Color.FromArgb(147, 86, 106),
            Color.FromArgb(126, 74, 92),
            Color.FromArgb(104, 60, 75),
            Color.FromArgb(77, 45, 56),
            Color.FromArgb(111, 107, 136),
            Color.FromArgb(95, 92, 117),
            Color.FromArgb(78, 75, 95),
            Color.FromArgb(58, 56, 72),
            Color.FromArgb(184, 131, 35),
            Color.FromArgb(158, 113, 31),
            Color.FromArgb(129, 92, 25),
            Color.FromArgb(97, 69, 19),
            Color.FromArgb(102, 116, 52),
            Color.FromArgb(87, 99, 44),
            Color.FromArgb(71, 81, 36),
            Color.FromArgb(53, 60, 28),
            Color.FromArgb(158, 76, 77),
            Color.FromArgb(136, 65, 66),
            Color.FromArgb(111, 53, 54),
            Color.FromArgb(84, 39, 40),
            Color.FromArgb(56, 40, 34),
            Color.FromArgb(48, 35, 30),
            Color.FromArgb(39, 28, 24),
            Color.FromArgb(30, 21, 18),
            Color.FromArgb(133, 106, 96),
            Color.FromArgb(115, 91, 83),
            Color.FromArgb(94, 74, 68),
            Color.FromArgb(70, 55, 50),
            Color.FromArgb(121, 72, 87),
            Color.FromArgb(104, 61, 74),
            Color.FromArgb(85, 50, 61),
            Color.FromArgb(63, 38, 45),
            Color.FromArgb(75, 61, 91),
            Color.FromArgb(64, 52, 78),
            Color.FromArgb(52, 42, 63),
            Color.FromArgb(39, 32, 47),
            Color.FromArgb(75, 49, 34),
            Color.FromArgb(64, 42, 30),
            Color.FromArgb(52, 35, 24),
            Color.FromArgb(39, 26, 18),
            Color.FromArgb(75, 81, 41),
            Color.FromArgb(64, 69, 35),
            Color.FromArgb(52, 56, 29),
            Color.FromArgb(39, 42, 22),
            Color.FromArgb(140, 59, 45),
            Color.FromArgb(121, 50, 38),
            Color.FromArgb(99, 41, 31),
            Color.FromArgb(74, 31, 24),
            Color.FromArgb(20, 178, 129),
            Color.FromArgb(17, 153, 111),
            Color.FromArgb(14, 125, 90),
            Color.FromArgb(10, 94, 68),
            Color.FromArgb(57, 140, 136),
            Color.FromArgb(49, 121, 117),
            Color.FromArgb(39, 99, 95),
            Color.FromArgb(30, 74, 72),
            Color.FromArgb(85, 43, 60),
            Color.FromArgb(73, 37, 51),
            Color.FromArgb(59, 31, 42),
            Color.FromArgb(44, 23, 31),
            Color.FromArgb(22, 125, 130),
            Color.FromArgb(18, 107, 112),
            Color.FromArgb(15, 87, 91),
            Color.FromArgb(11, 65, 68),
            Color.FromArgb(146, 62, 94),
            Color.FromArgb(125, 53, 81),
            Color.FromArgb(103, 43, 66),
            Color.FromArgb(77, 33, 50),
            Color.FromArgb(91, 25, 28),
            Color.FromArgb(78, 21, 24),
            Color.FromArgb(131, 33, 33),// was 63, 17, 19 changed due to typo
            Color.FromArgb(99, 25, 25), // was 47, 13, 15 changed due to typo
            Color.FromArgb(187, 47, 48),
            Color.FromArgb(161, 40, 41),
            Color.FromArgb(131, 33, 33),
            Color.FromArgb(99, 25, 24)
        };
        public static string[] dyeNameList = new string[232]
        {
            "flin+",
            "flin",
            "flin-",
            "flin--",
            "char+",
            "char",
            "char-",
            "char--",
            "ink+",
            "ink",
            "ink-",
            "ink--",
            "iron+",
            "iron",
            "iron-",
            "iron--",
            "ghas+",
            "ghas",
            "ghas-",
            "ghas--",
            "gunp+",
            "gunp",
            "gunp-",
            "gunp--",
            "ligh+",
            "ligh",
            "ligh-",
            "ligh--",
            "cobw+",
            "cobw",
            "cobw-",
            "cobw--",
            "bone+",
            "bone",
            "bone-",
            "bone--",
            "snow+",
            "snow",
            "snow-",
            "snow--",
            "grey+",
            "grey",
            "grey-",
            "grey--",
            "red+",
            "red",
            "red-",
            "red--",
            "cact+",
            "cact",
            "cact-",
            "cact--",
            "coco+",
            "coco",
            "coco-",
            "coco--",
            "lapi+",
            "lapi",
            "lapi-",
            "lapi--",
            "pdye+",
            "pdye",
            "pdye-",
            "pdye--",
            "cyan+",
            "cyan",
            "cyan-",
            "cyan--",
            "pink+",
            "pink",
            "pink-",
            "pink--",
            "lime+",
            "lime",
            "lime-",
            "lime--",
            "yell+",
            "yell",
            "yell-",
            "yell--",
            "lblu+",
            "lblu",
            "lblu-",
            "lblu--",
            "mage+",
            "mage",
            "mage-",
            "mage--",
            "oran+",
            "oran",
            "oran-",
            "oran--",
            "pump+",
            "pump",
            "pump-",
            "pump--",
            "melo+",
            "melo",
            "melo-",
            "melo--",
            "wart+",
            "wart",
            "wart-",
            "wart--",
            "pris+",
            "pris",
            "pris-",
            "pris--",
            "gras+",
            "gras",
            "gras-",
            "gras--",
            "gold+",
            "gold",
            "gold-",
            "gold--",
            "ice+",
            "ice",
            "ice-",
            "ice--",
            "leav+",
            "leav",
            "leav-",
            "leav--",
            "lapb+",
            "lapb",
            "lapb-",
            "lapb--",
            "doak+",
            "doak",
            "doak-",
            "doak--",
            "bric+",
            "bric",
            "bric-",
            "bric--",
            "lore+",
            "lore",
            "lore-",
            "lore--",
            "emer+",
            "emer",
            "emer-",
            "emer--",
            "birc+",
            "birc",
            "birc-",
            "birc--",
            "egg+",
            "egg",
            "egg-",
            "egg--",
            "magm+",
            "magm",
            "magm-",
            "magm--",
            "beet+",
            "beet",
            "beet-",
            "beet--",
            "myce+",
            "myce",
            "myce-",
            "myce--",
            "glow+",
            "glow",
            "glow-",
            "glow--",
            "slim+",
            "slim",
            "slim-",
            "slim--",
            "spid+",
            "spid",
            "spid-",
            "spid--",
            "soul+",
            "soul",
            "soul-",
            "soul--",
            "mush+",
            "mush",
            "mush-",
            "mush--",
            "chor+",
            "chor",
            "chor-",
            "chor--",
            "purp+",
            "purp",
            "purp-",
            "purp--",
            "podz+",
            "podz",
            "podz-",
            "podz--",
            "pota+",
            "pota",
            "pota-",
            "pota--",
            "appl+",
            "appl",
            "appl-",
            "appl--",
            "wnyl+",
            "wnyl",
            "wnyl-",
            "wnyl--",
            "wste+",
            "wste",
            "wste-",
            "wste--",
            "whyp+",
            "whyp",
            "whyp-",
            "whyp--",
            "wwar+",
            "wwar",
            "wwar-",
            "wwar--",
            "chyp+",
            "chyp",
            "chyp-",
            "chyp--",
            "cnyl+",
            "cnyl",
            "cnyl-",
            "cnyl--",
            "cste+",
            "cste",
            "cste-",
            "cste--"
        };
    }
}
