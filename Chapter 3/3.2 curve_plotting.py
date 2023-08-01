from numpy import *
from pylab import *
theta=linspace(0,2*pi,100)

x=2*cos(theta)+cos(2*theta)
y=2*sin(theta)-sin(2*theta)
plot(x,y)
xlabel('x')
ylabel('y')
title('X frente a Y')
show()

#b)
theta=linspace(0,10*pi,1000)
r=theta*theta
x=r*cos(theta)
y=r*sin(theta)
plot(x,y)
xlabel('x')
ylabel('y')
title('r=theta^2')
show()

#c) Fey's function
theta=linspace(0,24*pi,2000)
r=exp(cos(theta))-2*cos(4*theta)+(sin(theta/12))**5
x=r*cos(theta)
y=r*sin(theta)
plot(x,y)
xlabel('x')
ylabel('y')
title('Feys function')
show()