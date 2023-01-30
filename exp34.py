class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return (2*(self.length+self.breadth))
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
o=rectangle(l,b)
x=o.area()
y=o.perimeter()
print("The area is : ",x)
print("The perimeter is : ",y)

l1=int(input("Enter the length : "))
b1=int(input("Enter the breadth : "))
o1=rectangle(l1,b1)
z=o1.area()
p=o1.perimeter()
print("The area is : ",z)
print("The perimeter is : ",p)

if(x>z):
    print("The first rectangle is greater than second rectangle")
else:
    print("The second rectangle is greater than first rectangle")

