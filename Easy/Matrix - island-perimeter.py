class Solution:
    def islandPerimeter(self, grid):
        count_squares = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (grid[i][j] == 1):
                    count_squares += 1
        
        count_intersects = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])-1):
                if (grid[i][j] == 1 and grid[i][j+1] == 1):
                    count_intersects += 1

        for i in range(0, len(grid)-1):
            for j in range(0, len(grid[i])):
                if (grid[i][j] == 1 and grid[i+1][j] == 1):
                    count_intersects += 1

        return count_squares * 4 - count_intersects * 2