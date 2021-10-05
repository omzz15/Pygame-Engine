from components.position import Position

class PhysicsSettings:
    def __init__(self, mass = 0, frictionCoeff = 0, bounceCoeff = 0, static = False, collidable = False):
        self.mass = mass
        self.frictionCoeff = frictionCoeff
        self.bounceCoeff = bounceCoeff
        self.static = static
        self.collidable = collidable

class Physics:
    def __init__(self, position = Position(), settings = PhysicsSettings()):
        self.position = position
        self.settings = settings
    
    def 

    def run(self):
        pass