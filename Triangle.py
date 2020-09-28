class Triangle:
    def __init__(self,h,w):
        self.height = h
        self.width = w

    def area(self):
        return self.height * self.width / 2

triangle = Triangle(10,8)
print(triangle.area())


    
        
