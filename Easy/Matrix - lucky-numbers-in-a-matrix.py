import copy
class Solution:
    def luckyNumbers (self, matrix):
        rows = copy.deepcopy(matrix)

        cols = []
        for j in range(0, len(matrix[0])):
            col = []
            for i in range(0, len(matrix)):
                col.append(matrix[i][j])
            cols.append(col)
        rows_min_num = []
        for i in range(0, len(matrix)):
            rows_min_num.append(min(rows[i]))
        cols_max_num = []
        for j in range(0, len(matrix[0])):
            cols_max_num.append(max(cols[j]))

        ret_val = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])): # O(n*m)
                num = matrix[i][j]
                if (num == rows_min_num[i] and num == cols_max_num[j]): # max() => O(log m)
                    ret_val.append(num)

        return ret_val