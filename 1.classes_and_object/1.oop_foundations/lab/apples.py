import random


class Apple:
    lower = 0.2
    upper = 0.5

    def __init__(self):
        self.weight = random.uniform(Apple.lower, Apple.upper)


class Package:
    units_limit = 300
    units_counted = 0
    apples = 0

    def order(self, quantity):
        while (Package.units_counted <= Package.units_limit
               and Package.apples < quantity):
            apple = Apple()
            if apple.weight + Package.units_counted <= Package.units_limit:
                Package.apples += 1
                Package.units_counted += apple.weight
            else:
                break


print("A shop owner has asked for 1000 apples")
package = Package()
package.order(1000)
print(f'Apples in the package: {Package.apples}')
print(f'{Package.units_counted} Units')
