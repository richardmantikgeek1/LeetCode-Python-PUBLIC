class Solution:
    def singleNumber(self, array):
        ret_val = None
        for num in array:
            if (ret_val is None):
                ret_val = num
            else:
                ret_val ^= num
    
        return ret_val