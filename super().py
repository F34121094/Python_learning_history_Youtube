class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def area(self):
        return self.width*self.height*self.length

square = Square(3,3)
cube = Cube(2,7,5)

print(square.area())
print(cube.area())