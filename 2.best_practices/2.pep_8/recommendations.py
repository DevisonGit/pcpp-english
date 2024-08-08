# Bad:

if x == None:
    print("A")

# Good:

if x is None:
    print("A")

# Bad:

my_boolean_value = 2 > 1
if my_boolean_value == True:
    print("A")
else:
    print("B")

# Good:

my_boolean_value = 2 > 1
if my_boolean_value is True:
    print("A")
else:
    print("B")

# Better:

my_boolean_value = 2 > 1
if my_boolean_value:
    print("A")
else:
    print("B")

# Bad:

if not x is None:
    print("It exists")

# Good:

if x is not None:
    print("It exists")

# when you want to catch an exception, refer to specific exceptions
try:
    import my_module
except ImportError:
    my_module = None

# Bad:

if name[:4] == 'Adam':
    # do something
    pass

# Good:

if name.startswith('Adam'):
    # do something
    pass
