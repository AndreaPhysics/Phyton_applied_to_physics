from math import *

r=float(input("Enter the value of r: "))
theta=float(input("Enter the value of theta (degrees): "))

theta=theta*pi/180

#Conversion
x=r*cos(theta)
y=r*sin(theta)
print(f"The converted coordinates are (x,y)={x, y} ")