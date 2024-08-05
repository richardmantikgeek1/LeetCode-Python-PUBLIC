from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text):
        char_to_count_chars_map = defaultdict(int)
        for i in range(0, len(text)):
            c = text[i]
            char_to_count_chars_map[c] += 1

        balloon_map = defaultdict(int)
        for i in range(0, len('balloon')):
            c = 'balloon'[i]
            balloon_map[c] += 1
        
        count_balloons_array = []
        for k in balloon_map.keys():
            count_balloons_array.append(char_to_count_chars_map[k]//balloon_map[k])

        return min(count_balloons_array) 