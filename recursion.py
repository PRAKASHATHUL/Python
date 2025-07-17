def Fact(num):
    if num==1:
        return num
    else:
        return num*Fact(num-1)
print(Fact(4))
        
        
