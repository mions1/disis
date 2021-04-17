from card import Card
from deck import Deck

class Player():

	def __init__(self, id: int, name: str, score: int, cards: list):
		""" Player defines a player.

		Args:
			id (int): player id (incremental int)
			name (str): name of the player
			score (int): player's points
			cards (list): cards in player's hand
		"""
		self.id = id
		self.name = name
		self.score = score
		self.cards = cards

	def draw_a_card(self, deck: Deck):
		""" Player pick a card from the deck and add it to his hand

		Args:
			deck (Deck): deck from which pick the card
		"""
		card = deck.pick_a_card()
		card.owner = self
		self.cards.append(card)

	def play_a_card(self, card: Card):
		""" Play a card, so the chosen card in the hand

		Args:
			card (Card): chosen card

		Returns:
			bool: True if it's okay, False otherwise
		"""
		if card in self.cards:
			card.removed = True
			return True
		return False

	def __str__(self):
		text = str(self.id) + " "
		text += self.name + " "
		text += str(self.score) + " "
		text += "["
		for card in self.cards:
			text += str(card) + ", "
		return text
