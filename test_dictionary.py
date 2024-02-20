# List of tuples
users =[
    (0,"Bob","sssh"),
    (1,"Robi","122344"),
    (2,"Ary","aassddee"),
    (3,"Misko","asdews"),
]


for u in users:
    if u[1] == "Bob":
        print(u)
#(0, 'Bob', 'passsword')
                

# dictionary: This returns touple - u[1] vil return the name  ( es BoB) to use as a key of dictionary
utenti_mappati = {u[1]:u for u in users}
print(utenti_mappati)
# {'Bob': (0, 'Bob', 'passsword'), 'Robi': (1, 'Robi', '122344'), 'Ary': (2, 'Ary', 'aassddee'), 'Misko': (3, 'Misko', 'asdews')}

usr_input = input("username: ")
pwd_input = input("password: ")

# simple way to retive a user data from a dictionary using a username as a key
_, user, password = utenti_mappati[usr_input]

#Test user input for correct password
if pwd_input == password:
        print(f"wellcome {user}")
else:
      print(f"no way {user}")  


# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
   "name":"Jose",
   "school":"Computing",
   "grades":(66,77,88)
}
grades =  {u[1]: u[2] for u in  student}
print(sum(grades) / len(grades))



# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = {u[1]: u[2] for u in data}
    return sum(grades) / len(grades)



 

