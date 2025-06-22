class Shape:
    def __init__(self):
        pass
    def Area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width =width
    def Area(self):
        area_rec = self.length * self.width
        return area_rec

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def Area(self):
        import math
        area_circ = math.pi * (self.radius * self.radius)
        return area_circ