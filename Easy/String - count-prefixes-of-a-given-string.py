class Solution:
    def countPrefixes(self, words, s):
        ret_val = 0
        for prefix in words:
            if (s.startswith(prefix)):
                ret_val += 1
        
        return ret_val