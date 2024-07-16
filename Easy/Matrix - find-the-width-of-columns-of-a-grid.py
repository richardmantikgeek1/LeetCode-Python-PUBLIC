class Solution:
    def findColumnWidth(self, grid):
        ret_val = []
        for j in range(0, len(grid[0])):
            len_nums = [len(str(arr[j])) for arr in grid]
            ret_val.append(max(len_nums))
        
        return ret_val