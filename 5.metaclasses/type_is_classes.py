class Dog:
    pass


age = 10
codes = [33, 92]
dog = Dog()

print(type(age))
print(type(codes))
print(type(dog))
print(type(Dog))

print('\nWhat type of objects are built-in classes and the metaclass type?')
for t in (int, list, type):
    print(type(t))
