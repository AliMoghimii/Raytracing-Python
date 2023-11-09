from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine

def main():

    WIDTH = 320
    HEIGHT = 200

    camera = Vector(0,0,-1)
    objects = [Sphere(Point(0,0,0), 0.5, Color.HexToRgb("#FFFF00"))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene) 

    with open("3DTest.ppm", "w") as imgFile:
        image.exportImage(imgFile)

if __name__ == "__main__":
    main()


    #------------------------------------

    # COLOR TEST 
    
    # WIDTH = 3
    # HEIGHT = 2

    # image = Image(WIDTH,HEIGHT)

    # red = Color(x=1,y=0,z=0)
    # green = Color(x=0,y=1,z=0)
    # blue = Color(x=0,y=0,z=1)

    # image.setPixel(0, 0, red)
    # image.setPixel(1, 0, green)
    # image.setPixel(2, 0, blue)

    # image.setPixel(0, 1, red + green)
    # image.setPixel(1, 1, red + blue + green)
    # image.setPixel(2, 1, red * 0.001)

    # with open("colorTest.ppm", "w") as imgFile:
    #     image.exportImage(imgFile)

    #------------------------------------