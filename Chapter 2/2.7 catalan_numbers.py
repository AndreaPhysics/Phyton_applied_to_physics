C0=1
n=0
N=10 #Change this number to show more or less catalan numbers
list_N=list()
while n<=N:
  list_N.append(C0)
  C0=(4*n+2)*C0/(n+2)
  n+=1
print(list_N)
