from math import *
from numpy import *
from pylab import *
from gaussian_cuadrature import gaussxwab
#a)
def f(a,x):
  return x**(a-1)*exp(-x)

spacing=0.1
x=arange(0,5+spacing,spacing)

Int=[]
maximum=empty([3])
index=empty([3])
for i in range(2,5):
  for j in x:
    Int.append(f(i,j))
  plot(x,Int)
  maximum[i-2]=array(Int).max()
  index[i-2]=array(Int).argmax()
  Int.clear()
xlabel('x')
ylabel('Integrand')
plot(x[int(index[0])],maximum[0],'ko')
plot(x[int(index[1])],maximum[1],'ko')
plot(x[int(index[2])],maximum[2],'ko')
show()
#Si intentamos usar max(Int) no podemos, esto creo que es por haber importado de forma genérica the numpy package. Si hacemos import numpy as np (como en todas partes) me imagino que sí se podrá usar

#c) If we do some calculus, we can see that c must be the value of the maximums if we want the peaks to be located at z=1/2 (and, as a consequence, this method works properly)
def f2(a,c,z):
  return exp((a-1)*log(z*c/(1-z))-z*c/(1-z))*((c*(1-z)+z*c)/(1-z)**2)

def gamma(a):
  N=100
  a0=0.0
  b0=1.0
  x_gauss,w_gauss=gaussxwab(N,a0,b0)
  s=0.0
  #We want to know gamma(a) for that we need an accurate value of c, we look for the maximum value in each case
  x=arange(0,20,0.1)
  Integrand=[]
  for j in x:
    Integrand.append(f(a,j))
  index=array(Integrand).argmax()

  c=x[index]
  for k in range(N):
    s+=w_gauss[k]*f2(a,c,x_gauss[k])
  print(f'gamma({a})={s}')

gamma(3/2)

#d) gamma(3)=2!, gamma(6)=5!, gamma(10)=9!
gamma(3)
gamma(6)
gamma(10)