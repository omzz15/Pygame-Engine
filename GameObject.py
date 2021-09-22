class GameObject:
	def __init__(self, mass = 1, frictionCoeff = 0, static = False, collidable = False):
		self.mass = mass
		self.frictionCoeff = frictionCoeff
		self.static = static
		self.collidable = collidable