a=5
for i in range(1,a+1):
    string=""
    for j in range(1,a+1):
        if j==1 or j==a:
           string+="*"+" "
        elif i==1 or i==a:
            string+="*"+" "
        else:
            string+=" "+" "
    print(string)
    
        
    