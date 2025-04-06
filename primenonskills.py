# 1. Print the list of prime numbers and non prime numbers separately in given list.
a=[1,2,3,4,5,6,7,8,9,10]
prime=[]
non_prime=[]
for i in range(0,len(a),1):
    c=a[i]
    count1=0
    for j in range(1,c+1,1):
        if c%j==0:
           count1+=1
    if count1==2:
       prime.append(c)
    elif count1!=2:
       non_prime.append(c)
print(non_prime)    
print(prime)

#2. Count the skills through the dictionary.
a={
    "name":"rajasri",
    "skills":["c","html","css","python"],
    "languages":["telugu","hindi","english"]
}
b=a['skills']
print(len(b))

    
    
    