#1.Practice all Methods 
a={"r","a","j","a"}
b={"s","r","i","a"}
print(a.add("l"))
print(a.remove("j"))
print(a.discard("a"))
print(a.pop())
print(a.clear())
print(a.union(b))
print(b.union(a))
print(a.intersection(b))
print(b.intersection(a))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

x={1,2,3,4,5,"hello","hi"}
y=input("enter any element which you want to remove")
z=x.remove(y)
d={}
print(d.add(z))
#2.Take a set of no,take elements from the user, remove that element  from the existing set  and store in the new set.
x={"hi","r","a","j","a","s","r","i"}
y=input("enter any element which you want to remove")
z=set()
for i in y:
    if i in x:
        x.remove(i)
        z.add(i)
print("Existing set",x)
print("New set",z)
#3.Check whether the below methods are working for set or not. i.e. issubset(),issuperset(),isdisjoint() in description
"""Research Topic: issubset()
 -Returns True if all elements of the set are present in the specified set.
 -Returns False otherwise.
 issuperset()
- Returns True if all elements of the specified set are present in the set.
- Returns False otherwise.
isdisjoint()
- Returns True if the set has no elements in common with the specified set.
- Returns False otherwise."""




