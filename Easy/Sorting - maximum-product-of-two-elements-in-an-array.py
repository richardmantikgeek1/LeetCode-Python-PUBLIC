class Solution:
    def maxProduct(self, array):
        array = sorted(array)
        i = len(array)-1
        j = len(array)-2
        return ((array[i])-1) * ((array[j])-1)