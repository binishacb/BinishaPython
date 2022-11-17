string=input("Enter the string")
dict={}
for n in string:
    if n in dict:
        dict[n]+=1
        print(dict)
    else:
        dict[n]=1
        print(dict)
print("Character frequency is ")
for m,n in dict.items():
    print(m,n)