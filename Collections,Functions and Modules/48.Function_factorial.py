#Write a Python function to calculate the factorial of a number (a nonnegative integer)
def facto(a):
    fact=1
    for i in range(1,a+1):
            
        fact=fact*i
    return fact
print(facto(5))
