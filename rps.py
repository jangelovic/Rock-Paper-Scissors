# Name
# Rock Paper Scissors
# rps.py
# added comment for github
import random 
# Varibles
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]


# Welcome message
# prompt for name
print("Welcome to Rock Paper Scissors")
pName = input("What is your name? ")


# Score Tracker
# Make a function
def printScore()

	# Prints Score:
	print("Score: ")
# Shows player score
	print(pName + ": " + str(pScore))
# Shows computer score
	print("Computer Score: " + str(cScore))	
# Show how many ties
	print("Ties: " + str(ties))

# Game Loop
# loop until q is entered
while True: 
	# prompt for player move (r, q, s, p)
	pMove = input("Enter 'r' for rock, 'p' for paper, 's' for scissors pr 'q' to quit")
# print the score
	printScore()
# check if q is entered if so end the game
	if pMove == 'q':
		break
# get a computer move (random)
	cMove = random.choice(cMoves)
# compare player move wiht the computer move
	# player picks rock
	if pMove == "r":
		print(pName + " picked Rock") 
		if cMove == "rock":
			print("Computer picks Rock")
			print("Tie")
			tie += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print("Paper covers Rock")
			cScore += 1
		else:
			print("Computer picks scissors")
			print("Rocks breaks scissors")
			pScore += 1
	# player picks paper
	if pMove == "p":
		print(pName + " picked Paper") 
		if cMove == "rock":
			print("Computer picks Rock")
			print("Paper covers rock")
			pScore += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print("This is a tie")
			ties += 1
		else:
			print("Computer picks scissors")
			print("Scissors cuts paper")
			cScore += 1
	# player picks scissors
	if pMove == "s":
		print(pName + " picked Scissors") 
		if cMove == "rock":
			print("Computer picks Rock")
			print("Rock beats scissors")
			cScore += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print("Scissors cuts paper")
			pScore += 1
		else:
			print("Computer picks scissors")
			print("This is a tie")
			ties += 1
# check if pMove is vailed
	else:
		print("That is not an option")