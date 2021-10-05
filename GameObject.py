from components.physics import *

class GameObject:
	def __init__(self, components):
		self.componets = components
	
	def addComponents(self, component):
		component
		self.components.add(component)

	def run(self):
		for component in self.componets:
			component.run()
		