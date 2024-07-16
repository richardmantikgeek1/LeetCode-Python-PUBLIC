class Solution:
    def shiftGrid(self, grid, k):
        array = self.matrix_to_array(grid)
        k = k % (len(grid) * len(grid[0]))
        print(array, k)
        array = array[-k::] + array[0:-k]
        print(array)
        return self.array_to_matrix(array, len(grid), len(grid[0]))
    
    def matrix_to_array(self, grid):
        ret_val = []
        for i in range(0, len(grid)):
            ret_val.extend(grid[i])

        return ret_val
    
    def array_to_matrix(self, array, n, m):
        ret_val = []
        i = 0
        row = []
        while (i < len(array)):
            row.append(array[i])
            i += 1
            if ((len(row)) % m == 0):
                ret_val.append(row)
                row = []
        
        return ret_val