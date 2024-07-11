class Solution:
    def makeSmallestPalindrome(self, s):
        i = 0
        j = len(s)-1

        ret_val = [None] * len(s)
        while (i <= j):
            if (s[i] <= s[j]):
                ret_val[i] = s[i]
                ret_val[j] = s[i]
            else:
                ret_val[i] = s[j]
                ret_val[j] = s[j]
            i += 1
            j -= 1

        return ''.join(ret_val)
    
sol = Solution()
print(sol.makeSmallestPalindrome('abcd'))