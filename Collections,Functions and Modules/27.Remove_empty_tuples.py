#Write a Python program to remove an empty tuple(s) from a list of tuples.

tup=[(1,2,3),(4,5,6),()]
tup=[i for i in tup if i!=()]
print(tup)
