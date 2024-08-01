#Write a Python function that checks whether a passed string is
#palindrome or not


def pali(n):
    x=reversed(n)
    y="".join(x)
    if y==n:
        return ("Palindrome")
    else:
        return ("Not Palindrome")
print(pali("aba"))
