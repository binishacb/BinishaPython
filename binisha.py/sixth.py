x=[12,54,87,95]
y=[21,65,34,12]
if(len(x)==len(y)):
    print("The list are of same length ")
else:
    print("The list is not of same length ")


sum1=sum(x)
sum2=sum(y)
if(sum1==sum2):
    print("The list sums to the same value ")
else:
    print("The list sums not to the same value ")

print("common elements are : ")
for i in x:
   for j in y:
      if(i==j):
        print(i)