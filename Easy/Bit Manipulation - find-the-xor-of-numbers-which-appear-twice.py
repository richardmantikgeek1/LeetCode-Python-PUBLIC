class Solution:
    def duplicateNumbersXOR(self, array):
        memo = {}
        for num in array:
            if (num in memo.keys()):
                memo[num] += 1
            else:
                memo[num] = 1
        
        ret_val = 0
        for k in memo.keys():
            if (memo[k] == 2):
                ret_val ^= k
        
        return ret_val