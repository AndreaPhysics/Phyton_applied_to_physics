def simpson_function(a,b,N,f):
  if N%2!=0:
    print("N debe ser par")
    return

  h=(b-a)/N
  sum_odd=0
  sum_even=0
  for k in range(1,N,2):
    sum_odd+=f(a+k*h)
  for k in range(2,N,2):
    sum_even+=f(a+k*h)
  I=(h/3)*(f(a)+f(b)+4*sum_odd+2*sum_even)
  return I