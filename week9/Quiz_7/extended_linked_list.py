# Written by **** for COMP9021

from linked_list import *


class ExtendedLinkedList(LinkedList):
    def __init__(self, L=None):
        super().__init__(L)

    def rearrange(self):
        L2 = self.duplicate()

        self.AA = self.head.value
        node=self.head.next_node
        while node:
            next_node = node.next_node
            num=node.value
            if num<self.AA:
                self.AA=num
            node=next_node

        self.length = 0
        A = self.head
        while A:
            self.length += 1
            A = A.next_node

        start_location = L2.index_of_value(self.AA)
        self.head.value = self.AA
        index = start_location + 2
        node_n1 = self.head.next_node
        node_n2 = node_n1.next_node
        if start_location == self.length - 2:
            node_n1.value = L2.value_at(start_location - 1)
            node_n2.value = L2.value_at(0)
            index = 0
        elif start_location == self.length - 1:
            node_n1.value = L2.value_at(start_location - 1)
            node_n2.value = L2.value_at(1)
            index = 1
        elif start_location == 0:
            node_n1.value = L2.value_at(self.length - 1)
            node_n2.value = L2.value_at(2)
            index = 2
        else:
            node_n1.value = L2.value_at(start_location - 1)
            node_n2.value = L2.value_at(start_location + 2)
            index = start_location + 2
        while index != start_location:
            if index == self.length - 2:
                node_n1_next = node_n1.next_node.next_node
                node_n2_next = node_n2.next_node.next_node
                node_n1_next.value = L2.value_at(index - 1)
                if node_n2_next:
                    node_n2_next.value = L2.value_at(0)
                    index = 0
                    node_n1 = node_n1_next
                    node_n2 = node_n2_next
                else:
                    break
            elif index == self.length - 1:
                node_n1_next = node_n1.next_node.next_node
                node_n2_next = node_n2.next_node.next_node
                node_n1_next.value = L2.value_at(index - 1)
                if node_n2_next:
                    node_n2_next.value = L2.value_at(1)
                    index = 1
                    node_n1 = node_n1_next
                    node_n2 = node_n2_next
                else:
                    break
            elif index == 0:
                node_n1_next = node_n1.next_node.next_node
                node_n2_next = node_n2.next_node.next_node
                node_n1_next.value = L2.value_at(self.length - 1)
                if node_n2_next:
                    node_n2_next.value = L2.value_at(2)
                    index = 2
                    node_n1 = node_n1_next
                    node_n2 = node_n2_next
                else:
                    break
            else:
                node_n1_next = node_n1.next_node.next_node
                node_n2_next = node_n2.next_node.next_node
                node_n1_next.value = L2.value_at(index - 1)
                if node_n2_next:
                    node_n2_next.value = L2.value_at(index + 2)
                    index += 2
                    node_n1 = node_n1_next
                    node_n2 = node_n2_next
                else:
                    break

                    # Replace pass above with your code



