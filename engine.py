from image import Image
from ray import Ray
from point import Point
from color import Color

class RenderEngine:

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspectRatio = float(width) / height

        x0 = -1.0
        x1 = +1.0
        xdelta = (x1 - x0) / (width - 1)

        y0 = -1.0 / aspectRatio
        y1 = +1.0 / aspectRatio
        ydelta = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for j in range(height):
            y = y0 + j * ydelta
            for i in range(width):
                x = x0 + i * xdelta
                ray = Ray(camera, Point(x,y) - camera)
                pixels.setPixel(i, j, self.raytrace(ray, scene))
        return pixels
    
    def raytrace(self, ray, scene):
        color = Color(0,0,0)
        distanceHit, objectHit = self.getRayHit(ray, scene)
        if objectHit is None:
            return color
        hitPos = ray.origin + ray.direction * distanceHit
        color += self.colorAccumilation(objectHit, hitPos, scene)
        return color

#find nearest hit position
    def getRayHit(self, ray, scene):
        distanceMin = None
        objectHit = None

        for object in scene.objects:
            distance = object.intersects(ray)
            if distance is not None and (objectHit is None or distance < distanceMin):
                distanceMin = distance
                objectHit = object
            return (distanceMin, objectHit)

#recursive color at some point in the simulation (when bouncing off)        
    def colorAccumilation (self, objectHit, hitPosition, scene) :        
        return objectHit.material 

