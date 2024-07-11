class Solution:
    def sortString(self, s):
        map = {}
        for c in s:
            if (c in map.keys()):
                map[c] += 1
            else:
                map[c] = 1
        
        i = 0
        is_increasing = True
        c = sorted(map.keys())[0]
        map[c] -= 1
        if (map[c] == 0):
            map.pop(c)
        ret_val = c
        last_c = c
        while (i < len(sorted(map.keys()))):
            if (is_increasing):
                c = None
                for key in sorted(map.keys()):
                    if (key > last_c):
                        c = key
                        map[c] -= 1
                        if (map[c] == 0):
                            map.pop(c)
                        ret_val += c
                        last_c = c
                        break
                if (c is None):
                    c = list(reversed(sorted(map.keys())))[0]
                    map[c] -= 1
                    if (map[c] == 0):
                        map.pop(c)
                    ret_val += c
                    last_c = c
                    is_increasing = False
            else:
                c = None
                for key in reversed(sorted(map.keys())):
                    if (key < last_c):
                        c = key
                        map[c] -= 1
                        if (map[c] == 0):
                            map.pop(c)
                        ret_val += c
                        last_c = c
                        break
                if (c is None):
                    c = sorted(map.keys())[0]
                    map[c] -= 1
                    if (map[c] == 0):
                        map.pop(c)
                    ret_val += c
                    last_c = c
                    is_increasing = True
        
        return ret_val
    
s = 'gtqxozxzrssrzxzoxqtg'
sol = Solution()
result = sol.sortString(s)
print(result)

#abccbaabccba
#abccbaabccbaa