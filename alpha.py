a=5
count=96
for i in range(a):
    string=""
    for j in range(a):
        if i>=j:
            count=count+1
            string+=chr(count)+" "
    print(string)