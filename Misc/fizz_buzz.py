class Fizz:
    def __init__(self, range_for_n, n1, n2, first_word, second_word):
        self.range_for_n = (range_for_n + 1)
        self.n1 = n1
        self.n2 = n2
        self.first_word = first_word
        self.second_word = second_word
        self.biggest_word = ''.join([first_word, second_word])

    def print_i_condition(self, i, n, n2):
        if (i % self.n2 != 0 and i % self.n1 != 0):
            print i

    def fizz_or_buzz_condition(self, i, n, n2, message):
        if (i % n == 0 and i % n2 != 0):
            print message

    def fizz_buzz_condition(self, i, n):
        if (i % (self.n1 * self.n2) == 0):
            print self.biggest_word

    def fizz_buzz(self, i):
        self.fizz_buzz_condition(i, (self.n1 * self.n2))

    def fizz(self, i):
        self.fizz_or_buzz_condition(i, self.n1, self.n2, self.first_word)

    def buzz(self, i):
        self.fizz_or_buzz_condition(i, self.n2, self.n1, self.second_word)

    def print_i(self, i):
        self.print_i_condition(i, self.n2, self.n1)

    def output(self):
        n = self.range_for_n
        for i in range(n):
            self.fizz_buzz(i)
            self.fizz(i)
            self.buzz(i)
            self.print_i(i)

Fizz(30, 3, 5, 'Fizz', 'Buzz').output()
print '\n'
Fizz(30 , 3, 5, 'Hello', 'Goodbye').output()
