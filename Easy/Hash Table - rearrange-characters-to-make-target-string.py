from collections import defaultdict

class Solution:
    def rearrangeCharacters(self, s, target):
        target_map = defaultdict(int)
        for c in target:
            target_map[c] += 1
        
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1
        
        count_targets_array = []
        for c in target_map.keys():
            count_targets_array.append(s_map[c] // target_map[c])

        return min(count_targets_array)