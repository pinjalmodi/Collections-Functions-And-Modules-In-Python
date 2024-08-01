#Write a Python program to calculate surface volume and area of a cylinder

pie=3.14
r=int(input("Enter r"))
h=int(input("Enter h"))
sur_vol=pie*r*r*h

area=(2*pie*r*h )+ (2*pie*r*r)

print(area)
print(sur_vol)
