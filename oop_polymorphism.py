# poly  = many
#morphe = forms

#Two ways to achieve
#1. inheritence = Object can be treted as same type as parent class

class shape:
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side

class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
            return self.base * self.height * 0.5

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
            return 3.14 * self.radius **2

# polymorphism through inheritence

class roti(circle):      
    def __init__(self,flour,radius):
        super().__init__(radius)
        self.flour = flour

shapes = [rectangle(5),triangle(5,6),circle(5),roti("Wheat",4)]
for shape in shapes:
     print(f"{shape.area()}cm²")

