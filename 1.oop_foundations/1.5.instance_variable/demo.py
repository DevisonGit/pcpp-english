class Demo:
    def __init__(self, value):
        self.instance_var = value


d1 = Demo(100)
d2 = Demo(200)

print("d1's instance variable is equal to:", d1.instance_var)
print("d2's instance variable is equal to:", d2.instance_var)
