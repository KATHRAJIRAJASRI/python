a=5
for i in range(1,a+1):
    pat=""
    for j in range(1,a+1):
        if j==1 or i==j or i==a:
            pat=pat+"*"
        else:
            pat+=" "
    print(pat)
        