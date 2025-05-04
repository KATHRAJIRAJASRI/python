a=789456123
count=0
while a>0:
    last=a%10
    a=a//10
    if last%2==0:
        count+=last
print(count)