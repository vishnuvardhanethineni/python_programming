from abc import ABC ,  abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return  self.radius**2*3.1432
circle=Circle(4)
print(circle.area())
rectangle=Rectangle(4,2)
print(rectangle.area())