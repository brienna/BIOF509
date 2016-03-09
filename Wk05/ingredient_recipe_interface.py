class Ingredient(object):
    """The ingredient object that contains nutritional information"""
    
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        
    
    def __repr__(self):
        return 'Ingredient({0}, {1}, {2}, {3})'.format(self.name, self.carbs, self.protein, self.fat)
    
    
    def get_nutrition(self):
        """Returns the nutritional information for the ingredient"""
        return (self.carbs, self.protein, self.fat)
    

class Recipe(object):
    """The Recipe object containing the ingredients"""
    
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        
        
    def get_nutrition(self):
        """Returns the nutritional information for the recipe"""
        nutrition = [0, 0, 0]
        for amount, ingredient in self.ingredients:
            nutrition[0] += amount * ingredient.carbs
            nutrition[1] += amount * ingredient.protein
            nutrition[2] += amount * ingredient.fat
        return nutrition