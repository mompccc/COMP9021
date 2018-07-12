# Prompts the user for the name of a file and outputs
# how many occurrences of each digit has been input, if any.
#
# Written by Eric Martin for COMP9021


with open(input('Enter the name of a file: ')) as file:
    digit_found = False
    count = [0] * 10
    for line in file:
        for c in line:
            if c.isdigit():
                digit_found = True
                count[int(c)] += 1
    if not digit_found:
        print('There is no digit in this file.')
    else:
        print('Digits: ', end = '')
        for i in range(10):
            if count[i]:
                print('{:4d}'.format(i), end = '')
        print('\nCount:  ', end = '')
        for i in range(10):
            if count[i]:
                print('{:4d}'.format(count[i]), end = '')
        print()


          
        
