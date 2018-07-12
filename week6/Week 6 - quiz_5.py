# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out".
#
# Written by *** and Eric Martin for COMP9021

import copy
from random import seed, randrange
import sys

dim = 10

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()

# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s that make it with 2.
# We "colour" the second shape we find by replacing all the 1s that make it with 3.

try:
    for_seed, n = [int(i) for i in
                        input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) != 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

P = copy.deepcopy(grid)
for i in range(dim):
    for j in range(dim):
        if P[i][j]:
            P[i][j] = 1
        else:
            P[i][j] = 0

def valid(P,x,y):
    if (x>=0 and x<len(P) and y>=0 and y<len(P[0]) and P[x][y]==1):
        return True
    else:
        return False

colour = 2

def colour1(P, i, j):
    if valid(P, i, j):
        P[i][j] = colour
        if not colour1(P, i-1, j):
            P[i][j] = 0
        elif not colour1(P, i+1, j):
            P[i][j] = 0
        elif not colour1(P, i, j-1):
            P[i][j] = 0
        elif not colour1(P, i, j+1):
            P[i][j] = 0
    return colour

def colour_shapes():
    global colour
    for i in range(dim):
        for j in range(dim):
            if colour1(P, i, j):
                colour += 1
    return colour

def max_number_of_spikes(nb_of_shapes):
    global Y
    Y = [0]*12
    for i in range(len(Y)):
        Y[i] = [0]*12
    for a in range(dim):
        for b in range(dim):
            Y[a+1][b+1]=P[a][b]
    spike_max = 0
    for x in range(2, nb_of_shapes):
        spike = 0
        for i in range(1,dim+1):
            for j in range(1,dim+1):
                if Y[i][j] == x:
                    if Y[i-1][j] + Y[i+1][j] + Y[i][j-1] + Y[i][j+1] == x:
                        spike += 1
                        if spike > spike_max:
                            spike_max = spike
    return spike_max

def PP():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' {}'.format(P[i][j]),end = '')
        print()
    print()

nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is equal to {}'.format(max_number_of_spikes(nb_of_shapes)))
