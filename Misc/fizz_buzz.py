class Fizz:
    def __init__(self, n):
        self.n = n

    def print_i_condition(self, i, n, n2):
        if (i % 5 != 0 and i % 3 != 0):
            print i

    def fizz_or_buzz_condition(self, i, n, n2, message):
        if (i % n == 0 and i % n2 != 0):
            print message

    def fizz_buzz_condition(self, i, n, message):
        if (i % 15 == 0):
            print message

    def fizz_buzz(self, i):
        self.fizz_buzz_condition(i, 15, 'FizzBuzz')

    def fizz(self, i):
        self.fizz_or_buzz_condition(i, 3, 5, 'Fizz')

    def buzz(self, i):
        self.fizz_or_buzz_condition(i, 5, 3, 'Buzz')

    def print_i(self, i):
        self.print_i_condition(i, 5, 3)

    def output(self):
        n = self.n
        for i in range(n):
            self.fizz_buzz(i)
            self.fizz(i)
            self.buzz(i)
            self.print_i(i)

Fizz(16).output()
