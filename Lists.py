x=[3,'pranay',True] #x stores reference to the list and not actual values, lists are mutable
y=[4,5]
print(x[0])
print(len(x))
x.append(99)
print(x)
x.extend(y) #Combines two lists into x
print(x)
x.pop() #Removes and returns last element of list
print(len(x))
y=x
x[0]=7
print(y) #Change in x affects y
y=x[:] #Makes a copy instead thus changes in x does not affect y and vice versa
