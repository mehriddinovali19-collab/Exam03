class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    

    def area(self):
        return self.width * self.height
    
Rect = Rectangle(5, 6)
Rect2 = Rectangle(9, 7)

print(Rect.area())
print(Rect2.area())