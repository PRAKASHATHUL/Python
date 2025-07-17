"""for r in range(5,0,-1):
    print(" "* (5-r),"* "*r)"""
    

"""for a in range(1,6):
     print(" "* (5-a),"* "*a)
for k in range(5,0,-1):
    print(" "* (5-k),"* "*k)"""
    
    
"""for a in range(1,6):
    for b in range(a):
        print(chr(65+b),end=" ")
    print()"""
    

for a in range(1,6):
    k=a
    n=4
    for b in range(1,a+1):
        print(a,end=" ")
        a=a+n
        n-=1
    print()