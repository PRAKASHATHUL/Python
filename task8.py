"""name=(input("Enter your name:"))
score=int(input("Enter your score:"))

if score>=95 and score<=100:
    print("Yeah!!, {} got high distinction. keep it up.".format(name))
elif score>=90 and score<95:
    print("{} got A grade.\nGood".format(name))
elif score>=80 and score<90:
    print("{} got B grade".format(name))
elif score>=70 and score<80:
    print("{} got C grade".format(name))
elif score>=60 and score<70:
    print("{} got D grade".format(name))
elif score<=59:
    print("{} is failed . Better luck next time.".format(name))
else:
    print("Mark specified is not correct")
"""

num=int(input("Enter a number :"))
if num>0:
    print("{} is postive".format(num))
elif num==0:
    print("{} is Zero".format(num))
elif num<0:
    print("{} is Negative".format(num))
else:
    print("please enter a number")