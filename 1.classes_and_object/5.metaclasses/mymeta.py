def greetings(self):
    print('Just a greeting function, but it could be something more serious like a check sum')


class MyMeta(type):
    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj


class MyClass1(metaclass=MyMeta):
    pass


class MyClass2(metaclass=MyMeta):
    def greetings(self):
        print('We are ready to greet you!')


myobj1 = MyClass1()
myobj1.greetings()
myobj2 = MyClass2()
myobj2.greetings()
