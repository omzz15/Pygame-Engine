from components.position import *

class GameObjectBase:
	def __init__(self, position = Position(), mass = 1, frictionCoeff = 0, bounceCoeff = 0, static = False, collidable = False):
		self.position = position
		self.mass = mass
		self.frictionCoeff = frictionCoeff
		self.bounceCoeff = bounceCoeff
		self.static = static
		self.collidable = collidable

	def render():
		pass