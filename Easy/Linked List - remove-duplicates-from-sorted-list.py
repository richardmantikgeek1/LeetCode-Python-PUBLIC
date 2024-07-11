# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, l_list):
        curr_node = l_list
        while (curr_node is not None and curr_node.next is not None):
            while (curr_node is not None and curr_node.next is not None and curr_node.val == curr_node.next.val):
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next
        
        return l_list