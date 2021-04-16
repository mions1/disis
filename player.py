from card import Card

class Player():

	def __init__(self, id: int, name: str, score: int, cards: list):
		self.id = id
		self.name = name
		self.score = score
		self.cards = cards

	def __str__(self):
		text = str(self.id) + " "
		text += self.name + " "
		text += str(self.score) + " "
		text += "["
		for card in self.cards:
			text += str(card) + ", "
		return text
