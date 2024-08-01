#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers
def min_max(x):
    max=x[0]
    min=x[0]
    for i in x:
        if i>max:
            max=i
        elif i<min:
            min=i
    return max,min

print(min_max([1,2,3,4,5]))



