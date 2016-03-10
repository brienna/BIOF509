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
        nutrition = [0, 0, 0, 0]
        carbs = 0
        protein = 0
        fat = 0
        cholesterol = 0
        for amount, ingredient in self.ingredients:
            # if ingredient is a Recipe instance
            if isinstance(ingredient, Recipe):  
                ingredient = ingredient.ingredients  # update ingredient to recipe's ingredients
                for amt, ing in ingredient:
                    # print('ingredient within recipe: ', ing)
                    carbs += amt * ing.carbs
                    protein += amt * ing.protein
                    fat += amt * ing.fat
                    if hasattr(ing, 'cholesterol'):
                        cholesterol += amt * ing.cholesterol
                nutrition[0] += amount * carbs
                nutrition[1] += amount * protein
                nutrition[2] += amount * fat
                nutrition[3] += amount * cholesterol
            # if ingredient is an Ingredient instance
            else:
                # print('ingredient: ', ingredient)
                nutrition[0] += amount * ingredient.carbs
                nutrition[1] += amount * ingredient.protein
                nutrition[2] += amount * ingredient.fat
                if hasattr(ingredient, 'cholesterol'):
                        nutrition[3] += amount * ingredient.cholesterol
        return nutrition


    @property  
    def nutrition(self):
        info = self.get_nutrition()
        nutrients = {}
        nutrients['carbs'] = info[0]
        nutrients['protein'] = info[1]
        nutrients['fat'] = info[2]
        # note: currently there is no way to know whether a 'cholesterol': 0 
        # means no cholesterol content or no provided cholesterol values
        nutrients['cholesterol'] = info[3]
        return nutrients



