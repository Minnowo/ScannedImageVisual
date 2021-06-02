using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.ComponentModel;

namespace CreateImage.Dithering
{
    public static class DitherHelper
    {

        public static Bitmap RequestImageTransform(Bitmap image, IPixelTransform transform, IErrorDiffusion ditherer)
        {
            WorkerData workerData;

            if(image.PixelFormat != System.Drawing.Imaging.PixelFormat.Format32bppArgb)
                using(Bitmap tmp = image)
                {
                    image = tmp.Copy();
                }

            workerData = new WorkerData
            {
                Image = image,
                Transform = transform,
                Dither = ditherer
            };

            return backgroundWorker_RunWorkerCompleted(null, new RunWorkerCompletedEventArgs(GetTransformedImage(workerData), null, false));
        }

        public static Bitmap backgroundWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            if (e.Error != null)
            {
                Console.WriteLine(e.Error.Message);
                return null;
            }
            else
            {
                return e.Result as Bitmap;
            }
        }

        public static Bitmap GetTransformedImage(WorkerData workerData)
        {
            ArgbColor[] pixelData;
            Size size;
            IPixelTransform transform;
            IErrorDiffusion dither;

            transform = workerData.Transform;
            dither = workerData.Dither;

            using (Bitmap image = workerData.Image)
            {
                size = image.Size;
                pixelData = image.GetPixelsFrom32BitArgbImage();
            }

            if (dither != null && dither.Prescan)
            {
                // perform the dithering on the source data before
                // it is transformed
                ProcessPixels(pixelData, size, null, dither);
                dither = null;
            }

            // scan each pixel, apply a transform the pixel
            // and then dither it
            ProcessPixels(pixelData, size, transform, dither);

            // create the final bitmap
            return pixelData.ToBitmap(size);
        }

        public static void ProcessPixels(ArgbColor[] pixelData, Size size, IPixelTransform pixelTransform, IErrorDiffusion dither)
        {
            ArgbColor current;
            ArgbColor transformed;
            int index;

            for (int row = 0; row < size.Height; row++)
                for (int col = 0; col < size.Width; col++)
                {

                    index = row * size.Width + col;
                    current = pixelData[index];

                    // transform the pixel
                    if (pixelTransform != null)
                    {
                        transformed = pixelTransform.Transform(pixelData, current, col, row, size.Width, size.Height);
                        pixelData[index] = transformed;
                    }
                    else
                    {
                        transformed = current;
                    }

                    // apply a dither algorithm to this pixel
                    // assuming it wasn't done before
                    dither?.Diffuse(pixelData, current, transformed, col, row, size.Width, size.Height);
                }

        }
    }
}
