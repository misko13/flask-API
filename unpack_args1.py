#arg re converterd to a touple 
def test(*args):
    print(args)

test(1,2,4)
#(1, 2, 4)


#same as upper case: arg are converted  to a toup[le and then unopacked inside a for loop 
def multiply(*args):# here are converted all attributes to a touple !!!
    total=1
    for a in args:
        total*= a
    return total

print(multiply(1,2,4)) #this are atributes
#8

#-------------------------------------------------------------
#unpack arguments in a call from the LIST 1 to 1
def add(x,y):
        return x + y

nums = [7,5]  #list
print(add(*nums)) # thaks to * we instruct a python to unpack a list one to one
#12

#-------------------------------------------------------------

nums = {"x":11, "y":22} # this is a dictionary

print(add(nums["x"], nums["y"])) # call to function where argumentsd are get from a dictionary
print(add(x=nums["x"], y=nums["y"])) # NOMINAL arguments, trhe same as upper example
print(add(**nums)) # <--- double ** makes a disctionary became arguments in a automatic as NAMES arguments (the same name is mandatory)
# all prints 33

#-------------------------------------------------------------

def apply(*args, operator):
     if operator == "*":
        print(args)# we get (1, 2, 4, 5) , a touple
        return multiply(args)  # args is Touple , this will become inside a multiplu a Touple of Touples  !!!! This is why multiply will not run corretly
     elif operator == "+":
        return sum(args)
     else:
         return "no valid operator !"
     
print(apply(1,2,4,5, operator = "+"))
#12
print(apply(1,2,4,5, operator = "*"))
#(1, 2, 4, 5) here it happens that function muyltiply convert args to a TOUPLE. a touple * 1 returns a touple itself

def apply2(*args, operator):      
    if operator == "*":
        return multiply(*args)  # args is Touple , this will become inside a multiplu a Touple of Touples  !!!! This is why multiply will not run corretly
    else:
         return "no valid operator !"
     
print(apply2(1,2,4,5, operator = "*"))
#40  <--- it works as we instruct python to unpack touple inside argument

#-------------------------------------------------------------

def named(**kwargs):
    print (kwargs)

named(name="Bob", age=25)
#{'name': 'Bob', 'age': 25}  <-- we see the arguments a converted into a DICTIONARY !! This is waht **kwargs do


def named2(name, age):
    print(name, age)

details = {"name":"Bob", "age":25}

named2(**details) #** will UNPACK dictionary to 2 arguments
#we get: Bob 25

def named3(**kwargs): # ** collrect arguments to a DICTIONARY
    print(kwargs)

details = {"name":"Bob", "age":25}

named2(**details) #** will UNPACK dictionary to 2 arguments
#we get: Bob 25

def print_nicelly(**kwargs): # ** collrect arguments to a DICTIONARY , arguments are converted to a dictionary
    named2(**kwargs) # we use thet a **method to UNPACK dictionary in a nornal argumentys passed to a named2 call
    for arg, value in kwargs.items(): #here we use items() method of dictionaries to make a nice print
        print(f"{arg}, {value}")

print_nicelly(name="Misko", age=25)
#name, Misko 25  <- named2 print

#name, Misko
#age, 25

#-------------------------------------------------------------
def booth(*args, **kwargs): #WE CAN PASS UNLIMITED NUMBER OF ARGUMENTS IN THIS WAA
    print(args) # <- concerted into a touple 
    print(kwargs) # <- concerted into a dictionasry

booth(1,3,5, name ="Bob", age=25) # name and age ate NAMEDS argumentsm not a dictionary !!
#(1, 3, 5)  <- touple of arguments
#{'name': 'Bob', 'age': 25} <- dictionary of arguments

