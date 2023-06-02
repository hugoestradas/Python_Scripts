from datefinder import find_dates

text = """We have one meeting on Feb 17th, 2022 at 10:00am and another
meeting on 2/22/2022 at 1:00pm."""

matches = find_dates(text)

for match in matches:
    print("Date & hour: ", match)
    print("Only day: ", match.day)
    
