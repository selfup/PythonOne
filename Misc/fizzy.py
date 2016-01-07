def fizzbuzz(i, n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print'FizzBuzz'
        elif i % 3 == 0:
            print'Fizz'
        elif i % 5 == 0:
            print'Buzz'
        else:
            print i

fizzbuzz(0, 16)

a = [23, 32, 56, 65]
b = [12, 23, 34, 45, 56, 67, 78, 89]

def iter(a):
    for idx, num in enumerate(a):
        print num, b[idx]

print'\n'
iter(a)
print'\n'

def add(x, y):
    return x + y

print reduce(add, b)
print '\n'
