#1)Implement the program to print true when the first and last element in the list was even, else print false.
a=[2,3,5,6,8]
if a[0]%2==0 and a[len(a)-1]%2==0:
    print("true")
else:
    print("false")  
#2) implement the program to create a function which performs the count method. Without using any methods.
def count_element(lst, target):
    count = 0
    i = 0
    while i < len(lst):
        if lst[i] == target:
            count += 1
        i += 1
    return count

numbers = [1, 2, 3, 4, 5, 2, 2, 3, 1]
target_num = 2

result = count_element(numbers, target_num)
print(f"The number {target_num} occurs {result} times in the list.")


    #3) write a program to print the prime numbers in the new list from the existing list.

a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range(0,len(a),1):
    if a[i]%2==0:
        b.append(a[i])
print(b)        