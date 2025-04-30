a="malayali"
longest=""
for i in range(len(a)):
    temp=""
    for j in range(i,len(a)):
        temp=temp+a[j]
        if temp==temp[ ::-1] and len(temp)<len(longest):
            if len(temp)>2:
               longest=temp
print(longest)