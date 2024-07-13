class Solution:
    def maximumCount(self, array):
        count_positive_nums = 0
        count_negative_nums = 0

        for i in range(0, len(array)):
            num = array[i]
            if (num < 0):
                count_negative_nums += 1
            elif (num > 0):
                count_positive_nums += 1
        
        return max(count_negative_nums, count_positive_nums)
        