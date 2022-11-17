n=int(input("Enter the number of elements: "))
print("The elements are")
list=[]
for i in range(0,n):
    ele=int(input())

    if(ele%2!=0):
        list.append(ele)
print(list)