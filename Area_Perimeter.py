class Circle():
    __pi=3.14
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*Circle.__pi
    
    def perimeter(self):
        return 2*self.radius*Circle.__pi
    
ls = [10, 501, 22, 37, 100, 999, 87, 351]
for n in ls:
    NewCircle = Circle(n)
    print(f"Area of circle with {n}: {NewCircle.area()}")
    print(f"Perimeter of circle with {n}: {NewCircle.perimeter()}")

