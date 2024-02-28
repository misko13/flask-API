class Pereson:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    #def __str__(self) -> str:
    #    return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self) -> str:  #unambigius rappresentation of a method
        return f"<Person( '{self.name}', {self.age} )>"
    


bob = Pereson("Bob", 35)
print(bob)
#Person Bob, 35 years old
#<Person( 'Bob', 35 )>