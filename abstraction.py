from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def fun(self):
        pass
    
class Child(Parent):
    def display(self):
        print("HI")
    def fun(self):
        print("Abraction method")
    
ob=Child()
ob.display()
ob.fun()

