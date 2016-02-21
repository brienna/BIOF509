# Learn Python The Hard Way
# Exercise 43: Basic Object-Oriented Analysis and Design
# http://learnpythonthehardway.org/book/ex43.html

# Aliens have invaded a space ship and our hero has to go through a maze 
# of rooms defeating them so he can escape into an escape pod to the planet 
# below. The game will be more like a Zork or Adventure type game with text 
# outputs and funny ways to die. The game will involve an engine that runs 
# a map full of rooms or scenes. Each room will print its own description 
# when the player enters it and then tell the engine what room to run next 
# out of the map.

# Scenes: 
# Death: This is when the player dies and should be something funny.

# Central Corridor: This is the starting point and has a Gothon already 
# standing there they have to defeat with a joke before continuing.

# Laser Weapon Armory: This is where the hero gets a neutron bomb to blow 
# up the ship before getting to the escape pod. It has a keypad the hero 
# has to guess the number for. 

# The Bridge: Another battle scene with a Gothon where the hero places 
# the bomb.

# Escape Pod: Where the hero escapes but only after guessing the right 
# escape pod. 


class Map(object):  # inherits from the class 'object'

	def __init__(self, start_scene):  # necessary for instantiation below
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass


class Engine(object):  # inherits from the class 'object'

	def __init__(self, scene_map):  # necessary for instantiation below

	def play(self):
		pass


class Scene(object):  # inherits from the class 'object'

	def enter(self):
		pass


class Death(Scene):  # inherits from the class 'Scene'

	def enter(self):  # override parent method
		pass


class CentralCorridor(Scene):  # inherits from the class 'Scene'

	def enter(self):  # override parent method
		pass


class LaserWeaponArmory(Scene):  # inherits from the class 'Scene'

	def enter(self):  # override parent method
		pass


class TheBridge(Scene):  # inherits from the class 'Scene'

	def enter(self):  # override parent method 
		pass


class EscapePod(Scene):  # inherits from the class 'Scene'

	def enter(self):  # override parent method
		pass


a_map = Map('central_corridor')  # instantiate Map object
a_game = Engine(a_map)  # instantiate Engine object, passing Map instance
a_game.play()  

