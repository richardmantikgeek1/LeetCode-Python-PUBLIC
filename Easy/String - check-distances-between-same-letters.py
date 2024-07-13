class Solution:
    def checkDistances(self, s, distance):
        memo = {}
        my_distance = [0] * 26
        for i in range(0, len(s)):
            c = s[i]
            if (c in memo.keys()):
                my_distance[ord(c) - 97] = i - memo[c] - 1
            else:
                memo[c] = i

        for c in memo.keys():
            i = ord(c) - 97
            if (my_distance[i] != distance[i]):
                return False
        
        return True