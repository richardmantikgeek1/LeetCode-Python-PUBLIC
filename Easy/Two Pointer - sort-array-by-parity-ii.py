from collections import deque
class Solution:
    def sortArrayByParityII(self, array):
        i = 0 # even
        even_nums = deque([n for n in array if n % 2 == 0])
        odd_nums = deque([n for n in array if n % 2 == 1])
        
        ret_val = []
        step = 0
        while (len(even_nums) > 0 or len(odd_nums) > 0):
            if (step % 2 == 0):
                num = even_nums.popleft()
            else:
                num = odd_nums.popleft()
            ret_val.append(num)
            step += 1
        
        return ret_val

sol = Solution()
result = sol.sortArrayByParityII([4,2,5,7])
print(result)