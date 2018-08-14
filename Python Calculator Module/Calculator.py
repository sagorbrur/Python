def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def mul(x,y):
    return (x*y)
def div(x,y):
    if (y==0):
        print("Undefined")
    else:
        return (x/y)


print add(5,3)
print sub(5,3)
print mul(5,3)
print div(5,0)
print div(6,3)

