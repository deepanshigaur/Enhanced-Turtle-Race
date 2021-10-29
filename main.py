import turtle               #1. import modules
import random
import math

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
def race(michelangelo,leonardo):
	for racingTurtles in range (0,10):
		michelangelo.forward(random.randrange(0,10))
		leonardo.forward(random.randrange(0, 10))

		
# Part B - complete part B here

def main():
	michelangelo.down()
	race(michelangelo,leonardo)
	for shapeSides in [3,4,6,9,12]:
		michelangelo.clear()
		for k in range(shapeSides):
			michelangelo.forward(80)
			michelangelo.right(360/shapeSides)
	window.exitonclick()
	
main()

