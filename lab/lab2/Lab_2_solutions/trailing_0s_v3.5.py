# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.
#
# Written by Eric Martin for COMP9021


import sys
from math import factorial


def first_computation(x):
    nb_of_trailing_0s = 0
    while x % 10 == 0:
        nb_of_trailing_0s += 1
        x //= 10
    return nb_of_trailing_0s

def second_computation(x):
    min = 0
    for i in range(1,len(x)):
        if x[-i] == '0':
            min += 1
    return min
##    return min(i for i in range(1, len(x)) if x[-i] != '0') - 1

def third_computation(x):
    nb_of_trailing_0s = 0
    power_of_five = 5
    while x >= power_of_five:
        nb_of_trailing_0s += x // power_of_five
        power_of_five *= 5
    return nb_of_trailing_0s

try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

the_input_factorial = factorial(the_input)
print('Computing the number of trailing 0s in {}! by dividing by 10 for long enough:'.format(the_input),
      first_computation(the_input_factorial))
print('Computing the number of trailing 0s in {}! by converting it into a string:'.format(the_input),
      second_computation(str(the_input_factorial)))
print('Computing the number of trailing 0s in {}! the smart way:'.format(the_input),
      third_computation(the_input))
