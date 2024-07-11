class Solution:
    def largestLocal(self, grid):
        max_local = []
        for i in range(0, len(grid) - 3 + 1):
            max_local.append([None] * (len(grid[i])- 2))

        for i in range(0, len(grid) - 3 + 1):
            rows = (grid[i:i+3])
            for j in range(0, len(grid[i])-3 + 1):
                cols = []
                for row in rows:
                    cols.extend(row[j:j+3])
                max_local[i][j] = max(cols)
        
        return max_local
            

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
sol = Solution()
ret_val = sol.largestLocal(grid)
print(ret_val)