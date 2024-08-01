#Write a Python program to combine values in python list of dictionaries.

from collections import Counter

l1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, {'item': 'item1', 'amount': 750}]

result=Counter()

for d in l1:
      result[d['item']]=result[d['item']]+d['amount']
print(result)
