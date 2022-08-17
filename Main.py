# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
from typing import Optional

class Node:

    def __init__(self, data=None, next=None):
        """
        Initialises the Node with given attributes
        """
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        new = Node(data, None)
        current = self.head
        if current is None:
            self.head = new
        else:
            while current.next is not None:
                current = current.next
            current.next = new

    def status(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


class Solution:

    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        result = self.get_num(first_list) + self.get_num(second_list)
        sum_list = LinkedList()
        for digit in list(map(int, str(result)[::-1])):
            sum_list.insert_at_end(digit)
        return sum_list

    def get_num(self, l: Optional[LinkedList]) -> int:
        curr = l.head
        if curr is None:
            return 0
        num = ""
        while curr is not None:
            num = str(curr.data) + num
            curr = curr.next
        return int(num)

# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().st
                                
