# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys
import copy

dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()

def max_size_of1(mat, high, long):
    A = copy.deepcopy(mat)
    for i in range(high):
        for j in range(long):
            if A[i][j] >= 1:
                A[i][j] = 1
    B = copy.deepcopy(A[0])
    max_size = 0
    for i in range(1, high):
        for j in range(long):
            if A[i][j] == 1:
                B[j] = B[j] + 1
            else:
                B[j] = 0
        for x in range(2, high+1):
            L = 0
            for y in range(long):
                if B[y] >= x:
                    L = L+1
                else:
                    L = 0
                size = 0
                if L >= 2:
                    size = x * L
                if size > max_size:
                    max_size = size
    return max_size

def size_of_largest_parallelogram():
    max_size=max_size_of1(grid, 10, 10)
    M1=[[0 for x in range(20)] for x in range(10)]
    for i in range(dim):
        for j in range(dim):
            M1[i][j+i]=grid[i][j]
    max_size1=max_size_of1(M1, 10, 20)
    if max_size1 > max_size:
        max_size = max_size1
    M1=[[0 for x in range(20)] for x in range(10)]
    for i in range(dim):
        for j in range(dim):
            M1[i][j+dim-i]=grid[i][j]
    max_size2=max_size_of1(M1, 10, 20)
    if max_size2 > max_size:
        max_size = max_size2
    return max_size

    # Replace pass above with your code 


# Possibly add code for other functions

try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides has a size of', size, end = '.\n')
else:
    print('There is no parallelogram with horizontal sides.')
            


