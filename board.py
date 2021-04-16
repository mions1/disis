from player import Player
from card import Card

class Board():
	
	def __init__(self, players: list, cards: list, player_in_turn: Player):
		self.players = players
		self.cards = cards
		self.player_in_turn = player_in_turn

	def __str__(self):
		text = "["
		for player in self.players:
			text += str(player) + ", "
		text += "] ["
		for card in cards:
			text += str(card) + ", "
		text += "] "
		text += str(self.player_in_turn)
		return text