#modules needed for the randomization
from random import choice
from random import shuffle

#asks to play again
def credits():
	"""saves the results if wanted"""
	while True:
		answer = raw_input("\nPlay again?\n(y/n)> ").lower()
		if answer == "n":
			print "\nFinal scores:\n|--Rounds--|---", player1.attempts, \
			"----|----------|\n|---You----|---", player1.wins, \
			"----|----------|\n|--Dealer--|---", player2.wins , "----|----------|\n"
			while True:
				save_answer = raw_input("\nWould you like to save your results?\n(y/n)> ").lower()
				if save_answer == "y":
					with open("blackjack_scores.txt", "w") as blackjack_scores:
						blackjack_scores.write(str(player1.attempts))
						blackjack_scores.write("\n")
						blackjack_scores.write(str(player1.wins))
						blackjack_scores.write("\n")
						blackjack_scores.write(str(player2.wins))
						blackjack_scores.write("\n")
					break
				elif save_answer == "n":
					break
				else:
					print '\nExpected "y" or "n", please answer again:'
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
		"""initializes the deck"""
		self.deck = {
			"spades": [],
			"hearts": [],
			"diamonds": [],
			"clubs": []
		}
		for i in range(1, 53):
			"""distributes the values in the suits"""
			suit = i % 4
			face = i % 13
			if suit == 0:
				self.deck["spades"].append(face)
			elif suit == 1:
				self.deck["hearts"].append(face)
			elif suit == 2:
				self.deck["diamonds"].append(face)
			elif suit == 3:
				self.deck["clubs"].append(face)

	def shuffle_deck(self):
		"""shuffles the deck"""
		shuffle(self.deck["spades"])
		shuffle(self.deck["hearts"])
		shuffle(self.deck["diamonds"])
		shuffle(self.deck["clubs"])
		return self.deck

	def deck_to_player(self, playerx):
		"""selects a card in the deck and transfers it to the player's hand"""
		card_suit = choice(self.deck.keys())
		card = choice(self.deck[card_suit])
		if card == 0:
			card_name = "King"
		elif card == 12:
			card_name = "Queen"
		elif card == 11:
			card_name = "Jack"
		elif card == 1:
			card_name = "Ace"
		else:
			card_name = str(card)
		prehand = []
		prehand.append(card_name)
		prehand.append("of")
		prehand.append(card_suit)
		prehand = " ".join(prehand)
		playerx.hand.append(prehand)
		self.deck[card_suit].remove(card)
		if card == 0 or card == 11 or card == 12:
			card = 10
			playerx.hand_score += card
		elif card == 1:
			card = 11
			playerx.hand_score += card
		else:
			playerx.hand_score += card
		return playerx.hand_score
		
	def reset(self):
		"""resets the values of the deck"""
		self.__init__()
		return self.deck
		
#creates a class for the players
class Players(object):
	def __init__(self, name, hand_score, wins, attempts):
		"""allows creation of players objects"""
		self.name = name
		self.hand_score = hand_score
		self.wins = wins
		self.attempts = attempts
		self.hand = []
	
	def reset_hand(self):
		"""resets the values of the players' hands"""
		self.hand = []
		self.hand_score = 0
		return self.hand_score
	
	def read_hand(self, playerx):
		"""returns the value of the player's hand"""
		return playerx.name + str(playerx.hand_score) + " in hand."
	
	def ace(self, code_exec_x, playerx):
		"""adjusts the value of the ace"""
		if self.hand_score > 21:
			if any("Ace" in word for word in playerx.hand):
				self.hand_score = self.hand_score - 10
				code_exec[code_exec_x] = False
		return self.hand_score
	
	def win_check(self, playerx):
		"""checks if certain score conditions have been met"""
		if self.hand_score > 21:
			print self.name + "busted!"
			playerx.wins += 1
			code_exec[0], code_exec[2], code_exec[4] = False, False, False
			credits()
		elif self.hand_score == 21:
			self.wins += 1
			print self.name + "won!"
			code_exec[0], code_exec[2], code_exec[4] = False, False, False
			credits()
		return code_exec

#creates objects from the classes
deck1 = DeckOfCards()
player1 = Players("\nYou have ", 0, 0, 0)
player2 = Players("\nDealer has ", 0, 0, 0)

#presents the game to the user
raw_input("""\nWelcome to Blackjack!\n
You first receive two random cards, then you can ask for more.
Try to reach 21 without going over!
The dealer will take a card until he reaches 17.
Try to win more rounds than him!
\nPress Enter to start.""")

#asks to load a previous game
while True:
	load_answer = raw_input("\nDo you want to load a previous game?\n(y/n)> ")
	if load_answer == "y":
		try:
			with open("blackjack_scores.txt", "r") as blackjack_scores:
				player1.attempts = int(blackjack_scores.readlines()[0])
				blackjack_scores.seek(0)
				player1.wins = int(blackjack_scores.readlines()[1])
				blackjack_scores.seek(0)
				player2.wins = int(blackjack_scores.readlines()[2])
			print "\n|----------|-load game|----------|"
		except IOError:
			print "\nNo saved games to load."
		break
	elif load_answer == "n":
		print "\n|----------|-new game-|----------|"
		break
	else:
		print '\nExpected "y" or "n", please answer again:'

#sets the loop for the main program
while True:
	
	#resets the values each round
	deck1.reset()
	deck1.shuffle_deck()
	player1.reset_hand()
	player2.reset_hand()
	
	#list: [0]=program loop, [1]=player's turn, [2]=player2's turn, [3]=end results
	code_exec = [True, True, True, True, True]

	#updates the number of rounds played
	player1.attempts += 1
	
	#bumper for each round
	print "\n|----------|-new round|----------|\n|--Round---|---", player1.attempts, \
	"----|----------|\n|---You----|---", player1.wins, \
	"----|----------|\n|--Dealer--|---", player2.wins, "----|----------|\n"
		
	#player's turn
	deck1.deck_to_player(player1)
	while code_exec[0] == True:
		deck1.deck_to_player(player1)
		print "\nYour hand:", ", ".join(player1.hand)
		if code_exec[1] == True:
			player1.ace(1, player1)
		print player1.read_hand(player1)
		player1.win_check(player2)
		if code_exec[0] == True:
			while True:
				answer = raw_input("\nDo you want another card?\n(y/n)> ").lower()
				if answer == "y":
					break
				elif answer == "n":
					code_exec[0] = False
					break
				else:
					print "\nUnrecognized input, please answer again."
			
	#dealer's turn
	if code_exec[2] == True:
		print "\nDealer's turn:"
		deck1.deck_to_player(player2)
		deck1.deck_to_player(player2)
		print "\nDealer's hand:", ", ".join(player2.hand)
		print player2.read_hand(player2)
		player2.win_check(player1)
		while player2.hand_score < 17:
			raw_input("Press Enter.")
			deck1.deck_to_player(player2)
			print "\nDealer's hand:", ", ".join(player2.hand)
			if code_exec[3] == True:
				player2.ace(3, player2)
			print player2.read_hand(player2)
			player2.win_check(player1)

	#checks the end results
	if code_exec[4] == True:
		print "\nResults:%s%s" % (player1.read_hand(player1), player2.read_hand(player2))
		if player1.hand_score > player2.hand_score:
			print player1.name + "won!"
			player1.wins += 1
		elif player1.hand_score < player2.hand_score:
			print player1.name + "lost!"
			player2.wins += 1
		elif player1.hand_score == player2.hand_score:
			print "\nTie game."
		credits()
