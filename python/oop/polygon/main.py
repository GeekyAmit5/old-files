
from rectangle import rectangle
from triangle import triangle

t1=triangle()
r1=rectangle()

t1.set(30,20)
r1.set(10,40)
t1.set_color("Black")
r1.set_color("Red")

print("Area of Triangle is : ",t1.area())
print("Area of Rectangle is : ",r1.area())
print("Rectangle is",r1.get_color())
print("Triangle is",t1.get_color())