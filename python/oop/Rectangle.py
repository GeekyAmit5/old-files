class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

rect1 =  rectangle(int(input("Enter length of First Rectangle : ")),int(input("Enter breadth of First Rectangle : ")))
rect2 =  rectangle(int(input("Enter length of Second Rectangle : ")),int(input("Enter breadth of Second Rectangle : ")))

print("Area of First Rectangle is : ",rect1.length*rect1.breadth)
print("Area of Second Rectangle is : ",rect2.length*rect2.breadth)

print("Perimeter of First Rectangle is : ",2*(rect1.length+rect1.breadth))
print("Perimeter of Second Rectangle is : ",2*(rect2.length+rect2.breadth))