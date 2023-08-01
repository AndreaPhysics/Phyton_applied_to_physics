# Ball dropping from a tower
height=float(input("Enter the tower's height (m): "))
v0=0

# x=x0+v0t+1/2 at^2
g=9.81
time=(height*2/g)**(1/2)
print(f"The time it takes the ball to reach the ground is: {time}")
