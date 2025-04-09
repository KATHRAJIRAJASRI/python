# program to separate odd & even elements from list 
list=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.extend(odd)
print(even)
#program to separate unique elements from list and add "*" at EOL
a=[2,3,4,5,2,1,3,2]
b=[]
c=[]
for i in a:
    if i in b:
        c.append("*")
    else:
        b.append(i)
b.extend(c)
print(b)

    