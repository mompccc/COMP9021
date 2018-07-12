# Splits the National Data on the relative frequency of given names
# in the population of U.S. births into females and males,
# removing the field that determines the classification.
# The data are stored in a directory "names", in files named
# "yobxxxx.txt with xxxx (the year of birth) ranging from 1880 to 2013.
# They will be copied in a directory "names_classified", otherwise keeping
# the same file structure.
#
# Written by Eric Martin for COMP9021


import sys
import os


directory = 'names'
if not os.path.exists(directory):
    print('Sorry, could not find the directory')
    sys.exit()

new_directory = directory + '_classified'
if os.path.exists(new_directory):
    print('I tried to create a directory named {}, but it already exists.\n'
          'Better safe than sorry, I give up...'.format(new_directory))
    sys.exit()
    
female_subdirectory = new_directory + '/female'
male_subdirectory = new_directory + '/male'
os.mkdir(new_directory)
os.mkdir(male_subdirectory)
os.mkdir(female_subdirectory)

for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    with open(directory + '/' + filename) as file,\
         open(female_subdirectory + '/' + filename, 'w') as female_file,\
         open(male_subdirectory + '/' + filename, 'w') as male_file:
        for line in file:
            name, gender, tally = line.split(',')
            if gender == 'F':       
                print(name, tally, sep = ',', end = '', file = female_file)
            else:
                print(name, tally, sep = ',', end = '', file = male_file)

