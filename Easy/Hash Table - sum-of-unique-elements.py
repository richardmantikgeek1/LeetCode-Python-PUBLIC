class Solution:
    def sumOfUnique(self, array):
        memo = {}
        # memo[1] = 1
        # memo[2] = 2
        # memo[3] = 1
        for i in range(0, len(array)):
            num = array[i]
            if (num in memo.keys()):
                memo[num] += 1
            else:
                memo[num] = 1
        
        ret_val = 0
        for k in memo.keys():
            if (memo[k] == 1):
                ret_val += k
        
        return ret_val