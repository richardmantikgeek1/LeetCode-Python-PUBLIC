class NumArray:

    def __init__(self, nums):
        self.memo = {}
        prefix_sum = 0

        for i in range(0, len(nums)):
            num_i = nums[i]

            self.memo[i] = prefix_sum
            prefix_sum += num_i
        self.memo[len(nums)] = prefix_sum

    def sumRange(self, left, right):
        return self.memo[right+1] - self.memo[left]