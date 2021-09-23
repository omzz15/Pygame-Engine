class GameEngine:
	def __init__(self, gameObjects = []):
		self.gameObjects = gameObjects
	
	def runAll(self):
		for gameObject in self.gameObjects:
			gameObject.run()