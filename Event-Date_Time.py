import re
text = "7. Event Date/Time: Sep 15, 2023 - 03:30 PM"
pattern = r'([A-Za-z]{3} \d{2}, \d{4}) - (\d{2}:\d{2} [APap][Mm])'
match = re.search(pattern, text)
if match:
    event_date = match.group(1)
    event_time = match.group(2)
    print("Event Date:", event_date)
    print("Event Time:", event_time)
