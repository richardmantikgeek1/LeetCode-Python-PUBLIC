class Solution:
    def decodeMessage(self, key, message) -> str:
        u2 = 96
        memo = {}
        for c in key:
            if (c not in memo.keys() and c != ' '):
                u2 += 1
                memo[c] = chr(u2)

        ret_val = ''    
        i = 0
        while (i < len(message)):
            c = message[i]
            if (c != ' '):
                ret_val += memo[c]
            else:
                ret_val += ' '
            i += 1

        return ret_val
