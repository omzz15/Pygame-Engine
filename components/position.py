class Position:
	def __init__(self, X = 0, Y = 0):
		self.X = X
		self.Y = Y
	
	def add(self, pos2, returnVal = False):
		if(returnVal):
			return Position(self.X + pos2.X, self.Y + pos2.Y)
		else:
			self.X += pos2.X
			self.Y += pos2.Y

	def subtract(self, pos2, returnVal = False):
		if(returnVal):
			return Position(self.X - pos2.X, self.Y - pos2.Y)
		else:
			self.X -= pos2.X
			self.Y -= pos2.Y

	def multiply(self, factor, returnVal = False):
		if(returnVal):
			return Position(self.X * factor, self.Y * factor)
		else:
			self.X *= factor
			self.Y *= factor

	def divide(self, factor, returnVal = False):
		if(returnVal):
			return Position(self.X / factor, self.Y / factor)
		else:
			self.X /= factor
			self.Y /= factor
	
	def dot_product(self, pos2):
		return (self.X * pos2.X) + (self.Y * pos2.Y)

	def flip(self, returnVal = False):
		if(returnVal):
			return(Position(self.X * -1, self.Y * -1))
		else:
			self.X *= -1
			self.Y *= -1

	def invert(self, returnVal = False):
		if(returnVal):
			return(Position(1 / self.X, 1 / self.Y))
		else:
			self.X = 1 / self.X
			self.Y = 1 / self.Y