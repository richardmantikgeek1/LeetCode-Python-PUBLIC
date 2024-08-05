import math

class Solution:
    def maximumStrongPairXor(self, array):
        ret_val = - math.inf
        for i in range(0, len(array)):
            num_i = array[i]
            for j in range(0, len(array)):
                num_j = array[j]
                if (abs(num_i - num_j) <= min(num_i, num_j)):
                    temp = num_i ^ num_j
                    ret_val = max(ret_val, temp)

        return ret_val