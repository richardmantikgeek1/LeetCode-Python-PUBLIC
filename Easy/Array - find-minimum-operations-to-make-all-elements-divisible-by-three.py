class Solution:
    def minimumOperations(self, array):
        ret_val = 0
        for num in array:
            if (num % 3 == 0):
                pass
            elif (num % 3 == 1):
                ret_val += 1
            elif (num % 3 == 2):
                ret_val += 1
                
        return ret_val