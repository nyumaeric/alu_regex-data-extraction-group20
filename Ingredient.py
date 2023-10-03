import re

text = "2. Ingredients: Tomato, Basil, Mozzarella"
pattern = r'(.+?): (.+)'
match = re.match(pattern, text)
if match:
    ingredients = match.group(2).split(', ')
    print("Ingredients:", ingredients)