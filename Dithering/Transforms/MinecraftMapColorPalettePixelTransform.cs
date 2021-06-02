﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CreateImage.Dithering
{
    internal class MinecraftMapColorPalettePixelTransform : SimpleIndexedPalettePixelTransform
    {
        public MinecraftMapColorPalettePixelTransform()
  : base(new[]
         {
               ArgbColor.FromArgb(75, 75, 75),
            ArgbColor.FromArgb(64, 64, 64),
            ArgbColor.FromArgb(52, 52, 52),
            ArgbColor.FromArgb(39, 39, 39),
            ArgbColor.FromArgb(37, 22, 16),
            ArgbColor.FromArgb(31, 18, 13),
            ArgbColor.FromArgb(26, 15, 11),
            ArgbColor.FromArgb(19, 11, 8),
            ArgbColor.FromArgb(25, 25, 25),
            ArgbColor.FromArgb(21, 21, 21),
            ArgbColor.FromArgb(17, 17, 17),
            ArgbColor.FromArgb(13, 13, 13),
            ArgbColor.FromArgb(86, 91, 91),
            ArgbColor.FromArgb(74, 78, 78),
            ArgbColor.FromArgb(60, 63, 63),
            ArgbColor.FromArgb(45, 47, 47),
            ArgbColor.FromArgb(111, 111, 111),
            ArgbColor.FromArgb(95, 95, 95),
            ArgbColor.FromArgb(78, 78, 78),
            ArgbColor.FromArgb(58, 58, 58),
            ArgbColor.FromArgb(151, 151, 151),
            ArgbColor.FromArgb(130, 130, 130),
            ArgbColor.FromArgb(107, 107, 107),
            ArgbColor.FromArgb(80, 80, 80),
            ArgbColor.FromArgb(165, 165, 165),
            ArgbColor.FromArgb(142, 142, 142),
            ArgbColor.FromArgb(116, 116, 116),
            ArgbColor.FromArgb(87, 87, 87),
            ArgbColor.FromArgb(197, 197, 197),
            ArgbColor.FromArgb(169, 169, 169),
            ArgbColor.FromArgb(138, 138, 138),
            ArgbColor.FromArgb(104, 104, 104),
            ArgbColor.FromArgb(252, 249, 242),
            ArgbColor.FromArgb(217, 214, 208),
            ArgbColor.FromArgb(178, 175, 170),
            ArgbColor.FromArgb(133, 131, 127),
            ArgbColor.FromArgb(252, 252, 252),
            ArgbColor.FromArgb(217, 217, 217),
            ArgbColor.FromArgb(178, 178, 178),
            ArgbColor.FromArgb(133, 133, 133),
            ArgbColor.FromArgb(162, 166, 182),
            ArgbColor.FromArgb(139, 142, 156),
            ArgbColor.FromArgb(114, 117, 127),
            ArgbColor.FromArgb(85, 87, 96),
            ArgbColor.FromArgb(252, 0, 0),
            ArgbColor.FromArgb(217, 0, 0),
            ArgbColor.FromArgb(178, 0, 0),
            ArgbColor.FromArgb(133, 0, 0),
            ArgbColor.FromArgb(101, 125, 50),
            ArgbColor.FromArgb(87, 108, 43),
            ArgbColor.FromArgb(71, 88, 35),
            ArgbColor.FromArgb(53, 66, 27),
            ArgbColor.FromArgb(101, 75, 50),
            ArgbColor.FromArgb(87, 64, 43),
            ArgbColor.FromArgb(71, 52, 35),
            ArgbColor.FromArgb(53, 39, 27),
            ArgbColor.FromArgb(50, 75, 175),
            ArgbColor.FromArgb(43, 64, 151),
            ArgbColor.FromArgb(36, 52, 123),
            ArgbColor.FromArgb(27, 39, 93),
            ArgbColor.FromArgb(125, 62, 175),
            ArgbColor.FromArgb(108, 53, 151),
            ArgbColor.FromArgb(88, 43, 123),
            ArgbColor.FromArgb(66, 33, 93),
            ArgbColor.FromArgb(75, 125, 151),
            ArgbColor.FromArgb(64, 108, 130),
            ArgbColor.FromArgb(52, 88, 106),
            ArgbColor.FromArgb(39, 66, 80),
            ArgbColor.FromArgb(239, 125, 162),
            ArgbColor.FromArgb(206, 108, 140),
            ArgbColor.FromArgb(168, 88, 114),
            ArgbColor.FromArgb(126, 66, 86),
            ArgbColor.FromArgb(125, 202, 25),
            ArgbColor.FromArgb(108, 174, 21),
            ArgbColor.FromArgb(88, 142, 17),
            ArgbColor.FromArgb(66, 107, 13),
            ArgbColor.FromArgb(225, 225, 50),
            ArgbColor.FromArgb(195, 195, 43),
            ArgbColor.FromArgb(159, 159, 35),
            ArgbColor.FromArgb(120, 120, 27),
            ArgbColor.FromArgb(101, 151, 213),
            ArgbColor.FromArgb(87, 130, 183),
            ArgbColor.FromArgb(71, 107, 150),
            ArgbColor.FromArgb(53, 80, 112),
            ArgbColor.FromArgb(176, 75, 213),
            ArgbColor.FromArgb(151, 64, 183),
            ArgbColor.FromArgb(124, 52, 150),
            ArgbColor.FromArgb(93, 39, 112),
            ArgbColor.FromArgb(213, 125, 50),
            ArgbColor.FromArgb(184, 108, 43),
            ArgbColor.FromArgb(150, 88, 35),
            ArgbColor.FromArgb(113, 66, 27),
            ArgbColor.FromArgb(244, 230, 160),
            ArgbColor.FromArgb(210, 199, 138),
            ArgbColor.FromArgb(172, 162, 113),
            ArgbColor.FromArgb(128, 122, 85),
            ArgbColor.FromArgb(149, 108, 76),
            ArgbColor.FromArgb(128, 93, 65),
            ArgbColor.FromArgb(105, 75, 53),
            ArgbColor.FromArgb(78, 56, 39),
            ArgbColor.FromArgb(111, 2, 0),
            ArgbColor.FromArgb(95, 1, 0),
            ArgbColor.FromArgb(78, 1, 0),
            ArgbColor.FromArgb(58, 1, 0),
            ArgbColor.FromArgb(91, 216, 210),
            ArgbColor.FromArgb(78, 186, 180),
            ArgbColor.FromArgb(63, 152, 148),
            ArgbColor.FromArgb(47, 114, 110),
            ArgbColor.FromArgb(125, 176, 55),
            ArgbColor.FromArgb(108, 151, 47),
            ArgbColor.FromArgb(88, 124, 38),
            ArgbColor.FromArgb(66, 93, 29),
            ArgbColor.FromArgb(247, 235, 76),
            ArgbColor.FromArgb(212, 203, 65),
            ArgbColor.FromArgb(174, 166, 53),
            ArgbColor.FromArgb(130, 125, 39),
            ArgbColor.FromArgb(158, 158, 251),
            ArgbColor.FromArgb(136, 136, 217),
            ArgbColor.FromArgb(111, 111, 177),
            ArgbColor.FromArgb(83, 83, 133),
            ArgbColor.FromArgb(0, 123, 0),
            ArgbColor.FromArgb(0, 105, 0),
            ArgbColor.FromArgb(0, 86, 0),
            ArgbColor.FromArgb(0, 64, 0),
            ArgbColor.FromArgb(63, 63, 251),
            ArgbColor.FromArgb(5, 54, 217),
            ArgbColor.FromArgb(44, 44, 177),
            ArgbColor.FromArgb(33, 33, 133),
            ArgbColor.FromArgb(141, 118, 71),
            ArgbColor.FromArgb(122, 101, 61),
            ArgbColor.FromArgb(99, 83, 49),
            ArgbColor.FromArgb(74, 62, 37),
            ArgbColor.FromArgb(151, 50, 50),
            ArgbColor.FromArgb(130, 43, 43),
            ArgbColor.FromArgb(107, 36, 35),
            ArgbColor.FromArgb(80, 27, 27),
            ArgbColor.FromArgb(73, 126, 251),
            ArgbColor.FromArgb(62, 109, 217),
            ArgbColor.FromArgb(51, 89, 117),
            ArgbColor.FromArgb(39, 66, 133),
            ArgbColor.FromArgb(0, 214, 57),
            ArgbColor.FromArgb(0, 185, 49),
            ArgbColor.FromArgb(0, 151, 39),
            ArgbColor.FromArgb(0, 113, 30),
            ArgbColor.FromArgb(127, 85, 48),
            ArgbColor.FromArgb(110, 73, 41),
            ArgbColor.FromArgb(90, 59, 33),
            ArgbColor.FromArgb(67, 44, 25),
            ArgbColor.FromArgb(207, 175, 158),
            ArgbColor.FromArgb(178, 150, 136),
            ArgbColor.FromArgb(145, 123, 111),
            ArgbColor.FromArgb(109, 92, 84),
            ArgbColor.FromArgb(157, 81, 35),
            ArgbColor.FromArgb(135, 69, 31),
            ArgbColor.FromArgb(111, 56, 25),
            ArgbColor.FromArgb(83, 42, 19),
            ArgbColor.FromArgb(147, 86, 106),
            ArgbColor.FromArgb(126, 74, 92),
            ArgbColor.FromArgb(104, 60, 75),
            ArgbColor.FromArgb(77, 45, 56),
            ArgbColor.FromArgb(111, 107, 136),
            ArgbColor.FromArgb(95, 92, 117),
            ArgbColor.FromArgb(78, 75, 95),
            ArgbColor.FromArgb(58, 56, 72),
            ArgbColor.FromArgb(184, 131, 35),
            ArgbColor.FromArgb(158, 113, 31),
            ArgbColor.FromArgb(129, 92, 25),
            ArgbColor.FromArgb(97, 69, 19),
            ArgbColor.FromArgb(102, 116, 52),
            ArgbColor.FromArgb(87, 99, 44),
            ArgbColor.FromArgb(71, 81, 36),
            ArgbColor.FromArgb(53, 60, 28),
            ArgbColor.FromArgb(158, 76, 77),
            ArgbColor.FromArgb(136, 65, 66),
            ArgbColor.FromArgb(111, 53, 54),
            ArgbColor.FromArgb(84, 39, 40),
            ArgbColor.FromArgb(56, 40, 34),
            ArgbColor.FromArgb(48, 35, 30),
            ArgbColor.FromArgb(39, 28, 24),
            ArgbColor.FromArgb(30, 21, 18),
            ArgbColor.FromArgb(133, 106, 96),
            ArgbColor.FromArgb(115, 91, 83),
            ArgbColor.FromArgb(94, 74, 68),
            ArgbColor.FromArgb(70, 55, 50),
            ArgbColor.FromArgb(121, 72, 87),
            ArgbColor.FromArgb(104, 61, 74),
            ArgbColor.FromArgb(85, 50, 61),
            ArgbColor.FromArgb(63, 38, 45),
            ArgbColor.FromArgb(75, 61, 91),
            ArgbColor.FromArgb(64, 52, 78),
            ArgbColor.FromArgb(52, 42, 63),
            ArgbColor.FromArgb(39, 32, 47),
            ArgbColor.FromArgb(75, 49, 34),
            ArgbColor.FromArgb(64, 42, 30),
            ArgbColor.FromArgb(52, 35, 24),
            ArgbColor.FromArgb(39, 26, 18),
            ArgbColor.FromArgb(75, 81, 41),
            ArgbColor.FromArgb(64, 69, 35),
            ArgbColor.FromArgb(52, 56, 29),
            ArgbColor.FromArgb(39, 42, 22),
            ArgbColor.FromArgb(140, 59, 45),
            ArgbColor.FromArgb(121, 50, 38),
            ArgbColor.FromArgb(99, 41, 31),
            ArgbColor.FromArgb(74, 31, 24),
            ArgbColor.FromArgb(20, 178, 129),
            ArgbColor.FromArgb(17, 153, 111),
            ArgbColor.FromArgb(14, 125, 90),
            ArgbColor.FromArgb(10, 94, 68),
            ArgbColor.FromArgb(57, 140, 136),
            ArgbColor.FromArgb(49, 121, 117),
            ArgbColor.FromArgb(39, 99, 95),
            ArgbColor.FromArgb(30, 74, 72),
            ArgbColor.FromArgb(85, 43, 60),
            ArgbColor.FromArgb(73, 37, 51),
            ArgbColor.FromArgb(59, 31, 42),
            ArgbColor.FromArgb(44, 23, 31),
            ArgbColor.FromArgb(22, 125, 130),
            ArgbColor.FromArgb(18, 107, 112),
            ArgbColor.FromArgb(15, 87, 91),
            ArgbColor.FromArgb(11, 65, 68),
            ArgbColor.FromArgb(146, 62, 94),
            ArgbColor.FromArgb(125, 53, 81),
            ArgbColor.FromArgb(103, 43, 66),
            ArgbColor.FromArgb(77, 33, 50),
            ArgbColor.FromArgb(91, 25, 28),
            ArgbColor.FromArgb(78, 21, 24),
            ArgbColor.FromArgb(131, 33, 33),// was 63, 17, 19 changed due to typo
            ArgbColor.FromArgb(99, 25, 25), // was 47, 13, 15 changed due to typo
            ArgbColor.FromArgb(187, 47, 48),
            ArgbColor.FromArgb(161, 40, 41),
            ArgbColor.FromArgb(131, 33, 33),
            ArgbColor.FromArgb(99, 25, 24)
         })
        { }
    }
}