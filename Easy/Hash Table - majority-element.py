class Solution:
    def majorityElement(self, array):
        memo = {}
        for num in array:
            if (num in memo.keys()):
                memo[num] += 1
            else:
                memo[num] = 1

        majority_count = None
        majority_num = None
        for num in memo.keys():
            count_nums = memo[num]
            if (majority_num is None or count_nums > majority_count):
                majority_count = count_nums
                majority_num = num

        return majority_num
