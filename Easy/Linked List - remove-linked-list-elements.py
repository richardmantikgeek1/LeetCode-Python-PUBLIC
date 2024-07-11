# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, l_list, target):
        array = []
        curr_node = l_list
        while (curr_node is not None):
            array.append(curr_node)
            curr_node = curr_node.next

        array = [n for n in array if n.val != target]
        i = 0
        while (i < len(array) - 1):
            array[i].next = array[i+1]
            i+= 1
        
        if (len(array) > 0):
            array[i].next = None
            return array[0]
        else:
            return None