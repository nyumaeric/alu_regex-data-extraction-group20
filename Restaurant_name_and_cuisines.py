import re

raw_data = [
    "Pizza Hut - Italian",
    "McDonald's - Fast Food",
    "Sushi Palace - Japanese",
    "Burger King - Fast Food",
]

pattern = r'(.*) - (.*)'

restaurant_names = []
cuisine_types = []

for item in raw_data:
    match = re.match(pattern, item)
    if match:
        restaurant_name = match.group(1)
        cuisine_type = match.group(2)
        restaurant_names.append(restaurant_name)
        cuisine_types.append(cuisine_type)
print("Restaurant Names:", restaurant_names)
print("Cuisine Types:", cuisine_types)


