class student:
    def __init__(self,phy,maths,chem):
        self.physic = phy
        self.maths = maths
        self.chemistry = chem

    def percent(self):
        return (self.physic  + self.maths + self.chemistry)/3


stu1 = student(89,97,96)
print(stu1.percent())
stu1.physic = 98
print(stu1.percent())