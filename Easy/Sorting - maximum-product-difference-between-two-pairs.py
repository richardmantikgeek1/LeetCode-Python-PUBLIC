class Solution:
    def maxProductDifference(self, array):
        array = sorted(array)
        return array[len(array)-1] * array[len(array)-2] - array[1] * array[0]