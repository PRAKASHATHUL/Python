# *args

def Total(*n):    # *n is used to ethra arguments venelum kodukan patum
    print(n)      #It will print as a tuple
Total("vava","jesin",89,65)


def Total(*n): 
    print(sum(n))
Total(1,5,89,65)

def a(**student):
    print(f"My name is {student["name"]} and i'm {student["age"]} years old")  #dictinary{}
a(name="shahid",age=21)


def sample(a,b):
    return a,b
print(sample(2,5))

#Global

x=10
def a():
    global x     
    x=x+10
a()
print(x)

c=15
b=20
def add():
    global c
    d=c+b
    c=d
add()
print(c)

