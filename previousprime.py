#To print the previous prime number to that number
num=100
previous_prime_not_found=True
while previous_prime_not_found:
    num=num-1
    fact=0
    for i in range(2,num,1):
        if num%i==0:
            fact=fact+1
            break
    if fact==0:
        print(num)  
        previous_prime_not_found=False

