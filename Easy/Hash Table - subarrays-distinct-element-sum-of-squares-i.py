class Solution:
    def sumCounts(self, array):
        ret_val = 0
        for i in range(0, len(array)):
            for j in range(i, len(array)):
                memo = {}
                subarray = array[i:j+1]
                for a in subarray:
                    memo[a] = True
                ret_val += len(memo.keys()) ** 2
        
        return ret_val