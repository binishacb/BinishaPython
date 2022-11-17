colorlist1=input("Enter the colors")
colorlist_1=colorlist1.split(' ')
colorlist2=input("Enter the colors")
colorlist_2=colorlist2.split(' ')
a=[]
for i in colorlist_1:
    if i not in colorlist_2:
        a.append(i)
print(a)
