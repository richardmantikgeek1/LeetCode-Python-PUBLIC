class Solution:
    def romanToInt(self, s):
        int_val = 0
        memo = {}
        memo['I'] = 1
        memo['V'] = 5
        memo['X'] = 10
        memo['L'] = 50
        memo['C'] = 100
        memo['D'] = 500
        memo['M'] = 1000

        i = 0
        while (i < len(s)):
            c = s[i]
            c2 = s[i:i+2]
            if (c2 == 'IV'):
                int_val += 4
                i += 2
            elif (c2 == 'IX'):
                int_val += 9
                i += 2
            elif (c2 == 'XL'):
                int_val += 40
                i += 2
            elif (c2 == 'XC'):
                int_val += 90
                i += 2
            elif (c2 == 'CD'):
                int_val += 400
                i += 2
            elif (c2 == 'CM'):
                int_val += 900
                i += 2
            else:
                int_val += memo[c]
                i += 1
        
        return int_val
