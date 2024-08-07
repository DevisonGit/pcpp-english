try:
    print(int('a'))
except ValueError as e_variable:
    print(e_variable.args)
