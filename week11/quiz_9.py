# Prompts the user for a string, checks that it is a corect postfix expression
# built from positive numbers, + and spaces, and if it is,
# outputs a tree representation of the corresponding infix expression.

# Written by *** and Eric Martin for COMP9021


import sys
import re

from array_stack import *
from binary_tree import *


def store_in_two_stacks(expression):
    stack_1, stack_2 = ArrayStack(), ArrayStack()
    text = re.findall('[0-9]\d*|\+', expression)
    text.reverse()
    for i in text:
        if len(i)>1:
            if i[0] == '0':
                return None, None
    while text != []:
        stack_1.push(text.pop())
    stack_2 = stack_1
    return stack_1, stack_2
    # Replace above line with your code 
            
def stores_correct_postfix_expression(stack):
    if stack._data[0] == '+':
        return False
    new_stack = ArrayStack()
    for i in stack._data:
        if i.isdigit():
            new_stack.push(i)
        else:
            new_num = new_stack.pop()
            if new_stack._data != []:
                new_stack.push(new_num + '+' + new_stack.pop())
            else:
                break
    if new_stack._data == []:
        return False
    else:
        new_stack.pop()
        return new_stack.is_empty()
    # Replace pass above with your code 

def transfer_from_stack_to_tree(stack):
    if stack.peek() != '+':
        return BinaryTree(stack.pop())
    A = BinaryTree(stack.pop())
    A.left_node = transfer_from_stack_to_tree(stack)
    A.right_node = transfer_from_stack_to_tree(stack)
    return A
    # Replace pass above with your code

# Possibly define other functions

expression = input('Input an expression: ')
if not expression or expression.isspace():
    sys.exit()
stack_1, stack_2 = store_in_two_stacks(expression)
if not stack_1:
    print('Expression not built from nonnegative numbers and +')
else:
    if not stores_correct_postfix_expression(stack_1):
        print('Not a correct postfix expression')
    else:
        tree = transfer_from_stack_to_tree(stack_2)
        tree.print_binary_tree()
        
