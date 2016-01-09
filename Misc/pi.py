#!/usr/bin/python

import math

def make_pi(n):
    pi = str(math.pi)
    e_arr = []

    for d in pi:
        e_arr.append(d)

    e_arr.pop(1)
    print ''.join(e_arr[:n])

make_pi(4)
