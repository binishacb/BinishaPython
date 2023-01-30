# n=int(input("Enter the number of elements"))
# a=-1
# b=1
# sum=0
# if(n<=0):
#     print("Enter a valid number")
# else:
#     for i in range(0,n):
#         a=b
#         b=sum
#         sum=a+b
#         print(sum)


n=int(input("Enter the number of elements:"))
a=0
b=1
sum=0
if(n<=0):
    print("Enter a valid number:")
else:
    for i in range(0,n):
        a=b
        b=sum
        sum=a+b
        print(sum)
