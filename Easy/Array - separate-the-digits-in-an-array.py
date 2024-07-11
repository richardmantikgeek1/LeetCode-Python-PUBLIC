class Solution:
    def separateDigits(self, array):
        ret_val = []
        for i in range(0, len(array)):
            num = array[i]
            num_str = str(num)
            ret_val.extend([int(c) for c in num_str])

        return ret_val