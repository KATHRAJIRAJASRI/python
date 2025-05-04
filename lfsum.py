a=75547
b=str(a)
sum=0
sum1=int(b[0])+int(b[-1])
for i in range(1,len(b)-1):
    sum+=int(b[i])
if sum==sum1:
    print("equal")
else:
    print("not equal")
