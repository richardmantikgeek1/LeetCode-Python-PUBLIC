class Solution:
    def deleteGreatestValue(self, grid):
        ret_val = 0
        while (len(grid[0]) > 0):
            row_greatest_values = []
            for i in range(0, len(grid)):
                max_num_value = max(grid[i])
                max_num_index = grid[i].index(max_num_value)
                grid[i].pop(max_num_index)
                row_greatest_values.append(max_num_value)
            
            ret_val += max(row_greatest_values)
    
        return ret_val
