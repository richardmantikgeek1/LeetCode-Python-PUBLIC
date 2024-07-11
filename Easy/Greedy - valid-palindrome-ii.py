class Solution:
    def validPalindrome(self, s):
        if (s == s[::-1]):
            return True
        
        i = 0

        len_s = len(s)

        a_str_l = ''
        a_str_r = s[1:]

        r_str_l = s[len(s):0:-1]
        r_str_r = ''
        #print(r_str_l, '-', r_str_r)

        while (i < len_s):
            a_str = a_str_l + a_str_r
            r_str = r_str_l + r_str_r
            #print(a_str, r_str)

            if (a_str == r_str):
                return True
            c = s[i]
            i += 1
            a_str_l += c
            a_str_r = a_str_r[1:]

            r_str_l = r_str_l[:len_s - i-1]
            r_str_r = c + r_str_r
            #print(r_str_l, '-', r_str_r)
            #input()

        return False

s = 'abca'
sol = Solution()
print(sol.validPalindrome(s))