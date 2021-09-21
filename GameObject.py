class GameObject:
	def __init__(self, mass = 1, friction = 0, static = False, collidable = False):
		self.mass = mass
		self.static = static
		self.collidable = collidable

	def __init__(self):
		self.mass = 5

class t:
	def __init__(self):
		self.m = GameObject()
		self.t = GameObject(1,1,1,1)