class Vector:
    def __init__(self):
        self.a = [4, 5, 6, 0]
        self.b = [1, 0, 2, 1]
        self.pre_vect = []

    def mult_arrs(self):
        for idx, num in enumerate(self.a):
            self.pre_vect.append(num * self.b[idx])

    def output(self, mult_ar):
        return reduce(add, mult_ar)

    def result(self):
        self.mult_arrs()
        print self.output(self.pre_vect)

Vector().result()
