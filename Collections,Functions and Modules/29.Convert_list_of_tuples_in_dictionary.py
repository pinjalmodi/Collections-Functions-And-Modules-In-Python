#Write a Python program to convert a list of tuples into a dictionary.

l=[('x',1),('y',2),('z',3)]

d={}

for i,j in l:
    d.setdefault(i,[]).append(j)
print(d)
