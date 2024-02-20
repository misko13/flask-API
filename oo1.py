class Student:
    def __init__(self):# self is the  ref itself , INIT runs when object is created
        self.name = "Ralf"
        self.grades = (88,99,66,55)

    #this is a METHOD of the class
    def average(self):
        return sum(self.grades) / len(self.grades)

student_obj = Student() # istantiate a Student class 
print(student_obj.name)
print(student_obj.grades)
#Ralf
#(88, 99, 66, 55)

print(Student.average(student_obj)) # we call a class.method on a specific object (student)
#77.0

print(student_obj.average()) #It works also called fromn a specific object (student)
#77.0
