class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo_1 = {}
        memo_2 = {}
        for i in range(0, len(s)):
            if (s[i] not in memo_1.keys()):
                memo_1[s[i]] = t[i]
            else:
                if memo_1[s[i]] != t[i]:
                    return False
                
            if (t[i] not in memo_2.keys()):
                memo_2[t[i]] = s[i]
            else:
                if memo_2[t[i]] != s[i]:
                    return False

        return True