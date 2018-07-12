# Prompts the user for an amount, and outputs the minimal number of banknotes
# needed to match that amount, as well as the detail of how many banknotes
# of each type value are used.
# The available banknotes have a face value which is one of
# $1, $2, $5, $10, $20, $50, and $100.
#
# Written by Eric Martin for COMP9021


face_values = [1, 2, 5, 10, 20, 50, 100]
amount = int(input('Input the desired amount: '))

left = amount
charge = []
while left:
    value = face_values.pop()
    if left >= value:
        charge.append((value, left // value))
        left %= value

total = sum(A[1] for A in charge)

if total == 1:
    print('\n1 banknote is needed.')
else:
    print('\n{} banknotes are needed.'.format(total))
print('The detail is:')
for A in charge:
    print('{:>4}: {}'.format('$' + str(A[0]), A[1]))
