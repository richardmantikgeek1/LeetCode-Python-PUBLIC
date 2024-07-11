class Solution:
    def findMissingAndRepeatedValues(self, grid):
        memo = {}

        repeated_value = None
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (grid[i][j] in memo.keys()):
                    repeated_value = grid[i][j]
                memo[grid[i][j]] = True

        missing_value = None
        for k in range(1, max(memo.keys())+2):
            if (k not in memo.keys()):
                missing_value = k
                break
        
        return [repeated_value, missing_value]