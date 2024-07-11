class Solution:
    def sumOddLengthSubarrays(self, array):
        left_sum = []
        prefix_sum = 0
        for i in range(0, len(array)):
            num = array[i]
            
            left_sum.append(prefix_sum)
            prefix_sum += num
        left_sum.append(prefix_sum)
        
        ret_val = 0
        foo = 1
        while (foo <= len(array)):
            i = 0
            while (i + foo <= len(array)):
                ret_val += (left_sum[i+foo] - left_sum[i])
                i += 1
            foo += 2
        return ret_val

sol = Solution()
ret_val = sol.sumOddLengthSubarrays([1,4,2,5,3])
print(ret_val)       