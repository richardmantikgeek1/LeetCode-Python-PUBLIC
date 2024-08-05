from collections import defaultdict
class Solution:
    def canConstruct(self, ransom_note, magazine):
        char_to_freq_map = defaultdict(int)
        for i in range(0, len(magazine)):
            c = magazine[i]
            char_to_freq_map[c] += 1
        for i in range(0, len(ransom_note)):
            c = ransom_note[i]
            char_to_freq_map[c] -= 1
            if (char_to_freq_map[c] < 0):
                return False

        return True 
