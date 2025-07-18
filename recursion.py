def Fact(num):
    if num==1:
        return num
    else:
        return num*Fact(num-1)
print(Fact(4))
        
        
def Rev(s):
    if len(s)==0:
        return s
    else:
        return Rev(s[1:])+s[0]
print(Rev("Hello"))