
class Card():

	def __init__(self, id: int, img: str, owner, position: int):
		""" Card defines a card.

		Args:
			id (int): card id (incremental int)
			img (str): path of the card img
			owner (int): card owner player, or None if in the deck/used
			position (int): when it is played, the position to vote
			removed (bool): if the card is used in this turn, so removed before next
		"""
		self.id = id
		self.img = img
		self.owner = owner
		self.position = position
		self.removed = False

	def __str__(self):
		text = str(self.id) + " "
		text += self.img + " "
		#text += str(self.owner) + " "
		text += str(self.position) + " "
		return text
