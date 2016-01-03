from class_one import First
from class_two import Second

class Runner:
    x = First("Hi", "Bye")
    print(x.a + ' and ' + x.b)

    x2 = Second(First("Hi", "Bye"), "That was cool")
    print x2.x.a
    print x2.x.b
    print x2.z
