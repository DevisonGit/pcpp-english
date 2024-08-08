# Bad:

a         = 1
b         = a        + 2
my_string = 'string' * 2

# Good:

a = 1
b = a + 2
my_string = 'string' * 2

# Bad:

x=x+3
x -=1

x = x * 2 - 1
x = (x - 1) * (x + 2)

# Good:

x = x + 3
x -= 1

x = x*2 - 1  # Use your own judgement.
x = (x-1) * (x+2)  # Use your own judgement.

# Bad:

def my_function(x, y = 2):
    return x * y

# Good:

def my_function(x, y=2):
    return x * y
