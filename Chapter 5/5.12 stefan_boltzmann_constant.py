from math import exp,pi
from gaussian_cuadrature import gaussxwab
#a) Apartado a mano
#b) Change of variables given in Eq.(5.67)
kB=1.380649e-23
c=3e8
hb=1.05457e-34
def f(z):
  return ((z**3)/(((1-z)**5)*(exp(z/(1-z))-1)))

N=10
a=0
b=1
x,w=gaussxwab(N,a,b)
s=0.0
for k in range(N):
  s+=w[k]+f(x[k])
print(((kB**4)/(4*pi**2*c**2*hb**3))*s)