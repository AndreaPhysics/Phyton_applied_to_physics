from pylab import *
from numpy import *
step=0.01
r=arange(1,4,step)
x=1/2

x_obtenidas=[]
x_obtenidas_2=[]
for i in r:
  x=1/2
  for j in range(1000):
    x=i*x*(1-x)
  for k in range(100):
    x=i*x*(1-x)
    plot(i,x,'k.')
show()