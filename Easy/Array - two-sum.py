class Solution:
    def twoSum(self, array, target):
        memo = {}
        for i in range(0, len(array)):
            num_i = array[i]
            # num_i + num_j = target
            # num_i = target - num_j
            if (target-num_i not in memo.keys()):
                memo[target-num_i] = i

            if (num_i in memo.keys() and memo[num_i] < i):
                return [memo[num_i], i]

        return None