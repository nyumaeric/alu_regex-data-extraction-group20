text = "4. Visit us on Twitter: @sampleuser123"
pattern = r'@([A-Za-z0-9]+)'
match = re.search(pattern, text)
if match:
    username = match.group(1)
    print("Username:", username)
