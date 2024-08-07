try:
    print(1 / 0)
except ZeroDivisionError:
    print("Don't divide by zero!")

try:
    number = int(input("Enter an integer number: "))
except:
    number = 0
