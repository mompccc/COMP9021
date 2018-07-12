# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from array_queue import *
from collections import defaultdict


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def preferred_paths_to_corners():
    result = defaultdict(list)
    directions = {'NE':[(1, -1), (1, 0), (0, -1)],
                  'SE':[(1, 1), (1, 0), (0, 1)],
                  'SW':[(-1, 1), (-1, 0), (0, 1)],
                  'NW':[(-1, -1), (-1, 0), (0, -1)]}
    A=0
    paths=[(3,3)]
    while A < 200:
        path=paths[-1]
        x, y = path
        if (x, y) in corners:
            if (x, y) not in result:
                result[(x, y)] = paths
                paths=[(3,3)]
                continue
        for D_1, D_2 in directions[grid[y][x]]:
            next_x = x + D_1
            next_y = y+ D_2
            if next_x < 0 or next_x >= 7 or next_y < 0 or next_y >= 7:
                continue
            if (next_x, next_y) in paths:
                continue
            paths.append((next_x, next_y))
        A +=1
    return result
##    paths = ArrayQueue()
##    paths.enqueue([(3, 3)])
##    while not paths.is_empty():
##        P = paths.dequeue()
##        x, y = P[-1]
##        if (x, y) in corners:
##            if (x, y) not in result:
##                result[(x, y)] = P
##            continue
##        for D_1, D_2 in directions[grid[y][x]]:
##            next_x = x + D_1
##            next_y = y+ D_2
##            if next_x < 0 or next_x >= 7 or next_y < 0 or next_y >= 7:
##                continue
##            if (next_x, next_y) in P:
##                continue
##            P_next = list(P)
##            P_next.append((next_x, next_y))
##            paths.enqueue(P_next)
##    return result
    # replace pass above with your code (aim for around 21 lines of code)

try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

for i in range(dim):
    for j in range(dim):
        grid[i][j] = choice(directions)
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print('There is no path to {}'.format(corner))
    else:
        print('The preferred path to {} is:'.format(corner))
        print('  ', paths[corner])
