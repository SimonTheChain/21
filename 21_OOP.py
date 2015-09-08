#module needed to randomize an integer
from random import choice

#asks to play again
def credits():
	while True:
		answer = raw_input("\nPlay again?\n(y/n)> ").lower()
		if answer == "n":
			code_exec[0] = False
			raw_input("\nThank you for using this program by Simon Lachaine.\nPress Enter to quit.\n")
			quit()
		elif answer == "y":
			break
		else:
			print '\nExpected "y" or "n", please answer again:'
	return code_exec

#creates a class for the deck of cards
class DeckOfCards(object):
	def __init__(self):
		"""initializes a new deck with a list"""
		self.cards = range(1, 11)

	def reset(self):
		"""resets the values of the decks"""
		self.cards = range(1, 11)
		return self.cards
		
	def deck_to_player(self, playerx_hand, playerx):
		"""selects a value in the deck and transfers it to the player's hand"""
		shuffle = choice(self.cards)
		playerx_hand.append(shuffle)
		playerx.hand += shuffle
		self.deal = (self.cards).remove(shuffle)
		return playerx.hand

#creates a class for the players
class Players(object):
	def __init__(self, name, hand):
		"""allows creation of players objects"""
		self.name = name
		self.hand = hand
	
	def reset_hand(self):
		"""resets the values of the players' hands"""
		self.hand = 0
		return self.hand
	
	def read_hand(self, playerx):
		"""displays the value of the player's hand"""
		return playerx.name + str(playerx.hand) + " in hand."
	
	def win_check1(self, code_exec_x):
		"""checks if certain score conditions have been met"""
		if self.hand > 21:
			print self.name + "busted!"
			code_exec[1], code_exec[2], code_exec[3] = False, False, False
			credits()
		elif self.hand == 21:
			print self.name + "won!"
			code_exec[1], code_exec[2], code_exec[3] = False, False, False
			credits()
		return code_exec

#creates objects from the classes
deck1 = DeckOfCards()
deck2 = DeckOfCards()
player1 = Players("\nYou have ", 0)
player2 = Players("\nDealer has ", 0)

#presents the game to the user
raw_input("""\nThis is a simplified version of Blackjack.
Instead of receiving cards, you receive a random number from 1 to 10.
You'll start with two "cards"; try to reach 21 without going over!
\nPress Enter to start.""")

#sets the loop for the main program
code_exec = [True, True, True, True]
while code_exec[0] == True:
	
	#resets the values each round
	deck1.reset()
	deck2.reset()
	player1.reset_hand()
	player2.reset_hand()
	player1_hand = []
	player2_hand = []
	
	#list: [0]=program loop, [1]=player's turn, [2]=player2's turn, [3]=end results
	code_exec = [True, True, True, True]

	#bumper for each game
	print "\n|----------|-new game-|----------|"
	
	#player's turn
	deck1.deck_to_player(player1_hand, player1)
	while code_exec[1] == True:
		deck1.deck_to_player(player1_hand, player1)
		print "\nYour hand:", player1_hand
		print player1.read_hand(player1)
		player1.win_check1(1)
		if code_exec[1] == True:
			while True:
				answer = raw_input("\nDo you want another number?\n(y/n)> ").lower()
				if answer == "y":
					break
				elif answer == "n":
					code_exec[1] = False
					break
				else:
					print "\nUnrecognized input, please answer again."
			
	#dealer's turn
	if code_exec[2] == True:
		print "\nDealer's turn:"
		deck2.deck_to_player(player2_hand, player2)
		deck2.deck_to_player(player2_hand, player2)
		print "\nDealer's hand:", player2_hand
		print player2.read_hand(player2)
		while player2.hand < 17:
			raw_input("Press Enter.")
			deck2.deck_to_player(player2_hand, player2)
			print "\nDealer's hand:", player2_hand
			print player2.read_hand(player2)
			player2.win_check1(2)

	#checks the end results
	if code_exec[3] == True:
		print "\nResults:%s%s" % (player1.read_hand(player1), player2.read_hand(player2))
		if player1.hand > player2.hand:
			print player1.name + "won!"
		elif player1.hand < player2.hand:
			print player1.name + "lost!"
		elif player1.hand == player2.hand:
			print "\nTie game."
		credits()
