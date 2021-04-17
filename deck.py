import random

from card import Card

class Deck():
	def __init__(self, cards: list):
		""" Deck defines the cards deck.

		Args:
			cards (list): list of cards in the deck
		"""
		self.cards = cards

	def shuffle(self):
		""" Shuffle the deck
		"""
		random.shuffle(self.cards)

	def pick_a_card(self):
		""" Pick a card on the top of the deck

		Returns:
			Card: picked card on the top of the deck
		"""
		card = self.cards.pop()
		return card

	def __str__(self):
		text = ""
		for card in self.cards:
			text += str(card) + ", "
		return text