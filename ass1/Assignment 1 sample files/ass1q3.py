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
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
finally:
    file.close()

B = A[0:int(len(A)/2)]
C = A[int(len(A)/2):len(A)]

if len(A) % 2 != 0 or len(A)<4:
    print('Sorry, input file does not store valid data.')
    sys.exit()
for i in range(len(B)):
    if C[i] >= B[i]:
        print('Sorry, input file does not store valid data.')
        sys.exit()

deep = 1
deep_max = 1
for j in range(0,B[0]-C[0]):
    deep = 1
    for i in range(1, len(B)):
        if C[i]<=(C[0]+j) and B[i]>(C[0]+j):
            deep += 1
            if deep > deep_max:
                deep_max = deep
        else:
            break
print('From the west, one can into the tunnel over a distance of',deep_max)

deep1 = 1
deep1_max = 1
for x in range(len(B)):
    if x < len(B)-1:
        for j in range(B[x]-C[x]):
            deep1 = 1
            for i in range(x+1, len(B)):
                if C[i]<=(C[x]+j) and B[i]>(C[x]+j):
                    deep1 += 1
                    if deep1 > deep1_max:
                        deep1_max = deep1
                else:
                    break

print('Inside the tunnel, one can into the tunnel over a maximum distance of',deep1_max)
