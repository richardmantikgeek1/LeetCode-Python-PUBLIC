class Solution:
    def findPermutationDifference(self, s, t):
        s_map = {}
        for i in range(0, len(s)):
            cs = s[i]
            s_map[cs] = i
        t_map = {}
        for j in range(0, len(t)):
            ct = t[j]
            t_map[ct] = j
        
        ret_val = 0
        for a in range(97, 97 + 26):
            if (chr(a) in s_map.keys()
                and chr(a) in t_map.keys()):
                ret_val += abs(s_map[chr(a)] - t_map[chr(a)])
        
        return ret_val