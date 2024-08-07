import copy

# Initial warehouse data
warehouse = [
    {'name': 'Lolly Pop', 'price': 0.4, 'weight': 133},
    {'name': 'Licorice', 'price': 0.1, 'weight': 251},
    {'name': 'Chocolate', 'price': 1, 'weight': 601},
    {'name': 'Sours', 'price': 0.01, 'weight': 513},
    {'name': 'Hard candies', 'price': 0.3, 'weight': 433}
]

# One-liner to deepcopy the list
proposal = copy.deepcopy(warehouse)

# Iterate over the proposal list to adjust prices
for candy in proposal:
    if candy['weight'] > 300:
        candy['price'] *= 0.8

# Print the original list of candies
print('Source list of candies')
for item in warehouse:
    print(item)

print('******************')

# Print the proposal list of candies with adjusted prices
print('Price proposal')
for item in proposal:
    print(item)
