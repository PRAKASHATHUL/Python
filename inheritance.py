#Multiple Inheritance

"""class Father:
    def skills(self):
        print("Father: Gardening,Cooking")

class Mother:
    def skills(self):
        print("Mother: Art,Craft")

class Child(Father,Mother):
    def skills(self):
        print("Child: Coding")
        Father.skills(self)
        Mother.skills(self)
c=Child()
c.skills()
print(c)"""


class Person:
    def __init__(self,name,s):
        self.name=name
        super().__init__(s)
        print("Person constructor")

class Employee:
    def __init__(self,salary):
        self.salary=salary
        print("Employee constructor")
        
class Manager(Person,Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

        print("Manager constructor")
        
m=Manager("Nadhil",50000)
print(m.name)
print(m.salary)
        
        
    
    