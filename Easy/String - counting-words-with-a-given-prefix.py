class Solution:
    def prefixCount(self, words, pref) -> int:
        ret_val = 0
        for word in words:
            if (word.startswith(pref)):
                ret_val += 1
        
        return ret_val