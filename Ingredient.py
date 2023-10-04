import re

# Sample raw API response containing recipe data
raw_data = [
    "Spaghetti, Tomato Sauce, Meatballs",
    "Chocolate Chips, Flour, Sugar, Eggs",
    "Chicken, Garlic, Onion, Bell Pepper, Rice",
]

# Define a regular expression pattern for ingredient lists
pattern = r'([^,]+(?:, [^,]+)*)'

# Initialize a list to store extracted ingredient lists
ingredient_lists = []

# Loop through the raw data and extract ingredient lists
for item in raw_data:
    matches = re.findall(pattern, item)
    if matches:
        ingredients = [ingredient.strip() for ingredient in matches]
        ingredient_lists.append(ingredients)

# Print the extracted ingredient lists
for i, ingredients in enumerate(ingredient_lists, start=1):
    print(f"Recipe {i} Ingredients:", ingredients)
