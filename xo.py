a=5
for i in range(1,a+1):#1 2 3 4 5
    pat=""
    for j in range(1,a+1):#1 2 3 4 5
        if i%2==0 and j%2==0:
            pat=pat+"x"+" "
        elif i%2!=0 and j%2!=0:
            pat=pat+"x"+" "
        else:
            pat+="o"+" "
    print(pat)        