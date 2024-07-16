class Solution:
    def numSpecial(self, matrix):
        ret_val = 0
        maybe_special_positions_h = set()
        for i in range(0, len(matrix)):
            maybe_special_position = True
            one_coord = None
            for j in range(0, len(matrix[0])):
                if (matrix[i][j] == 1 and one_coord is None):
                    one_coord = (i, j)
                elif(matrix[i][j] == 1 and one_coord is not None):
                    maybe_special_position = False
            if (maybe_special_position and one_coord is not None):
                maybe_special_positions_h.add(one_coord)
        
        ret_val = 0
        for pos in maybe_special_positions_h:
            if (self.is_special_pos(pos[0], pos[1], matrix)):
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