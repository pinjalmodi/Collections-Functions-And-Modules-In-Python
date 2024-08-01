#Write a Python program to print all unique values in a dictionary.

d={1:2,1:3,2:2,2:3,3:4,3:5}

d1={}
for i,j in d.items():
    if i not in d1:
        d1[i]=j
print(d1)
