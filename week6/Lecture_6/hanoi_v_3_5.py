# Solves the Tower of Hanoi puzzle.
#
# Written by Eric Martin for COMP9021

# Move a tower of n disks on the start-peg to the finish-peg,
# using the spare-peg as an intermediate.


def move_towers(n, start, finish, spare):
    if n == 1:
        print('Move a disk from peg {} to peg {}'.format(start, finish))
    else:
        move_towers(n - 1, start, spare, finish)
        print('Move a disk from peg {} to peg {}'.format(start, finish))
        move_towers(n - 1, spare, finish, start)

while True:
    try:
        n = int(input('Enter a positive integer: '))
        if n < 0:
            raise ValueException
        break
    except ValueError:
        print('Incorrect input, try again.')
        
move_towers(n, 1, 3, 2)
