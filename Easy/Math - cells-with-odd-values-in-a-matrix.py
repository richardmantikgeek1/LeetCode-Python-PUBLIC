class Solution:
    def oddCells(self, n, m, indices):
        matrix = []
        for i in range(0, n):
            matrix.append([0] * m)
        
        for (r,c) in indices:
            for i in range(0, len(matrix[r])):
                matrix[r][i] += 1

            for i in range(0, len(matrix)):
                matrix[i][c] += 1

        ret_val = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if (matrix[i][j] % 2 == 1):
                    ret_val += 1

        return ret_val