"""class Laptops:
    def Spec(self):
        self.Ram="8GB"
        self.model="hp"
lap1=Laptops()
lap1.Spec()
print(lap1.model)
print(lap1.Ram)"""


"""class Laptops:
    def Spec(self,r,n):
        self.Ram=r
        self.model=n
lap1=Laptops()
lap2=Laptops()
lap1.Spec(r="16GB",n="Dell")
lap2.Spec(r="16GB",n="hp")
print(lap2.model)
print(lap1.model)"""


#init - It is a constructor that is automatically called when a new obejct of class is created.
"""class Laptops:
    owner="Athul"
    def __init__(self,r,m):
        self.Ram=r
        self.model=m
lap1=Laptops(r="4GB",m="Dell")
lap2=Laptops(r="8GB",m="lenovo")
print(lap1.model)
print(lap2.Ram)
print(Laptops.owner)"""

#Inheritance

class Vehicles:
    def Detail(self,m,model):
        self.make=m
        self.model=model
        
class Car(Vehicles):
    def __init__(self,c,p):
        self.color=c
        self.power=p
c1=Car(c="Red",p="199bhp")
c1.Detail(m="1969",model="Ambassador")
print(c1.color)
print(c1.model)
