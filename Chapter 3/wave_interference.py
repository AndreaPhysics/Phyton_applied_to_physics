from numpy import *
from pylab import imshow, show
#Initial values
points=500
separation=20.0 #cm between the centers
side=100.0 #cm 
space=side/points
wavelength=5
amplitude=1
k=2*pi/wavelength

#Height of the different points in the grid
xi=empty([points,points],float)

#Cálculos
x1=side/2+separation/2 #x coordinate for the first drop
y1=side/2 #y coordinate for the first drop
x2=side/2-separation/2
y2=side/2 

r1=[]
for i in range(int(points)):
  y=i*space
  for j in range(int(points)):
    x=j*space
    r1=sqrt((x-x1)**2+(y-y1)**2)
    r2=sqrt((x-x2)**2+(y-y2)**2)
    xi[i,j]=amplitude*sin(k*r1)+amplitude*sin(k*r2)

#Representation
imshow(xi, origin="lower",extent=[0,side,0,side])
show()