

namespace CreateImage.Dithering
{
  public interface IPixelTransform
  {
    #region Methods

    ArgbColor Transform(ArgbColor[] data, ArgbColor pixel, int x, int y, int width, int height);

    #endregion
  }
}
