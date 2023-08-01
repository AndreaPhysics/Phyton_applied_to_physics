# Ball_tower
height=float(input("The height of the tower: "))
time=float(input("Time: "))

# x=x0+v0t+1/2 at^2
g=9.81
position=height-(1/2)*g*time
print(f"The ball's position is {position}")