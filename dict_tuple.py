#Take a list of dictionary{Name: ,age: ,citize: } check whether that person is eligible for vote or not and also check the citizen.if both conditions are True add { eligible: True}
a=[{"name":"shiriha","age":19,"citizenship":"indian"},{"name":"shivani","age":21,"citizenship":"pakisthani"}]
for i in range(len(a)):
     if a[i]["age"]>18 and a[i]["citizenship"]=="indian":
         a[i].update({"eligible":True})
     else:
         print(a.remove(a[i]))
print(a)
#Take a tuple of elements, print the unique elements in the new list
a=(1,1,1,2,2,2,3,4,5,6,7,7,8)
b=list(a)
d=[]
for i in b:
    c=b.count(i)
    if c==1:
        d.append(i)
print(d)
       