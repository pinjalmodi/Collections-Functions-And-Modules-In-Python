list1=[1,2,3,4,5,6]
sub_list=[2,3,4,6,7]

for i in range(len(list1)-len(sub_list)+1):
    if list1[i:i+len(sub_list)]==sub_list:
        print("True")
        break
    else:
        print("False")
        break
print("--------------------")

