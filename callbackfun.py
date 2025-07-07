def num():
    n1=int(input("enter your number"))
    return n1
def prime():
    n=num()
    p=2
    c=0
    while c<=n:
        fact=0
        for i in range(2,p):
           if p%i==0:
            fact+=1
            break
        if fact==0:
            c=c+1
            if c==n:
              print(p)
        p=p+1
prime()