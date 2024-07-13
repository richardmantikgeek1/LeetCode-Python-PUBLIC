from collections import deque
class Solution:
    def findTheArrayConcVal(self, array):
        queue = deque(array)
        ret_val = 0
        while (len(queue) > 1):
            front_num = queue.popleft()
            back_num = queue.pop()
            concatenation_num = int(str(front_num) + str(back_num))
            ret_val += concatenation_num

        if (len(queue) == 1):
            front_num = queue.popleft()
            concatenation_num = int(str(front_num))
            ret_val += concatenation_num
        
        return ret_val
