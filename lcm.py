a=2
b=4
c=6
a_set=set()
b_set=set()
c_set=set()
for i in range(1,11):
    a_multiple=a*i
    d=a_set.add(a_multiple)
    b_multiple=b*i
    e=b_set.add(b_multiple)
    c_multiple=c*i
    f=c_set.add(c_multiple)
print(a_set)
print(b_set)
print(c_set)
print("lcm of a,b,c is",a_set.intersection(b_set,c_set))

