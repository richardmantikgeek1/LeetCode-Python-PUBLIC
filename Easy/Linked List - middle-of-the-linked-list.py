# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, l_list):
        array = []
        curr_node = l_list
        while (curr_node is not None):
            array.append(curr_node)
            curr_node = curr_node.next
        
        start_index = 0
        end_index = len(array) - 1
        mid_index = math.ceil((start_index + end_index) / 2)

        return array[mid_index]