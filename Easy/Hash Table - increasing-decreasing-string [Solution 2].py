class Solution:
    def sortString(self, s):
        s = sorted(s)
        is_increasing = True
        ret_val = ''
        last_c = None
        i = 0
        while (len(s) > 0):
            if (is_increasing):
                if (i == len(s)):
                    is_increasing = False
                    i = len(s) - 1
                    last_c = None
                elif (last_c is None or (i < len(s) and s[i] > last_c)):
                    c = s[i]
                    ret_val += c
                    last_c = c
                    s.pop(i)
                else:
                    i += 1
            else:
                if (i < 0):
                    is_increasing = True
                    i = 0
                    last_c = None
                if (last_c is None or (i >= 0 and s[i] < last_c)):
                    c = s[i]
                    ret_val += c
                    last_c = c
                    s.pop(i)
                    if (i > 0):
                        i -= 1
                else:
                    i -= 1
                
    
        return ret_val
    
s = 'aaaabbbbcccc'
sol = Solution()
result = sol.sortString(s)
print(result)

#abccbaabccbaa
#abccbaabccba