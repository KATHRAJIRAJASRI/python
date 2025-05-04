num=1234568
ec=0
while num>0:
   last=num%10
   if last%2==0:
      ec=ec+1
   num=num//10
print(ec)