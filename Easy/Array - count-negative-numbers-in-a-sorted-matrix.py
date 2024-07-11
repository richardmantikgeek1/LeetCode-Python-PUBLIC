class Solution:
    def countNegatives(self, grid):
        count_positives = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (grid[i][j] < 0):
                    break
                else:
                    count_positives += 1
        
        return len(grid) * len(grid[0]) - count_positives