# Prompts the user for a strictly positive integer, nb_of_elements,
# generates a list of nb_of_elements random integers between 0 and 99, prints out the list,
# computes the number of elements equal to 0, 1, 2 3 modulo 4, and prints those out.
#
# Written by Eric Martin for COMP9021


from random import seed, randrange
import sys

# Prompts the user for a seed for the random number generator,
# and for a strictly positive number, nb_of_elements.
arg_for_seed = input('Input a seed for the random number generator: ')
try:
    arg_for_seed = int(arg_for_seed)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()   
nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()

# Generates a list of nb_of_elements random integers between 0 and 99.
seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_of_elements)]

print('\nThe list is:' , L)
print()
# - remainders_modulo_4[0] to record the number of elements equal to 0 modulo 4,
# - remainders_modulo_4[1] to record the number of elements equal to 1 modulo 4,
# - remainders_modulo_4[2] to record the number of elements equal to 2 modulo 4,
# - remainders_modulo_4[3] to record the number of elements equal to 3 modulo 4.
A = [0] * 4
for i in range(len(L)):
    if 0<=L[i]<=4:
        A[0] += 1
    if 5<=L[i]<=9:
        A[1] += 1
    if 10<=L[i]<=14:
        A[2] += 1
    if 15<=L[i]<=19:
        A[3] += 1
for i in range(4):
    print('There are {} elements'.format(A[i]), end = ' ')
    print('equal to {} modulo 4.'.format(i))
##remainders_modulo_4 = [0] * 4
##for i in range(nb_of_elements):
##    remainders_modulo_4[L[i] % 4] += 1
##for i in range(4):
##    if remainders_modulo_4[i] == 0:
##        print('There is no element', end = ' ')
##    elif remainders_modulo_4[i] == 1:
##        print('There is 1 element', end = ' ')
##    else:
##        print('There are {} elements'.format(remainders_modulo_4[i]), end = ' ')
##    print('equal to {} modulo 4.'.format(i))
