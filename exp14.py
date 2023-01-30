list1 = [6,8,12,34]
list2 = [7,14,8,6]
x = len(list1)
y = len(list2)
sum1 = sum(list1)
sum2 = sum(list2)
if(x == y):
    print("List are of same length..")
else:
    print("Length of the lists are different..")
if(sum1 == sum2):
    print("Sums of the list are of same value..")
else:
    print("sums are different..")
print("Common elements are : ")
for i in list1:
    for j in list2:
        if(i == j):
            print(i)

