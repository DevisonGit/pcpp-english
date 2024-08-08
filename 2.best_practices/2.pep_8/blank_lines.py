#  two blank lines to function and class definitions
class ClassOne:
    pass


class ClassTwo:
    pass


def my_top_level_function():
    return None


# a single blank line to method definitions inside a class
class MyClass:
    def method_one(self):
        return None

    def method_two(self):
        return None


# blank line in functions in order to indicate logical sections
def calculate_average():
    how_many_numbers = int(input("How many numbers? "))

    if how_many_numbers > 0:
        sum_numbers = 0
        for i in range(0, how_many_numbers):
            number = float(input("Enter a number: "))
            sum_numbers += number

        average = 0
        average = sum_numbers / how_many_numbers

        return average
    else:
        return "Nothing happens."
