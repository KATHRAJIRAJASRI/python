a=5
b=96
for i in range(1,a+1):
    string=""
    for j in range(1,a+1):
        if i==j or j==1 or i==a:
            b=b+1
            string+=chr(b)+" "
        else:
            string+=" "+" "
    print(string)
    