# Код программы Recipe Scaling Tool

recipe = {
    "eggs": 2,
    "flour": 250,
    "sugar": 100,
    "butter": 50,
    "milk": 200
}

serving_size = int(input("How many servings does the recipe make? "))
desired_size = int(input("How many servings do you want to make? "))

scaling_factor = desired_size / serving_size

for ingredient, amount in recipe.items():
    new_amount = amount * scaling_factor
    print(f"{ingredient}: {new_amount}g")
