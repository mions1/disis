from player import Player
from card import Card
from board import Board
from deck import Deck
import random
from copy import deepcopy
from utilities import print_deck_d, print_players_d

how_many_pg = 3

def init(players: list, cards: list, deck: Deck, board: Board):
	""" Init the game.
	    Creates players according to the number of them.
		Creates cards and add them to the deck.
		Init the board.

	Args:
		players (list): Players list
		cards (list): Cards list
		deck (Deck): Deck filled by cards list
		board (Board): Board game
	"""

	# init cards:
	cards.append(Card(0, "prova0.img", None, None))
	cards.append(Card(1, "prova1.img", None, None))
	cards.append(Card(2, "prova2.img", None, None))
	cards.append(Card(3, "prova3.img", None, None))
	cards.append(Card(4, "prova4.img", None, None))
	cards.append(Card(5, "prova5.img", None, None))
	cards.append(Card(6, "prova6.img", None, None))
	cards.append(Card(7, "prova7.img", None, None))
	cards.append(Card(8, "prova8.img", None, None))
	# init deck
	deck = Deck(cards)
	deck.shuffle()
	print_deck_d(deck)
	# init players
	for i in range(how_many_pg):
		players.append(Player(i, "Player_"+str(i), 0, []))
	for player in players:
		for i in range(2):
			player.draw_a_card(deck)
	print_players_d(players)
	# init board
	board = Board(players, random.choice(players))

	return players, cards, deck, board

def print_board(board: Board):
	""" Print the board and the ranking

	Args:
		board (Board): board game
	"""
	print("\nI giocatori sono cosi classificati: ")
	for player, score in board.get_ranking().items():
		print(player.name, score)

	print("\nLe carte in gioco sono: ")
	for player,card in board.cards.items():
		print(card)

def print_hand(player: Player):
	""" Print the cards in player's hand.

	Args:
		player (Player): player to print him cards
	"""
	print("\n" + player.name + ", le tue carte sono: ")
	for i, card in enumerate(player.cards):
		print(i, card.img)

def play_player_in_turn(board: Board):
	""" The player in turn can choose the theme of the match

	Args:
		boad (Board): board game
	"""
	player = board.player_in_turn
	board.theme = input(player.name + ", scegli il tema: ")

def play_a_card(board: Board, player: Player):
	""" Player chooses a card in his hand to play

	Args:
		board (Board): board game
		player (Player): player playing
	"""
	card_idx = int(input("Gioca una carta: "))
	board.play_a_card(player.cards[card_idx], player)
	print(board.cards)

def vote(board: Board, player: Player):
	""" Let the players vote the played cards

	Args:
		board (Board): board game
		player (Player): Player who have to vote
	"""
	voto = int(input(player.name + ", vota la carta: "))
	board.vote(player, voto)

def print_after_vote(board: Board):
	""" Print results after voting phase

	Args:
		board (Board): board game
	"""
	print("\nIl giocatore " + str(board.player_in_turn.name) 
		+ " ha scelto il tema " + board.theme
		+ " e la carta " + str(board.cards[board.player_in_turn]) 
		+ "\n")
	
	points = board.assign_points()
	if board.player_in_turn in points:
		print("Il giocatore in turno ha guadagnato 3 punti!!")
		del points[board.player_in_turn]
	
	for player, value in points.items():
		score = 0
		if 0 in value:
			print(player.name + " ha indovinato la carta vincente", end="")
			value.remove(0)
			score += 3
		if len(value) > 0 and score == 3:
			print(", inoltre lo ha votato: ")
		if len(value) > 0 and score == 0:
			print("\n" + player.name + " lo ha votato:")
		for p in value:
			print(p.name)
			score += 1
		print("Facendo cosi " + str(score) + " punti")
	
def clean_board(board: Board, players: list, deck: Deck):
	""" Clean the board after every turn.
	    So, remove used cards from both players hand and board.
		All players draw a card.

	Args:
		board (Board): board game
		players (list): players list
	"""
	# remove cards from hands
	for player in players:
		player.remove_cards()
	# reset board
	board.reset()
	# draw
	for player in players:
		player.draw_a_card(deck)

def game(players, cards, deck, board):
	# init game
	players, cards, deck, board = init(players, cards, deck, board)
	print_board(board)

	while True:
		# il giocatore inizia scegliendo il tema
		play_player_in_turn(board)

		# i giocatori, a turno, giocano la propria carta
		for player in players:
			print_hand(player)
			play_a_card(board, player)		
			
		# mostra il tavolo con le carte giocate
		print_board(board)

		# FIXME: Vieta ad un giocatore di votare se stesso
		# i giocatori (tranne che quello in turno) votano
		for player in players:
			if player != board.player_in_turn:
				vote(board, player)

		# stampa i risultati
		print_after_vote(board)

		# resetta il tavolo e pesca le carte
		clean_board(board, players, deck)

		# ripeti


players = []
cards = []
deck = None
board = None

#players, cards, deck, board = init(players, cards, deck, board)
print("\n\n--------------------")

game(players, cards, deck, board)