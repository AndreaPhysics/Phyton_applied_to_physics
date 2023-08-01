def mass_formula(A, Z):
  a1, a2, a3, a4 =15.8, 18.3, 0.714, 23.2
  if A%2!=0:
    a5=0
  elif A%2==0 and Z%2==0:
    a5=12.0
  else:
    a5=-12.0
  B=a1*A-a2*A**(2/3)-a3*(Z**2)/(A**(1/3))-a4*(A-2*Z)**2/A+a5/(A**(1/2))
  return B, B/A

#Values
A, Z= 58, 28
print(f'B={mass_formula(A,Z)[0]} MeV')
print(f'B/A={mass_formula(A,Z)[1]}')


def mass_formula_2(Z):
  a1, a2, a3, a4 =15.8, 18.3, 0.714, 23.2

  #Find the largest B
  Avalues=list(range(Z, 3*Z+1, 1)) #CUIDADO, PONER EL +1
  B=[]
  for x in Avalues:
    if x%2!=0:
      a5=0
    elif x%2==0 and Z%2==0:
      a5=12.0
    else:
      a5=-12.0
    B.append(a1*x-a2*x**(2/3)-a3*(Z**2)/(x**(1/3))-a4*(x-2*Z)**2/x+a5/(x**(1/2)))

  return max(B) , Avalues[B.index(max(B))]
  
print(mass_formula_2(28)) #Largest B and it's corresponding value of A

#Another way to do it
"""for i in range(len(Avalues)-1):
    if Avalues[i]%2!=0:
      a5=0
    elif Avalues[i]%2==0 and Z%2==0:
      a5=12.0
    else:
      a5=-12.0
    B.append(a1*Avalues[i]-a2*Avalues[i]**(2/3)-a3*(Z**2)/(Avalues[i]**(1/3))-a4*(Avalues[i]-2*Z)**2/Avalues[i]+a5/(Avalues[i]**(1/2)))

  return max(B) , Avalues[B.index(max(B))]""" 

def mass_function_3(Z):
  a1, a2, a3, a4 =15.8, 18.3, 0.714, 23.2
  B=[]
  BA=[]
  Max_Avalues=[]
  Max_Bvalues=[]
  Max_BAvalues=[]
  for y in Z:
    B.clear()
    BA.clear()
    Avalues=list(range(y,3*y+1,1))
    for x in Avalues:
      if x%2!=0:
        a5=0
      elif x%2==0 and y%2==0:
        a5=12.0
      else:
        a5=-12.0
      B.append(a1*x-a2*x**(2/3)-a3*(y**2)/(x**(1/3))-a4*(x-2*y)**2/x+a5/(x**(1/2)))
      BA.append((a1*x-a2*x**(2/3)-a3*(y**2)/(x**(1/3))-a4*(x-2*y)**2/x+a5/(x**(1/2)))/x)
    
    Max_Avalues.append(Avalues[B.index(max(B))])
    Max_Bvalues.append(max(B))
    Max_BAvalues.append(max(BA))
  
  #print(Max_Avalues)
  #print(Max_Bvalues)
  #print(Max_BAvalues)
  print(Z[Max_BAvalues.index(max(Max_BAvalues))])

Z=list(range(1,101))
mass_function_3(Z)
# We have just proved that the maximum binding energy per nucleon occurs for Nickel Z=28