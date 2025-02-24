# Solves the tower and m glass marbles problem. The user is
# prompted to enter the number n of floors of a building.
# Using m marbles, one has to discover the highest floor,
# if any, such that dropping a marble from that floor makes
# it break, using a strategy that minimises the number of
# drops in the worst case (it is assumed that any marble would
# break when dropped from a floor where one marble breaks, and
# also when dropped from any higher floor; the marbles might
# not break when dropped from any floor).
#
# The idea is to ask: what is the maximum height h of a building
# such that an answer can always be found with no more than d
# drops? Let H(d, m) denote that maximum height.
# - If the marble breaks, m - 1 marbles remain and no higher floor needs to be tested.
# - If the marble does not break, m marbles remain and no lower floor needs to be tested.
# - In any case, d - 1 drops remain.
# This yields: H(d, m) = H(d - 1, m - 1) + H(d - 1, m) + 1.
# The base cases are when either d = 0 or m = 0, in which case H(d, m) = 0.
# This allows one to compute d as the least integer with H(d, m) >= n.
# For the simulation, if low is the highest floor from which
# it is known that a marble can be dropped without breaking,
# d' is the number of drops that remain, and m' is the number
# of marbles that remain, then the next marble should be dropped
# from floor low + H(d' - 1, m' - 1) + 1.
#
# Set B(0, k) = 1 for all k, B(n, 0) = 1 for all n, and
# B(n + 1, k + 1) = B(n, k) + B(n, k + 1).
# The recurrence relation is identical to the one that
# determines the binomial coefficients.
# It is easy to verify that:
# - H(n, k) is equal to B(n, k) - 1;
# - if k > n then B(n, k) is equal to B(n, n);
# - if k <= n then B(n, k) is equal to the sum of n choose k1
# where k1 ranges over {0, ..., k}.
# The values B(n, k) determine the Bernouilli rectangle,
# whose rows are computed similarly to the rows of
# Pascal triangle. The program makes direct use of B(., .),
# and indirect use of H(., .):
#
# 0  1  2  3  4  5  6       
#  --- nb of marbles  --->
# 1  1  1  1  1  1  1  ...  |     0
# 1  2  2  2  2  2  2  ...  nb    1
# 1  3  4  4  4  4  4  ...  of    2
# 1  4  7  8  8  8  8 ...   drops 3
# 1  5 11 15 16 16 16 ...   |     4
# 1  6 16 26 31 32 32 ...   |     5
# ........................  V
#
# Written by Eric Martin for COMP9021


from random import randint


while True:
    # The n from the program description.
    n = input('Enter the number of floors (a strictly positive number): ')
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')
while True:
    # The m from the program description.
    m = input('Enter the number of marbles (a strictly positive number): ')
    try:
        m = int(m)
        if m <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')


# Compute and store B(i, k) for all i in {0, ..., d} and k in {0, ..., m}
# where d is from the program description, determined as the least number d'
# with by H(d', m) == B(d', m) - 1 >= n.
bernouilli_rows = [[1] * (m + 1), [1] + [2] * m]
d = 1
while bernouilli_rows[d][m] <= n:
    row = bernouilli_rows[d]
    bernouilli_rows.append([1] + [row[i - 1] + row[i] for i in range(1, len(row))])
    d += 1
if d == 1:
   print('At most 1 drop will be needed.\n')
else:
   print('At most', d, 'drops will be needed.\n')

        
# The highest floor such that it is known that a marble dropped
# from that floor does not break.
low = 0
# The smallest floor such that it is known that a marble dropped
# from that floor breaks (it is convenient to assume that a glass
# dropped from a level one more than the height of the building breaks).
high = n + 1
drop = 0
marble = 1
# We randomly make marbles break on one of floors 1, 2, ..., n + 1
# (in case the value is n + 1, the marble does not break when dropped
# from any floor of the building).
breaking_floor = randint(1, n + 1)
while low < high - 1:
    d -= 1
    floor = min(low + bernouilli_rows[d][m - 1], high - 1)
    drop += 1
    if breaking_floor <= floor:
       print('Drop #{} with marble #{}, from floor {}... marble breaks!'.format(drop, marble, floor))
       marble += 1
       high = floor
       m -= 1
    else:
       print('Drop #{} with marble #{}, from floor {}... marble does not break!'.format(drop, marble, floor))
       low = floor
