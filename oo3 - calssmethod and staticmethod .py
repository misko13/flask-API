#different types of methods
class ClassMethods:
    def instance_method(self): #mostly used to produce ACTION that uses data inside the  object
        print(f"Call to instance method {self}")

    @classmethod # factory example - it calls the class itself cls
    def class_method(cls):
         print(f"Call to a class method {cls}")

    @staticmethod # Used just to place a method inside a Class - like a function
    def static_method():
         print(f"Call to a static method ")

class Book:
    TYPES=("hardcover","paperback") #thos ate the class properties

    def __init__(self, name: str, book_type: str, weight:int) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"<Book  {self.name}, {self.book_type}, weight: {self.weight} gr>"
    
    #those methods are FACTORY mathods and can be used instead if direct init that do not controll a THPES
    @classmethod  #FACTORY class for hardcover books
    def hardcover(cls, name: str, page_weight: int) -> "Book" :
        #cls stanbds for Class call : Book !!
        return cls(name, cls.TYPES[0], page_weight + 100)  #Type is automatic, extra weight for hardcover, same like : Book(name, cls.TYPES[0], page_weight + 100) 
    
    @classmethod  #FACTORY class for hardcover books
    def paperback(cls, name: str, page_weight: int) -> "Book":
        #cls stanbds for Class call : Book !!
        return cls(name, cls.TYPES[1], page_weight)  #Type is automatic, extra weight for hardcover



#------------------------ Classmethods -- -----------------------------
test = ClassMethods()

test.instance_method()
ClassMethods.class_method()
ClassMethods.static_method()

#Call to instance method <__main__.ClassMethods object at 0x000001F8F6CA71A0>
#Call to a class method <class '__main__.ClassMethods'>
#Call to a static method

#------------------------ @classmethod Book -----------------------------
#we call a Class directly to access a   @classmethod 
book  = Book.hardcover("harry Potter", 1500)
light = Book.paperback("python 101", 500)

print(book) #print uses __repr__ 
print(light)
##<Book  harry Potter, hardcover, weight: 1600 gr>
#<Book  python 101, paperback, weight: 500 gr>