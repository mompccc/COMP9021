# Prints out the representation of a nonnegative number in base 2,
# using two recursive procedures, one of which is tail-recursive.
#
# Written by Eric Martin for COMP9021


def print_binary_representation_1(n):
    '''
    >>> print_binary_representation_1(0)
    0
    >>> print_binary_representation_1(1)
    1
    >>> print_binary_representation_1(2)
    10
    >>> print_binary_representation_1(5)
    101
    >>> print_binary_representation_1(23)
    10111
    '''
    _print_binary_representation_1(n)
    print()
    
def _print_binary_representation_1(n):
    if n >= 2:
        _print_binary_representation_1(n // 2)
    print(n % 2, end = '')


def print_binary_representation_2(n):
    '''
    >>> print_binary_representation_1(0)
    0
    >>> print_binary_representation_1(1)
    1
    >>> print_binary_representation_1(2)
    10
    >>> print_binary_representation_1(5)
    101
    >>> print_binary_representation_1(23)
    10111
    '''
    _print_binary_representation_2(n, n.bit_length() - 1)
    
def _print_binary_representation_2(n, exp):
    if exp < 0:
        print()     
    if 2 ** exp <= n:
        print(1, end = '')
        _print_binary_representation_2(n - 2 ** exp, exp - 1)
    else:
        print(0, end = '')
        _print_binary_representation_2(n, exp - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
