class Solution:
    def buildArray(self, nums):
        ret_val = []
        for i in range(0, len(nums)):
            ret_val.append(nums[nums[i]])

        return ret_val