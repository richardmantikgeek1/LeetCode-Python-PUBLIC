class Solution:
    def minimumMoves(self, s):
        i = 0
        j = 0
        ret_val = 0
        while (i < len(s)):
            if (s[i] == 'O'):
                i+=1
            else:
                j = i
                while (j < len(s) and j-i < 3):
                    j+=1
                ret_val += 1
                i = j
        return ret_val
    
sol = Solution()
print(sol.minimumMoves('XXOX'))