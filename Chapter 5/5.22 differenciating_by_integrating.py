from cmath import *
from math import factorial
from numpy import *

def f(z):
  return exp(2*z)

def derivadas_cauchy(m,N):
  #m: derivada de grado m
  #N: number of slices
  sum=0.0
  for k in range(N):
    z=exp(1j*2*pi*k/N)
    sum+=f(z)*exp(-1j*2*pi*k*m/N)

  deriv=(factorial(m)/N)*sum
  return deriv

#The first 20 derivatives:
N=10000
derivatives=empty([20],float)
for i in range(20):
  derivatives[i]=derivadas_cauchy(i,N)

print(derivatives)
