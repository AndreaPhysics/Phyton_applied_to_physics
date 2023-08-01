from numpy import loadtxt
from pylab import *

data=loadtxt("millikan.txt",float)
x=data[:,0]
y=data[:,1]
N=len(x)
plot(x,y,'k.')

#b) Ex, Ey, Exx, Exy
Ex=sum(x)/N
Ey=sum(y)/N
Exx=sum(x*x)/N
Exy=sum(x*y)/N
m=(Exy-Ex*Ey)/(Exx-Ex**2)
c=(Exx*Ey-Ex*Exy)/(Exx-Ex**2)
y_points=m*x+c
plot(x,y_points,'b-')

show()
e=1.602e-19
print(f'La constante de Planck obtenida es h={m*e}')