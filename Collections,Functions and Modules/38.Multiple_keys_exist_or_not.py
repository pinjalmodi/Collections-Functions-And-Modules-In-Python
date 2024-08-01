#Write a Python program to check multiple keys exists in a dictionary
d={1:2,2:3,3:4,4:5}
l={1,2}

for i in l:
    if i in d:
        print(i,"Exist")
    else:
        print(i,"Doesnot Exist")
