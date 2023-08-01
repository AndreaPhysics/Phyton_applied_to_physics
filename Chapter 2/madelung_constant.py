from numpy import *
from math import sqrt
def madelung(L, a):
  #L: number of atoms in a row
  #a: distance between two consecutive atoms
  sum=0
  for i in range(-L,L+1):
    for j in range(-L,L+1):
      for k in range(-L,L+1):
        if i==0 and j==0 and k==0:
          continue
        elif abs(i+j+k)%2==0:
          sum+=1/(sqrt(i**2+j**2+k**2))
        else:
          sum-=1/(sqrt(i**2+j**2+k**2))
  Mconstant=sum
  return Mconstant

L=10
a=0.000000000564
M=madelung(L,a)
print(f"Madelung constant for a={a} and L={L}: {M} ")