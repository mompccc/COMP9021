# Generates a list L of random nonnegative integers at most equal to some value
# input by the user, and of length also input by the user, and outputs a list
# consisting of the longest streak of consecutive occurrences of the same value in L,
# possibly looping around (as if the list was a ring). In the case multiple value
# have the longest streak of consecutive occurrences in L, then the smallest value is chosen.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('\nThe generated list is:')
print('  ', L)

R = []
length_current = 1
length_longest = 1
if L == []:
    smallest = []
else:
    for i in range(-len(L) , 1):
        if L[i + 1] == L[i]:
            length_current += 1
        else:
            if length_current > length_longest:
                R = [L[i]] * length_current
                length_longest = length_current
            elif length_current == length_longest:
                if length_longest != 1:
                    R.extend([L[i]] * length_current)
            length_current = 1
    if R != []:
        smallest = [min(R)] * length_longest
    if length_longest == 1:
        smallest = [min(L)]
    if max(L) == min(L):
        smallest = L


print('\nThe longest streak of the same value is:')
print('  ', smallest)
