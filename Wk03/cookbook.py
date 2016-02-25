
class Cookbook(object): 
	"""A class definition for a cookbook. The following attributes are supported:
    
    Attributes:
    name: A string representing the Cookbook's name
    recipes: A list of recipe objects"""

	def __init__(self, name):
		"""Initalize a Cookbook object with name set to the value supplied, and initialize recipes array"""
		self.name = name
		self.recipes = []

	def open(self, recipe_name):
		"""Return a recipe. 

		Arguments received:
		recipe_name -- string representing the recipe name
		"""
		for i in range(len(self.recipes)):
			if self.recipes[i].name == recipe_name:
				return self.recipes[i]

	def add(self, recipe):
		'''Append recipe object to Cookbook instance's recipes array

		Arguments received:
		recipe -- the recipe object to append
		'''
		self.recipes.append(recipe)


class Recipe():
	"""A class definition for a recipe. The following attributes are supported: 

	Attributes: 
	name: a string representing the recipe's name
	ingredients: a dictionary of ingredients the recipe needs 
	equipment: a list of equipment the recipe needs
	instructions: a string representing the instructions 
	servings: an integer representing the number of people the recipe can serve
	nutrition_info: a dictionary of nutrition info for each ingredient
	cooking_time: a float representing cooking time in minutes
	"""

	def __init__(self, name, ingredients, equipment, instructions, servings, cooking_time):
		"""Initialize a Recipe object with name, ingredients, equipment, instructions,
        servings, nutrition_info, prep_time, cooking_time set to the values supplied"""
		self.name = name
		self.ingredients = ingredients  
		self.equipment = equipment
		self.instructions = instructions
		self.servings = servings
		# self.nutrition_info, loops thru ingredients dict to retrieve nutrition info from each ingredient
		self.cooking_time = cooking_time

	def __str__(self):
		"""Return a basic string representation of the Recipe instance"""
		return "Recipe: {0}.\nServes {1}.\nIngredients: {2}.\nInstructions: {3}.\nCooking time: {4} min.".format(self.name, self.servings, self.ingredients, self.instructions, self.cooking_time)


class Ingredient(object):
	'''A class definition for an ingredient. The following attributes are supported:

	Attributes: 
	name: a string representing the ingredient's name
	quantity: a string representing the quantity of ingredient needed
	nutrition_info: a string representing nutrition info of ingredient
	'''

	def __init__(self, name, quantity, nutrition_info):
		'''Initialize a Ingredient object with name, quantity, nutrition_info set to values supplied'''
		self.name = name
		self.quantity = quantity
		self.nutrition_info = nutrition_info

	def __str__(self):
		'''Return a basic string representation of the Ingredient instance'''
		pass

	def scale(self, old_servings, new_servings):
		'''Scales quantity of ingredient according to new/old serving sizes

		Arguments accepted:
		old_servings -- an integer representing the number of people the recipe can currently serve
		new_servings -- 'an integer representing the number of people the recipe needs to serve'''
		pass

	def convert(self):
		'''Converts quantity of ingredient from metric to imperial, or vice versa'''
		pass


# create banana bread recipe
flour = Ingredient('flour', '2 cups', 'flour nutrition info')
baking_soda = Ingredient('baking soda', '1 tsp', 'baking soda nutrition info')
salt = Ingredient('salt', '1/4 tsp', 'salt nutrition info')
butter = Ingredient('butter', '1/2 cup', 'butter nutrition info')
brown_sugar = Ingredient('brown sugar', '3/4 cup', 'brown sugar nutrition info')
bananas = Ingredient('bananas', '2 1/3 cups', 'banana nutrition info')
ingredients = [flour, baking_soda, salt, butter, brown_sugar, bananas]
equipment = ['9x5 inch loaf pan', 'oven', 'bowl', 'wooden spoon', 'measuring cups/spoons']
bananaBread = Recipe('banana bread', ingredients, equipment, 'instructions', 12, 80.0)

a_cookbook = Cookbook('My Delicious Noms')  # instantiate Cookbook
a_cookbook.add(bananaBread)  # add banana bread recipe to the Cookbook instance
recipe = a_cookbook.open('banana bread')  # open the banana bread recipe
print(recipe)

