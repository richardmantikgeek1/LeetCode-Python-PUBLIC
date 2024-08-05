class Solution:
    def hasTrailingZeros(self, array):
        binary_nums = []
        for num in array:
            binary_nums.append(format(num, 'b'))
        
        count_has_trailing_zeros = 0
        for b in binary_nums:
            if (b[len(b)-1] == '0'):
                count_has_trailing_zeros += 1

        return count_has_trailing_zeros >= 2
    
sol = Solution()
result = sol.hasTrailingZeros([1,2,3,4,5])
print(result)