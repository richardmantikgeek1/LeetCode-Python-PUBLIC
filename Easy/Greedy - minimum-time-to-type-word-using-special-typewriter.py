class Solution:
    def minTimeToType(self, word: str) -> int:
        pointer = 'a'
        ret_val = 0
        for c in word:
            if ord(c) <= ord('z') and ord(c) >= ord('n') and ord(pointer) <= ord('m'):
                temp = (ord('z') - ord(c) + ord(pointer) - ord('`') )
                if (temp > 13):
                    temp = 26 - temp
                ret_val += temp
                ret_val += 1
                pointer = c
            elif ord(pointer) <= ord('z') and ord(pointer) >= ord('n') and ord(c) <= ord('m'):
                temp = (ord(c) - ord('`') + ord('z') - ord(pointer))
                if (temp > 13):
                    temp = 26 - temp
                ret_val += temp
                ret_val += 1
                pointer = c
            elif (ord(c) <= ord('m') and ord(pointer) <= ord('m')):
                ret_val += abs(ord(c) - ord(pointer))
                ret_val += 1
                pointer = c
            elif ord(pointer) <= ord('z') and ord(pointer) >= ord('n') and ord(c) <= ord('z') and ord(c) >= ord('n'):
                ret_val += abs(ord(c) - ord(pointer))
                ret_val += 1
                pointer = c
        
        return ret_val

sol = Solution()
result = sol.minTimeToType('p')
print(result)