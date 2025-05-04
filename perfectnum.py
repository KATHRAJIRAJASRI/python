a=25
sum=0
for i in range(1,28):
    if a%i==0:
        sum=sum+i
if sum==a :              
    print("perfect number")
else:
    print("not a perfect number")