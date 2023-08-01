def binomial_function(n,k):
  num=1 #Numerador
  den=1 #Denominador
  for x in range(k):
    num*=(n-x)
    den*=(x+1)
  return int(num/den)

def Pascal_triangle(m):

  for i in range(1,m+1):
    for j in range(i+1):
      print(binomial_function(i,j),end=" ") #Así los pone seguidos
    print(" ")

Pascal_triangle(5)

# Probabilities of a tossed coin
n=100 #It n=1 and k=1 --> P1=0.5, lo que es de esperar
k=60
P1=binomial_function(n,k)/(2**n)
print(f'The probability is {P1}')

#Probability that it comes up heads 60 or more times. I think this is the sum of probabilities
sum=0
for h in range(60,101):
  P1=binomial_function(n,h)/(2**n)
  sum+=P1
print(f'The acumulative probability is {sum}')