class Solution:
    def sortedSquares(self, nums):
        ret_val = sorted([a**2 for a in nums])

        return ret_val