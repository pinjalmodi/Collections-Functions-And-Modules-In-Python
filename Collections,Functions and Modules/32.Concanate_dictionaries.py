#Write a Python script to concatenate following dictionaries to create a new one.
x={1:2,3:4}
y={4:5,5:6}
z={6:7,7:8}
p={}
for d in (x,y,z):
    p.update(d)
print(p)
