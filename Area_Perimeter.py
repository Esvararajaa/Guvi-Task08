class Circle():
    # private variable pi
    _pi=3.14

    # constructor with variable radius
    def __init__(self, r):
        self.radius = r

    # Method to find the area of circle
    def area(self):
        return self.radius**2*Circle._pi
    
    # Method to find the perimeter of circle
    def perimeter(self):
        return 2*self.radius*Circle._pi

# Used the below list as the argument(radius)     
ls = [10, 501, 22, 37, 100, 999, 87, 351]

# Created object and used the object to call the defined method
for n in ls:
    NewCircle = Circle(n)
    print(f"Area of circle with {n}: {NewCircle.area()}")
    print(f"Perimeter of circle with {n}: {NewCircle.perimeter()}")

