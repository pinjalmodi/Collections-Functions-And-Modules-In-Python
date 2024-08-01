from collections import defaultdict,Counter
s1='w3resource'
d={}

for i in s1:
    d[i]=d.get(i,0)+1
print(d)
