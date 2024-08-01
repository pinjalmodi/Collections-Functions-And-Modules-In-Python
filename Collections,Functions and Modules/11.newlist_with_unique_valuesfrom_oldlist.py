#Write a Python function that takes a list and returns a new list with unique
#elements of the first list.

list1=[1,2,3,1,2,3]
list2=[]

for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
