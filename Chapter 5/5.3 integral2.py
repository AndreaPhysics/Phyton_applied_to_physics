from simpson_integration import simpson_function
from math import *
from numpy import *
from pylab import *

def f(x):
  return x*x

N=100
x=arange(0,3,0.1)
E=[]
for i in range(len(x)):
  E.append(simpson_function(0,x[i],N,f))

#Graph
plot(x,E)
xlabel('x')
ylabel('E(x)')
show()