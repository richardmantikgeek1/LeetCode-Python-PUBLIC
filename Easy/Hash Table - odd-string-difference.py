from collections import defaultdict

class Solution:
    def oddString(self, words):
        difference = []
        for i in range(0, len(words)):
            word = words[i]
            j = 0
            diff = []
            while (j < len(word) - 1):
                diff.append(ord(word[j+1]) - ord(word[j]))
                j += 1
            difference.append(diff)
        
        difference_map = defaultdict(list)
        for i in range(0, len(difference)):
            diff = difference[i]
            diff_str = ','.join([str(d) for d in diff])
            difference_map[diff_str].append(i)
        
        for diff_str in difference_map.keys():
            if (len(difference_map[diff_str]) == 1):
                return words[difference_map[diff_str][0]]
        
        return None