import math

class Circle:
    def __init__(self,h,):
        self.hankei = h             

    def  area(self):
        return  self.hankei * self.hankei * math.pi

circle = Circle(5)
print(circle.area())

    
