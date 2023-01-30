str=input("Enter the string:")
dic={}
a=str.split()
print(a)
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i] = 1
print(dic)
print("Word frequency:")
for x,y in dic.items():
    print(x,y)
