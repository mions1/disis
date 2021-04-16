
class Card():

	def __init__(self, id: int, img: str, owner_id: int, position: int):
		self.id = id
		self.img = img
		self.owner_id = owner_id
		self.position = position

	def __str__(self):
		text = str(self.id) + " "
		text += self.img + " "
		text += self.owner_id + " "
		text += str(self.position) + " "
		return text
