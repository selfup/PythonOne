from math import sqrt
from sys import argv

script, num = argv

def fib(num):
    n = int(num)
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

print fib(num)
