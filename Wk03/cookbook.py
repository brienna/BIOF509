
# Description: The cookbook shows options from which you choose a category of recipes. 
# Inside the category of recipes, you see a list of recipes to choose from. Once you choose
# a recipe, you view its ingredients, equipment needed and instructions. The recipe is 
# scalable to different numbers of servings with the amount of ingredients adjusted
# appropriately and viewable in metric and imperial units. Nutritional information should 
# be tracked.


def Cookbook(object): 

    def __init__:
        pass

    def open():
        '''Opens cookbook. 

        Takes and returns no arguments.
        '''


def Recipe():


def Dessert(Recipe):

def MainCourse(Recipe):

def Appetizer(Recipe):

def Ingredients(object):

    def __init__(self, quantity):
        self.quantity = quantity





a_cookbook = Cookbook()  # instantiate Cookbook object
a_cookbook.open()  # call a method on Cookbook instance




# DISCUSSED IN CLASS

# classes:
# appetizers
# main courses
# desserts
# recipe
#      __Attributes/Methods__
#             - preparation time
#             - cooking time
#             - serving portion
#             - servings
#             - name
#             - nutritional information
#             - ingredients
#             - methods
#             - scaling
#             - equipment
#             - special occasion 
#             - instructions
#      __Interactions__
#             - Cookbook
#             - Ingredients
#             - Instructions
#             - Nutrition
#             - Equipment
#             - Scaling
#             - Portions
# servings
# ingredients
#  - quantity (mass/volume)
#     - units
#  - nutritional info
#  - specific dietary info
#  - cost
#  - storage temperature
#  - sustitute options
#  - name
#  - translations
#  - alternative names
#  - special handling instructions
#  - sources
#      * can interact with the following classes:
#      * recipe
#      * Instructions
#      * Equipment
#      * nutrition 
#      * scaling
#      * portions 
#      * cookbook
#      * units
# solid ingredients
# liquid ingredients
# equipment
# instructions
# nutritional info
# style
# units conversion
# scaling 
# portions
# cookbook

# (recipe class can have an attribute, list of ingredients which are instances of another class themselves)
# (classes interact with each other often in an app like this)
# (instructions can be a class, and an instance of it can be saved as an attribute in Recipe class)