class GameObject:
	def __init__(self, mass = 1, frictionCoeff = 0, bounceCoeff = 0, , static = False, collider = None):
		self.mass = mass
		self.frictionCoeff = frictionCoeff
		self.bounceCoeff = bounceCoeff
		self.static = static
		self.collidable = collidable
	
	def run(self):
		