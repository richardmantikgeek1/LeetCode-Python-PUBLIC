class Solution:
    def minStartValue(self, array):
        memo = {}
        prefix_sum = 0
        for i in range(0, len(array)):
            num = array[i]

            memo[prefix_sum] = True
            prefix_sum += num
        memo[prefix_sum] = True

        startValue = 1
        while (startValue + min(memo.keys()) < 1):
            startValue += 1

        return startValue

nums = [1,-2,-3]
sol = Solution()
sol.minStartValue(nums)