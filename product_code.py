import re
text = "5. Product Code: XYZ456"
pattern = r'([A-Za-z]{3}\d{3})'
match = re.search(pattern, text)
if match:
    product_code = match.group(1)
    print("Product Code:", product_code)
