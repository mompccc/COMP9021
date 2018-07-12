# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx (the year of birth)
# ranging from 1880 to2013.
# Prompts the user for a female first name, and finds out the years when this name was most popular
# in terms of ranking. Displays the ranking, and the years in decreasing order of frequency.

from collections import defaultdict
import sys
import os


directory = 'names'
targeted_first_name = input('Enter a female first name: ')
rank = 0
best_years=1
def best_years():
    pass

rank_per_year = defaultdict(list)
for filename in os.listdir(directory):
    rank = 0
    population = 0
    T=0
    R=0
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3: 7])
    with open(directory + '/' + filename) as file:
        for line in file:
            name, gender, tally = line.split(',')
            if gender == 'F':
                tally = tally.split('\n')[0]
                max_tally = tally
                population += int(tally)
                if tally <= max_tally:
                    rank += 1
                if name == targeted_first_name:
                    R=rank
                    T=int(tally)
        if R>0:
            rank_per_year[R].append([T/population,year])
            

                

A = sorted(rank_per_year.keys())
if A == []:
    print('{} is not a female first name in my records.'.format(targeted_first_name))
    sys.exit()
B = rank_per_year[A[0]]
B.sort(reverse = True)
C=[]
for x in range(len(B)):
    C.append(B[x][1])
# Replace this comment with your code

print('By decreasing order of frequency, {} was most popular in the years: '.format(targeted_first_name), end = '')
for year in C:
    print(year, end = ' ')
print('\nIts rank was {} then.'.format(A[0]))
