class Solution:
    def balancedStringSplit(self, s):
        a_map = {}
        i = 0
        count_balanced_string = 0
        while i < len(s):
            c = s[i]
            if (c in a_map.keys()):
                a_map[c] += 1
            else:
                a_map[c] = 1

            if ('L' in a_map.keys() and 'R' in a_map.keys() and a_map['L'] == a_map['R']):
                count_balanced_string += 1
                a_map = {}
            i += 1 

        return count_balanced_string
    
sol = Solution()
count_balanced_string = sol.balancedStringSplit('RLRRLLRLRL')
print(count_balanced_string)