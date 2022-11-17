str1=input("Enter the string")
dict={}
str1_list=str1.split(' ')
print(str1_list)
for n in str1_list:
    if n in dict:
      dict[n]+=1
    else:
        dict[n]=1
for m,n in dict.items():
    print(m,n)




