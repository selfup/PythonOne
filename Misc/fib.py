from math import sqrt
import sys

try:
    script, num = sys.argv

    def fib(num):
        n = int(num)
        return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

    def fibby(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibby(n-1)+fibby(n-2)

    print fib(num)
    print fibby(21)

except ValueError:
    print "\n\nPlease add a number after the file name with a space before it :)\n\n**"
    print "  example: python fib.py 23\n**\n"
