def add(x,y):
    return x+y
def operate(x,y): #We can return multiple values of a function as a tuple
    return x+y,x*y

print("The sum of 3,5 is:",add(3,5))
r1,r2=operate(3,5)
print(r1,r2)