class Solution:
    def sumOfSquares(self, array):
        ret_val = 0
        len_array = len(array)
        for i in range(0, len(array)):
            num = array[i]
            if (len_array % (i+1) == 0):
                ret_val += num ** 2
        
        return ret_val