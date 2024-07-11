class Solution:
    def minimumOperations(self, array):
        ret_val = 0
        pos_nums = [a for a in array if a > 0]
        while (len(pos_nums) > 0):
            min_pos_num = min(pos_nums)
            i = 0
            while (i < len(array)):
                if (array[i] > 0):
                    array[i] -= min_pos_num
                i += 1
            ret_val += 1
            pos_nums = [a for a in array if a > 0]
    
        return ret_val
        