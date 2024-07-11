class Solution:
    def findNumbers(self, array):
        ret_val = 0
        for num in array:
            num_str = str(num)
            if (len(num_str) % 2 == 0):
                ret_val += 1
        
        return ret_val
        