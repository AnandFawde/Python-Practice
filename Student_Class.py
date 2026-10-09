class students:
    @staticmethod     #used to create a class inside class
    def decorator():  # (run by itself without using self)
        print("Hi")
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        self.decorator()
        total = 0
        for average in self.marks:
            total +=average
        print(self.name)
        print("You Have Scored : ",total/3)

s1 = students("Captain",[60,45,91])
s2 = students("Thor",[30,46,23])
s3 = students("Banner",[98,96,99])

s1.avg()