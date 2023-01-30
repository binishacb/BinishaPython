n=int(input("Enter the number of elements:"))
print("Enter the elements:")
li=[]
for i in range(0,n):
    el=int(input())
    if( el%2!=0):
        li.append(el)
print(li)
