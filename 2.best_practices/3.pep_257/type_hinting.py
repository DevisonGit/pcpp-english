# No type information added:
def hello(name):
    return "Hello, " + name


# Type information added to a function:
def hello_type(name: str) -> str:
    return "Hello, " + name
