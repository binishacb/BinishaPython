def longestlength(a):
    max1 = len(a[0])
    for i in a:
        if (len(i) > max1):
            max1 = len(i)
    print("length is", max1)
a=[]
n=int(input("enter the number of words:"))
for j in range (0, n):
    i = input()
    a.append(i)

longestlength(a);