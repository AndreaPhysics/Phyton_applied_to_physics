from numpy import loadtxt
from pylab import *
a=loadtxt("sunspots.txt", float)
month=a[:,0]
number_sunspot=a[:,1]

#Representation
#plot(month,number_sunspot)

#Only the first 1000 data points 
plot(month[0:1000],number_sunspot[0:1000])

#Running average of the data
window=5
m=list(range(-window,window,1))

average=[]
for i in range(len(number_sunspot[0:1000])):
  sum=0
  number=2*window
  for j in m:
    if i+j<0 or i+j>1000:
      number-=1
    elif i+j>=0 and i+j<=1000:
      sum=sum+number_sunspot[i+j]
  average.append(sum/number)

plot(month[0:1000],average)
show()