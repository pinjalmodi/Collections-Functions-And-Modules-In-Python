def perfect_num(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum=sum+x
    if sum==n:
        return ("Perfect Number")
    else:
        return ("Not Perfect Number")
print(perfect_num(28))
