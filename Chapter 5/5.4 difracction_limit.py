from pylab import *

def func(t,m,x):
  return (1/pi)*cos(m*t-x*sin(t))

def J(m,x):
  a=0
  b=pi
  N=1000
  #func= lambda t : (1/pi)*cos(m*t-x*sin(t))
  h=(b-a)/N
  sum_odd=0
  sum_even=0
  for k in range(1,N,2):
    sum_odd+=func(a+k*h,m,x)
  for k in range(2,N,2):
    sum_even+=func(a+k*h,m,x)
  I=(h/3)*(func(a,m,x)+func(b,m,x)+4*sum_odd+2*sum_even)
  return I

separation=0.1
x=arange(0,20+separation,separation)
J0=empty([len(x),len(x)],float)
for j in range(3):
  for i in range(len(x)):
    J0[i,j]=(J(j,x[i])) #Por columnas

plot(x,J0[:,0])
plot(x,J0[:,1])
plot(x,J0[:,2])
xlabel('x')
ylabel('Ji')
show()

#b)
k=2*pi/500
x=arange(-1000,1000,10)
y=arange(-1000,1000,10)
values=empty([len(x),len(x)],float)
for i in range(len(y)):
  for j in range(len(x)):
    r=sqrt(x[j]**2+y[i]**2)
    if r==0:
      I=1/2
    else:
      I=(J(1,k*r)/(k*r))**2
    values[i,j]=I

imshow(values, origin="lower",vmax=0.01)
show()