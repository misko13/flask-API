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
# no test for a wrong input
_, user, password = utenti_mappati[usr_input]

#Test user input for correct password
if pwd_input == password:
        print(f"wellcome {user}")
else:
      print(f"no way {user}")  


