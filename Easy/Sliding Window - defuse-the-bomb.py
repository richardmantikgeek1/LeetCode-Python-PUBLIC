class Solution:
    def decrypt(self, code, k):
        ret_val = []
        i = 0
        while (i < len(code)):
            j = 0
            sum_next_3_nums = 0
            if (k >= 0):
                while (j < k):
                    num_j = None
                    x = i + 1 + j
                    num_j = code[x % len(code)]
                    sum_next_3_nums += num_j
                    j += 1
            elif (k < 0):
                while (j < -k):
                    num_j = None
                    x = i - 1 - j
                    num_j = code[x]
                    sum_next_3_nums += num_j
                    j += 1
            ret_val.append(sum_next_3_nums)
            i += 1
    
        return ret_val
        
code = [2,4,9,3]
k = -2
sol = Solution()
result = sol.decrypt(code, k)
print(result)
