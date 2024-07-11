class Solution:
    def numIdenticalPairs(self, array):
        memo = {}
        ret_val = 0
        for i in range(0, len(array)):
            num = array[i]
            
            if (num in memo.keys()):
                ret_val += memo[num]

            if (num in memo.keys()):
                memo[num] += 1
            else:
                memo[num] = 1 
      
        return ret_val
    
array = [1,2,3,1,1,3]
sol = Solution()
print(sol.numIdenticalPairs(array))