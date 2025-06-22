class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width =width
    def area(self):
        area_rec = self.length * self.width
        return area_rec

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        import math
        area_circ = math.pi * (self.radius ** 2)
        return area_circ