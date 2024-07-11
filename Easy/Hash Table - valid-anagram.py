class Solution:
    def isAnagram(self, s, t):
        a_map = self.str_to_map(s)
        b_map = self.str_to_map(t)
        return a_map == b_map
    
    def str_to_map(self, s):
        a_map = {}
        for c in s:
            if (c in a_map.keys()):
                a_map[c] += 1
            else:
                a_map[c] = 1
        return a_map