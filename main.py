import turtle               #1. import modules
import random

#Part A
window = turtle.Screen() 
window.title("Turtle Race")      # 2.  Create a screen
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

def winner(michelangelo,leonardo):
	return michelangelo.pos() > leonardo.pos()

def positonTurtle(michelangelo,leonardo):
	michelangelo.pos()
	leonardo.pos()
	print("michelangelo position: ",michelangelo.pos())
	print("leonardo.position: ",leonardo.pos()) 
	
def distance(michelangelo,leonardo):
	return michelangelo.pos()-leonardo.pos()
		
# Part B - complete part B here
def main():
	guess = ""
	guesses = False
	while guesses is False:
		guess = str(input("guess the winner: "))
		if (guess == "michelangelo" or guess == "leonardo"):
		 	guesses = True
	michelangelo.down()
	race(michelangelo,leonardo)
	if winner(michelangelo,leonardo):
		print( "MICHELANGELO WINS!")
		leonardo.setpos(-100,200)
		leonardo.write("Winner: Michelangelo",font = ["Arial", 30, "normal"])
		if guess == "michelangelo":
			print("your guess is correct!")
		else:
			print("your guess is wrong!")
	else:
		print( "LEONARDO WINS!")
		leonardo.setpos(-100,200)
		leonardo.write("Winner: Leonardo",font = ["Arial", 30, "normal"])
		if guess == "leonardo":
			print("your guess is correct!")
		else:
			print("your guess is wrong!")
	positonTurtle(michelangelo,leonardo)
	print ("The distance between the winner and the loser is:",  distance(michelangelo,leonardo))
	for shapeSides in [3,4,6,9,12]:
		michelangelo.clear()
		for k in range(shapeSides):
			michelangelo.forward(80)
			michelangelo.right(360/shapeSides)
	window.exitonclick()
	
main()

