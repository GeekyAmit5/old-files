
from polygon import polygon
from shape import shape

class triangle(polygon,shape):
    def area(self):
        return  self.get_length() * self.get_breadth() /2