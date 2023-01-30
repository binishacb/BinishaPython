def longestLength(a):
    max1 = len(a[0])
    for i in a:
        if (len(i) > max1):
            max1 = len(i)
    print("Length is ", max1)

a=[]
n =int(input("Enter the number of words : "))
for j in range (0,n):
    i=input("Enter element"+str(j+1)+":")
    a.append(i)

longestLength(a)
