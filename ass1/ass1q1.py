import sys
import copy

try:
    number_list = [int(x) for x in input('Please input the heroes\' powers: ').split()]
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()

try:
    nb_of_swiches = input('Please input the number of power flips: ')
    nb_of_swiches = int(nb_of_swiches)
    if nb_of_swiches < 0 or nb_of_swiches > len(number_list):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()

a = nb_of_swiches
a_1 = nb_of_swiches
a_2 = nb_of_swiches
b = copy.deepcopy(number_list)
b_1 = copy.deepcopy(number_list)
b_2 = copy.deepcopy(number_list)
#First
while a > 0:
    b.sort()
    b[0] = -b[0]
    a -= 1
print('Possibly flipping the power of the same hero many times, the greatest achievable power is '
      + str(sum(b)) + '.')
      
#Second
blank = []
while a_1 > 0:
    b_1.sort()
    b_1[0] = -b_1[0]
    z = b_1.pop(0)
    blank.append(z)
    a_1 -= 1
b_1.extend(blank)
print('Flipping the power of the same hero at most once, the greatest achievable power is '
      + str(sum(b_1))+ '.')

#Third
Q=0
mat = []
if a_2 == len(number_list):
    print('Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is '
          + str(-sum(b_2)) + '.')
if a_2 < len(number_list):
    for i in range(0, len(b_2) - a_2 + 1):
        mat.append(sum(b_2[i:i+a_2]))
    Q = sum(number_list) - min(mat) -min(mat)
    print('Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is '
          + str(Q) +'.')

#Fourth
A = []
B = []
for z in range(0, len(number_list)):
    A = A + [number_list[z]]
    B.append(-sum(A))
    if -sum(A) < 0:
        A = []
C = sum(number_list) + 2*max(B)
if min(number_list) < 0:
    print('Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is ' + str(C) + '.')
else:
    print('Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is ' + str(sum(number_list)) + '.')

