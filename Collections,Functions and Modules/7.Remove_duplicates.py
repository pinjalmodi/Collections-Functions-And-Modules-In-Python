l=[]
p=[1,2,3,1,2,3]

for i in p:
    if i not in l:
        l.append(i)
print(l)

print("-------------------")

p = [1, 2, 3, 1, 2, 3]
l = list(dict.fromkeys(p))
print(l)
