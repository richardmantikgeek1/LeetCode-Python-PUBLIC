class Solution:
    def countPairs(self, nums, target):
        ret_val = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] < target):
                    ret_val.append([i, j])
        return len(ret_val)