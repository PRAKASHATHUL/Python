
"""name=(input("Enetr your name:"))
age=int(input("Enter your age:"))

if age>=18:
    print("{} can apply for lisence".format(name))
else:
    print("{} is not eligible to apply for lisence".format(name)) 
    print("you can only apply when you get 18 years old")   
    """

"""num1=int(input("Enter a number:"))

if num1%2==0:
    print(num1,"is even")
else:
    print(num1,"is odd")    
    """

"""leap_year=int(input("Enter a year :"))

if (leap_year%4==0 & leap_year%100 !=0 )| leap_year%400==0:
    print(leap_year,"is a leap year")
else:
    print(leap_year,"is not a leap year")
    """

"""weather=int(input("Enter the temperature :"))

if weather>=30:
    if weather>=35:
        print("Its too hot,Take an umperlla with you!!")
    else:
        print("Its hot outside")
else:
    print("Safe to go outside")
"""

"""
num1=int(input("Enter firts number :"))
num2=int(input("Enter second number :"))

print("Select your choice : \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
choice=int(input("Enter your choice :"))
if  choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("Invalid choice")
"""


"""distance=int(input("Enter the distance you want to travel(in km) :"))
if   distance==1:
     print("you can travel by walking")
elif distance>=3 and distance<=50:
     print("you can travel by cycle or bike")
elif distance>=50 and distance<=500:
     print("you can travel by bus or car")
elif distance>=500:
     print("you can travel by train or flight")
else:
     print("stay home")    
"""

age=int(input("Enter your age:"))
distance=int(input("Enter the distance(in km) :" ))

tckt_rate=distance*10
if age<=5 and age!=0:
    print("No charge for travelling")
elif age>5 and age<=18:
    print("Your ticket charge is",tckt_rate/2)
elif age>18 and age<=60:
    print("Youe ticket charge is",tckt_rate) 
elif age>60:
    print("Your ticket charge is",tckt_rate/2)
else:
    print("Age not enetered")