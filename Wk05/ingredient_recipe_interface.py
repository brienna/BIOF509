class Ingredient(object):
    """The ingredient object that contains nutritional information"""
    
    def __init__(self, name, *args):
        self.name = name

        amounts = []
        nutrients_tracked = ['carbs', 'protein', 'fat', 'cholesterol']  

        for arg in args:
            # if argument is a dict, set keys & values as instance attributes
            if isinstance(arg, dict):
                for key in arg.keys():
                    setattr(self, key, arg[key])  # self.key = arg[key] doesn't work?
            # if argument isn't a dict, add argument to list
            else: 
                amounts.append(arg)

        # if non-dict arguments were added to list, set them as instance attributes
        if len(amounts) > 0:
            for nutrient, amount in zip(nutrients_tracked, amounts):
                setattr(self, nutrient, amount)

        
    def __repr__(self):
        # if instance contains 'cholesterol' attribute, include it in str representation
        if hasattr(self, 'cholesterol'):
            return 'Ingredient({0}, {1}, {2}, {3}, {4})'.format(self.name, self.carbs, self.protein, self.fat, self.cholesterol)
        else:
            return 'Ingredient({0}, {1}, {2}, {3})'.format(self.name, self.carbs, self.protein, self.fat)


    def get_nutrition(self):
        """Returns the nutritional information for the ingredient"""
        return (self.carbs, self.protein, self.fat)
    

class Recipe(object):
    """The Recipe object containing the ingredients"""
    
    def __init__(self, name, ingredients,):
        self.name = name
        self.ingredients = ingredients
    

    def __repr__(self):
        return 'Recipe({0}, {1})'.format(self.name, self.ingredients)


    def get_nutrition(self):
        """Returns the nutritional information for the recipe"""
        nutrition = [0, 0, 0]
        for amount, ingredient in self.ingredients:
            nutrition[0] += amount * ingredient.carbs
            nutrition[1] += amount * ingredient.protein
            nutrition[2] += amount * ingredient.fat
        return nutrition


    @property  
    def nutrition(self):
        info = self.get_nutrition()
        nutrients = {}
        nutrients['carbs'] = info[0]
        nutrients['protein'] = info[1]
        nutrients['fat'] = info[2]
        return nutrients



