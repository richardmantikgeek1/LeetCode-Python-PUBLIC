class Solution:
    def transpose(self, matrix):
        ret_val = []
        if (len(matrix) == 0):
            return ret_val

        for i in range(0, len(matrix[0])):
            ret_val.append([0] * len(matrix))

        for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix)):
                ret_val[i][j] = matrix[j][i]
        
        return ret_val

matrix = [[1,2,3],[4,5,6],[7,8,9]]     
sol = Solution()
ret_val = sol.transpose(matrix)
print(ret_val)