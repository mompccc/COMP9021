# Uses National Data on the relative frequency of given names
# in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt
# with xxxx (the year of birth)
# ranging from 1880 to 2013.
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by Eric Martin for COMP9021


import os
from sys import exit


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

all_name = {'F' : {}, 'M' : {}}
the_name = {'F' : {}, 'M' : {}}
per = {'F' : {}, 'M' : {}}
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3:7])
    with open(directory + '/' + filename) as file:
        all_name['F'][year] = 0
        all_name['M'][year] = 0
        the_name['F'][year] = 0
        the_name['M'][year] = 0
        for line in file:
            name, gender, count = line.split(',')
            count = int(count)
            all_name[gender][year] += count
            if name == first_name:
                the_name[gender][year] = count

for i in all_name['M'].keys():
    if the_name['M'][i]:
        per['M'][i] =  (the_name['M'][i] / all_name['M'][i]) * 100
for i in all_name['F'].keys():
    if the_name['F'][i]:
        per['F'][i] = (the_name['F'][i] / all_name['F'][i]) * 100

A = sorted(per['F'].items(), key=lambda item:item[1], reverse = True)
B = sorted(per['M'].items(), key=lambda item:item[1], reverse = True)

if per['F']:
    min_female_frequency, female_first_year = A[0][1], A[0][0]
if per['M']:
    min_male_frequency, male_first_year = B[0][1], B[0][0]
if not female_first_year:
    print('In all years, {} was never given as a female name.'.format(first_name))
else:
    print('In terms of frequency, {} was the most popular '.format(first_name) +
          'as a female name first in the year {}.\n'.format(female_first_year) +
          '  It then accounted for {:.2f}% of all female names'.format(min_female_frequency))
if not male_first_year:
    print('In all years, {} was never given as a male name.'.format(first_name))
else:
    print('In terms of frequency, {} was the most popular '.format(first_name) +
          'as a male name first in the year {}.\n'.format(male_first_year) +
          '  It then accounted for {:.2f}% of all male names'.format(min_male_frequency))

