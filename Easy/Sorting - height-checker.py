class Solution:
    def heightChecker(self, heights):
        ret_val = 0
        sorted_heights = sorted(heights)
        for i in range(0, len(heights)):
            if (heights[i] != sorted_heights[i]):
                ret_val += 1

        return ret_val