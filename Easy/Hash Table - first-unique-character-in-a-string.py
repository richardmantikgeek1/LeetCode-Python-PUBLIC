from collections import defaultdict
class Solution:
    def firstUniqChar(self, s):
        char_to_indices_map = defaultdict(list)
        for i in range(0, len(s)):
            c = s[i]
            char_to_indices_map[c].append(i)
        indices_to_char_map = defaultdict(str)
        for c in char_to_indices_map.keys():
            indices = char_to_indices_map[c]
            if (len(indices) == 1):
                indices_to_char_map[indices[0]] = c
        for i in range(0, len(s)):
            if (i in indices_to_char_map):
                return i

        return -1
