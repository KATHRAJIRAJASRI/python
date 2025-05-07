#pattern-1
a=5
for i in range(a,0,-1):
    res=""
    for j in range(1,i+1,1):
        res=res+str(i)
    print(res)
    
#pattern-2
a=5
mid=a//2+1
for i in range(1,a+1):
    str=""
    for j in range(1,a+1):
        if j==1 or j==a or i==mid:
           str+="*"+" "
        else:
           str+=" "+" "
    print(str)
    
#pattern-3
a=5
b=a/2
for i in range(1,a+1):
    str=""
    for sp in range(i-1):
        str+=" "
    for j in range(a-i+1):
        str+="* "
    print(str)