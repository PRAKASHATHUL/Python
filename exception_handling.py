"""a,b=10,0
try:
    c=a/b
    print(c)
except Exception:
    print("Plaese enter a valid number")"""

"""my_list=[2,3,4,5]
try:
    print(my_list[6])
except IndexError:
    print("It is out of range")"""
    
"""a,b=10,8
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Please enter a number than zero")
except NameError:
    print("The value is not defined")
except Exception as e:
    print(e)
else:
    print("No errors found")"""
   
   
   
#Split

"""a,b=map(int,input("Enter two numbers: ").split())
c=a/b
print(c)"""
 
 
while True:
    try:
        a,b=map(int,input("Enter two numbers: ").split())
        try:
            c=a/b
            print(c)
            break

        except ZeroDivisionError:
            print("Please enter a number that is greater than zero")
        except NameError:
            print("The value is not defined")
        except Exception as e:
            print("Error",e)
    except ValueError:
        print("Please enter an integer")
    
    finally:
      print("Program is executed")