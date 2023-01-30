class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        self.area=self.length*self.width
        print("Area is :",self.area)
    def __it__(self,other):
        if self.area<other.area:
            return True
        else:
            return False
l1=int(input("Enter the length of first rectangle:"))
w1=int(input("Enter the width of first rectangle:"))
l2=int(input("Enter the length of second rectangle:"))
w2=int(input("Enter the width of second rectangle:"))

o1=rectangle(l1,w1)
o2=rectangle(l2,w2)
o1.area()
o2.area()

