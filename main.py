from GameObject import GameObject

class Test:
	def __init__(self):
		self.test = GameObject(frictionCoeff = 4)
		
	def pr(self):
		print(self.test.frictionCoeff)

t = Test()
t.pr()