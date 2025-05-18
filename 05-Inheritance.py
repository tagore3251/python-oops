"""
Inheritance :

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class - is the class being inherited from, also called base class or Super class.
Child class - is the class that inherits from another class, also called derived class or Sub class.
"""

class A:
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")

class B (A): #B is inheritance the features from A ,  # Single Level Inheritance
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")

class C(B):  #Multi Level Inheritance
    def feature5(self):
        print("Feature 5 Working")

class D: 
    def feature6(self):
        print("Feature 6 Working")


class E(A,D):  #Multiple Inheritance
    def feature7(self):
        print("Feature 7 Working")


a1 =A()

a1.feature1()
a1.feature2()

b1 =B()

b1.feature3()  #here u can see the options - feature1,feature2,feature3,feature4

c1 = C()
c1.feature5()

e1 = E()
e1.feature1()