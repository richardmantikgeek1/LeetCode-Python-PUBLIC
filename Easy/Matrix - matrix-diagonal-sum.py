class Solution:
    def diagonalSum(self, matrix):
        diagonal_sum = 0
        for i in range(0, len(matrix)):
            if (matrix[i][len(matrix)-1-i] is not None):
                diagonal_sum += matrix[i][len(matrix)-1-i]
            matrix[i][len(matrix)-1-i] = None
        for i in range(0, len(matrix)):
            if (matrix[i][i] is not None):
                diagonal_sum += matrix[i][i]
            matrix[i][i] = None
        
        return diagonal_sum