from image import Image
from color import Color

def main():

    WIDTH = 3
    HEIGHT = 2

    image = Image(WIDTH,HEIGHT)

    red = Color(x=1,y=0,z=0)
    green = Color(x=0,y=1,z=0)
    blue = Color(x=0,y=0,z=1)

    image.setPixel(0, 0, red)
    image.setPixel(1, 0, green)
    image.setPixel(2, 0, blue)

    image.setPixel(0, 1, red + green)
    image.setPixel(1, 1, red + blue + green)
    image.setPixel(2, 1, red * 0.001)

    with open("test.ppm", "w") as imgFile:
        image.exportImage(imgFile)

if __name__ == "__main__":
    main()