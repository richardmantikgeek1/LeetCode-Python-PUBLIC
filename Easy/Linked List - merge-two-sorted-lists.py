# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l_list_1, l_list_2):
        dummy_node = ListNode(None)
        curr_node = dummy_node
        curr_node_1 = l_list_1
        curr_node_2 = l_list_2
        while (True):
            if (curr_node_1 is not None and curr_node_2 is not None and curr_node_1.val <= curr_node_2.val):
                curr_node.next = curr_node_1
                curr_node = curr_node_1
                curr_node_1 = curr_node_1.next
                
            elif (curr_node_1 is not None and curr_node_2 is not None and curr_node_2.val < curr_node_1.val):
                curr_node.next = curr_node_2
                curr_node = curr_node_2
                curr_node_2 = curr_node_2.next
            else:
                break
            
        if (curr_node_1 is not None):
            curr_node.next = curr_node_1
        elif (curr_node_2 is not None):
            curr_node.next = curr_node_2

        return dummy_node.next
