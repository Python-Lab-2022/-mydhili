a=float(input("enter the side:"))
s_area=lambda a:a*a
print("Area of square=",s_area(a))
l=float(input("enter the length"))
w=float(input("enter the width"))
r_area=lambda l,w:l*w
print("Area of rectangle=",r_area(l,w))
b=float(input("Enter the base:"))
h=float(input("enter the height:"))
t_area=lambda b,h:(h*b)/2
print("Area of triangle=",t_area(b,h))