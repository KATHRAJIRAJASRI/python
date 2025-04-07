#take a nested list and to find the minimum and maximum values in each sublist
list=[[1,2,4],[9,4,7],[56,89,68]]
max_list=[]
min_list=[]
for i in list:
       b=max(i)
       c=min(i)
       max_list.append(b)
       min_list.append(c)
print("max list is",max_list)
print("min list is",min_list)