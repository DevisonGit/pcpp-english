import copy


# Define the Delicacy class
class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{{'name': '{self.name}', 'price': {self.price}, 'weight': {self.weight}}}"


# Create a list of Delicacy objects
warehouse = [
    Delicacy('Lolly Pop', 0.4, 133),
    Delicacy('Licorice', 0.1, 251),
    Delicacy('Chocolate', 1, 601),
    Delicacy('Sours', 0.01, 513),
    Delicacy('Hard candies', 0.3, 433)
]

# One-liner to deepcopy the list
proposal = copy.deepcopy(warehouse)

# Iterate over the proposal list to adjust prices
for candy in proposal:
    if candy.weight > 300:
        candy.price *= 0.8

# Print the original list of candies
print('Source list of candies')
for item in warehouse:
    print(item)

print('******************')

# Print the proposal list of candies with adjusted prices
print('Price proposal')
for item in proposal:
    print(item)

# Experiment with copy.copy()
shallow_copy_warehouse = copy.copy(warehouse)

# Modify shallow copy and observe changes
if shallow_copy_warehouse[0].weight < 150:
    shallow_copy_warehouse[0].price *= 1.1

print('******************')

# Print the original list of candies after shallow copy modification
print('Source list of candies after shallow copy modification')
for item in warehouse:
    print(item)

print('******************')

# Print the shallow copy list of candies
print('Shallow copy of candies')
for item in shallow_copy_warehouse:
    print(item)
