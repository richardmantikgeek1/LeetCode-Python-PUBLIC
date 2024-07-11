class Solution:
    def countConsistentStrings(self, allowed, words):
        memo = {}
        start_index = 0
        while (start_index < len(allowed)):
            c = allowed[start_index]
            memo[c] = True
            start_index += 1

        ret_val = 0

        for word in words:
            is_consistent = True
            start_index = 0
            while (start_index < len(word)):
                c = word[start_index]
                if (c not in memo.keys()):
                    is_consistent = False
                start_index += 1
                
            if (is_consistent):
                ret_val += 1

        return ret_val