from numpy import loadtxt
from pylab import imshow, show
data=loadtxt("stm.txt",float)

imshow(data, origin="lower")
#colorbar()
show()