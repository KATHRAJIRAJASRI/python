a=5
mid=(a//2)+1
for i in range(1,a+1):
    str=""
    for j in range(1,a+1):
        if i==1  or i==a or j==1 or j==a or (j==i==mid):
            str+="*"+" "
        else:
            str+=" "+" "
    print(str)