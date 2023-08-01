from pylab import *
from numpy import *
from cmath import *
from math import log
N=1000
iterations=100
side=4
spacing=side/N

xs=arange(-2,2+spacing,spacing)
ys=arange(-2,2+spacing,spacing)

points=empty([len(ys),len(xs)],int)
for i in range(len(ys)):
  for j in range(len(xs)):
    z=complex(0,0)
    it=0
    for k in range(iterations):
      z=z**2+complex(xs[j],ys[i])
      it+=1
      if abs(z)>=2:
        points[i,j]=it#log(it)
        break
    if abs(z)<2:
      points[i,j]=0

imshow(points,origin="lower",extent=[-2,2,-2,2])
jet()
show()