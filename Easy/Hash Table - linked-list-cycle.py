class Solution:
    def hasCycle(self, l_list):
        memo = {}
        head = l_list
        while (head is not None):
            if (head.next in memo.keys()):
                return True
            memo[head] = True
            head = head.next
            
        return False
        