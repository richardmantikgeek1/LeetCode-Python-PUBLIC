class Solution:
    def smallerNumbersThanCurrent(self, array):
        memo = {}
        ret_val = []
        for i in range(0, len(array)):
            num_i = array[i]
            count_smaller_nums = len([a for a in array if a < num_i])
            ret_val.append(count_smaller_nums)
        return ret_val