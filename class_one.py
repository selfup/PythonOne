class First:
    def __init__(self, param1, param2):
        self.a = param1
        self.b = param2

x = First("Hi", "Bye")
print(x.a + ' and ' + x.b)

class Second:
    def __init__(self, param1, param2):
        self.x = param1
        self.z = param2

x2 = Second(First("Hi", "Bye"), "That was cool")
print x2.x.a
print x2.x.b
print x2.z
