"""
OOPS - Object Oriented Programming Language

Python is Object Oriented Programming Language
          Functional Programming
          Procedure Oriented Programming

Class - A Class is like an object constructor, or a "blueprint" for creating objects.
          
"""
class Computer:
    #Attributes -> Variables
    #Behaviour -> Methods [Function]

    def config(self):
        print("i5,16gb,1TB")

com1 = Computer()
com2 = Computer()

"""Computer.config(com1)
Computer.config(com2)"""

com1.config()
com2.config()


#The __init__() Function :
"""
Special  1.Special Variables -> __name__
         2.Special Methods   -> __init__

The __init__() function is called automatically every time the class is being used to create a new object.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """def details(self):
        print("Details is",self.name,self.age)"""

p1 = Person("Tagore", 20)
#p1.details()
print(p1.name)
print(p1.age)



#The __str__() Function :

"""
The __str__() function controls what should be returned when the class object is represented as a string.
If the __str__() function is not set, the string representation of the object is returned:
"""
#The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tagore", 20)

print(p1)

#The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Tagore", 20)

print(p1)


# The self Parameter :
"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Tagore", 20)
p1.myfunc()


# Modify Object Properties :  p1.age = 21

# Delete Object Properties : del p1.age

# del p1.age : del p1

# The pass Statement
"""class definitions cannot be empty, but if you for some reason have a class definition with no content, 
put in the pass statement to avoid getting an error.
"""
class Person:
  pass
