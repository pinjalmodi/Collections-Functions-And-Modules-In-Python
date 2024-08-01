#Write a Python function that takes two lists and returns true if they have
#at least one common member

list1=[1,2,3]
list2=[1,4,5]

for i in list1:
    for j in list2:
        if i==j:
            print("True")
print("-----------------------")

list1=[1,2,3]
list2=[1,4,5]

for i in list1:
    if i in list2:
        print("True")
