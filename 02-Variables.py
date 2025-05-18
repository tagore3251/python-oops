"""
Variables - Instance Variables (they are different for different Objects )
            Class(Static) Variables  

namespace : namespace is an area where you created and store object/variable - Class namespace
                                                                             - Object/Instance namespace
"""

class Car:
    wheels = 4      #Class(Static) Variables  
    def __init__(self):
        self.mil = 10      #Instance Variables
        self.com = "BMW"   #Instance Variables

c1 = Car()
c2 = Car()

c1.mil =8
Car.wheels = 5

print(c1.com , c1.mil , c1.wheels)
print(c2.com , c2.mil , c2.wheels)