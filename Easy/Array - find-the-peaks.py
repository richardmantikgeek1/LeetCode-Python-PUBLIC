class Solution:
    def findPeaks(self, mountain):
        ret_val = []
        
        for i in range(1, len(mountain) - 1):
            if (mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]):
                ret_val.append(i)
        
        return ret_val