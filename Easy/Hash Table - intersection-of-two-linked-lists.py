# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, l_list_1, l_list_2):
        h1 = l_list_1
        memo = {}
        while (h1 is not None):
            memo[h1] = True
            h1 = h1.next
        
        h2 = l_list_2
        while (h2 is not None):
            if (h2 in memo.keys()):
                return h2
            h2 = h2.next

        return None