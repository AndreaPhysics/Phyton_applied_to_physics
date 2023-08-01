# CHAPTER 2
This chapter simply suggests some easy challenges to get started with Python.

* **Exercise 2.1: Another ball dropped from a tower.** 
A ball is again dropped from a tower of height h with initial velocity zero. Write a
programthat asks the user to enter the height inmeters of the tower and then calculates
and prints the time the ball takes until it hits the ground, ignoring air resistance. Use
your program to calculate the time for a ball dropped from a 100m high tower.
* **Exercise 2.3:**
Write a program to perform the inverse operation to that of Example 2.2.
That is, ask the user for the Cartesian coordinates x, y of a point in two-dimensional
space, and calculate and print the corresponding polar coordinates, with the angle θ
given in degrees.
* **Exercise 2.4:**
A spaceship travels from Earth in a straight line at relativistic speed v to
another planet x light years away. Write a program to ask the user for the value of x
and the speed v as a fraction of the speed of light c, then print out the time in years that
the spaceship takes to reach its destination (a) in the rest frame of an observer on Earth
and (b) as perceived by a passenger on board the ship. Use your program to calculate
the answers for a planet 10 light years away with v = 0.99c.
* **Exercise 2.7: Catalan numbers.**
The Catalan numbers Cn are a sequence of integers 1, 1, 2, 5, 14, 42, 132. . . that play
an important role in quantum mechanics and the theory of disordered systems. (They
were central to EugeneWigner’s proof of the so-called semicircle law.) They are given by
C0 = 1, Cn+1 = (4n + 2)/(n + 2)*Cn.
Write a program that prints in increasing order all Catalan numbers less than or equal
to one billion.
* **Exercise 2.9: The Madelung constant.**
Write a program to calculate and print the Madelung constant for sodium chloride.
Use as large a value of L as you can, while still having your program run in reasonable
time—say in a minute or less.
* **Exercise 2.10: The semi-empirical mass formula**
a) Write a program that takes as its input the values of A and Z, and prints out
the binding energy for the corresponding atom. Use your program to find the
binding energy of an atom with A = 58 and Z = 28. (Hint: The correct answer is
around 500MeV.)
b) Modify your programto print out not the total binding energy B, but the binding
energy per nucleon, which is B/A.
c) Now modify your program so that it takes as input just a single value of the
atomic number Z and then goes through all values of A from A = Z to A = 3Z,
to find the one that has the largest binding energy per nucleon. This is the most
stable nucleus with the given atomic number. Have your program print out the
value of A for this most stable nucleus and the value of the binding energy per
nucleon.
d) Modify your program again so that, instead of taking Z as input, it runs through
all values of Z from 1 to 100 and prints out the most stable value of A for each
one. At what value of Z does the maximum binding energy per nucleon occur?
* **Exercise 2.11: Binomial coefficients**
a) Using this formfor the binomial coefficient, write a Python user-defined function
binomial(n,k) that calculates the binomial coefficient for given n and k. Make
sure your function returns the answer in the form of an integer (not a float) and
gives the correct value of 1 for the case where k = 0.
b) Using your function write a program to print out the first 20 lines of “Pascal’s
triangle.” The nth line of Pascal’s triangle contains n + 1 numbers, which are the
coefficients (n,0), (n,1), and so on up to (n,n).
The probability that an unbiased coin, tossed n times, will come up heads k times
is (n,k)/2^n. Write a program to calculate (a) the total probability that a coin tossed
100 times comes up heads exactly 60 times, and (b) the probability that it comes
up heads 60 or more times.
