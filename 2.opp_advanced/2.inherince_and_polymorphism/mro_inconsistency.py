class A:
    def info(self):
        print('Class A')


class B(A):
    def info(self):
        print('Class B')


class C(A):
    def info(self):
        print('Class C')


class D(A, C):
    pass


D().info()
