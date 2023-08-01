from numpy import *
from gaussian_cuadrature import gaussxwab
from pylab import *
#Apartado a)Done on my notebook (contact me if you need the answer)
#b)
def f(x,a):
  m=1
  return sqrt(8*m)*(1/sqrt(a**4-x**4))

N=50 #sample points
spacing=0.01
a=arange(0+spacing,2+spacing,spacing) #Puntos finales
b=0 #Punto inicial
Int=[]
for i in a:
  x,w=gaussxwab(N,b,i)
  s=0.0
  for k in range(N):
    s+=w[k]*f(x[k],i)
  Int.append(s)

plot(a,Int)
xlabel('a(m)')
ylabel('T(s)')
show()