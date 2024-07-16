class Solution:
    def scoreOfString(self, s):
        i = 0
        ret_val = 0
        while (i < len(s) - 1):
            c = s[i]
            next_c = s[i+1]
            score = abs(ord(c) - ord(next_c))
            ret_val += score
            i += 1
        
        return ret_val
        