class Solution:
    def minCostClimbingStairs(self, cost):
        memo = (len(cost) + 1)* [0]

        i = 2
        while (i <= len(cost)):
            memo[i] = (min (memo[i-2] + cost[i-2], memo[i-1] + cost[i-1]))
            i = i + 1
        return memo[i-1]