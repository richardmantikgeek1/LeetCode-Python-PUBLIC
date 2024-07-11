class Solution:
    def maximizeSum(self, nums, k):
        max_sum = 0
        while (k > 0):
            max_i   = None
            max_num = None
            for i in range(0, len(nums)):
                num = nums[i]
                if (max_num is None or max_num < num):
                    max_i   = i
                    max_num = num
            
            m = nums.pop(max_i)
            max_sum += m
            nums.append(m + 1)
            k-=1
            
        return max_sum


array = [1,2,3,4,5]
sol = Solution()
max_sum = sol.maximizeSum(array, 3)
print(max_sum)