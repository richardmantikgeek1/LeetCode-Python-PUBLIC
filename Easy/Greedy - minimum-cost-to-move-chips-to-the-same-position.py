class Solution:
    def minCostToMoveChips(self, positions):
        memo = {}
        for i in range(0, len(positions)):
            pos = positions[i]
            if (pos in memo.keys()):
                memo[pos] += 1
            else:
                memo[pos] = 1

        ret_val = None
        for pos_1 in memo.keys():
            local_sum_cost = 0
            for pos_2 in memo.keys():
                count_coins = memo[pos_2]
                dist = abs(pos_1 - pos_2)
                cost = 0
                if (dist % 2 == 1):
                    cost = 1
            
                local_sum_cost += cost * count_coins
                
            if (ret_val is None or local_sum_cost < ret_val):
                ret_val = local_sum_cost
        
        return ret_val
    
sol = Solution()
print(sol.minCostToMoveChips([2,3,3]))