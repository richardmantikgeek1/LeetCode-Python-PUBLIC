class Solution:
    def decompressRLElist(self, array):
        ret_val = []
        for i in range(0, len(array), 2):
            freq = array[i]
            val = array[i+1]
            ret_val.extend([val] * freq)
        
        return ret_val
        