
class Ingredients:
    def __init__(self, ingredient_type, name, serving_size, calories, fat, protien, carbs, servings_per_roll, idnum):
        self.name = name
        self.ingredient_type = ingredient_type
        self.serving_size = serving_size
        self.calories = calories
        self.fat = fat
        self.protien = protien
        self.carbs = carbs
        self.servings = servings_per_roll
        self.idnum = idnum

class SushiRoll:
    def __init__(self, name, pieces, calories, fat, protien, carbs, ingredients):
        self.name = name
        self.pieces = pieces
        self.calories = calories
        self.fat = fat
        self.protien = protien
        self.carbs = carbs
        self.ingredients = ingredients
        self.actions = ["Adjust", "Save", "Return", "Quit"]

    def get_fat(self):
        return self.fat

    def get_calories(self):
        return self.calories

    def get_carbs(self):
        return self.carbs

    def get_protien(self):
        return self. protien

    def get_pieces(self):
        return self.pieces

    def changing_servings(self, ingredient, new_serving_size):
        print("Old calories: ", self.calories)
        change = float(new_serving_size)
        new_fat = self.ingredients[ingredient].fat * change
        new_protien = self.ingredients[ingredient].protien * change
        new_carbs = self.ingredients[ingredient].carbs * change
        new_calories = self.ingredients[ingredient].calories * change
        self.ingredients[ingredient].fat = new_fat
        self.ingredients[ingredient].protien = new_protien
        self.ingredients[ingredient].carbs = new_carbs
        self.ingredients[ingredient].calories = new_calories
        self.update_nutrition()
        return print(self.calories)

    def choose_action(self):
        i = 1
        for item in self.actions:
            print("      " + str(i) + ":", item)
            i += 1

    def update_nutrition(self):
        self.calories = 0
        self.fat = 0
        self.protien = 0
        self.carbs = 0
        for item in self.ingredients:
            self.fat += item.fat
            self.carbs += item.carbs
            self.protien += item.protien
            self.calories += item.calories