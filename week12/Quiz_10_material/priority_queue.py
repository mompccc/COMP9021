# Written by *** for COMP9021


from binary_tree import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.data = [None]

    def insert(self, value):
        self.num += 1
        self.data.append(value)
        self._bubble_up(self.num)
        B = self.list_into_tree(1)
        B.print_binary_tree()


    def list_into_tree(self, i):
        A = BinaryTree(self.data[i])
        if i*2 < len(self.data):
            A.left_node = self.list_into_tree(i * 2)
        if i*2 + 1 < len(self.data):
            A.right_node = self.list_into_tree(i * 2 + 1)
        return A

    def _bubble_up(self, position):
        if position == 1:
            return
        if self.data[position // 2] > self.data[position]:
            self.data[position // 2], self.data[position] = self.data[position], self.data[position // 2]
            self._bubble_up(position // 2)
        # Replace pass above with your code
