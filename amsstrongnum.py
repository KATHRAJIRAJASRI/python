a=678
b=a
temp=a
len=0
while a>0:
      a=a//10
      len=len+1   
t=0
while b>0:
    last=b%10
    sq=last**len
    t=t+sq
    b=b//10
if temp==t:
    print("amstrong")
else:
    print("not amstrong")
