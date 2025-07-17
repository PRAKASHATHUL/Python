#Function is a reusable code.
#Function is a block of code which is executed when it is called.
#def fun(): - bracketinta akath kodukanen Parameters en parayum.
#    print("Hello")
#fun() - brackinta akath kodukanen Arguments en parayum
#Functin is used to avoid the repeatation of code.

"""def fun():
    print("Good Bye Zaman")
    print("Alvaro carreras")
fun()"""

#def fun():
#   pass - pass kodutha intentaction error kanikula, ee function kanikula
#fun()-Function call

"""def name(num):
    f=count=1
    while count<=num:
        f=f*count
        count+=1
    print(f)
name(5)

def is_even(num):
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
num=int(input("Enter the no:"))
is_even(num)"""

"""def is_positive(num):
    if num>=0:
        print(num,"is positive")
    else:
        print("Please enter a positive number")
num=int(input("Enter the no "))
is_positive(num)"""


"""def Addition(a,b):
    return a+b
print(Addition(56,3))"""
        
#Return

def total(num):
    a=0
    for b in num:
        a=a+b
    return a
my_list=[1,2,3,4,5]
d=total(my_list)
print("average is",d//len(my_list)) 