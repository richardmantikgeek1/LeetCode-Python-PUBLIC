from collections import deque
class Solution:
    def lastVisitedIntegers(self, array):
        seen = deque()
        ans = deque()
        count_consercutive_neg_num = 0
        last_num = None
        for i in range(0, len(array)):
            num = array[i]
            if (num >= 0):
                seen.appendleft(num)
                count_consercutive_neg_num = 0
            else:
                if (count_consercutive_neg_num < len(seen)):
                    ans.append(seen[count_consercutive_neg_num])
                else:
                    ans.append(-1)
                if (last_num is None or last_num == -1):
                    count_consercutive_neg_num += 1
                else:
                    count_consercutive_neg_num = 1
            
            last_num = num
        
        return ans
    
nums = [1,-1,2,-1,-1]
sol = Solution()
result = sol.lastVisitedIntegers(nums)
print(result)