class MyMeta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj


class MyObject(metaclass=MyMeta):
    pass


print(MyObject.__dict__)
