# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, l_list):
        array = []
        curr_node = l_list
        while (curr_node is not None):
            array.append(curr_node)
            curr_node = curr_node.next
        
        values = [n.val for n in array]
        return values == values[::-1]