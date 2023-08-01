from math import *
from gaussian_cuadrature import gaussxwab
from numpy import *
from pylab import *
#a)
def H(n,x):
  H0=1
  H1=2*x
  if n==0:
    return H0
  elif n<0:
    return
  elif n==1:
    return H1
  else:
    for i in range(n-1):
      Hh=2*x*H1-2*n*H0
      H0=H1
      H1=Hh
    return Hh

def phi(n,x):
  return 1/(sqrt(2**n*factorial(n)*sqrt(pi)))*exp(-x**2/2)*H(n,x)

spacing=0.1
x=arange(-4,4+spacing,spacing)
phi_values=[]
for i in range(4):
  for k in x:
    phi_values.append(phi(i,k))
  plot(x,phi_values)
  phi_values.clear()
xlabel('x')
ylabel('wavefunction')
show()

#b)
n=30
spacing=0.01
x=arange(-10,10+spacing,spacing)
result=[]
for j in x:
  result.append(phi(n,j))
plot(x,result)
xlabel('x')
ylabel('wavefunction')
show()

#c)
def f(n,z):
  return (sin(z)**2/cos(z)**4)*(phi(n,tan(z)))**2

N=100
a=-pi/2
b=pi/2
n=5
x,w=gaussxwab(N,a,b)
s=0.0
for k in range(N):
  s+=w[k]*f(n,x[k])

print(f'Uncertainty: {sqrt(s)}')