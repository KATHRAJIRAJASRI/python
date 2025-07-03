a=7654321
prev=a%10

asc=True
while a!=0:
    last=a%10
    if prev>last:
        asc=False
        break
    prev=last
    a=a//10
if asc:
    print("decsending order")
else:
    print("not descending order")    
    
