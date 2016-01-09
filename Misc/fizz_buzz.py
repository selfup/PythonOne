class Fizz:
    def __init__(self, n):
        self.n = n

    def fizz_buzz(self, i):
        if (i % 15 == 0):
            print 'FizzBuzz'

    def fizzzy(self, i):
        if (i % 3 == 0 and i % 5 != 0):
            print 'Fizz'

    def buzzzy(self, i):
        if (i % 5 == 0 and i % 3 != 0):
            print 'Buzz'

    def print_i(self, i):
        if (i % 5 != 0 and i % 3 != 0):
            print i

    def output(self):
        n = self.n
        for i in range(n):
            self.fizz_buzz(i)
            self.fizzzy(i)
            self.buzzzy(i)
            self.print_i(i)

Fizz(16).output()
