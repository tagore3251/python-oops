"""
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
with the same name that can be executed on many objects or classes.

 Poly   Morph  ism  
  |       |
 Many   Form
 
 1.Duck Typing
 2.Operator Overloading
 3.Method Overloading
 4.Method Overriding
"""

#1.Duck Typing
"""
Duck Test : If it looks like a duck,
            swims like a duck,and
            quacks like a duck,
            then it probably is a duck.
"""

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")
    

class Laptop :
    def code(self,ide):
        ide.execute()
        
#ide = PyCharm()
ide = MyEditor()
lap1= Laptop()

lap1.code(ide)


#2.Operator Overloading
"""a = 5
b = 6

print(a + b)
print(int._add_(a,b))
"""

class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        
        return s3
      
    def __gt__(self,other):
        r1 = self.m1 + self.m2 
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1 , self.m2)
        
s1= Student(51,12)
s2= Student(18,17)

s3 = s1 + s2    # -> Student._add_(s1,s2)

print(s3.m1)

if s1 > s2 :
    print("s1 wins")
    
else : 
    print("s2 wins")
    
a = 9
#print(a)
print(a.__str__())


print(s1)
print(s2)



#3.Method Overloading  - same method name but the number of arguments are different

class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!= None and b!=None and c!= None :
            s = a+b+c
            
        elif a!= None and b!= None :
            s = a+b
            
        else :
            s = a
        return s

s1= Student(51,18)

print(s1.sum(5,9))


#4.Method Overriding  - same method name and same no.of arguments but in different class

class A :
    def show (self):
        print("in A Show")
        
class B(A) :
    def show(self):
        print("in B Show")
        
        
a1 = B()
a1.show()
