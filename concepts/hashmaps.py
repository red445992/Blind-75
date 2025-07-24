# initializing 
"""
city_map = {}

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
city_map["usa"] = cities

print(city_map)
"""


# Array vs Hashmap
stock_prices = [["march 1",100], ["march 2", 120], ["march 3", 130], ["march 4", 140]]
print(stock_prices)

# to access elements in array
for i in stock_prices:
    if i[0] == "march 2":
        print(i[1])

# to access elements in hashmap
stock_prices_map = {
    "march 1": 100,
    "march 2": 120,
    "march 3": 130,
    "march 4": 140
}
print(stock_prices_map["march 1"])