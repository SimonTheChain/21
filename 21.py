#module needed to randomize an integer
from random import randint

#defines a random number between 1 and 10
def random_number():
	return randint(1, 10)

#asks if the player wants another card
def player_card():
	while True:
		answer = raw_input("\nDo you want another number?\n(y/n)> ").lower()
		if answer == "y":
			scores[0] += random_number()
			break
		elif answer == "n":
			turns[0] = False
			break
		else:
			print '\nExpected "y" or "n", please answer again:'
	return scores

#deals a number to House if it has less than 17
def house_card():
	if scores[1] < 17:
		scores[1] += random_number()
	elif scores[1] >= 17:
		turns[1] = False
	return scores

#thanks the user and satisfies my ego ;-)
def credits():
	raw_input("\nThank you for using this program by Simon Lachaine.\nPress Enter to quit.\n")
	quit()

#presents the game to the user
raw_input("""\nThis is a simplified version of Blackjack.
Instead of receiving cards, you receive a random number from 1 to 10.
You'll start with two "cards"; try to reach 21 without going over!
\nPress Enter to start.""")

#sets the initial values of the lists
scores = [0, 0]
turns = [True, True]
	
#deals a first hand of 2 random numbers to the player and the house
scores[0], scores[1] = scores[0] + random_number() + random_number(), \
scores[1] + random_number() + random_number()

#player's turn
while turns[0] == True:
	print "\nYou have " + str(scores[0])
	player_card()
	if scores[0] > 21:
		print "\nYou have " + str(scores[0]) + "\nYou busted, you lose!"
		credits()
	elif scores[0] == 21:
		print "\nYou have " + str(scores[0]), "\nYou win!"
		credits()

#house's turn
print "\nHouse's turn"
while turns[1] == True:
	print "\nHouse has " + str(scores[1])
	raw_input("\nPress Enter")
	house_card()
	if scores[1] > 21:
		print "\nHouse has " + str(scores[1]), "\nHouse busted, you win!"
		credits()

#checks the winning conditions		
if scores[0] > scores[1]:
	print "\nYou have " + str(scores[0]), "\nHouse has " + str(scores[1]), "\nYou win!"
	credits()
elif scores[0] < scores[1]:
	print "\nYou have " + str(scores[0]), "\nHouse has " + str(scores[1]), "\nYou lose."
	credits()
elif scores[0] == scores[1]:
	print "\nYou have " + str(scores[0]), "\nHouse has " + str(scores[1]), "\nTie game."
	credits()
#program end
