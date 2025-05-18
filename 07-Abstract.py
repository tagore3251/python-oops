"""
Python by default don't support abstract class but we have a module ABC(Abstract Base Classes) module.



"""
from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer) :
    def process(self):
        print("it's Running")

class Whiteboard(Computer):
    def write(self):
        print("it's Writing")

class Programmer:
    def work(self,com):
        print("Solving Bugs")

#com = Computer()
com1 = Laptop()
#com2 =Whiteboard()
#com.process()
prog1 =Programmer()
prog1.work(com1)

#com1.process()