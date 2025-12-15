class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
cir1 = Circle(21)
print(cir1.area())
print(cir1.perimeter())