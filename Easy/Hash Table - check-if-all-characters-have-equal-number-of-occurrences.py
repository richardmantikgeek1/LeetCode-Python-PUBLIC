class Solution:
    def areOccurrencesEqual(self, s):
        map = {}
        for c in s:
            if (c in map.keys()):
                map[c] += 1
            else:
                map[c] = 1
        
        return min(map.values()) == max(map.values())
        