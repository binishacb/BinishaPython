import csv
c_column = ['ID', 'Name','Age']      #creating the header part
dict_data = [{'ID':1,'Name':'binisha','Age':21},
           {'ID':2,'Name':'amisha','Age':18},
           {'ID':3,'Name':'ammu','Age':25},
           {'ID':4,'Name':'arya','Age':8},
           {'ID':5,'Name':'anna','Age':31},
           {'ID':6,'Name':'ramu','Age':14},
           {'ID':7,'Name':'anu','Age':41},
           {'ID':8,'Name':'binya','Age':20},
           {'ID':9,'Name':'appu','Age':11},
           {'ID':10,'Name':'amil','Age':21}]
try: # keyword to start a file and handling error
    with open("name.csv","w")as f:
        write=csv.DictWriter(f,fieldnames=c_column)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)
except IOError:
    print("input/output error")
d=csv.DictReader(open("name.csv"))
print("csv file output is: ")
for i in d:
    print(i)

