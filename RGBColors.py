import re
text = "3. Background Color: rgb(255, 0, 0)"
pattern = r'rgb\((\d+), (\d+), (\d+)\)'
match = re.search(pattern, text)
if match:
    red = match.group(1)
    green = match.group(2)
    blue = match.group(3)
    print("Red:", red)
    print("Green:", green)
    print("Blue:", blue)