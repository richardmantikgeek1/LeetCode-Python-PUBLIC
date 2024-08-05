from collections import defaultdict
class Solution:
    def checkAlmostEquivalent(self, word_1, word_2):
        char_to_freq_map_1 = defaultdict(int)
        for i in range(0, len(word_1)):
            c = word_1[i]
            char_to_freq_map_1[c] += 1
        print(char_to_freq_map_1)

        char_to_freq_map_2 = defaultdict(int)
        for j in range(0, len(word_2)):
            c = word_2[j]
            char_to_freq_map_2[c] += 1
        print(char_to_freq_map_2)

        for A in range(ord('a'), ord('z') + 1):
            freq_1 = char_to_freq_map_1[chr(A)]
            freq_2 = char_to_freq_map_2[chr(A)]
            if (abs(freq_1 - freq_2) > 3):
                return False
        
        return True