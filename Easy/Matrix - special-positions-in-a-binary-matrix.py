class Solution:
    def numSpecial(self, matrix):
        ret_val = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if (self.is_special_pos(i, j, matrix)):
                    ret_val += 1
        
        return ret_val

    def is_special_pos(self, i, j, matrix):
        for y in range(0, len(matrix)):
            if (y != i and matrix[y][j] == 1):
                return False
        for x in range(0, len(matrix[0])):
            if (x != j and matrix[i][x] == 1):
                return False
        return matrix[i][j] == 1