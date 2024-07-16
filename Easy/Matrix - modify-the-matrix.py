import copy
class Solution:
    def modifiedMatrix(self, matrix):
        matrix_copy = copy.deepcopy(matrix)
        memo = {}
        for j in range(0, len(matrix_copy[0])):
            max_col_val = None
            for i in range(0, len(matrix_copy)):
                num = matrix_copy[i][j]
                if (max_col_val is None or num > max_col_val):
                    max_col_val = num
            memo[j] = max_col_val

        for i in range(0, len(matrix_copy)):
            for j in range(0, len(matrix_copy[i])):
                if (matrix[i][j] == -1):
                    matrix_copy[i][j] = memo[j]
        
        return matrix_copy