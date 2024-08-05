class Solution:
    def findChampion(self, grid):
        max_num_index = None
        max_num_value = None
        for i in range(0, len(grid)):
            row = grid[i]
            num_str = ''.join([str(b) for b in row])
            num = int(num_str, 2)
            if (max_num_index is None or max_num_value < num):
                max_num_index = i
                max_num_value = num

        return max_num_index
