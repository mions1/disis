from player import Player
from card import Card

class Board():
	
	def __init__(self, players: list, player_in_turn: Player):
		""" Board defines the board of the game.

		Args:
			players (list): list of players
			cards (list): list of played cards of the turn
			player_in_turn (Player): player who chose the theme
		"""
		self.players = players
		self.cards = dict()
		self.player_in_turn = player_in_turn

	def play_a_card(self, card: Card, player: Player):
		""" Add the player's card to the played cards around the board

		Args:
			card (Card): played card
			player (Player): player who plays the card
		"""
		card.position = len(self.cards)+1
		self.cards[player] = card
		player.play_a_card(card)

	def get_ranking(self):
		""" Get ranking, so a players (keys) dict in ascending order by 
		    score (value)

		Returns:
			dict: dict of the ranking. Key=player Value=score
		"""
		rank = dict()
		for player in self.players:
			rank[player] = player.score

		rank = dict(sorted(rank.items(), key=lambda item: item[1], reverse=True))

		return rank

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