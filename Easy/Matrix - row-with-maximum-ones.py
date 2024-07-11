class Solution:
    def rowAndMaximumOnes(self, matrix):
        max_row_count_ones = None
        max_row_count_ones_index = None
        for i in range(0, len(matrix)):
            row = matrix[i]
            row_count_ones = row.count(1)
            if (max_row_count_ones_index is None or max_row_count_ones < row_count_ones):
                max_row_count_ones_index = i
                max_row_count_ones = row_count_ones
        
        return [max_row_count_ones_index, max_row_count_ones]