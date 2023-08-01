from gaussian_cuadrature import gaussxwab
from numpy import *
from pylab import *
from math import *
def cv(T):
  #The sample in this case has the following properties:
  V=0.001 #m^3
  rho=6.022e-28 #m^-3
  thetaD=428 #K
  N=50 #sample points
  kB=1.3806e-23 #J/K
  a=0.0
  b=thetaD/T
  def f(x):
    return 9*V*rho*kB*((T/thetaD)**3)*(x**4*exp(x))/((exp(x)-1)**2)
  x,w=gaussxwab(N,a,b)
  s=0.0
  for k in range(N):
    s+=w[k]*f(x[k])
  return s

#b)
T=arange(5,500,1)
for i in T:
  I=cv(i)
  plot(i,I,'k.')
xlabel('Temperature')
ylabel('Heat capacity')
show()