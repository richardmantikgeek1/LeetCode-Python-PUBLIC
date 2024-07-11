from collections import deque
class Solution:
    def leftRightDifference(self, array):
        left_sum    = deque()
        right_sum   = deque()
        prefix_sum  = 0

        for i in range(0, len(array)):
            num = array[i]

            left_sum.append(prefix_sum)
            prefix_sum += num
        
        prefix_sum = 0
        for i in range(len(array) - 1, -1, -1):
            num = array[i]

            right_sum.appendleft(prefix_sum)
            prefix_sum += num

        ret_val = []
        for i in range(0, len(left_sum)):
            ret_val.append(abs(right_sum[i] - left_sum[i]))
        
        return ret_val

