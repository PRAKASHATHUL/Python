#Private - It works inside the class,classinta porath kodutha wrk avula (2 underscore is used)

class Students:
    def __init__(self):
        self.__name="Shibly"
        print(self.__name)
        
    def age(self):
        self.age=1
    
stud=Students()
print(stud.age)