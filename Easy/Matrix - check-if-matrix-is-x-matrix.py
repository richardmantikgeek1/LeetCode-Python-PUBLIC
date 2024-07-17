class Solution:
    def checkXMatrix(self, grid) -> bool:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (self.is_diagonal_coord(i, j, grid) and grid[i][j] == 0):
                    return False
                if (not self.is_diagonal_coord(i, j, grid) and grid[i][j] != 0):
                    return False
        return True
    
    def is_diagonal_coord(self, i, j, grid):
        if (i == j):
            return True
        elif (len(grid[0])-1-i == j):
            return True
        return False