tup=(1,2,3,3,4,5,5,5)
s=()
for i in tup:
    count=tup.count(i)
    if count>1 and i not in s:
        print(i,":",count)
        s=s+(i,)
