import time


class Meta(type):
    instantiated_classes = []

    def __new__(cls, name, bases, dct):
        # Create the new class
        new_class = super().__new__(cls, name, bases, dct)
        # Add the instantiation_time class attribute
        new_class.instantiation_time = time.time()

        # Add the get_instantiation_time method
        def get_instantiation_time(cls):
            return cls.instantiation_time

        new_class.get_instantiation_time = classmethod(get_instantiation_time)
        # Append the class name to the instantiated_classes list
        cls.instantiated_classes.append(name)
        return new_class


# Create a few distinct legacy classes using the metaclass
class LegacyClass1(metaclass=Meta):
    pass


class LegacyClass2(metaclass=Meta):
    pass


class LegacyClass3(metaclass=Meta):
    pass


# Instantiate objects based on the classes
obj1 = LegacyClass1()
obj2 = LegacyClass2()
obj3 = LegacyClass3()

# List the class names that are instantiated by the metaclass
print("Classes instantiated by the metaclass:")
for class_name in Meta.instantiated_classes:
    print(class_name)

# Check the instantiation time for each class
print("Instantiation times:")
print(f"LegacyClass1: {LegacyClass1.get_instantiation_time()}")
print(f"LegacyClass2: {LegacyClass2.get_instantiation_time()}")
print(f"LegacyClass3: {LegacyClass3.get_instantiation_time()}")
