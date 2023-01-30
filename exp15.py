n = int (input ("Enter the number of elements: "))
print ("Elements are ")
list = []
for i in range (0,n+1):
    ele=int(input())
    if (ele>100):
        list.append ("over")
    else:
        list.append (ele)
print (list)