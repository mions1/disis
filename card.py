
class Card():

	def __init__(self, id: int, img: str, owner_id: int, position: int):
		""" Card defines a card.

		Args:
			id (int): card id (incremental int)
			img (str): path of the card img
			owner_id (int): id of the owner player, or None if in the deck/used
			position (int): when it is played, the position to vote
		"""
		self.id = id
		self.img = img
		self.owner_id = owner_id
		self.position = position

	def __str__(self):
		text = str(self.id) + " "
		text += self.img + " "
		text += str(self.owner_id) + " "
		text += str(self.position) + " "
		return text
