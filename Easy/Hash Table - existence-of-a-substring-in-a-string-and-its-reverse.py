class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        memo = {}
        reversed_s = s[::-1]
        for i in range(0, len(s)):
            sub_str = s[i:i+2]
            if (len(sub_str) == 2):
                memo[sub_str] = True

        for j in range(0, len(reversed_s)):
            sub_str = reversed_s[j:j+2]
            if (sub_str in memo.keys()):
                return True
        
        return False