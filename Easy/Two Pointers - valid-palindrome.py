class Solution:
    def isPalindrome(self, S):
        i = 0
        j = len(S) - 1
        while (j >= 0 and i < len(S)):
            while (i < len(S) and (not S[i].isalnum() or S[i] == ' ')):
                i += 1
            while (j >= 0 and (not S[j].isalnum() or S[j] == ' ')):
                j -= 1

            if (i > j): break

            if  (j >= 0 and i < len(S) and S[i].lower() != S[j].lower()):
                return False

            i+=1
            j-=1
        return True

res = Solution().isPalindrome('')
print(res)