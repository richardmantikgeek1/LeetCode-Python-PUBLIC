class Solution:
    def isSubsequence_sliding_window(self, s, t): # O(|s|+|t|) 
        i = j = 0
        count_matches = 0
        while(i < len(s)): # O(|s|)
            while(j < len(t)): # O(|t|)
                if (s[i] == t[j]):
                    count_matches += 1
                    j+=1
                    if (i+1 < len(s)):
                        i+=1
                else:
                    j+=1
            
            i+=1
        return count_matches == len(s)
    
sol = Solution()
print(sol.isSubsequence('bx', 'abc'))