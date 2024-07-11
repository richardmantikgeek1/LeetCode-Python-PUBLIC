class Solution:
    def returnToBoundaryCount(self, array):
        prefix_sum = 0
        ret_val = 0
        for i in range(0, len(array)):
            num = array[i]

            prefix_sum += num

            if (prefix_sum == 0):
                ret_val += 1
        
        return ret_val