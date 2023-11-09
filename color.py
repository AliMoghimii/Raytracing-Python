from vector import Vector

class Color(Vector):
    
    @classmethod
    def HexToRgb(cls, hexValue = "#000000"):
        x = int(hexValue[1:3], 16) / 255.0
        y = int(hexValue[3:5], 16) / 255.0
        z = int(hexValue[5:7], 16) / 255.0
        return cls(x, y, z)