from collections import defaultdict

class Solution:
    def findTheDifference(self, s, t):
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1

        for c in t_map.keys():
            if (c not in s_map.keys() or t_map[c] > s_map[c]):
                return c
        
        return None