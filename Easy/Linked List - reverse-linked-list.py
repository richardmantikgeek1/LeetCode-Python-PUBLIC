# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, l_list):
        if (l_list is None): return None
        curr_node = l_list
        next_node = None
        prev_node = None
        while(curr_node.next is not None):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        curr_node.next = prev_node
        return curr_node
        
        
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(7)

sol = Solution()
res = sol.reverseList(head)