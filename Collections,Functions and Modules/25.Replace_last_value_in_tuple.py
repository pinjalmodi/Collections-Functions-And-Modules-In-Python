#Write a Python program to replace last value of tuples in a list

tup1=[(1,2,3,4,5),(1,2,3),(1,2,3)]
new=0
new_list=([tup[:-1]+(new,) for tup in tup1])
print(new_list)
