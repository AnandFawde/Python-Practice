class Student:

    class_year = 2026
    no_student = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.no_student +=1 

stu1 = Student("Ayushman",18)
stu2 = Student("Vinayak",19)
stu3 = Student("_andkishor",20)

print(f"My graduating class of {Student.class_year} has {Student.no_student} students")
print(stu1.name)
print(stu2.name)
print(stu3.name)

    
