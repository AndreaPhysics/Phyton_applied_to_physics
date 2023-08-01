#This exercise has been modified to adapt it to an exercise I had to do for my electromagnetism university class
from numpy import *
from pylab import *
from math import *
import matplotlib.pyplot as plt

def func_derivative(x,h):
  deriv=empty([len(x)],float)
  #forward difference
  deriv[0]=(x[1]-x[0])/h
  #central difference
  nlen=len(x)
  for i in range(1,nlen-1):
    deriv[i]=(x[i+1]-x[i-1])/(2*h)
  #backward difference
  deriv[nlen-1]=(x[nlen-1]-x[nlen-2])/h
  return deriv


spacing=0.01
x=arange(-0.5,0.5+spacing,spacing)
y=arange(-0.5,0.5+spacing,spacing)

separation=0.1
x1=-separation/2
y1=0
x2=separation/2
y2=0

epsilon0=8.85e-12
q=1
phi=empty([len(y),len(x)],float)
for i in range(len(y)):
  for j in range(len(x)):
    r1=sqrt((y[i]-y1)**2+(x[j]-x1)**2)
    r2=sqrt((y[i]-y2)**2+(x[j]-x2)**2)
    phi[i,j]=q/(4*pi*epsilon0*r1)+q/(4*pi*epsilon0*r2)


imshow(phi, origin="lower",vmax=50e10)

#b) Partial derivatives
dphi_dx=empty([len(y),len(x)],float)
dphi_dy=empty([len(y),len(x)],float)

for i in range(len(y)):
  medio=phi[i,:]
  dphi_dx[i,:]=-func_derivative(medio,spacing)
for j in range(len(x)):
  medio=phi[:,j]
  dphi_dy[:,j]=-func_derivative(medio,spacing)

for i in range(len(y)):
  for j in range(len(x)):
    if abs(dphi_dx[i,j])>10e11:
      dphi_dx[i,j]=0
    if abs(dphi_dy[i,j])>10e11:
      dphi_dy[i,j]=0


"""result=where(dphi_dx==amax(dphi_dx))
dphi_dx[int(result[0]),int(result[1])]=0
result=where(dphi_dy==amax(dphi_dy))
dphi_dy[int(result[0]),int(result[1])]=0
result=where(dphi_dx==amax(dphi_dx))
dphi_dx[int(result[0]),int(result[1])]=0
result=where(dphi_dy==amax(dphi_dy))
dphi_dy[int(result[0]),int(result[1])]=0 """


X,Y=meshgrid(x,y)
# Creating plot
fig, ax = plt.subplots(figsize = (5,5))
ax.quiver(X,Y,dphi_dx,dphi_dy)
ax.plot(x1,y1,'bo')
ax.plot(x2,y2,'bo')
ax.set_title('Quiver plot with one arrow')

# Show plot
plt.show()

#Not finished