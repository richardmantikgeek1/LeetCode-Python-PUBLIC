import math
from functools import cmp_to_key

class MatrixCell:
    def __init__(self, row_index = -1, col_index= -1, distance_to_center = None):
        self.row_index = row_index
        self.col_index = col_index
        self.distance_to_center = distance_to_center
    
    def __str__(self):
        return '(' + str(self.row_index) + ', ' + str(self.col_index)+', ' + str(self.distance_to_center) + ')'

class Solution:
    def allCellsDistOrder(self, rows, cols, r_center, c_center):
        matrix = []
        for i in range(0, rows):
            matrix_row = []
            for j in range(0, cols): 
                matrix_cell = MatrixCell()
                matrix_cell.row_index = i
                matrix_cell.col_index = j
                matrix_cell.distance_to_center = abs(i-r_center) + abs(j-c_center)
                matrix_row.append(matrix_cell)
            matrix.append(matrix_row)
        
        matrix_cells = []
        for i in range(0, rows):
            matrix_cells.extend(matrix[i])
        
        matrix_cells = sorted(matrix_cells, key=cmp_to_key(self.my_compare))
        ret_val = [[mc.row_index, mc.col_index] for mc in matrix_cells]
        return ret_val

    def my_compare (self, matrix_cell_1, matrix_cell_2):
        if matrix_cell_1.distance_to_center < matrix_cell_2.distance_to_center:
            return -1
        else:
            return 1
        

sol = Solution()
result = sol.allCellsDistOrder(3,5,2,3)
print(result)