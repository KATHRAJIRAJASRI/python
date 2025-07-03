a=123456226
b=2
count=0
m=[]
pos=0
while a!=0:
    last=a%10
    pos=pos+1
    if last==b:
        count=count+1
        m.append(pos)
    a=a//10
print("number is present & it is",count,"times present in number and positions are")
for i in m:
    print(i,",",end='')
   
