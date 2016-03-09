from ingredient_recipe_interface import Ingredient, Recipe


bread = Recipe('Bread', [(820, Ingredient('Flour', 0.77, 0.10, 0.01)), 
                         (30, Ingredient('Oil', 0, 0, 1)), 
                         (36, Ingredient('Sugar', 1, 0, 0)), 
                         (7, Ingredient('Yeast', 0.3125, 0.5, 0.0625)),
                         (560, Ingredient('Water', 0, 0, 0))])
print(bread.ingredients)
# Should be roughly [(820, Ingredient(Flour, 0.77, 0.1, 0.01)), (30, Ingredient(Oil, 0, 0, 1)), 
# (36, Ingredient(Sugar, 1, 0, 0)), (7, Ingredient(Yeast, 0.3125, 0.5, 0.0625)), (560, Ingredient(Water, 0, 0, 0))]

print(bread.nutrition)
#Should be roughly {'carbs': 669.5875, 'protein': 85.5, 'fat': 38.6375} the order is not important

#Points to note:
# - The different call to Ingredient, you can use isinstance or type to change the 
#   behaviour depending on the arguments supplied
# - Cholesterol as an extra nutrient, your implementation should accept any nutrient
# - Use of Recipe (bread) as an ingredient
basic_french_toast = Recipe('Basic French Toast', [(300, Ingredient('Egg', {'carbs': 0.0077, 'protein': 0.1258, 
                                                                            'fat': 0.0994, 'cholesterol': 0.00423})), 
                                                  (0.25, bread)])
print(basic_french_toast.ingredients)
# Should be roughly:
# [(300, Ingredient(Egg, 0.0077, 0.1258, 0.0994)), (0.25, Recipe(Bread, [(820, Ingredient(Flour, 0.77, 0.1, 0.01)), 
# (30, Ingredient(Oil, 0, 0, 1)), (36, Ingredient(Sugar, 1, 0, 0)), (7, Ingredient(Yeast, 0.3125, 0.5, 0.0625)), 
# (560, Ingredient(Water, 0, 0, 0))]))]
# Note the formatting for the Recipe object, a __repr__ method will be needed

print(basic_french_toast.nutrition)
# Should be roughly {'protein': 59.115, 'carbs': 169.706875, 'cholesterol': 1.2690000000000001, 'fat': 39.479375000000005}
# The order is not important