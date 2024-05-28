#Ignores last value, range returns sequence of integers
for i in range(1,10): 
    print(i)
for i in range(1,10,2): #Includes step value
    print(i)
for i in range(10):
    print(i)
for i in ['Hello','World',True]:
    print(i)
x=[4,5,6]
for i in range(len(x)):
    print(x[i])

i=0

while i<10:
    print(i)
    if i==5:
        break
    i+=1


