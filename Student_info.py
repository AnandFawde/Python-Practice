#  Class method = allows operations related to class itself
#              use (cls) as first parameter

class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name , gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"The Total No Of Students :{cls.count}"

    @classmethod
    def get_gpa(cls):
        if cls.count == 0 :
            return 0
        else:
            return f"Average GPA : {round(cls.total_gpa/cls.count,2)}"

Keshv = Student("Keshv",8.3)
Atharv = Student("Atharv",7.4)
Kishor = Student("Kishor",9.2)

print(Keshv.info())
print(Student.get_count())
print(Student.get_gpa())

    
    