class Student:
    def __init__(self, vname, vgrades):# self is the  ref itself , INIT runs when object is created
        self.name = vname
        self.grades = vgrades

    #this is a METHOD of the class
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student_obj = Student("Misko", (88,99,66,55)) # istantiate a Student class 
student_obj2 = Student("Ary", (77,99,66,77)) # another 

print(student_obj)
#<__main__.Student object at 0x00000181C88D77D0>  this is object raopresentation
print(student_obj.name)
print(student_obj.grades)
#Ralf
#(88, 99, 66, 55)

print(Student.average_grade(student_obj)) # we call a class.method on a specific object (student)
#77.0

print(student_obj.average_grade()) #It works also called fromn a specific object (student)
#77.0
print(student_obj2.average_grade())
#79.75
