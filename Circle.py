# Online Python - IDE, Editor, Compiler, Interpreter
import math
#Default constructor
class Circle:
    def __init__(self, name = None):
        self.radius = 1
        self.diameter = 2
#Construct a Circle with Radius, Diameter and Area       
    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = 2*radius
        self.area = math.pi*radius**2
#return the Diameter of a circle
    def diameter(self, radius): 
        return 2*radius
#return the Area of a circle      
    def area (self, radius):
        return math.pi*radius**2
#String representation    
    def __repr__(self):
        return f"Circle{self.radius}"

c = Circle(5)

print(c.radius.__repr__())
print(c.diameter.__repr__())
print(c.area.__repr__())

c = Circle ()

print(c.radius.__repr__())
print(c.diameter.__repr__())
print(c.area.__repr__())

if __name__ == None:
    print(c.radius.__repr__())
    print(c.diameter.__repr__())
    print(c.area.__repr__())
