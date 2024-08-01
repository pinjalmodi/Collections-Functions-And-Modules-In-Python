#Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary.

from itertools import product

d={'1':['a','b','c'],'2':['c','d','a']}

for x,y in product(*d.values()):
    print(x+y)
