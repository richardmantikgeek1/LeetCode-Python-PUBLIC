class Solution:
    def findKthPositive(self, array, k):
        memo = {}
        for num in array:
            memo[num] = True
        max_num = max(array)
        pos_nums = list(range(1, max_num + k + 1))
        missing_pos_nums = [a for a in pos_nums if a not in memo.keys()]
        return missing_pos_nums[k-1]