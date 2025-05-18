"""
Types of methods :
  Instance methods
     Accessor methods - if u want to fetching the values 
     Mutator methods - if u want to modify the values
  Class methods
  Static methods
"""

class Student:
    name = "Tagore" #class or static variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1  #Instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):  #Instance methods
        return (self.m1 + self.m2 + self.m3)/3

    """def get_m1(self): #Accessor methods
        return self. m1
    
    def sef_m1(self,value): #Mutator methods
        self.m1 = value """
    
    # if u want working with instance u will use self keyword ,if u want working with class variables u will use cls keyword
    @classmethod  
    def getName(cls):
        return cls.name
    
    #if u want a method which has nothing to do with instance variables amd class variables at that we will be using static method
    @staticmethod
    def info():
        print("This is Student Class.. in abc module")

s1 = Student(18,12,51)
print(s1.avg())
print(s1.getName())


Student.info()