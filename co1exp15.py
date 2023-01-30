list1=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    i = input()
    list1.append(i)  # adding the element
print(list1)
list2=[]
k = int(input("Enter number of elements : "))
for i in range(0, k):
    i = input()
    list2.append(i)  # adding
print(list2)
print("colours present in list 1 but not in list 2 are:")
c=list(set(list1).difference(list2))
print(c)
