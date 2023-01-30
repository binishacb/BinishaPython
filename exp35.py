class bank:
    def __init__(self,acno,name,actype):
        self.acno=acno
        self.name=name
        self.actype=actype
        self.bal=0
    def printamount(self):
        print("Account holder name: ",self.name)
        print("Account number : ",self.acno)
        print("Account type : ",self.actype)
        print("Your balance amount : ",self.bal)
    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withd(self,w1):
        self.bal=self.bal-w1
        return self.bal

n=input("Enter your name : ")
a=int(input("Enter your account no. : "))
t=input("Enter your account type : ")
o=bank(a,n,t)
o.printamount()
while(True):
    print("MENU")
    print("\n 1.Deposit \n 2.withdraw ")
    c=int(input("Enter your choice: "))

    if(c==1):
        d=int(input("Enter the amount to deposit : "))
        print("your total balance amount is", o.dep(d))
    elif(c==2):
        w=int(input("Enter the amount to be withdrawn : "))
        if(w>d):
            print("insufficient balance ")
        else:
            print("your total balance amount is :",o.withd(w))
    else:
        print("enter a invalid choice ")



