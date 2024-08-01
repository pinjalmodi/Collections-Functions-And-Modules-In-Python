#Write a Python script to merge two Python dictionaries

d={1:2,2:3}
p={3:4,4:5}
l={}

l=d.copy()
l.update(p)

print(l)
