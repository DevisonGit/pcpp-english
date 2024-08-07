try:
    import abcdefghijk

except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)
