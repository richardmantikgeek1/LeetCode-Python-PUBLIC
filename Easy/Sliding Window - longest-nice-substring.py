from collections import defaultdict

class Solution:
    def longestNiceSubstring(self, s):
        max_nice_substr = ''

        len_substr = len(s)
        while (len_substr > 1):
            start_index = 0
            end_index = start_index + len_substr - 1
            while (end_index < len(s)):
                map = {}
                for i in range(start_index, end_index+1):
                    c = s[i]
                    map[c] = True
                
                if (self.is_nice_map(map)):
                    return s[start_index:end_index+1]

                start_index += 1
                end_index = start_index + len_substr - 1

            len_substr -= 1

        return max_nice_substr

    def is_nice_map(self, map):
        for c in map.keys():
            if ((c.lower() in map.keys() and c.upper() not in map.keys())
                or (c.upper() in map.keys() and c.lower() not in map.keys())):
                return False
        return True

s = 'YazaAay'
sol = Solution()
result = sol.longestNiceSubstring(s)
print(result)