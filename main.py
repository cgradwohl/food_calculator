food_calculator_data = {
    "240g Strauss Cream Top Milk": {"fiber": 0, "protein": 9, "carbohydrate": 11, "fat": 9},
    "350g Strauss Cream Top Milk": {"fiber": 0, "protein": 13.5, "carbohydrate": 16, "fat": 13.5},
    "1 scoop Thorne Whey Protein Powder": {"fiber": 0, "protein": 21, "carbohydrate": 4, "fat": 1},
    "2 scoops Thorne SGS Powder": {"fiber": 0, "protein": 20, "carbohydrate": 9, "fat": 3.5},
    "1 Anabar Protein Bar": {"fiber": 1, "protein": 20, "carbohydrate": 28, "fat": 11},
    "1 serving of Thorne AM vitamins": {"fiber": 0, "protein": 0, "carbohydrate": 0, "fat": 0},
    "1 serving of Thorne PM vitamins": {"fiber": 0, "protein": 0, "carbohydrate": 0, "fat": 0},
    "1 serving 5-MTHF": {"fiber": 0, "protein": 0, "carbohydrate": 0, "fat": 0},
    "1 egg": {"fiber": 0, "protein": 6, "carbohydrate": 0.5, "fat": 5},
    "1 10-inch flour tortilla": {"fiber": 0, "protein": 8, "carbohydrate": 36, "fat": 5},
    "8g bacon (1 slice)": {"fiber": 0, "protein": 3, "carbohydrate": 0, "fat": 4},
    "1/2 pound (227g) chicken breast": {"fiber": 0, "protein": 43, "carbohydrate": 0, "fat": 3},
    "1/2 pound (227g) chicken thigh": {"fiber": 0, "protein": 34, "carbohydrate": 0, "fat": 12},
    "1/2 pound (227g) ribeye steak": {"fiber": 0, "protein": 46, "carbohydrate": 0, "fat": 37},
    "1/2 pound (227g) pork chop": {"fiber": 0, "protein": 42, "carbohydrate": 0, "fat": 18},
    "1/2 pound (227g) lamb chop": {"fiber": 0, "protein": 44, "carbohydrate": 0, "fat": 33},
    "1/2 pound (227g) ground beef (80% lean)": {"fiber": 0, "protein": 38.5, "carbohydrate": 0, "fat": 40},
    "1/2 pound (227g) ground lamb": {"fiber": 0, "protein": 40, "carbohydrate": 0, "fat": 44},
    "150g Sweet Potato cooked in olive oil": {"fiber": 4.5, "protein": 2, "carbohydrate": 33, "fat": 7},
    "150g Russet Potato cooked in olive oil and butter": {"fiber": 2, "protein": 3, "carbohydrate": 28, "fat": 11},
    "14g Chia Seeds": {"fiber": 5, "protein": 2.5, "carbohydrate": 6, "fat": 4.5},
    "1 Banana": {"fiber": 3.5, "protein": 1, "carbohydrate": 28, "fat": 0},
    "1 Apple": {"fiber": 3, "protein": 1, "carbohydrate": 25, "fat": 0},
    "1 Orange": {"fiber": 3, "protein": 1, "carbohydrate": 11, "fat": 0},
    "1 Adrenal Cocktail": {"fiber": 13, "carbohydrate": 34, "fat": 24.5, "protein": 4.5}
}


meal_data = {
    "Meal 1": [
        "2 scoops Thorne SGS Powder",
        "350g Strauss Cream Top Milk",
        "14g Chia Seeds",
        "1 serving of Thorne AM vitamins",
        "1 serving 5-MTHF"
    ],
    "Meal 2": [
        "1 egg",
        "1 egg",
        "1 egg",
        "1 egg",
        "1 10-inch flour tortilla",
        "1 Adrenal Cocktail"
    ],
    "Meal 3": [
        "1 Anabar Protein Bar",
        "1 scoop Thorne Whey Protein Powder",
        "350g Strauss Cream Top Milk",
        "14g Chia Seeds",
        "1 Apple",
        "1 Banana"
    ],
    "Meal 4": [
        "1 serving of Thorne PM vitamins",
        "1/2 pound (227g) pork chop",
        "150g Sweet Potato cooked in olive oil"
    ]
}


def calculate_meal_totals(food_data, meal_data):
    meal_totals = {}

    for meal, foods in meal_data.items():
        meal_totals[meal] = {
            "fiber": 0, "protein": 0, "carbohydrate": 0, "fat": 0}

        for food in foods:
            if food not in food_data:
                raise ValueError(f"Data for {food} not found in food_data.")

            meal_totals[meal]["fiber"] += food_data[food]["fiber"]
            meal_totals[meal]["protein"] += food_data[food]["protein"]
            meal_totals[meal]["carbohydrate"] += food_data[food]["carbohydrate"]
            meal_totals[meal]["fat"] += food_data[food]["fat"]

    return meal_totals


def print_result_as_markdown_table(result):
    print("| Meal   | Fiber (g) | Protein (g) | Carbohydrate (g) | Fat (g) | Total Calories |")
    print("|--------|------------|--------------|------------------|---------|")

    total_fiber = 0
    total_protein = 0
    total_carbohydrate = 0
    total_fat = 0
    total_calories = 0

    for meal, totals in result.items():
        fiber = totals['fiber']
        protein = totals['protein']
        carbohydrate = totals['carbohydrate']
        fat = totals['fat']
        calories = totals['protein'] * 4 + totals['carbohydrate'] * 4 + totals['fat'] * 9

        total_fiber += fiber
        total_protein += protein
        total_carbohydrate += carbohydrate
        total_fat += fat
        total_calories += calories
        
        print(f"| {meal} | {fiber} | {protein} | {carbohydrate} | {fat} | { calories } |")


    print("\n")
    print("| Total Fiber (g) | Total Protein (g) | Total Carbohydrate (g) | Total Fat (g) | Total Calories |")
    print("|------------|--------------|------------------|---------|")
    print(f"| {total_fiber} | {total_protein} | {total_carbohydrate} | {total_fat} | { total_calories } |")


try:
    result = calculate_meal_totals(food_calculator_data, meal_data)
    print(result)
    print_result_as_markdown_table(result)
except ValueError as e:
    print(e)
