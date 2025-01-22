dict = {
    "botswana": 0,
    "ethiopia": 50,
    "kenya": 50,
    "namibia": 140, # or 40
    "south-africa": 0,
    "tanzania": 50,
    "zambia": 50,
    "zimbabwe": 30
}

n = int(input())
countries = []

for _ in range(n):
    countries.append(input())
    
if "namibia" in countries and "south-africa" in countries and countries.index("south-africa") < countries.index("namibia"):
    dict["namibia"] = 40

if "zambia" in countries and "zimbabwe" in countries:
    dict["zambia"] = 25
    dict["zimbabwe"] = 25

price = 0

for country in countries:
    price += dict[country]

print(price)
