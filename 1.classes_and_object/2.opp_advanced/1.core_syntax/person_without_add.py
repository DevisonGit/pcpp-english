class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary


p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)
