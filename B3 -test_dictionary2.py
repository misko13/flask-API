# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
# down: the LIST oF DICTIONARIES !
student = [{
   "name":"Jose",
   "school":"Computing",
   "grades":(66,77,88)
},
{
   "name":"Misko",
   "school":"Computing",
   "grades":(55,44,33)
},
{
   "name":"Ary",
   "school":"Computing",
   "grades":(22,37,44)
}
]
print('loop all in List and print from dict.----------------------------------------')
for st in student:  
    print(f"student: {st['name']} your grades are : {st['grades']} ant total is : {sum(st['grades'])}")



# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =  data['grades']
    return sum(grades) / len(grades)


print('call average_grade function in loop all ------------------')
for st in student:
    print(f"student: {st['name']} average grade is : {average_grade(st)}")

# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    # read all students
    for student in student_list:
        # access to student grades
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count

