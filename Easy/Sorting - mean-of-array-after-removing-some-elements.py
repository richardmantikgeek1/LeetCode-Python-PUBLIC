class Solution:
    def trimMean(self, array):
        count_removed_largest_nums = int(5/100 * len(array))
        count_removed_smallest_nums = int(5/100 * len(array))
        array = sorted(array)[count_removed_smallest_nums:-count_removed_largest_nums]
        return sum(array)/len(array)