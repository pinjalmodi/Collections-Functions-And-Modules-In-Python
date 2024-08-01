#Write a Python program to find the second smallest number in a list.

list=[1,2,3,4,5,6,10,9,7,8]

smallest=list[0]
second_small=list[5]

for i in list:
    if i<smallest:
        second_small=smallest
        smallest=i
    elif i<second_small and i!=smallest:
        second_small=i
print(smallest)
print(second_small)


