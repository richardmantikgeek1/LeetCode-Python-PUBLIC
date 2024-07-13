from collections import deque
class Solution:
    def replaceElements(self, array):
        i = len(array) - 1
        ret_val = deque()
        max_num_on_the_right = -1
        while (i >= 0):
            ret_val.appendleft(max_num_on_the_right)
            max_num_on_the_right = max(array[i], max_num_on_the_right)
            i-=1
        
        return ret_val