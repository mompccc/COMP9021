# Prompts the user for an integer N at least equal to 5,
# computes the largest number l >= 1 such that l consecutive prime numbers
# add up to a prime number at most equal to N,
# and outputs l and the larger such prime number.
#
# Written by *** and Eric Martin for COMP9021
import math
import copy
from math import sqrt
import sys
names = locals()

try:
    N = int(input('Enter an integer at least equal to 5: '))
    if N < 5:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

R=[]
x = 0
Z = N
def is_prime(N):
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True

if N > 1000:
    Z = int(N/2)
for x in range(2, Z):
    if is_prime(x):
        R.append(x)

while sum(R) > N * 2:
    R.pop()

L = copy.deepcopy(R)
X = copy.deepcopy(R)

while sum(L) > N:
    L.pop()
while is_prime(sum(L)) == False:
    L.pop()

if __name__ == '__main__':
    mat = [];
    temp = [];
    for b in range(0, len(X) - 1):
        if R != []:
            R.pop(0)
        temp = copy.deepcopy(R)
        while sum(temp) > N:
            temp.pop()
        while is_prime(sum(temp)) == False:
            temp.pop()
            if temp == []:
                break
        mat.append(temp)


long = 0
longest = 0
number = 0
D=[0]
for x in range(0, len(mat) - 1):
    if len(mat[x]) >= max(len(line) for line in mat):
        D.append(sum(mat[x]))

longest = max(len(line) for line in mat)
number = max(D)
if len(L) > max(len(line) for line in mat):
    longest = len(L)
    number = sum(L)

    # Insert your code here

print('The largest sequence of consecutive primes that add up\n  '
          'to a prime P equal to ' + str(N) + ' at most has a length of ' + str(longest) + '\n'
          'The largest such P is ' + str(number))

