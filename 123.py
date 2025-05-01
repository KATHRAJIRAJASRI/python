a=5
count=0
for i in range(1,a+1):
    b=""
    for j in range(1,a+1):
        if i>=j:
           count=count+1
           b=b+str(count)+" "
    print(b)