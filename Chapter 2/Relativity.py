from math import *

light_years=float(input("Enter the distance in light years (x=ac, enter a):"))
speed=float(input("Enter the speed as a fraction of the speed of light c (v=ac, enter a): "))

#Observer in Earth
time_earth=light_years/speed
#Observer on board
distance=light_years*sqrt(1-speed**2)
time_board=distance/speed
print(f"From Earth the time observed: {time_earth}, and from the spaceship the time observed: {time_board}")