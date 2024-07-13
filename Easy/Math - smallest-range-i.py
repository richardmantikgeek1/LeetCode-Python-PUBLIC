class Solution:
    def smallestRangeI(self, array, k):
        score = max(array) - min(array) - (2 * k)
        if (score < 0):
            return 0
        else:
            return max(array) - min(array) - (2 * k)

sol = Solution()
result = sol.smallestRangeI([1,3,6], 3)
print(result)