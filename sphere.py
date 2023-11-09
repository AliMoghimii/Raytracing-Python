from math import sqrt

class Sphere:

    def __init__(self, center, radius, material):
        self.center = center;
        self.radius = radius;
        self.material = material;

    def intersects(self, ray):
        #معادله درجه دوم 

        rayDirection = ray.origin - self.center
        a = 1
        b = 2 * ray.direction.dot(rayDirection)
        c = rayDirection.dot(rayDirection) - self.radius * self.radius

        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None