

class Solution:
    def countCharacters(self, words, chars):
        memo = {}

        for c in chars:
            if (c in memo.keys()):
                memo[c] += 1
            else:
                memo[c] = 1

        memo_backup = memo.copy()

        ret_val = 0
        for word in words:
            can_be_formed_by_chars = True
            for c in word:
                if (c not in memo.keys()):
                    can_be_formed_by_chars = False
                else:
                    memo[c] -= 1
                    if (memo[c] == 0):
                        memo.pop(c)
            if (can_be_formed_by_chars):
                ret_val += len(word)
            
            memo = memo_backup.copy()
        
        return ret_val
        
