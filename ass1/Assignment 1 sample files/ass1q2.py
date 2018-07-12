import os.path
import sys
from collections import defaultdict
import copy

try:
    file = open(input('Please enter the name of the file you want to get data from: '))
except FileNotFoundError:
    print('Sorry, there is no such file.')
    sys.exit()
try:
    text = file.read()
    A = [int(i) for i in text.split()]
    pass
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
finally:
    file.close()
if len(A) <= 1 or min(A) <= 0 or A != sorted(A):
    print('Sorry, input file does not store valid data.')
    sys.exit()
gap = 0
L = 1
L_max = 1
for i in range(len(A)-2):
    gap = A[i+1]-A[i]
    if A[i+2]-A[i+1]==gap:
        L += 1
    else:
        gap = A[i+2]-A[i+1]
        L = 1
    if L > L_max:
        L_max = L

dict_H = {}
Q = [[0]]
W = [[0]]
Z=[]
X=[]

for i in range(1, len(A)):
    for j in range(i):
        dict_H[A[i]-A[j]] = 2
        for x in range(len(Q[j])):
            if A[i]-A[j] == Q[j][x]:
                dict_H[A[i]-A[j]] = W[j][x] + 1
    for a in dict_H.keys():
        Z.append(a)
    for b in dict_H.values():
        X.append(b)
    Q.append(Z)
    W.append(X)
    dict_H = {}
    Z=[]
    X=[]

number = 0
number_max = 0
for i in range(len(W)):
    number = max(W[i])
    if number > number_max:
        number_max = number

if number_max == len(A):
    print('The ride is perfect!')
else:
    print('The ride could be better...')

print('The longest good ride has a length of: ' + str(L_max))
print('The minimal number of pillars to remove to build a perfect ride from the rest is: ' + str(len(A) - number_max))
