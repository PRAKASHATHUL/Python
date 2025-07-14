"""count=1
while count<=10:
    print(count)
    count+=1"""
    
    
#Factorial

"""num=int(input("Enter the number you want to find the factorial:"))
f=count=1
while count<=num:
    f=f*count
    count+=1
print(f)    
    """
    
#Multiplication table
    
"""num=int(input("Enter the no:"))
mul=1
while mul<=10:
    print(f"{mul} * {num} = {mul * num}")
    mul+=1
    """
       
while True:
    num1=int(input("Enter the first no:"))  
    num2=int(input("Enter the second no:"))
    print("Please enter your choice:\n 1.Addition \n 2.Subraction \n 3.Division \n 4.Multiplication")
    choice=int(input("Enter your choice:1,2,3,4: ")) 
    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1/num2)
    elif choice==4:
        print(num1*num2)
    else:
        print("Please enter a valid choice")
    s=str(input("Do you want to continue(yes/no):"))
    if s.lower()!="yes":
        break