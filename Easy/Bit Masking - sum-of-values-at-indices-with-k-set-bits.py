class Solution:
    def sumIndicesWithKSetBits(self, array, k):
        sum_nums = 0
        for i in range(0, len(array)):
            b = format(i, 'b')
            if (b.count('1') == k):
                sum_nums += array[i]
        
        return sum_nums