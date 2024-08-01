#Write a Python script to check if a given key already exists in a dictionary.
d={1:2,2:3,3:4,4:5}
k=1

if k in d:
    print("Exist")
else:
    print("Does not exist")

print("----------------------------")

d={1:2,2:3,3:4,4:5}
k={1,2}

for i in k:
    if i in d:
        print("Exist")
    else:
        print("Does not exist")
