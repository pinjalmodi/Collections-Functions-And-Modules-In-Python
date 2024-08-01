# Write a Python program to returns sum of all divisors of a number

n=int(input("Enter a number"))
sum=0
for x in range(1,n):
    if n%x==0:
        sum=sum+x
print(sum)
