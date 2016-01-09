class One:
    def __init__(self, param1 = "PARAMONE", param2 = "PARAMTWO"):
        self.a = "Hey"
        self.b = "There"
        self.param1 = param1
        self.param2 = param2

    def output_both(self, a, b):
        a = self.a
        b = self.b
        print "Attributes: %s %s" % (a, b)

print One().a
One().output_both("AAA", "BBB")
print One("yoyoyoo").param1

class Two:
    def __init__(self, x, y = "Nevermind"):
        self.x = x
        self.y = y

print Two(One("Hello There This is Strange")).x.param1
print Two(One("Hello There This is Strange")).x.param2

array_one = [1, "k", 90, "plpl", "sup", 10.12]

for index, list_element in enumerate(array_one):
    print index
    print str(list_element).upper()

print "lololol".upper()
