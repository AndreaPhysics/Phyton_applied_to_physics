## Chapter 3
This chapter focuses on graphics and visualization.

* **Exercise 3.1: Plotting experimental data**
In the on-line resources you will find a file called sunspots.txt, which contains the
observed number of sunspots on the Sun for each month since January 1749. The file
contains two columns of numbers, the first being the month and the second being the
sunspot number.
a) Write a program that reads in the data and makes a graph of sunspots as a function
of time.
b) Modify your program to display only the first 1000 data points on the graph.
c) Modify your program further to calculate and plot the running average of the
data, defined by (see link below for the expression) where r = 5 in this case (and the yk are the sunspot numbers). Have the program
plot both the original data and the running average on the same graph, again
over the range covered by the first 1000 data points.
* **Exercise 3.2: Curve plotting**
Although the plot function is designed primarily for plotting standard xy graphs, it
can be adapted for other kinds of plotting as well.
a) Make a plot of the so-called deltoid curve, which is defined parametrically by the
equations
x = 2 cos q + cos 2q, y = 2 sin q − sin 2q,
where 0 ≤ q < 2p. Take a set of values of q between zero and 2p and calculate x
and y for each from the equations above, then plot y as a function of x.
b) Taking this approach a step further, one can make a polar plot r = f (q) for some
function f by calculating r for a range of values of q and then converting r and
q to Cartesian coordinates using the standard equations x = r cos q, y = r sin q.
Use this method to make a plot of the Galilean spiral r = q2 for 0 ≤ q ≤ 10p.
c) Using the same method, make a polar plot of “Fey’s function”
r = ecos q − 2 cos 4q + sin5 q
12
in the range 0 ≤ q ≤ 24p.
* **Exercise 3.3:** There is a file in the on-line resources called stm.txt, which contains a
grid of values from scanning tunneling microscope measurements of the (111) surface
of silicon. A scanning tunneling microscope (STM) is a device that measures the shape
of a surface at the atomic level by tracking a sharp tip over the surface and measuring
quantum tunneling current as a function of position. The end result is a grid of values
that represent the height of the surface and the file stm.txt contains just such a grid of
values. Write a program that reads the data contained in the file and makes a density
plot of the values. Use the various options and variants you have learned about tomake
a picture that shows the structure of the silicon surface clearly.
* **Exercise 3.6: Deterministic chaos and the Feigenbaumplot.**
Write a programthat calculates and displays the behavior of the logistic map.
Give answers to the following questions:
a) For a given value of r what would a fixed point look like on the Feigenbaum plot?
How about a limit cycle? And what would chaos look like?
b) Based on your plot, at what value of r does the system move from orderly behavior
(fixed points or limit cycles) to chaotic behavior? This point is sometimes
called the “edge of chaos.”
* **Exercise 3.7: The Mandelbrot set.**
Write a programtomake an image of theMandelbrot set by performing the iteration
for all values of c = x + iy on an N × N grid spanning the region where −2 ≤ x ≤ 2
and −2 ≤ y ≤ 2. Make a density plot in which grid points inside the Mandelbrot set
are colored black and those outside are colored white. The Mandelbrot set has a very
distinctive shape that looks something like a beetle with a long snout—you’ll know it
when you see it.
* **Exercise 3.8: Least-squares fitting and the photoelectric effect.**
a) In the on-line resources you will find a file called millikan.txt. The file contains
two columns of numbers, giving the x and y coordinates of a set of data points.
Write a programto read these data points andmake a graph with one dot or circle
for each point.
b) Add code to your program, before the part that makes the graph, to calculate the
quantities Ex, Ey, Exx, and Exy defined above, and from them calculate and print
out the slope m and intercept c of the best-fit line.
c) Now write code that goes through each of the data points in turn and evaluates
the quantity mxi + c using the values of m and c that you calculated. Store these
values in a new array or list, and then graph this new array, as a solid line, on the
same plot as the original data. You should end up with a plot of the data points
plus a straight line that runs through them.
d)The data in the file millikan.txt are taken from a historic experiment by Robert
Millikan that measured the photoelectric effect. Calculate from Millikan’s experimental
data a value for Planck’s constant.
