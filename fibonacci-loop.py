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

    # we can shortcut in the case of 0 or 1
    # these also serve as our base cases in the recursive version
    if n == 0: return 0
    if n == 1: return 1

    # otherwise, let's build an Fibonacci sequence
    numbers = [0, 1]

    # beware of the fencepost error here! F(n) will be the
    # last element of a sequence of n+1 elements, counting F(0).
    while(len(numbers) <= n):
        numbers.append(sum(numbers[-2:])) # add the last two elements

    return numbers[-1] # return the last element of the list


if __name__ == '__main__':
    # argv is a list containing the name of the program and
    # any args. we don't care about the name of the program,
    # and only care about the first arg.
    number = int(sys.argv[1])

    print(f'F({number}) = {fibonacci(number)}')
