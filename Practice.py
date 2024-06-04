def evenOrOdd(t):
    if t%2==0:
        print("Number is even")
    else:
        print("Number is odd")

def prime(x):
    p=0
    if(x==0 or x==1):
        print("Not Prime")
    else:
        for i in range(2,x-1):
            if(x%i==0):
                p=1
                print("Not prime")
                break
        if p==0:
            print("Prime")

def sumOfList(z):
    sum=0
    for i in z:
        sum+=i
    return sum

def capitalize(l):
    l=l.upper()
    return l

x=int(input("Enter a number to check for even/odd and prime:  "))
evenOrOdd(x)
prime(x)
y=[]
print("Enter the elements:")

for i in range (4):
    j = int(input())
    y.append(j)

print("The sum is: ",sumOfList(y))

st=input("Enter a word ")
print("Capitalized word is: ",capitalize(st))
