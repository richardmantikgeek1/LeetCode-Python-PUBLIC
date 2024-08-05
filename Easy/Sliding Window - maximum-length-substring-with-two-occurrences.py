from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s):
        a_map = defaultdict(int)

        left_index          = 0
        right_index         = 0

        max_length_substr   = 0
        length_substr       = 0
        length_s = len(s)
        while(left_index < length_s):
            while (right_index < length_s):
                c = s[right_index]
                if (a_map[c] + 1 <= 2):
                    a_map[c] += 1
                    right_index += 1

                    length_substr = right_index - left_index
                    max_length_substr = max(length_substr, max_length_substr)
                else:
                    break                    

            if (left_index < length_s):
                c = s[left_index]
                a_map[c] -= 1
                left_index += 1
                length_substr = right_index - left_index
        
        return max_length_substr

sol = Solution()
result = sol.maximumLengthSubstring('bcbbbcba')
print(result)