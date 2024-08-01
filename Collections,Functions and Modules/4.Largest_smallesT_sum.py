#Write a Python function to get the largest number, smallest num and sum of all from a list.

l=[1,2,3,4,5]
sum=0
for i in l:
    max=l[0]
    min=l[0]
    if i>max:
        max=i
    elif i<min:
        min=i
        
    sum=sum+i
print(max)
print(min)
print(sum)
