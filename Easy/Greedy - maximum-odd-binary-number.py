class Solution:
    def maximumOddBinaryNumber(self, s):
        len_str = len(s)
        count_0s = s.count('0')
        
        return (len_str-count_0s-1) * '1' + count_0s * '0' + '1'
    
sol = Solution()
print(sol.maximumOddBinaryNumber('0101'))