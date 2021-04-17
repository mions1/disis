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
		self.votes = dict()
		self.player_in_turn = player_in_turn
		self.theme = ""

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

	def vote(self, player: Player, vote):
		""" Let the player vote the played cards

		Args:
			player (Player): player who votes
			vote (int): voted card (its position on the table)
		"""
		self.votes[player] = self.get_card_in_position(vote)

	def get_card_in_position(self, position: int):
		""" Get the card on the specified position (position on the table)

		Args:
			position (int): position of the card on the table

		Returns:
			Card: voted card
		"""
		for card in self.cards.values():
			if card.position == position:
				return card

	def reset(self):
		""" Clear the board removing cards, theme, votes and selecting the new player
		    in turn.
		"""
		self.cards = dict()
		self.votes = dict()
		self.player_in_turn = self.players[(self.player_in_turn.id + 1) % len(self.players)]
		self.theme = ""

	def assign_points(self):
		""" Assing points according to the results.

		Returns:
			dict: results after the turn
		"""
		card_in_turn = self.cards[self.player_in_turn]
		points = dict()
		winners = 0
		for player, voted_card in self.votes.items():
			# player has voted the right card, so (MAYBE) the player_in_turn 
			# and him gain 3 points
			if voted_card == card_in_turn:
				winners += 1
				if player not in points:
					points[player] = []
				points[player].append(0)
				player.score += 3
			else:
				if voted_card.owner not in points:
					points[voted_card.owner] = []
				points[voted_card.owner].append(player)
				voted_card.owner.score += 1
		
		if winners > 0 and winners < len(self.players)-1:
			points[self.player_in_turn] = 0
			self.player_in_turn.score += 3
		
		return points

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