a=int(input("Enter the number of  elements : "))
print("enter the elements : ")
list=[]
for i in range(0,a):
    ele=int(input())
    if(ele%2!=0):
        list.append(ele)
print(list)