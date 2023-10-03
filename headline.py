text = "6. Headline: Breaking News - Major Event"
pattern = r'(.+?) - (.+)'
match = re.match(pattern, text)
if match:
    headline = match.group(1)
    subheader = match.group(2)
    print("Headline:", headline)
    print("Subheader:", subheader)
