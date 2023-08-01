from math import *
from numpy import *
from pylab import *
from gaussian_cuadrature import gaussxwab
def C(t):
  return cos((pi*t**2)/2)
def S(t):
  return sin((pi*t**2)/2)

wavelength=1
z=3
spacing=0.1
a=0.0
N=50
x=arange(-5,5+spacing,spacing)
I_I0=[]
for i in range(len(x)):
  u=x[i]*sqrt(2/(wavelength*z))
  #C, S
  xx,w=gaussxwab(N,a,u)
  s1=0.0
  s2=0.0
  for k in range(N):
    s1+=w[k]+C(xx[k])
    s2+=w[k]+S(xx[k])
  I_I0.append((1/8)*((2*s1+1)**2+(2*s2+1)**2))

plot(x,I_I0)
xlabel('Intensity')
ylabel('x')
show()