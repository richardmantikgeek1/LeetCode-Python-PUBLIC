class Solution:
    def createTargetArray(self, nums, indices):
        target_array = []
        for j in range(0, len(indices)):
            i = indices[j]
            target_array.insert(i, nums[j])

        return target_array