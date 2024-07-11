class Solution:
    def findNonMinOrMax(self, array):
        min_num = min(array)
        max_num = max(array)
        for num in array:
            if (num not in ([min_num, max_num])):
                return num
        
        return -1
        