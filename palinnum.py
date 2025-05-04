d=1215
b=d
c=0
while b>0:
    last=b%10
    c=c*10+last
    b=b//10
if c==d:
    print("palindromic number")
else:
    print("not a palinmdromic number")
