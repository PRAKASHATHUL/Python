def swap(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            func(a,b)
    return wrapper

@swap
def substract(a,b):
    c=a-b
    print("Result:",c)
substract(2,10)
    