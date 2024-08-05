class Solution:
    def findSubarrays(self, array):
        memo = {}
        for i in range(0, len(array)):
            subarray = array[i:i+2]
            if (len(subarray) == 2 and sum(subarray) in memo.keys()):
                return True
            
            if (len(subarray) == 2):
                memo[sum(subarray)] = True
        return False