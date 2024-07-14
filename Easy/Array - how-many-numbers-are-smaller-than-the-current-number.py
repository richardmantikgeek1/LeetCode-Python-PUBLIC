class Solution:
    def smallerNumbersThanCurrent(self, array):
        ret_val = []
        sorted_array = sorted(array)
        memo = {}
        for i in range(0, len(sorted_array)):
            num = sorted_array[i]
            if (num not in memo.keys()):
                memo[num] = i
        
        for i in range(0, len(array)):
            num = array[i]
            ret_val.append(memo[num])

        return ret_val