"""manupolazione stringhe"""
name = "Bob"
helloGreeting = f"Hello, {name}"
print(helloGreeting)

print(f"Hello, {name}")


name = "Mark"
templateGr = "Hello, {}"
compsedGr1 = templateGr.format(name)
compsedGr2 = templateGr.format("Misko")
print(compsedGr1)
print(compsedGr2)

inStr = False
if inStr :
    dayofWeek = input("What is the day today? ")
    templateGrComplex = "Hello, {},  today is {}"
    print(templateGrComplex.format(name, dayofWeek))



# We have used the decimal module
from decimal import Decimal, InvalidOperation
def is_decimal(s):
    try:
        Decimal(s)
        return True
    except InvalidOperation:
        return False


""" segue input numerico e conversione"""
test = False
while not test:
    ft2 = input("Give a number integer of squere foot? ")
    test = is_decimal(ft2)
    if test:
        mt2 =  float(ft2)/10.8
        print(f"squere foot: {ft2}  is equivalent to {mt2:.2f} m2")
    else:
        print("Error, not a number")

a = 42
# Complete the function by making sure it returns 42. .
def return_42(a):
    # Complete function here
    return a  
    
res = return_42(a)
print(f"result is:  {res} ")
