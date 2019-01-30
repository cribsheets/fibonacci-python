#!/usr/bin/env python3

# the sys module contains the simplest way
# to retrieve command line arguments
import sys

def fibonacci(n):
    ''' compute the nth Fibonacci number '''

    # remember the rules:
    # read a single argument n, and compute F(n) where:

    # - F(0) = 0
    # - F(1) = 1
    # - F(n) = F(n-1) + F(n-2)

    # our base cases are 0 and 1
    if n == 0: return 0
    if n == 1: return 1

    # in all other cases, we return the sum of the two
    # previous Fibonacci numbers. this is a quite literal
    # translation of the formula
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':

    # argv is a list containing the name of the program and
    # any args. we don't care about the name of the program,
    # and only care about the first arg.
    number = int(sys.argv[1])

    print(f'F({number}) = {fibonacci(number)}')
